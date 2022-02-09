import multiprocessing
import time
import math


def calculate(i):
    start_time = time.perf_counter()
    print(f"Calculating formula #{i}")
    
    result = 0
    for n in range(10_000):
        result += n**3 + math.isqrt(n) + math.factorial(n)

    print(f"End calculating formula #{i}")
    end_time = time.perf_counter()
    run_time = end_time - start_time
    print(f"Finished {calculate.__name__!r} with arguments {i!r} in {run_time:.4f} secs")
    return result


def main():
    start_time = time.perf_counter()
    ps = []

    for i in range(5):
        p = multiprocessing.Process(target=calculate, args=(i+1,))
        p.start()
        ps.append(p)

    for p in ps:
        p.join()

    end_time = time.perf_counter()
    run_time = end_time - start_time
    print(f"Finished {main.__name__!r} in {run_time:.4f} secs")


if __name__ == "__main__":
    main()
