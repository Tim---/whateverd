#!/usr/bin/env python3

import logging
import asyncio
from whateverd.service import WhateverInterface
from sdbus import request_default_bus_name_async

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def task(param: str) -> None:
    logger.info(f"starting task: {param}")
    try:
        await asyncio.Future()
    finally:
        logger.info("stopping task")


async def run() -> None:
    intf = WhateverInterface(task)
    await request_default_bus_name_async("org.example.whatever")
    intf.export_to_dbus("/org/example/whatever")
    await asyncio.Future()


def main():
    asyncio.run(run())
