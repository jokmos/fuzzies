#!/usr/local/bin/python3

def is_prime(num):
    if num == 0:
        return False
    elif num == 1:
        return True
        
    for i in range(2,num):
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
    last_prime = 1
    i = 1000
    while i > 0:
        if is_prime(i) and is_palindrome(i):
            print(i)
            break
        i -= 1
        

    
if __name__ == "__main__": main()