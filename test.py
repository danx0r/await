import asyncio
import time

def write(msg):
    print(msg, flush=True)

async def say1():
    await asyncio.sleep(1)
    write("Hello 1!")

async def say2():
    await asyncio.sleep(1)
    write("Hello 2!")

write("start")
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(
    say1(),
    say2()
))
write("exit")

loop.close()
