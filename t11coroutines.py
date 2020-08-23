# Use asyncio library to define coroutines via 'async def'.
# The result is a coroutine object, and you can then use 'await future'
# to suspend the coroutine and await for future to return.
# You can also await another coroutine. A coroutine object is not
# running until an event loop is running.
#
# Similar to JS promises.

import asyncio


async def compute(future):
    print("Starting...")

    res = await answer()
    future.set_result(res)


async def answer():
    await asyncio.sleep(1)
    return 42


def coroutines():
    f = asyncio.Future()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(compute(f))
    loop.close()

    print(f.result())
