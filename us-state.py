#! /usr/bin/env python3

import re

import util


URL = (
    "https://en.wikipedia.org/wiki/"
    + "List_of_U.S._state_and_territory_abbreviations"
    + "?action=raw&section=1"
)
CACHE = "article.wiki"
COLUMNS = ["Abbreviation", "State"]
ABBREV = re.compile(r"\|([A-Z]{2})\|")
STATE = re.compile(r"\|\{\{flag\|([A-Za-z ]+)\}\}\|")


def scrape():
    for line in open(util.get_cache_file(CACHE, URL)):
        abbrev, state = ABBREV.search(line), STATE.search(line)
        if abbrev and state and abbrev != "US":
            abbrev, state = abbrev.group(1), state.group(1)
            yield abbrev, state


if __name__ == "__main__":
    util.write_csv(COLUMNS, scrape())
