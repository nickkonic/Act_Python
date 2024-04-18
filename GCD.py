def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def gcd_of_list(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result = gcd(result, num)
    return result

num_of_integers = int(input("No. of Integers: "))
numbers = []
for i in range(num_of_integers):
    num = int(input(f"Input Number {i+1}: "))
    numbers.append(num)

result_gcd = gcd_of_list(numbers)
print(f"The GCD is {result_gcd}")
