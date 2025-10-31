myname = input("What is your name?:")
if myname == "Albaraae":
    print("Hello, ALbaraae!")

import math
radius = float(input("What is the radius of the circle?:"))
area = math.pi*radius**2
print(f"the area of the circle is: {area}")


length = x = float(input("What is the length of the rectangle?:"))
width = y = float(input("What is the width of the rectangle?:"))
perimeter = x*2 + y*2
area = x*y
print(f"The perimeter of the rectangle is:{perimeter}")
print(f"The area of the rectangle is:{area}")

a = int(input("Give me an integer:\n"))
b = int(input("Give me an integer:\n"))
c = int(input("Give me an integer:\n"))
sum = a + b + c
product = a*b*c
average = sum/3
print(f"The sum of the integers is:{sum}")
print(f"The products of the integers is:{product}")
print(f"The average of the integers is:{average}")
import math
from traceback import FrameSummary

talents = float(input("Enter talents:\n"))
pounds = float(input("Enter pounds:\n"))
lots = float(input("Enter lots:\n"))
a = poundspertalent = 20
b = lotsperpound = 32
c = gramsperlots = 13.3
gram = (talents*a*b*c + pounds*b*c + lots*c)
kilograms = int(gram//1000)
grams = gram%1000
print(f"The weight in modern units is: {kilograms} kilograms and {grams:.2f} grams")

import random
nm1 = random.randint(0, 9)
nm2 = random.randint(0, 9)
nm3 = random.randint(0, 9)
nm4 = random.randint(1, 6)
nm5 = random.randint(1, 6)
nm6 = random.randint(1, 6)
nm7 = random.randint(1, 6)
print(f"first code is: {nm1} {nm2} {nm3}")
print(f"second code is: {nm4} {nm5} {nm6} {nm7}")