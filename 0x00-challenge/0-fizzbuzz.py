#!/usr/bin/env python

# 0x00-challenge/0-fizzbuzz.py

def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz"),
        elif i % 3 == 0:
            print("Fizz"),
        elif i % 5 == 0:
            print("Buzz"),
        else:
            print(i),

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python 0-fizzbuzz.py <number>")
        sys.exit(1)
    n = int(sys.argv[1])
    fizzbuzz(n)

