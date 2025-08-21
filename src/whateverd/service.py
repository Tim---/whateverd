import asyncio
from collections.abc import Callable, Coroutine
from typing import Optional
from sdbus import (
    DbusInterfaceCommonAsync,
    DbusFailedError,
    dbus_property_async,
    dbus_method_async,
)


class WhateverInterface(
    DbusInterfaceCommonAsync, interface_name="org.example.whatever"
):
    def __init__(self, func: Callable[[str], Coroutine[None, None, None]]):
        super().__init__()
        self.func = func
        self.task: Optional[asyncio.Future[None]] = None

    @dbus_method_async("s", "")
    async def start(self, param: str) -> None:
        if self.task:
            raise DbusFailedError()
        s = self.func(param)
        self.task = asyncio.create_task(s)

    @dbus_property_async("b")
    def running(self) -> bool:
        return self.task is not None

    @dbus_method_async("", "")
    async def stop(self) -> None:
        if not self.task:
            raise DbusFailedError()
        self.task.cancel()
        self.task = None
