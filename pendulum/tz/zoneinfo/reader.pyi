# Stubs for pendulum.tz.zoneinfo.reader (Python 3.7)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .exceptions import InvalidTimezone, InvalidZoneinfoFile
from .posix_timezone import PosixTimezone, posix_spec
from .timezone import Timezone
from .transition import Transition
from .transition_type import TransitionType
from collections import namedtuple

_offset = namedtuple('offset', 'utc_total_offset is_dst abbr_idx')

header = namedtuple('header', 'version utclocals stdwalls leaps transitions types abbr_size')

class Reader:
    def __init__(self, extend: bool=...) -> None: ...
    def read_for(self, timezone: str) -> Timezone: ...
    def read(self, file_path: str) -> Timezone: ...
