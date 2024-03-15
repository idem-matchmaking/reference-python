from enum import Enum


class FactionEnum(str, Enum):
    GRELL = "grell"
    LEGION = "legion"
    PROTECTORAT = "protectorat"
    XOL = "xol"

    def __str__(self) -> str:
        return str(self.value)
