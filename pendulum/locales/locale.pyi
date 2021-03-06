# Stubs for pendulum.locales.locale (Python 3.7)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional, Union

class Locale:
    def __init__(self, locale: str, data: Any) -> None: ...
    @classmethod
    def load(cls: Any, locale: Union[str, Locale]) -> Locale: ...
    @classmethod
    def normalize_locale(cls: Any, locale: str) -> str: ...
    def get(self, key: str, default: Optional[Any] = ...) -> Any: ...
    def translation(self, key: str) -> Any: ...
    def plural(self, number: int) -> str: ...
    def ordinal(self, number: int) -> str: ...
    def ordinalize(self, number: int) -> str: ...
    def match_translation(self, key: Any, value: Any): ...
