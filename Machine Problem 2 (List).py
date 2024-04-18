import random

n = int(input("How many numbers?: "))

nums = list(range(1, 46))
result = random.sample(nums, n)

print(n, "randomly selected nos.")
print(result)
