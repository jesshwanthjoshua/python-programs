rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
option = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors."))
print(f"\n\nYou Chose {option}")
if option == 0:
  print("Rock",rock)
elif option == 1:
  print("Paper",paper)
else:
  print("Scissors",scissors)

computer_option =  random.randint(0,2)

print(f"\n\nComputer Chose {computer_option}")

if computer_option == 0:
  print("Rock",rock)
elif computer_option == 1:
  print("Paper",paper)
else:
  print("Scissors",scissors)

if option == computer_option:
  print("You chose the same. It's a Draw!!")
  
else:
  if option == 0:
    if computer_option == 1:
      print("You lose. Paper beats Rock.")
    elif computer_option == 2:
      print("You Win. Rock beats Scissors.")
  
  elif option == 1:
    if computer_option == 2:
      print("You lose. Scissors beat Paper.")
    elif computer_option == 0:
      print("You Win. Paper beats Rock.")
      
  else:
    if computer_option == 0:
      print("You lose. Rock beats Scissors.")
    elif computer_option == 1:
      print("You Win. Scissors beat Paper.") 
