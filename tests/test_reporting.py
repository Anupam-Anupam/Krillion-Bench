from copy import deepcopy

from reporting import enrich_report, markdown, result_details


def test_result_parser_ignores_legend():
    text = 'PLANKTON · 10\nRARE · 60\nONE IN A KRILLION · 100\nSCHOOLER\n“Pierogi”\n+30 PTS · sink 300m'
    assert result_details(text) == dict(accepted_answer='Pierogi', rarity='Schooler', points=30, rarity_source='displayed_result')
    assert result_details('RARE · 60')['rarity'] is None
    assert result_details('', 85)['rarity_source'] == 'points_mapping'


def test_historical_attempts_and_daily_percentile_are_evidence_based():
    row = dict(round='PROMPT 1 OF 7', prompt='Food?', points=30,
               result_text='SCHOOLER\n“Pierogi”\n+30 PTS',
               submissions=[dict(answer='nope', elapsed_s=1), dict(answer='nope', elapsed_s=3), dict(answer='pierogi', elapsed_s=5)])
    raw = dict(status='agent_finished', model='test', rounds=[row] + [{} for _ in range(6)],
               final_score='210', scoreboard=[f'Round {n}: Pierogi, 30 pts' for n in range(1, 8)])
    for n, r in enumerate(raw['rounds'][1:], 2):
        r.update(round=f'PROMPT {n} OF 7', prompt='Food?')
    original = deepcopy(raw)
    events = [dict(event='round_open', round=row['round'], elapsed_s=10),
              dict(event='model_input', elapsed_s=12, observation=dict(page=dict(
                  round_label=row['round'], prompt='Food?', text='"nope": no echo. try again')))]
    report = enrich_report(raw, "50% SCORE\nBETTER THAN 80% OF TODAY’S PLAYERS", events)
    assert raw == original
    assert report['daily_percentile'] == 80
    attempts = report['rounds'][0]['submissions']
    assert [s['outcome'] for s in attempts] == ['rejected', 'unconfirmed', 'accepted']
    assert [s['rarity'] for s in attempts] == [None, None, 'Schooler']
    assert 'better than 80%' in markdown(report)
    raw['scoreboard'].pop()
    partial = enrich_report(raw, "BETTER THAN 80% OF TODAY'S PLAYERS", events)
    assert partial['daily_percentile'] is None
    assert 'partial points' in markdown(partial)


def test_absent_percentile_and_unmatched_canonical_answer_are_not_invented():
    raw = dict(status='failed', rounds=[dict(round='1', prompt='Food?', points=60,
               result_text='RARE\n“Canonical name”\n+60 PTS', submissions=[dict(answer='different name')])])
    report = enrich_report(raw, 'Score 60%')
    assert report['daily_percentile'] is None
    assert report['rounds'][0]['accepted_answer'] == 'Canonical name'
    assert report['rounds'][0]['submissions'][0]['outcome'] == 'unconfirmed'


def test_markdown_escapes_answer_table_content():
    raw = dict(status='failed', rounds=[dict(round='1', prompt='<tag>', submissions=[dict(answer='a|b\nc')])])
    text = markdown(enrich_report(raw))
    assert 'a&#124;b c' in text and '&lt;tag&gt;' in text


def test_correction_and_remote_submission_timestamp_race():
    raw = dict(status='failed', rounds=[dict(round='1', prompt='Cardio?', submissions=[
        dict(answer='Rowing machine', elapsed_s=3)])])
    events = [dict(event='round_open', round='1', elapsed_s=10),
              dict(event='action', round='1', elapsed_s=12, action=dict(kind='click', target='DIVE')),
              dict(event='model_input', elapsed_s=12.9, observation=dict(page=dict(round_label='1', prompt='Cardio?',
                   text='“Rowing machine” → \ncorrects to\n“Rowing”\nsubmit again to confirm · or edit')))]
    report = enrich_report(raw, events=events)
    sub = report['rounds'][0]['submissions'][0]
    assert sub['outcome'] == 'confirmation_required'
    assert sub['suggested_answer'] == 'Rowing'
    assert sub['rarity'] is None


def test_verified_scorecard_fills_missing_result_with_labeled_mapping():
    raw = dict(status='agent_finished', final_score='70',
               scoreboard=[f'Round {n}: Answer {n}, 10 pts' for n in range(1, 8)],
               rounds=[dict(round=f'PROMPT {n} OF 7', prompt='Question', submissions=[dict(answer=f'answer {n}')])
                       for n in range(1, 8)])
    report = enrich_report(raw)
    for row in report['rounds']:
        sub = row['submissions'][0]
        assert sub['outcome'] == 'accepted'
        assert sub['rarity'] == 'Plankton'
        assert sub['rarity_source'] == 'points_mapping'
        assert sub['evidence'] == 'verified_scorecard'


def test_zero_scorecard_round_never_becomes_an_accepted_answer():
    raw = dict(status='agent_finished', final_score='0',
               scoreboard=[f'Round {n}: —, 0 pts' for n in range(1, 8)],
               rounds=[dict(round=f'PROMPT {n} OF 7', prompt='Question', submissions=[dict(answer='—')])
                       for n in range(1, 8)])
    report = enrich_report(raw, "BETTER THAN 0% OF TODAY'S PLAYERS")
    assert report['scorecard_verified'] and report['daily_percentile'] == 0
    assert all(r['points'] == 0 and r['round_outcome'] == 'missed' for r in report['rounds'])
    assert all(r['accepted_answer'] is None and r['rarity'] is None for r in report['rounds'])
    assert all(r['submissions'][0]['outcome'] == 'unconfirmed' for r in report['rounds'])


def test_archive_percentile_uses_original_players_and_requires_score_evidence():
    raw = dict(status='agent_finished', final_score='70',
               scoreboard=[f'Round {n}: Answer {n}, 10 pts' for n in range(1, 8)],
               rounds=[dict(round=f'PROMPT {n} OF 7', prompt='Question') for n in range(1, 8)])
    report = enrich_report(raw, "BETTER THAN 99% OF DAY #114'S ORIGINAL PLAYERS")
    assert report['daily_percentile'] == 99
    assert report['percentile_reference_day'] == 114
    assert enrich_report(raw, "BETTER THAN 101% OF DAY #114'S ORIGINAL PLAYERS")['daily_percentile'] is None
    raw['scoreboard'].pop()
    assert enrich_report(raw, "BETTER THAN 99% OF DAY #114'S ORIGINAL PLAYERS")['daily_percentile'] is None
