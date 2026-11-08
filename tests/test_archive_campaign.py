from pathlib import Path
from types import SimpleNamespace
from unittest.mock import AsyncMock, Mock

import pytest

from archive_aggregate import game_dates
from archive_campaign import plan, report_path, verify_archive_page
from campaign import SOURCES


def inputs(tmp_path):
    for filename in (*SOURCES, 'private_storage.py', 'archive_campaign.py', 'archive_aggregate.py'):
        (tmp_path / filename).write_text('synthetic source')
    roster = {'runs': [{'model': f'test/model-{i}'} for i in range(100)]}
    catalog = {'data': [{'id': r['model'], 'pricing': {}} for r in roster['runs']]}
    games = [{'date': d, 'url': f'https://krillion.io/test-only/{d}',
              'visible_label': 'Synthetic ' + d} for d in game_dates()]
    return roster, games, catalog


def test_plan_preserves_exact_roster_and_dates(tmp_path):
    roster, games, catalog = inputs(tmp_path)
    result = plan(roster, games, catalog, tmp_path, 4)
    assert [m['id'] for m in result['models']] == [r['model'] for r in roster['runs']]
    assert result['dates'] == game_dates()
    assert report_path(result, 'test/model-1', result['dates'][0]) != report_path(result, 'test/model-2', result['dates'][0])


def test_missing_model_does_not_silently_substitute(tmp_path):
    roster, games, catalog = inputs(tmp_path)
    catalog['data'].pop()
    with pytest.raises(ValueError, match='unavailable'):
        plan(roster, games, catalog, tmp_path, 4)


def test_wrong_date_duplicate_url_and_unlock_links_fail_closed(tmp_path):
    roster, games, catalog = inputs(tmp_path)
    games[0]['date'] = '2026-11-07'
    with pytest.raises(ValueError, match='November 6'):
        plan(roster, games, catalog, tmp_path, 4)
    games[0]['date'] = game_dates()[0]
    games[0]['url'] = games[1]['url']
    with pytest.raises(ValueError, match='unique'):
        plan(roster, games, catalog, tmp_path, 4)
    games[0]['url'] = 'https://krillion.io/unlock?session_id=private'
    with pytest.raises(ValueError, match='non-authenticated'):
        plan(roster, games, catalog, tmp_path, 4)


async def test_archive_redirect_cannot_be_mistaken_for_requested_game():
    page = Mock(url='https://krillion.io/')
    page.get_by_text.return_value.wait_for = AsyncMock()
    with pytest.raises(RuntimeError, match='URL changed'):
        await verify_archive_page(page, {'url': 'https://krillion.io/test-only/date', 'visible_label': 'Archive date'})
    page.get_by_text.assert_called_once_with('Archive date', exact=True)
