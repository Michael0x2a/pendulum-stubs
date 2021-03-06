# Stubs for pendulum.duration (Python 3.7)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import TypeVar, overload, Tuple
from .constants import (
    SECONDS_PER_DAY,
    SECONDS_PER_HOUR,
    SECONDS_PER_MINUTE,
    US_PER_SECOND,
)
from datetime import timedelta
from typing import Any, Optional

_TSelf = TypeVar("_TSelf", bound="Duration")

class Duration(timedelta):
    def __new__(
        cls,
        days: int = ...,
        seconds: int = ...,
        microseconds: int = ...,
        milliseconds: int = ...,
        minutes: int = ...,
        hours: int = ...,
        weeks: int = ...,
        years: int = ...,
        months: int = ...,
    ): ...
    def total_minutes(self) -> float: ...
    def total_hours(self) -> float: ...
    def total_days(self) -> float: ...
    def total_weeks(self) -> float: ...
    def total_seconds(self) -> float: ...
    @property
    def years(self): ...
    @property
    def months(self): ...
    @property
    def weeks(self): ...
    @property
    def days(self): ...
    @property
    def remaining_days(self): ...
    @property
    def hours(self): ...
    @property
    def minutes(self): ...
    @property
    def seconds(self): ...
    @property
    def remaining_seconds(self): ...
    @property
    def microseconds(self): ...
    @property
    def invert(self): ...
    def in_weeks(self): ...
    def in_days(self): ...
    def in_hours(self): ...
    def in_minutes(self): ...
    def in_seconds(self): ...
    def in_words(self, locale: Optional[Any] = ..., separator: str = ...): ...
    def as_timedelta(self): ...
    def __add__(self: _TSelf, other: timedelta) -> _TSelf: ...
    def __radd__(self: _TSelf, other: timedelta) -> _TSelf: ...
    def __sub__(self: _TSelf, other: timedelta) -> _TSelf: ...
    def __neg__(self) -> Duration: ...
    def __mul__(self: _TSelf, other: float) -> _TSelf: ...
    def __rmul__(self: _TSelf, other: float) -> _TSelf: ...
    @overload
    def __floordiv__(self, other: timedelta) -> int: ...
    @overload
    def __floordiv__(self: _TSelf, other: int) -> _TSelf: ...
    @overload
    def __truediv__(self, other: timedelta) -> float: ...
    @overload
    def __truediv__(self: _TSelf, other: float) -> _TSelf: ...
    @overload
    def __div__(self, other: timedelta) -> int: ...
    @overload
    def __div__(self: _TSelf, other: int) -> _TSelf: ...
    def __mod__(self: _TSelf, other: timedelta) -> _TSelf: ...
    def __divmod__(self: _TSelf, other: timedelta) -> Tuple[int, _TSelf]: ...

class AbsoluteDuration(Duration):
    def __new__(
        cls,
        days: int = ...,
        seconds: int = ...,
        microseconds: int = ...,
        milliseconds: int = ...,
        minutes: int = ...,
        hours: int = ...,
        weeks: int = ...,
        years: int = ...,
        months: int = ...,
    ): ...
    def total_seconds(self): ...
    @property
    def invert(self): ...
