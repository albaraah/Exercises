import random
def ran_dice():
    return random.randint(1,6)

while True:
    result = random.randint(1,6)
    print(result)
    if result == 6:
        print("You got 6")
        break




import random
def ran_dice(side):
    return random.randint(1,21)
while True:
    side = random.randint(1,21)
    print(side)
    if side == 21:
        break


def quantity_of_gasoline(gallons):
    liters = 3.8 * gallons
    return (liters)
while True:
    gallons = int(input("What is the volume in American gallons? "))
    if (gallons)<0:
        break
    liters = quantity_of_gasoline(gallons)
    print(liters,"liters")



lst = [5, 9 ,8 ,17]
def sum_lst(nums):
    total = 0
    for n in nums:
       total += n
    return total
print(sum_lst(lst))



lst1 = [13, 7, 99, 22, 15, 12, 3]
lst2 = []
def even_nums(nums):
    for i in nums:
        if i%2 == 0:
            lst2.append(i)
    return lst2
print(even_nums(lst1))


import math
def pizza1(diameter_cm, price):
    diameter_m = diameter_cm / 100
    surface = math.pi * (diameter_m/2)**2
    unit_price = price  / surface
    return unit_price
def pizza2(diameter_cm2, price2):
    diameter_m2 = diameter_cm2 / 100
    surface2 = math.pi * (diameter_m2/2)**2
    unit_price = price2  / surface2
    return unit_price
diameter_cm = float(input("What is the diameter of the first pizza in cm?: "))
price = float(input("What is the price of the first pizza in euros?: "))
print("The unit price of the first pizza is:", pizza1(diameter_cm, price))
diameter_cm2 = float(input("What is the diameter of the second pizza in cm?: "))
price2 = float(input("What is the price of the second pizza in euros?: "))
print("The unit price of the second pizza is:", pizza2(diameter_cm2, price2))
if pizza1(diameter_cm, price) < pizza2(diameter_cm2, price2):
    print("The first pizza provides better value for the money.")
elif pizza1(diameter_cm, price) > pizza2(diameter_cm2, price2):
    print("The second pizza provides better value for the money.")
else:
    print("Both pizzas provide the same value.")



