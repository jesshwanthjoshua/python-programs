print("Welcome to the Roller Coaster Program.")

height = int(input("Please enter your height in cm: "))
bill = 0

if height > 120:
  print("You are allowed to ride the roller coaster.")
  age = int(input("Please enter your age: "))
  if age < 12:
    bill = 5
  elif age >= 12 and age < 18:
    bill = 7
  elif age >= 18:
    if age >= 45 and age <= 55:
      bill = 0
    else:
      bill = 12

  photo = input ("Type y to take photo, or n to not take photo: ")
  if photo == "y":
    bill += 3
  
  print(f"Your total bill is {bill}$")
else:
  print("You are not allowed to ride the roller coaster.")
