# 5! = 5*4*3*2*1
# 4! = 4*3*2*1
# 2! = 2*1
# 1! = 1
# n! = n*(n-1)!

def fact(n):
    if n == 1: return 1

    return n * fact(n-1)

def fact_plain(n):
    result = 1
    for num in range(n, 1, -1):
        result *= num
    
    return result

if __name__ == "__main__":
    print("5! =", fact(5))
    print("5! =", fact_plain(5))
    print("10! =", fact(10))
