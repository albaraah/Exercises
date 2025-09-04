import random
dice_roll = int(input("How many dice to roll?:\n"))
total_num = 0
for dice in range(dice_roll):
    total_num += random.randint(1,6)
print(f"The sum of numbers is {total_num}")

numbers = []
while True:
    number = input("Enter your number:")
    if number == "":
        break
    numbers += [int(number)]
numbers.sort(reverse=True)
for five_greatest in numbers[:5]:
 print(f"{five_greatest}")

integer = int(input("Enter an integer:"))
if integer < 2:
    print("This is not a prime number")
else:
 for i in range(2,integer):
    if integer % i == 0:
        print("This is not a prime number")
        break
 else:
    print("This is a prime number")


cities = []
for i in range (1,6):
    city = input(f"Enter the name of a city {i}:")
    cities.append(city)

print("These are the cities you entered:")
for city in cities:
    print(f" {city}")