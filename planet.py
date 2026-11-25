earth_weight = float(input("Enter weight on Earth: "))

relative_gravity = int(input("Enter a number of planet: "))

if relative_gravity == 1:
    relative_gravity = 0.38
    destination_weight = earth_weight * relative_gravity
    print(destination_weight)
    
elif relative_gravity == 2:
    relative_gravity = 0.91
    destination_weight = earth_weight * relative_gravity
    print(destination_weight)

elif relative_gravity == 3:
    relative_gravity = 0.38
    destination_weight = earth_weight * relative_gravity
    print(destination_weight)

elif relative_gravity == 4:
    relative_gravity = 2.53
    destination_weight = earth_weight * relative_gravity
    print(destination_weight)

elif relative_gravity == 5:
    relative_gravity = 1.07
    destination_weight = earth_weight * relative_gravity
    print(destination_weight)

elif relative_gravity == 6:
    relative_gravity = 0.89
    destination_weight = earth_weight * relative_gravity
    print(destination_weight)

elif relative_gravity == 7:
    relative_gravity = 1.14
    destination_weight = earth_weight * relative_gravity
    print(destination_weight)

else:
    print("Invalid")

