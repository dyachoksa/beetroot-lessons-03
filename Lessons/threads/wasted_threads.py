import time
import threading
import math


def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time

        print(f"Finished {func.__name__!r} with arguments {args!r} in {run_time:.4f} secs")

        return result

    return wrapper


@time_it
def calculate(i):
    print(f"Calculating formula #{i}")
    
    result = 0
    for n in range(10_000):
        result += n**3 + math.isqrt(n) + math.factorial(n)

    print(f"End calculating formula #{i}")
    return result


@time_it
def main():
    threads = []

    for i in range(5):
        thread = threading.Thread(target=calculate, args=(i+1,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()
