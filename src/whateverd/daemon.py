#!/usr/bin/env python3

import asyncio
from whateverd.service import WhateverInterface
from sdbus import request_default_bus_name_async


async def task(param: str) -> None:
    print(f"starting task: {param}")
    try:
        await asyncio.Future()
    finally:
        print("stopping task")


async def run() -> None:
    intf = WhateverInterface(task)
    await request_default_bus_name_async("org.example.whatever")
    intf.export_to_dbus("/org/example/whatever")
    await asyncio.Future()


def main():
    asyncio.run(run())
