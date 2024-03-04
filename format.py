#!/usr/bin/env python3

import re
import sys
from datetime import date


EVENTS_HEADING = "## Events"


def err(code: int, msg: str) -> int:
    print(f"Err: {msg}", file=sys.stderr)
    return code


# TODO: I should probably also run this on the PR branch to check if if it
# follows the style. I could set a `ON_MAIN` env variable to only do changes
# if it is done on `main`, otherwise only run it in "inspect" mode.
def main(args: list[str]) -> int:
    if len(args) == 1:
        return err(1, "Argument(s) required.")

    with open(args[1], "r+", encoding="utf-8") as readme:
        header, events_str = readme.read().split(EVENTS_HEADING, 1)
        # FIXME: This breaks if someone forgets to put a new line between events...
        events = [event.strip() for event in events_str.split("\n\n-") if event]

        if len(events) == 1:
            return 0
      
        iso_date_pattern = re.compile(r"(?s).*> Date: (\d\d\d\d-\d\d\-\d\d)", flags=re.S)

        def parse_date(event: str) -> date:
            # FIXME: Could be None. Related with the TODO above.
            match = re.match(iso_date_pattern, event)
            # FIXME: Could be None. Related with the TODO above.
            event_date = match.group(1)
            return date.fromisoformat(event_date)

        readme.seek(0)
        readme.write(header)
        readme.write(EVENTS_HEADING)

        for event in sorted(events, key=parse_date):
            readme.write(f"\n\n-{event}")

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
