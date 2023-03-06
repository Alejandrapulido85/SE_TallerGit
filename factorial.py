import sys
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python factorial.py <number>")
        sys.exit(1)
        
    n = int(sys.argv[1])

    result = factorial(n)
    print(result)