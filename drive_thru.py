# Write code below 💖
def get_item(argument):
  if argument == 1:
    return "Cheeseburger"
  elif argument ==2:
    return "Fries"
  elif argument ==3:
    return "Soda"
  elif argument ==4:
    return "Ice Cream"
  elif argument ==5:
    return "Cookie"
  else:
    print("Please provide a correct number of an order")

def welcome():
  print("1 - 🍔 Cheeseburger ")
  print("2 - 🍟 Fries")
  print("3 - 🥤 Soda")
  print("4 - 🍦 Ice Cream")
  print("5 - 🍪 Cookie")

welcome()
argument = int(input("Provide the number of your order 1-5: "))

print(get_item(argument))
