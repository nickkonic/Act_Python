import itertools
import math

items = [1, 2, 3, 4]
perms = itertools.permutations(items)
for perm in perms:
    print("Permutation", perm)

combs = itertools.combinations(items, 2)
for comb in combs:
    print("Combination", comb)

n = 5
fact = math.factorial(n)
print("Factorial", fact)

n = 5
k = 2
coeff = math.comb(n, k)
print("binomial coefficients", coeff)

