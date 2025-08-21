#!/usr/bin/env python3

import asyncio
import argparse
from whateverd.service import WhateverInterface


class WhateverClient(WhateverInterface):
    def __init__(self) -> None:
        self._proxify("org.example.whatever", "/org/example/whatever")


async def start(client: WhateverClient, args: argparse.Namespace):
    await client.start(args.command)


async def status(client: WhateverClient, args: argparse.Namespace):
    if await client.running:
        print("running")
    else:
        print("not running")


async def stop(client: WhateverClient, args: argparse.Namespace):
    await client.stop()


async def run():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(required=True)
    parser_start = subparsers.add_parser("start")
    parser_start.set_defaults(func=start)
    parser_start.add_argument("command")
    parser_status = subparsers.add_parser("status")
    parser_status.set_defaults(func=status)
    parser_stop = subparsers.add_parser("stop")
    parser_stop.set_defaults(func=stop)

    args = parser.parse_args()
    client = WhateverClient()
    await args.func(client, args)


def main():
    asyncio.run(run())
