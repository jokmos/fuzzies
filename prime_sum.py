#!/usr/local/bin/python3
# Sum of the first 1000 primes

def is_prime(num):
    if num == 0 or num == 1: # 0 or 1 is no primes
        return False
        
    for i in range(2,num):
        if num % i == 0:
            return False
    else:
        return True

def main():
    sum, i, primes = 0, 0, 0
    while primes < 1000:
        if is_prime(i):
            sum += i
            primes += 1
        i += 1
    print(sum)
        

    
if __name__ == "__main__": main()