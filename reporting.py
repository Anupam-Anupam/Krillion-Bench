"""Evidence-based run reports, including backfills from saved UI observations."""
import argparse
from copy import deepcopy
import html
import json
from pathlib import Path
import re

TIERS = {10: 'Plankton', 15: 'Too Clever', 30: 'Schooler', 60: 'Rare',
         85: 'Deep Cut', 100: 'One in a Krillion'}
RESULT = re.compile(r'(PLANKTON|TOO CLEVER|SCHOOLER|RARE|DEEP CUT|ONE IN A KRILLION)\s*\n[“"](.+?)[”"]\s*\n\+(\d+) PTS', re.I)
REJECTION = re.compile(r'["“](.+?)["”]:\s*no echo\. try again', re.I)


def rejection(text):
    match = REJECTION.search(text)
    return match.group(1) if match else None


def correction(text):
    match = re.search(r'[“"](.+?)[”"]\s*→\s*corrects to\s*[“"](.+?)[”"]\s*submit again to confirm', text, re.I)
    return dict(answer=match[1], suggested_answer=match[2]) if match else None


def result_details(text, points=None):
    match = RESULT.search(text)
    if match:
        return dict(accepted_answer=match[2], rarity=match[1].title(),
                    points=int(match[3]), rarity_source='displayed_result')
    return dict(accepted_answer=None, rarity=TIERS.get(points), points=points,
                rarity_source='points_mapping' if points in TIERS else None)


def scorecard_verified(report):
    entries = [re.fullmatch(r'Round (\d+): (.*), (\d+) pts', s)
               for s in report.get('scoreboard', [])]
    score = str(report.get('final_score', ''))
    return (len(report.get('rounds', [])) == 7 and len(entries) == 7 and all(entries)
            and {int(m[1]) for m in entries} == set(range(1, 8))
            and score.isdigit() and sum(int(m[3]) for m in entries) == int(score))


def enrich_report(report, final_text='', events=()):
    """Copy, never rewrite historical observations or timing measurements."""
    report = deepcopy(report)
    report['report_version'] = 2
    report['scorecard_verified'] = scorecard_verified(report)
    pct = re.search(r"BETTER THAN\s+(\d+(?:\.\d+)?)%\s+OF TODAY['’]S PLAYERS", final_text, re.I)
    report['daily_percentile'] = (float(pct[1]) if pct and 0 <= float(pct[1]) <= 100
                                  and report['scorecard_verified'] else None)
    report.setdefault('navigation_recovery', 'off (historical)')
    report['recoveries'] = [e for e in events if e['event'] == 'navigation_recovery']
    report['assisted'] = any(e.get('result') == 'ok' for e in report['recoveries'])
    opened = {e['round']: e['elapsed_s'] for e in events if e['event'] == 'round_open'}
    for row in report['rounds']:
        details = result_details(row.get('result_text', ''), row.get('points'))
        if details['accepted_answer'] is None and report['scorecard_verified']:
            number = re.search(r'PROMPT (\d+) OF 7', row['round'])
            entries = [re.fullmatch(r'Round (\d+): (.*), (\d+) pts', value)
                       for value in report['scoreboard']]
            entry = next((m for m in entries if number and m[1] == number[1]), None)
            if entry:
                details = result_details('', int(entry[3]))
                details['accepted_answer'] = entry[2]
        row.update({k: v for k, v in details.items() if k != 'points'})
        submissions = row.setdefault('submissions', [])
        for sub in submissions:
            sub.setdefault('outcome', 'unconfirmed')
            sub.setdefault('rarity', None)
            sub.setdefault('points', None)
        # Historic logs recorded rejection messages in model observations. Match each
        # message to the most recent preceding attempt, including repeated answers.
        clicks = [e for e in events if e['event'] == 'action' and e.get('round') == row['round']
                  and e.get('action', {}).get('kind') == 'click' and e['action'].get('target') == 'DIVE']
        for event in events:
            page = event.get('observation', {}).get('page', {})
            if page.get('round_label') != row['round'] or page.get('prompt') != row['prompt']:
                continue
            rejected = rejection(page.get('text', ''))
            corrected = correction(page.get('text', ''))
            if rejected is None and corrected is None:
                continue
            # Old submissions were timestamped after the remote press returned.
            # Pair with pre-press action events when their counts match, avoiding
            # the observer/keypress race without adding timing tolerance.
            if clicks and len(clicks) == len(submissions):
                preceding = [sub for sub, click in zip(submissions, clicks)
                             if click['elapsed_s'] <= event['elapsed_s']]
            else:
                preceding = [sub for sub in submissions if row['round'] in opened
                             and sub.get('elapsed_s', float('inf')) <= event['elapsed_s'] - opened[row['round']]]
            if not preceding or preceding[-1]['outcome'] != 'unconfirmed':
                continue
            sub = preceding[-1]
            if rejected is not None and sub['answer'].casefold() == rejected.casefold():
                sub.update(outcome='rejected', evidence='visible_no_echo')
            elif corrected and sub['answer'].casefold() == corrected['answer'].casefold():
                sub.update(outcome='confirmation_required', evidence='visible_correction',
                           suggested_answer=corrected['suggested_answer'])
        # Attribute an accepted result only when it matches the final submitted text.
        # If the game canonicalizes spelling unexpectedly, retain the round result
        # separately rather than pretending an unconfirmed attempt was accepted.
        if submissions and details['accepted_answer'] is not None:
            sub = submissions[-1]
            if sub['answer'].strip().casefold() == details['accepted_answer'].strip().casefold():
                sub.update(outcome='accepted', rarity=details['rarity'], points=details['points'],
                           evidence='displayed_result' if details['rarity_source'] == 'displayed_result' else 'verified_scorecard', rarity_source=details['rarity_source'])
    return report


def cell(value):
    return html.escape(str(value if value is not None else '—')).replace('|', '&#124;').replace('\n', ' ')


def markdown(report):
    verified = report['scorecard_verified']
    score = report.get('final_score') if verified else sum(r.get('points', 0) for r in report['rounds'])
    pct = report['daily_percentile']
    lines = [f"# Krillion run: {cell(report.get('model') or report.get('command'))}", '',
             f"Status: **{cell(report['status'])}**. Score: **{score}{'/700' if verified else ' partial points'}**.", '',
             f"Final daily percentage: **{'unavailable (no verified final percentile)' if pct is None else f'better than {pct:g}% of today’s players'}**.", '',
             f"Navigation recovery: {cell(report['navigation_recovery'])}; successful assistance: {sum(e.get('result') == 'ok' for e in report['recoveries'])}.", '',
             'Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.', '']
    if report.get('error_type'):
        lines += [f"Failure: {cell(report['error_type'])}.", '']
    for row in report['rounds']:
        lines += [f"## {cell(row['round'])}: {cell(row['prompt'])}", '',
                  '| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |',
                  '|---:|---|---|---|---:|---:|']
        for n, sub in enumerate(row['submissions'], 1):
            lines += ['| ' + ' | '.join(map(cell, [n, sub['answer'], sub['outcome'] + (f" → {sub['suggested_answer']}" if sub.get('suggested_answer') else ''), sub['rarity'], sub['points'], sub.get('timer')])) + ' |']
        if not row['submissions']:
            lines += ['| — | No recorded submission | — | — | — | — |']
        if row.get('points') is not None:
            lines += ['', f"Round result: {cell(row.get('accepted_answer'))} · {cell(row['rarity'])} · {row['points']} points (source: {cell(row['rarity_source'])})."]
        lines += ['']
    if report['recoveries']:
        lines += ['## Navigation recovery log', '']
        for e in report['recoveries']:
            lines += [f"- {e['elapsed_s']:.2f}s: {cell(e['target'])} — {cell(e['result'])} ({cell(e['reason'])})."]
        lines += ['']
    return '\n'.join(lines)


def write_report(report, output, final_text='', events=(), prefix='report'):
    enriched = enrich_report(report, final_text, events)
    (output / f'{prefix}.json').write_text(json.dumps(enriched, indent=2) + '\n')
    (output / f'{prefix}.md').write_text(markdown(enriched))
    return enriched


def read_events(output):
    path = output / 'events.jsonl'
    return [json.loads(line) for line in path.read_text().splitlines()] if path.exists() else []


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Backfill reports without overwriting historical report.json')
    parser.add_argument('runs', type=Path, nargs='+')
    args = parser.parse_args()
    for output in args.runs:
        raw = json.loads((output / 'report.json').read_text())
        final = output / 'final.txt'
        write_report(raw, output, final.read_text() if final.exists() else '', read_events(output), prefix='report.enriched')
