import asyncio
import time
import sys

async def say1():
    await asyncio.sleep(1)
    print ("Hello 1!", time.time()-t0)
    sys.stdout.flush()

async def say2():
    await asyncio.sleep(1)
    print ("Hello 2!", time.time()-t0)
    sys.stdout.flush()

print ("start")
loop = asyncio.get_event_loop()
t0 = time.time()
loop.run_until_complete(asyncio.gather(
    say1(),
    say2()
))
print ("done")

loop.close()
