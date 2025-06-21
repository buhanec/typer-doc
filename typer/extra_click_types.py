import sys
from datetime import date, datetime, time
from typing import Any, Dict, Optional, Sequence

import click

if sys.version_info < (3, 9):
    from backports import zoneinfo
else:
    import zoneinfo

try:
    import pytz
except ImportError:
    pytz = None  # type: ignore


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


class ZoneInfo(click.ParamType):
    name = "timezone"

    def to_info_dict(self) -> Dict[str, Any]:
        info_dict = super().to_info_dict()
        info_dict["available_timezones"] = zoneinfo.available_timezones()
        return info_dict

    def convert(
        self,
        value: Any,
        param: Optional[click.Parameter],
        ctx: Optional[click.Context],
    ) -> Any:
        if isinstance(value, zoneinfo.ZoneInfo):
            return value
        try:
            return zoneinfo.ZoneInfo(value)
        except zoneinfo.ZoneInfoNotFoundError:
            self.fail(f"Unknown timezone {value}", param, ctx)

    def __repr__(self) -> str:
        return "ZoneInfo"


class PytzTimezone(click.ParamType):
    name = "timezone"

    def to_info_dict(self) -> Dict[str, Any]:
        info_dict = super().to_info_dict()
        info_dict["available_timezones"] = list(pytz.all_timezones)
        return info_dict

    def convert(
        self,
        value: Any,
        param: Optional[click.Parameter],
        ctx: Optional[click.Context],
    ) -> Any:
        if isinstance(value, pytz.BaseTzInfo):
            return value
        try:
            return pytz.timezone(value)
        except pytz.UnknownTimeZoneError:
            try:
                offset = int(value)
            except ValueError:
                self.fail(f"Unknown timezone or bad offset: {value}", param, ctx)
            else:
                return pytz.FixedOffset(offset)

    def __repr__(self) -> str:
        return "PytzTimezone"
