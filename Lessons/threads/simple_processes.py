import multiprocessing
import os


def info(message):
    print(message)
    print("Process ID:", os.getpid())
    print("Parent process ID:", os.getppid())


def task(name):
    info("Running task()...")
    print("Doing usefull calculation for {}".format(name))


def main():
    info("Running main()...")
    p = multiprocessing.Process(target=task, args=("Sergey",))
    p.start()
    p.join()


if __name__ == "__main__":
    main()
