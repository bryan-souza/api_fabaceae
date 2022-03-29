from typing import Optional


class AcessViolationError(Exception):
    def __init__(self, message: Optional[str] = '') -> None:
        self.message = message
