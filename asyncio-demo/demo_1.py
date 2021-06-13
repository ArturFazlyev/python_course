import asyncio

from loguru import logger


async def foo():
    logger.info("foo start")
    await asyncio.sleep(.1)
    logger.info("foo finish")


async def bar():
    logger.info("bar start")
    await asyncio.sleep(.1)
    logger.info("bar finish")


def run_main_async():
    logger.info("Starting main")
    coros = [
        foo(),
        bar()
    ]
    coro = asyncio.wait(coros)
    asyncio.run(coro)
    logger.info("Starting finish")


if __name__ == '__main__':
    run_main_async()
