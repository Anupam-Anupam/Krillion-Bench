"""Aggregate-only public exports; trajectory text never crosses this boundary."""
from datetime import date, timedelta
import math
import random
import statistics


def game_dates(end='2026-11-06', count=75):
    last = date.fromisoformat(end)
    if not 1 <= count <= 3650:
        raise ValueError('Invalid number of archived games')
    return [(last - timedelta(days=i)).isoformat() for i in range(count)]


def mean_interval(values, *, seed=20261107, samples=10000):
    if not values:
        return dict(mean=None, n=0, ci95=None)
    if any(isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(v) for v in values):
        raise ValueError('Metrics must be finite numbers')
    n = len(values)
    mean = statistics.mean(values)
    if n < 2:
        return dict(mean=mean, n=n, ci95=None)
    rng = random.Random(seed)
    boot = sorted(sum(values[rng.randrange(n)] for _ in range(n)) / n for _ in range(samples))
    def quantile(p):
        pos = (len(boot) - 1) * p
        lo = math.floor(pos)
        return boot[lo] + (boot[min(lo + 1, len(boot) - 1)] - boot[lo]) * (pos - lo)
    return dict(mean=mean, n=n, ci95=[quantile(.025), quantile(.975)])


def export_archive(manifest, reports):
    """Require a complete fixed panel, and fail closed on duplicate or missing games."""
    models = manifest['models']
    dates = manifest['dates']
    if len(set(dates)) != len(dates) or len({m['id'] for m in models}) != len(models):
        raise ValueError('Duplicate model or date in manifest')
    expected = {(m['id'], d) for m in models for d in dates}
    panel = {}
    for record in reports:
        key = (record['model'], record['game_date'])
        if key not in expected or key in panel:
            raise ValueError('Unexpected or duplicate model/game report')
        report = record['report']
        if not report.get('scorecard_verified'):
            raise ValueError('Unverified scorecard: cannot publish a complete-panel average')
        score = float(report['final_score'])
        if not math.isfinite(score) or not 0 <= score <= 700:
            raise ValueError('Invalid verified score')
        panel[key] = report
    if set(panel) != expected:
        raise ValueError(f'Campaign not complete: {len(panel)} of {len(expected)} verified games')
    rows = []
    for model in models:
        games = [panel[model['id'], d] for d in dates]
        # Same bootstrap index sequence across models preserves the paired dates.
        score = mean_interval([float(g['final_score']) for g in games])
        daily = mean_interval([g['daily_percentile'] for g in games if g.get('daily_percentile') is not None])
        stats = {}
        for field in ('run_cost_usd', 'output_cost_usd', 'output_tokens', 'run_duration_s', 'inference_duration_s'):
            values = []
            for g in games:
                metric = g['metrics']
                value = metric.get(field)
                if value is None:
                    continue
                if field.endswith('cost_usd'):
                    basis = metric['cost_basis' if field == 'run_cost_usd' else 'output_cost_basis']
                    if basis == 'unavailable' or basis.startswith('partial_'):
                        continue
                if field == 'output_tokens' and not metric.get('usage_complete'):
                    continue
                values.append(value)
            stats[field] = mean_interval(values)
        metrics = {field: result['mean'] for field, result in stats.items()}
        for field, basis_field in [('run_cost_usd', 'cost_basis'), ('output_cost_usd', 'output_cost_basis')]:
            sources = {g['metrics'].get(basis_field) for g in games
                       if g['metrics'].get(field) is not None and
                       not g['metrics'].get(basis_field, 'unavailable').startswith('partial_')}
            metrics[basis_field] = ('unavailable' if not sources else next(iter(sources)) if len(sources) == 1 else 'mixed')
        metrics.update(usage_complete=stats['output_tokens']['n'] == len(dates),
                       usage_calls=sum(g['metrics'].get('usage_calls', 0) for g in games),
                       model_calls=sum(g['metrics'].get('model_calls', 0) for g in games))
        rows.append(dict(model=model['id'], name=model.get('name', model['id']),
                         provider=model['id'].split('/')[0], selection_rank=model.get('rank'),
                         complete=True, status='aggregate', score=score['mean'], score_ci95=score['ci95'],
                         games=len(games), daily_percentile=daily['mean'],
                         aggregate_stats=dict(score=score, daily_percentile=daily, **stats),
                         metrics=metrics, rounds=[], rounds_scored=7 * len(games),
                         recoveries=sum(len(g.get('recoveries', [])) for g in games),
                         missed_rounds=sum(r.get('round_outcome') == 'missed' for g in games for r in g['rounds'])))
    return dict(schema_version=1, aggregation='archive_mean', date=max(dates),
                date_start=min(dates), date_end=max(dates), games_per_model=len(dates),
                label='Archived daily games', settings=manifest['settings'], runs=rows,
                uncertainty=dict(method='percentile bootstrap over game dates', level=.95,
                                 resamples=10000, seed=20261107,
                                 interpretation='Variation across archived games; one run per model per game.'))
