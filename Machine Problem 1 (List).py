num1 = int(input("First Number: "))
num2 = int(input("Second Number: "))

nums = [num1, num2]

for i in range(10):
    next_num = nums[-1] + nums[-2]
    nums.append(next_num)

print(nums)
