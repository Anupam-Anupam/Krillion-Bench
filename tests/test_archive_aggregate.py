import json
import pytest
from archive_aggregate import export_archive, game_dates, mean_interval


def records():
    manifest = dict(models=[{'id': 'test/a'}], dates=['2026-11-06', '2026-11-05'], settings={})
    rows = [dict(model='test/a', game_date=d, report=dict(scorecard_verified=True,
        final_score=str(score), daily_percentile=pct, private='must not publish',
        rounds=[{'prompt': 'private prompt', 'round_outcome': 'missed' if score == 0 else 'accepted'}],
        metrics=dict(run_cost_usd=cost, cost_basis=basis, output_cost_usd=cost,
                     output_cost_basis=basis, output_tokens=10, usage_complete=True,
                     run_duration_s=100, inference_duration_s=80)))
        for d, score, pct, cost, basis in zip(manifest['dates'], [0, 700], [None, 99],
                                             [.5, 1], ['partial_reported', 'reported'])]
    return manifest, rows


def test_same_75_dates_end_yesterday():
    dates = game_dates()
    assert len(dates) == 75 and len(set(dates)) == 75
    assert dates[0] == '2026-11-06' and dates[-1] == '2026-08-24'


def test_zero_scores_count_missing_metrics_do_not_and_no_trajectories_export():
    manifest, rows = records()
    result = export_archive(manifest, rows)
    row = result['runs'][0]
    assert row['score'] == 350 and row['games'] == 2
    assert row['daily_percentile'] == 99
    assert row['aggregate_stats']['daily_percentile']['n'] == 1
    assert row['metrics']['run_cost_usd'] == 1
    assert row['aggregate_stats']['run_cost_usd']['n'] == 1
    assert row['score_ci95'] == [0, 700]
    assert 'private' not in json.dumps(result) and row['rounds'] == []


def test_unbalanced_panel_duplicates_and_unverified_scores_block_publication():
    manifest, rows = records()
    with pytest.raises(ValueError, match='not complete'):
        export_archive(manifest, rows[:1])
    with pytest.raises(ValueError, match='duplicate'):
        export_archive(manifest, rows + rows[:1])
    rows[0]['report']['scorecard_verified'] = False
    with pytest.raises(ValueError, match='Unverified'):
        export_archive(manifest, rows)


def test_confidence_interval_is_reproducible_and_not_fabricated_for_one_game():
    assert mean_interval([100] * 75)['ci95'] == [100, 100]
    assert mean_interval([100])['ci95'] is None
    a = mean_interval([0, 100, 200, 300])
    assert a == mean_interval([0, 100, 200, 300])
    assert a['ci95'][0] < a['mean'] < a['ci95'][1]
