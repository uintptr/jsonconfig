
from typing import Any


class JSONConfig:
    def __init__(self, file_path: str | None = None) -> None:
    def get(self, path: str, default: Any | None = None) -> Any:
    def get_int(self, path: str, default: int | None = None) -> int:
    def get_str(self, path: str, default: str | None = None) -> str:
    def get_float(self, path: str, default: float | None = None) -> float:
    def set(self, path: str, value: Any | None) -> None:
