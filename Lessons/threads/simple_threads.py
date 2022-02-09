from concurrent.futures import ThreadPoolExecutor
import time
import threading
import os


def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time

        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")

        return result

    return wrapper


@time_it
def task1():
    print("Executing task 1...")
    print("Thread 1 ID:", threading.get_native_id())
    print("Thread 1 process ID:", os.getpid())
    
    time.sleep(2)

    print("Finished task 1")


@time_it
def task2():
    print("Executing task 2...")
    print("Thread 2 ID:", threading.get_native_id())
    print("Thread 1 process ID:", os.getpid())
    
    time.sleep(1)

    print("Finished task 2")


@time_it
def task3():
    print("Executing task 3...")
    print("Thread 3 ID:", threading.get_native_id())
    print("Thread 1 process ID:", os.getpid())
    
    time.sleep(2)

    print("Finished task 3")


@time_it
def main():
    print("Main thread ID:", threading.get_native_id())
    print("Main thread process ID:", os.getpid())

    # task1()
    # task2()
    # task3()

    # Threaded version 1

    # task1_thread = threading.Thread(target=task1)
    # task1_thread.start()

    # task2_thread = threading.Thread(target=task2)
    # task2_thread.start()

    # task3_thread = threading.Thread(target=task3)
    # task3_thread.start()

    # task1_thread.join()
    # task2_thread.join()
    # task3_thread.join()

    # Threaded version 2
    tasks = [task1, task2, task3]
    threads = []

    for task in tasks:
        thread = threading.Thread(target=task)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    # Threaded version 3
    # tasks = [task1, task2, task3, task2, task1, task3, task2]

    # with ThreadPoolExecutor(max_workers=3) as executor:
    #     for task in tasks:
    #         executor.submit(task)

    print("Finished main")


if __name__ == "__main__":
    main()
