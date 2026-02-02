import sys


def factorial(n):
    if n == 0:
        return 1 #until it becomes 1
    else:
        return n * factorial(n-1) #operation that needs to recur

def main():
    sys.setrecursionlimit(2000) #do NOT use this. This is for Demo only
    num = int(input("Enter a number: "))
    print("Factorial:",factorial(num))
    

if __name__ == "__main__":
    main()