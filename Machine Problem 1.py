import math

print("Calculataing the Area of a Circle")
def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier

def area_of_circle(diameter):
    radius = diameter / 2
    area = math.pi * radius ** 2
    return area

diameter = float(input("Enter the diameter of the circle: "))
area = area_of_circle(diameter)

print("The area of the circle is: ", round_up(area, 2) ,"sq. units")
