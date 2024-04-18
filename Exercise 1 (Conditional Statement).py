num1 = int(input("Enter number: "))
num2 = int(input("Enter number: "))
num3 = int(input("Enter number: "))
num4 = int(input("Enter number: "))
num5 = int(input("Enter number: "))

smallest = num1
largest = num1

if num2 < smallest:
    smallest = num2
if num3 < smallest:
    smallest = num3
if num4 < smallest:
    smallest = num4
if num5 < smallest:
    smallest = num5
if num2 > largest:
    smallest = num2
if num3 > largest:
    smallest = num3
if num4 > largest:
    smallest = num4
if num5 > largest:
    smallest = num5

print ("The smallest number is ", smallest)
print ("The largest number is ", largest)
