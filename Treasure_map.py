line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?

alpha_index = position[0]
num_index = position[1]
print(alpha_index + " " + num_index)
num_index = int(position[1])

if alpha_index == "A":
  if num_index == 1:
    line1[0] = "X"
  elif num_index == 2:
    line2[0] = 'X'
  elif num_index == 3:
    line3[0] = 'X'

elif alpha_index == "B":
  if num_index == 1:
    line1[1] = 'X'
  elif num_index == 2:
    line2[1] = 'X'
  elif num_index == 3:
    line3[1] = 'X'

else:
  if num_index == 1:
    line1[2] = 'X'
  elif num_index == 2:
    line2[2] = 'X'
  elif num_index == 3:
    line3[2] = 'X'

print(f"{line1}\n{line2}\n{line3}")
print(map)
