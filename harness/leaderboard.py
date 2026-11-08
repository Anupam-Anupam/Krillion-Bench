"""Export a public static leaderboard from reports; never ship raw traces or API credentials."""
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path

from metrics import aggregate, pricing_for


def export_campaign(summary, manifest, reports, events_by_model=None, catalog=None):
    events_by_model, catalog = events_by_model or {}, catalog or manifest
    metadata = {m['id']: m for m in manifest['models']}
    output = []
    for row in summary['runs']:
        model = row['model']
        report = reports.get(model, {})
        metrics = report.get('metrics') or aggregate(events_by_model.get(model, []), pricing_for(catalog, model),
                                                     row.get('started_at'), row.get('ended_at'))
        verified = bool(row.get('scorecard_verified'))
        rounds = []
        for r in report.get('rounds', []):
            rounds.append({k: r.get(k) for k in ('round', 'prompt', 'points', 'accepted_answer', 'rarity', 'interruptions')})
            rounds[-1]['submissions'] = [{k: s.get(k) for k in ('answer', 'outcome', 'rarity', 'points', 'timer', 'suggested_answer')}
                                         for s in r.get('submissions', [])]
        output.append(dict(model=model, name=metadata.get(model, {}).get('name', model),
                           provider=model.split('/')[0], selection_rank=row['rank'],
                           status=row['status'], error_type=row.get('error_type'), complete=verified,
                           score=row.get('score') if verified else None, partial_points=row.get('partial_points'),
                           daily_percentile=row.get('daily_percentile') if verified else None,
                           rounds_scored=row.get('rounds_scored', 0), recoveries=row.get('navigation_recoveries', 0),
                           missed_rounds=sum(r.get('round_outcome') == 'missed' for r in report.get('rounds', [])),
                           scorecard_assisted=any(e.get('phase') == 'verified' for e in report.get('scorecard_collection', [])),
                           issues=[{k: e.get(k) for k in ('round', 'category', 'reason', 'http_status', 'provider_name', 'error_type')}
                                   for field in ('model_issues', 'inference_interruptions', 'agent_failures')
                                   for e in report.get(field, [])],
                           metrics=metrics, rounds=rounds))
    return dict(schema_version=1, date=manifest['utc_date'], updated_at=summary['updated_at'],
                label='OpenRouter · Top 100' if len(output) == 100 else 'OpenRouter campaign',
                settings=manifest['settings'], source_sha256=manifest.get('source_sha256', {}), runs=output)


def load_campaign(directory, summary_path=None, answers_path=None, catalog_path=None):
    manifest = json.loads((directory/'manifest.json').read_text())
    summary = json.loads((summary_path or directory/'summary.json').read_text())
    reports = {r['model']: r for r in json.loads(answers_path.read_text())['models']} if answers_path else {}
    events = {}
    for row in summary['runs']:
        folder = directory / row['directory']
        if not answers_path and (folder/'report.json').exists():
            reports[row['model']] = json.loads((folder/'report.json').read_text())
        if (folder/'events.jsonl').exists():
            events[row['model']] = [json.loads(s) for s in (folder/'events.jsonl').read_text().splitlines()]
    catalog = json.loads(catalog_path.read_text()) if catalog_path else None
    return export_campaign(summary, manifest, reports, events, catalog)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('campaign', type=Path)
    parser.add_argument('--summary', type=Path)
    parser.add_argument('--answers', type=Path)
    parser.add_argument('--catalog', type=Path)
    parser.add_argument('--output', type=Path, default=Path(__file__).resolve().parents[1] / 'web/data/leaderboard-data.json')
    args = parser.parse_args()
    data = load_campaign(args.campaign, args.summary, args.answers, args.catalog)
    args.output.write_text(json.dumps(data, indent=2, allow_nan=False) + '\n')
    print(f'Exported {len(data["runs"])} models to {args.output}')
