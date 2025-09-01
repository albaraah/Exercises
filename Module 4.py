a = 3
while 1<a<1000:
    print(a)
    a = a + 3

while True:
 inch = float(input("Write a positive value in inches:\n"))
 value = 2.54*inch
 if inch < 0:
     print("Program ended")
     break
 elif inch >= 0:
     print(f"{value} centimeters")

num1 = input("What is your number?:\n")
if num1 =="":
    print("You didn't type any numbers.")
else:
    num1 = float(num1)
    smallest = num1
    largest = num1
    while True:
        number = input("What is your number?:\n")
        if number == "":
            break
        number = float(number)
        if number < smallest:
            smallest = number
        if number > largest:
            largest = number
    print(f"Smallest number: {smallest}")
    print(f"Largest number: {largest}")

import random
number = random.randint (1,10)
while True:
    user_number = int(input("What is your number?:\n"))
    if user_number > number:
        print("Too high")
    elif user_number < number:
        print("Too low")
    else:
        print("Correct")
        break

attempts = 0
maximum_attempts = 5
while attempts < maximum_attempts:
    username = input("What is your username?:\n")
    password= input("What is your password?:\n")
    if (username == "python" and password != "rules") or (username != "python" and password == "rules") or (username != "python" and password != "rules"):
        attempts = attempts + 1
        print("Try again")
    else:
        print("Welcome")
        break
if attempts == maximum_attempts:
    print("Access denied!")

import random
N = int(input("How many points to generate?:\n"))
n = 0
points = N
while True:
    if N == 0:
        break
    x = random.randint(-10000, 10000) / 10000
    y = random.randint(-10000, 10000) / 10000
    if x**2 + y**2<1:
        n = n + 1
    N = N - 1
pi_value = 4 * n / points
print(f"pi value : {pi_value}")
