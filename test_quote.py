import pytest
from quotes import get_random_quote, get_all_quotes, count_quotes

def test_random_quote_not_empty():
    quote = get_random_quote()
    assert quote is not None

def test_random_quote_has_text():
    quote = get_random_quote()
    assert len(quote["quote"]) > 0

def test_get_all_quotes():
    all_quotes = get_all_quotes()
    assert len(all_quotes) > 0

def test_count_quotes():
    assert count_quotes() == 5
