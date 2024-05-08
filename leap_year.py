year = int(input())

quo = year /100
if year % 4 == 0:
  if quo % 4 == 0:
    print("Leap year")
  elif quo % 4 != 0 and year % 100 == 0:
    print("Not leap year")
  elif  year % 4 == 0:
    print("Leap year")
else:
  print("Not leap year")
