import math

def is_prime_list(numbers):
    def is_prime(n):
        if n < 2: 
            return False
        if n == 2: 
            return True
        if n % 2 == 0:  
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):  
            if n % i == 0:
                return False
        return True
    
    return [is_prime(num) for num in numbers]  