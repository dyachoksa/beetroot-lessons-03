"""
Write a function called oops that explicitly raises an IndexError exception when called. 
Then write another function that calls oops inside a try/except state­ment to catch the error. 
What happens if you change oops to raise KeyError instead of IndexError?
"""


def oops():
    raise IndexError()


def main():
    try:
        oops()
    except IndexError:
        print("Got an IndexError error")


main()
