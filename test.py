import asyncio


async def task_func():
    print('in task_func')
    await asyncio.sleep(3)
    return 'the result'


async def main(loop):
    print('creating task')
    task = asyncio.create_task(task_func())
    print('waiting for {!r}'.format(task))
    return_value = await task
    print('task completed {!r}'.format(task))
    print('return value: {!r}'.format(return_value))


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(event_loop))
finally:
    event_loop.close()

