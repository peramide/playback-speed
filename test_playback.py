import pytest 

from playback import playback

def main():
    test_playback()

def test_playback():
    assert playback("This is CS50") == "This...is...CS50"