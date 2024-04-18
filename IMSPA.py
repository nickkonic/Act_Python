def find_prime_factors(n):
    factors = []
    divisor = 2
    while divisor <= n:
        if n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        else:
            divisor += 1
    return factors

def find_common_prime_factors(a, b):
    prime_factors_a = find_prime_factors(a)
    prime_factors_b = find_prime_factors(b)
    common_factors = set(prime_factors_a) & set(prime_factors_b)
    return list(common_factors)

def gcd_middle_school(a, b):
    prime_factors_a = find_prime_factors(a)
    prime_factors_b = find_prime_factors(b)
    common_factors = find_common_prime_factors(a, b)
    
    print(f"Prime factors of {a}: {prime_factors_a}")
    print(f"Prime factors of {b}: {prime_factors_b}")
    print(f"Common prime factors: {common_factors}")
    
    gcd = 1
    for factor in common_factors:
        gcd *= factor
    
    return gcd

num1 = 120
num2 = 45
result = gcd_middle_school(num1, num2)
print(f"GCD of {num1} and {num2} is {result}")