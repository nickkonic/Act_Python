import time

def gcd_consecutive(m, n):
    smaller = min(m, n)
    for i in range(smaller, 0, -1):
        if m % i == 0 and n % i == 0:
            return i

def gcd_euclidean(m, n):
    while n:
        m, n = n, m % n
    return m

m, n = 31415, 14142

start_time = time.time()
result_consecutive = gcd_consecutive(m, n)
end_time = time.time()
consecutive_time = end_time - start_time

start_time = time.time()
result = gcd_euclidean(m, n)
end_time = time.time()
euclidean_time = end_time - start_time

sum = 14142 / 7
rounded_num =round(sum)

print(f"GCD by Consecutive Integer Algorithm: {result}")
print(f"Time taken by Consecutive Integer Algorithm: {consecutive_time} seconds")
print(f"\nGCD by Euclidean Algorithm: {result}")
print(f"Time taken by Euclidean Algorithm: {euclidean_time} seconds")
print(rounded_num, "times faster")


