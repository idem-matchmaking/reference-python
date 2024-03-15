from enum import Enum


class PlayerStatusEnum(str, Enum):
    MATCHED = "matched"
    WAITING = "waiting"

    def __str__(self) -> str:
        return str(self.value)
