#!/usr/bin/env python3
"""
ICS linter for UA Military & Defenders Calendar.

Checks:
- Each .ics file parses as a VCALENDAR.
- Each VEVENT has required properties (UID, SUMMARY, DTSTART).
- UIDs are unique within a file.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Iterable

from icalendar import Calendar
from icalendar.cal import Component


CALENDARS_DIR = Path("calendars")
REQUIRED_EVENT_PROPERTIES: tuple[str, ...] = ("UID", "SUMMARY", "DTSTART")


def find_ics_files(root: Path) -> list[Path]:
    """Return a sorted list of all .ics files under the given root directory."""
    return sorted(path for path in root.rglob("*.ics") if path.is_file())


def load_calendar(file_path: Path) -> Calendar | None:
    """
    Load and parse an ICS file.

    Returns:
        Calendar instance if valid VCALENDAR, otherwise None (with error printed).
    """
    try:
        ics_content = file_path.read_text(encoding="utf-8")
    except Exception as exc:  # noqa: BLE001
        print(f"{file_path}: read error: {exc}")
        return None

    try:
        component: Component = Calendar.from_ical(ics_content)
    except Exception as exc:  # noqa: BLE001
        print(f"{file_path}: parse error: {exc}")
        return None

    if not isinstance(component, Calendar):
        # Technically from_ical can return any Component; we require VCALENDAR.
        print(
            f"{file_path}: top-level component is '{component.name}', "
            f"expected 'VCALENDAR'"
        )
        return None

    return component


def iter_event_components(calendar: Calendar) -> Iterable[Component]:
    """Yield all VEVENT components from the given calendar."""
    # walk(name="VEVENT") returns only VEVENT components.
    return calendar.walk(name="VEVENT")


def validate_event_properties(
    file_path: Path,
    event: Component,
    seen_uids: set[str],
) -> list[str]:
    """Validate VEVENT required properties and UID uniqueness."""
    errors: list[str] = []

    # Required properties
    for prop_name in REQUIRED_EVENT_PROPERTIES:
        if prop_name not in event:
            errors.append(f"{file_path}: VEVENT missing {prop_name}")

    # UID
    uid_raw = event.get("UID")
    uid = str(uid_raw).strip() if uid_raw is not None else ""

    if not uid:
        errors.append(f"{file_path}: VEVENT without UID")
    elif uid in seen_uids:
        errors.append(f"{file_path}: duplicate UID: {uid}")
    else:
        seen_uids.add(uid)

    return errors


def lint_calendar(file_path: Path, calendar: Calendar) -> bool:
    """
    Lint a single calendar file.

    Returns:
        True if file passes all checks, False otherwise.
    """
    errors: list[str] = []

    if calendar.name != "VCALENDAR":
        errors.append(
            f"{file_path}: invalid top-level component: '{calendar.name}', "
            f"expected 'VCALENDAR'"
        )

    seen_uids: set[str] = set()

    for event in iter_event_components(calendar):
        errors.extend(validate_event_properties(file_path, event, seen_uids))

    if errors:
        print("\n".join(errors))
        return False

    print(f"{file_path}: OK")
    return True


def main() -> int:
    if not CALENDARS_DIR.is_dir():
        print(f"'{CALENDARS_DIR}' directory not found", file=sys.stderr)
        return 1

    ics_files = find_ics_files(CALENDARS_DIR)
    if not ics_files:
        print(f"No .ics files found in '{CALENDARS_DIR}'", file=sys.stderr)
        return 1

    has_errors = False

    for file_path in ics_files:
        calendar = load_calendar(file_path)
        if calendar is None:
            has_errors = True
            continue

        if not lint_calendar(file_path, calendar):
            has_errors = True

    if has_errors:
        print("ICS lint failed.", file=sys.stderr)
        return 1

    print("All ICS files passed lint.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
