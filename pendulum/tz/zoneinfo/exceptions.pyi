# Stubs for pendulum.tz.zoneinfo.exceptions (Python 3.7)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class ZoneinfoError(Exception): ...
class InvalidZoneinfoFile(ZoneinfoError): ...

class InvalidTimezone(ZoneinfoError):
    def __init__(self, name: Any) -> None: ...

class InvalidPosixSpec(ZoneinfoError):
    def __init__(self, spec: Any) -> None: ...
