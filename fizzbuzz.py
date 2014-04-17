#!/usr/local/bin/python3
# Fizz buzz test program
"""Usage ./fizzbuzz.py <filename>"""


import sys

def fizzbuzz(num, a, b):
    msg = ""
    if num % a == 0:
        msg += "F"
    if num % b == 0:
        msg += "B"
    return msg or str(num)

def process_input(name):
    infile = open(name, 'r')
    for line in infile:
        variables = line.split()
        N = int(variables[2])
        for i in range(1, N):
            print(fizzbuzz(i, int(variables[0]), int(variables[1])), end=' ')
        print(fizzbuzz(N, int(variables[0]), int(variables[1])))

def main():
    if len(sys.argv) <= 1:
        sys.exit(__doc__)    
    file_name = sys.argv[1]
    process_input(file_name)

if __name__ == "__main__": main()