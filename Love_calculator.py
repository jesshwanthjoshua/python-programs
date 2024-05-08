print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?

true_count = 0
love_count = 0
name = name1+name2
name = name.lower()
for i in name:
  if i == "t" or i == "r" or i == "u" or i == "e":
    true_count +=1
for j in name:
  if j == "l" or j == "o" or j== "v" or j == "e":
    love_count +=1

score = str(true_count)+str(love_count)

if int(score)>=40 and int(score)<=50:
  print(f"Your score is {score}, you are alright together.")
elif int(score)< 10 or int(score)>90:
   print(f"Your score is {score}, you go together like coke and mentos.")
else:
  print(f"Your score is {score}.")
