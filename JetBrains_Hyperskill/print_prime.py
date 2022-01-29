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

prime_number = [n for n in range(2, 1001) if is_prime(n)]

prime_number = [n for n in range(2, 1001) if all(n % i != 0 for i in range(2, n))]