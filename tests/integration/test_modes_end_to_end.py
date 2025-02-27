"""End-to-end testing of the whole package. Use different types of Modes.
"""
import pytest

from wakepy.core import CURRENT_PLATFORM
from wakepy.core.method import Method
from wakepy.core.mode import Mode

pytest.skip("These need to be fixed", allow_module_level=True)


class MethodEnterExit(Method):
    supported_platforms = (CURRENT_PLATFORM,)

    def enter_mode(self):
        ...

    def exit_mode(self):
        ...


class HeartBeatMethod(Method):
    supported_platforms = (CURRENT_PLATFORM,)

    def heartbeat(self):
        ...


class MyMode(Mode):
    methods = [MethodEnterExit, HeartBeatMethod]


def test_that_switching_works():
    mode = MyMode()
    with mode as m:
        assert m.success
