from web_scraper import __version__
import pytest
from web_scraper.scraper import get_citations_needed_count, get_citations_needed_report

def test_version():
    assert __version__ == '0.1.0'

def test_import():
    assert get_citations_needed_count
    assert get_citations_needed_report

def test_count():
    url = "https://en.wikipedia.org/wiki/History_of_Mexico"
    assert get_citations_needed_count(url) == 5

def test_one_citation():
    url = 'https://en.wikipedia.org/wiki/History_of_Mexico'
    actual = get_citations_needed_report(url)
    expected = 'There are 5 needed citations for this wiki page'
    assert actual == expected