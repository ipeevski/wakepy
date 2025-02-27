"""Common terms and definitions used in many places"""
from .strenum import StrEnum, auto


class PlatformName(StrEnum):
    WINDOWS = auto()
    LINUX = auto()
    MACOS = auto()
    OTHER = auto()


class ModeName(StrEnum):
    """The names of the modes wakepy supports

    See: wakepy/modes/keep.py for full definitions of the modes.
    """

    KEEP_RUNNING = "keep.running"
    KEEP_PRESENTING = "keep.presenting"


class ControlMsg(StrEnum):
    """Send to worker threads"""

    TERMINATE = auto()


class WorkerThreadMsgType(StrEnum):
    """Send from worker threads"""

    OK = auto()
    EXCEPTION = auto()


class BusType(StrEnum):
    """Type of D-Bus bus."""

    SESSION = auto()
    SYSTEM = auto()
