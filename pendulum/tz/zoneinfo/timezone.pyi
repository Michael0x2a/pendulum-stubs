# Stubs for pendulum.tz.zoneinfo.timezone (Python 3.7)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .posix_timezone import PosixTimezone
from .transition import Transition
from .transition_type import TransitionType
from typing import List, Optional

class Timezone:
    def __init__(self, transitions: List[Transition], posix_rule: Optional[PosixTimezone]=..., extended: bool=...) -> None: ...
    @property
    def transitions(self) -> List[Transition]: ...
    @property
    def posix_rule(self): ...
