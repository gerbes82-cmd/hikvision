import asyncio
from hikvision import fetch


async def run():
    while True:
        fetch()
        await asyncio.sleep(60)
