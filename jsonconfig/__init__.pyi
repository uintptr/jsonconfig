
from typing import Any, TypeVar

T = TypeVar('T')


class JSONConfig:
    def __init__(self, file_path: str | None = None) -> None: ...
    def get(self, path: str, default: Any | None = None) -> Any: ...
    def get_bool(self, path: str, default: bool | None = None) -> bool: ...
    def get_int(self, path: str, default: int | None = None) -> int: ...
    def get_str(self, path: str, default: str | None = None) -> str: ...
    def get_float(self, path: str, default: float | None = None) -> float: ...
    def get_list(self, path: str, default: list[Any] | None) -> list[Any]: ...
    def set(self, path: str, value: Any | None) -> None: ...
