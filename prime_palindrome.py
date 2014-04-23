#!/usr/local/bin/python3
# Prints the largest prime palindrom under 1000
import math

def is_prime(num):
    if num == 0 or num == 1: # 0 or 1 is no primes
        return False
        
    for i in range(2,int(math.sqrt(num))):
        if num % i == 0:
            return False
    else:
        return True

def is_palindrome(num):
    if str(num) == (str(num)[::-1]):
        return True
    else:
        return False

def main():
    i = 1000
    while i > 0:
        if is_prime(i) and is_palindrome(i):
            print(i)
            break
        i -= 1
        

    
if __name__ == "__main__": main()