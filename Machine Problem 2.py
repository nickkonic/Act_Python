print("Computing Net Salary")

num1 = float (input("No. of Hours Worked: "))
num2 = float (input("Rate per Hour: "))

sss = 0.02
pagibig = 0.01
tax = 0.05

salary = num1 * num2
a = salary * sss
b = salary * pagibig
c = salary - a - b
d = c * tax
e = c - d

print("Computed Salary is ", (salary))
print("SSS Contribution is ", (a))
print("Pag-Ibig Contribution is ", (b))
print("Tax is ", (d))
print("NET Salary is ", (e))
