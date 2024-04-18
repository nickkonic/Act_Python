n = int(input("How many numbers? "))
numbers = []
for i in range(n):
    number = int(input("Input Numbers: "))
    numbers.append(number)

common_divisors = set()
for i in range(1, min(numbers)+1):
    is_divisor = True
    for number in numbers:
        if number % i != 0:
            is_divisor = False
            break
    if is_divisor:
        common_divisors.add(i)

print("DIvisors")
for number in numbers:
    divisors = []
    for i in range(1, number+1):
        if number % i == 0:
            divisors.append(i)
    print(f"{number}: {divisors}")
    
print("COMMON Divisors is/are: ", common_divisors)
