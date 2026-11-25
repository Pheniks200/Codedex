import random

print("==============================")
print("Rock Paper Scissors Lizard Spock")
print("==============================")
print()
print("1) ✊")
print("2) ✋")
print("3) ✌️")
print("4) 🦎")
print("5) 🖖")

player = int(input("Pick a number: "))
computer = random.randint(1, 5)

if player == 1:
  print("You chose: ✊")
elif player == 2:
  print("You chose: ✋")
elif player == 3:
  print("You chose: ✌️")
elif player == 4:
  print("You chose: 🦎")
elif player == 5:
  print("You chose: 🖖")

if computer == 1:
  print("CPU chose: ✊")
elif computer == 2:
  print("CPU chose: ✋")
elif computer == 3:
  print("CPU chose: ✌️")
elif computer == 4:
  print("CPU chose: 🦎")
elif computer == 5:
  print("CPU chose: 🖖")

if player == computer:
  print("It's a tie!")
elif (player == 1 and computer == 3) or (player == 1 and computer == 4):
  print("The player won!")
elif (player == 2 and computer == 1) or (player == 2 and computer == 5):
  print("The player won!")
elif (player == 3 and computer == 2) or (player == 3 and computer == 4):
  print("The player won!")
elif (player == 4 and computer == 5) or (player == 4 and computer == 2):
  print("The player won!")
elif (player == 5 and computer == 3) or (player == 5 and computer == 1):
  print("The player won!")
else:
  print("The computer won!")