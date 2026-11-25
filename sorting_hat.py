dec_1 = int(input("Q1) Do you like Dawn or Dusk? Press 1 or 2: "))

Gryffindor = 0
Ravenclaw = 0 
Hufflepuff  = 0 
Slytherin = 0


if dec_1 == 1:
    Gryffindor += 1
    Ravenclaw += 1
elif dec_1 == 2:
    Hufflepuff += 1
    Slytherin += 1
else:
    print("Wrong input")

dec_2 = int(input("Q2) When I’m dead, I want people to remember me as? 1) The Good 2) The Great 3) The Wise 4) The Bold; Press 1-4: "))

if dec_2 == 1:
    Hufflepuff += 2
elif dec_2 == 2:
    Slytherin += 2
elif dec_2 == 3:
    Ravenclaw += 2
elif dec_2 == 4:
    Gryffindor += 2
else:
    print("Wrong input")


dec_3 = int(input("Q3) Which kind of instrument most pleases your ear? 1) The violin 2) The trumpet 3) The piano 4) The drum; Press 1-4: "))

if dec_3 == 1:
    Slytherin += 4
elif dec_3 == 2:
    Hufflepuff += 4
elif dec_3 == 3:
    Ravenclaw += 4
elif dec_3 == 4:
    Gryffindor += 4
else:
    print("Wrong input")

print(f"Final score for Slytherin: " + str(Slytherin) )
print(f"Final score for Hufflepuff: " + str(Hufflepuff))
print(f"Final score for Ravenclaw: " + str(Ravenclaw) )
print(f"Final score for Gryffindor: " + str(Gryffindor) )