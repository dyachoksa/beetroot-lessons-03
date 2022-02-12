import asyncio
import threading
import os

async def main():
    print("Start of main()")
    print("Process id:", os.getpid())
    print("Thread id:", threading.get_native_id())

    # do something usefull here
    print("Hello!")
    await asyncio.sleep(2)
    print("World!")

    print("End of main()")

if __name__ == "__main__":
    print("Process id:", os.getpid())
    print("Thread id:", threading.get_native_id())
    asyncio.run(main())
