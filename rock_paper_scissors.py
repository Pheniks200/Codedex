# Write code below 💖
import random

print("===================")
print("Rock Paper Scissors")
print("===================")
print()
print('✊')
print('✋')
print('✌️')

player = int(input("Pick a number: "))
computer = random.randint(1,3)


if player == 1:
  print("You chose:✊")
elif player == 2:
  print('You chose:✋')
elif player == 3:
  print('You chose:✌️')

if computer == 1:
  print("CPU chose:✊")
elif computer == 2:
  print('CPU chose:✋')
elif computer == 3:
  print('CPU chose:✌️')

if player == 1 and computer == 3:
  print("The plater won!")
elif player == 2 and computer == 1:
  print("The plater won!")
elif player == 3 and computer == 2:
  print("The plater won!")
elif player == computer:
  print("Tie")
else:
  print("The computer won!")