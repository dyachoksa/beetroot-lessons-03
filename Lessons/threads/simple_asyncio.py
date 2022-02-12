import asyncio
import time
import threading
import os
import random


def time_it(func):
    async def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = await func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time

        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")

        return result

    return wrapper


def info():
    print("process id:", os.getpid())
    print("thread id", threading.get_native_id())


async def sleep(delay):
    await asyncio.sleep(delay)
    return delay


@time_it
async def task(task_id, delay):
    print("starting task with id:", task_id)
    info()

    # doing something usefull
    result = await sleep(delay)

    print("finished task with id:", task_id)
    return result


@time_it
async def main():
    # await asyncio.gather(
    #     task(1, random.randint(1, 5)),
    #     task(2, random.randint(1, 5)),
    #     task(3, random.randint(1, 5))
    # )

    tasks = [task(idx, random.randint(1, 5)) for idx in range(1, 4)]
    
    result = await asyncio.gather(*tasks)
    
    print(result)
    print(sum(result))


if __name__ == "__main__":
    asyncio.run(main())
