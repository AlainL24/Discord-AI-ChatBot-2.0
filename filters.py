BAD_SITES = [
    "dictionary",
    "thesaurus",
    "grammar",
    "writingcenter",
    "merriam-webster",
    "punctuation",
    "vocabulary"
]


TRUSTED_DOMAINS = [
    "espn.com",
    "nba.com",
    "weather.gov",
    "noaa.gov",
    "reuters.com",
    "bbc.com",
    "nytimes.com"
]


def is_valid_source(title, url):
    """
    Filter out irrelevant websites like dictionaries or grammar pages.
    """

    text = (title + url).lower()

    for word in BAD_SITES:
        if word in text:
            return False

    return True
