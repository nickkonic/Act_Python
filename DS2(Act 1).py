def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def calculate_permutations(n, r):
    return factorial(n) // factorial(n - r)

def calculate_combinations(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

numbers = [3, 2, 1]
r = 2

permutations_count = calculate_permutations(len(numbers), r)
combinations_count = calculate_combinations(len(numbers), r)

print(f'There are {permutations_count} ways to permute {r} numbers from {numbers}.')
print(f'There are {combinations_count} ways to combine {r} numbers from {numbers}.')
