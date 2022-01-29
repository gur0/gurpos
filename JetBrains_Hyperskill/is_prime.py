n = int(input())

def print_prime(f):
    if f:
        print("This number is prime")
    else:
        print("This number is not prime")

def is_prime(num):
    if num <= 1:
        return False
    
    if num in (2, 3):
        return True
        
    count = 0
    for i in range(2, num + 1):
        if (num % i) == 0:
            count += 1
    if count == 1:
        return True
    return False

print_prime(is_prime(n))
