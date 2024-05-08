print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

sides = input("You are at a cross road, choose \"right\" or \"left\" to choose your direction: ").lower()

if sides == "left":
  print("You chose the correct direction. Proceeding to level 2.")

  option = input("You reached level 2. You can either wait or proceed to swim in the lake. Type 'S' to swim or 'W' to wait: ").lower()
  if option == "w":
    print("You chose the right thing. You reached level 3.")

    color = input("You appear at 3 door entrance. You are asked to one of three color doors. Type 'Y' for Yellow, 'R' for Red, 'B' for Blue: ").lower()
    if color == "y":
      print("You have chosen the right color. You have reached the Treasure. You Win!!")
    elif color == "r":
      print("You have chosen the wrong color. You are burned alive. You lose!!")
    elif color == "b":
      print("You have chosen the wrong color. You are eaten alive by the beasts. You lose!!")
      
  else:
    print("You are attacked by a Trout. You Lose. Game Over.")

else:
  print("You chose the wrong direction. You lose. Game Over.")
