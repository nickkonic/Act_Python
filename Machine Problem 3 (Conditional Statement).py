num1 = int(input("enter hours worked: "))
num2 = int(input("enter rate per hour: " ))

over_time = 0 
basic_pay = num1 * num2 

if num1 >= 40:
  over_time = 1000
 
incentives = over_time * 0.2 
net_salary = basic_pay + incentives 

print("basic pay" , basic_pay)
print("overtime" , over_time) 
print("incentive" , incentives)
print("net salary" , net_salary)
