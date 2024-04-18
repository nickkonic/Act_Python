num1 = int(input("Enter number: "))
num2 = int(input("Enter number: "))
num3 = int(input("Enter number: "))
num4 = int(input("Enter number: "))
num5 = int(input("Enter number: "))

even = 0
odd = 0

if num1%2:
    even=even+num1
else:
    odd=odd+num1
if num2%2:
    even=even+num2
else:
    odd=odd+num2
if num3%2:
    even=even+num3
else:
    odd=odd+num3
if num4%2:
    even=even+num4
else:
    odd=odd+num4
if num5%2:
    even=even+num5
else:
    odd=odd+num5

print("Sum of all even: ", odd)
print("Sum of all odd: ", even)
