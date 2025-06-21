from datetime import date, datetime, time
from typing import Any, Optional, Sequence

import click


class Date(click.DateTime):
    name = "date"

    def __init__(self, formats: Optional[Sequence[str]] = None):
        super().__init__(formats or ["%Y-%m-%d"])

    def _try_to_convert_date(self, value: Any, format: str) -> Optional[date]:  # type: ignore[override]
        try:
            return datetime.strptime(value, format).date()
        except ValueError:
            return None

    def __repr__(self) -> str:
        return "Date"


class Time(click.DateTime):
    name = "time"

    def __init__(self, formats: Optional[Sequence[str]] = None):
        super().__init__(formats or ["%H:%M", "%H:%M:%S"])

    def _try_to_convert_date(self, value: Any, format: str) -> Optional[time]:  # type: ignore[override]
        try:
            return datetime.strptime(value, format).time()
        except ValueError:
            return None

    def __repr__(self) -> str:
        return "Time"
