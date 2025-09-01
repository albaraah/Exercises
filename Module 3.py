length = int(input("What is the zander's length?:\n"))
remaining = 42-length
if length < 42:
    print(f"Release the fish back into the lake, the caught fish is {remaining} centimeter below the size limit")


cabin_class = input("What is the cabin class of the cruise ship?:\n")
if cabin_class == "LUX":
    print("It's an upper-deck cabin with a balcony.")
elif cabin_class == "A":
    print("It's an above the car deck, equipped with a window.")
elif cabin_class == "B":
    print("It's a windowless cabin above the car deck.")
elif cabin_class == "C":
    print("It's a windowless cabin below the car deck.")
else:
    print("Invalid cabin class.")


biological_gender = input("What is your biological gender?:\n")
hemoglobin_value = int(input("What is your hemoglobin value in g/l?:\n"))
if biological_gender == "male" and hemoglobin_value < 134:
    print("Low")
elif biological_gender == "male" and hemoglobin_value > 167:
    print("High")
elif biological_gender == "male" and 134<= hemoglobin_value <= 167:
    print("Normal")
if biological_gender == "female" and hemoglobin_value < 117:
    print("Low")
elif biological_gender == "female" and hemoglobin_value > 155:
    print("High")
elif biological_gender == "female" and 117 <= hemoglobin_value <= 155 :
    print("Normal")


year = int(input("Enter a year:\n"))
if year % 4 == 0 and year % 100 == 0 and year % 400 != 0:
    print("This is not a leap year")
elif year % 4 == 0 and year % 100 != 0:
    print("This is a leap year")
elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
    print("This is a leap year")
else:
    print("This is not a leap year")