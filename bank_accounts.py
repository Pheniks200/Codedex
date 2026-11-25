# Write code below 💖

class BankAccount:
  def __init__(self,first_name, last_name, account_id, account_type, pin, balance):
    self.first_name = str(first_name)
    self.last_name = str(last_name)
    self.account_id = int(account_id)
    self.account_type = str(account_type)
    self.pin = int(pin)
    self.balance = float(balance)
  
  def deposit(self, amount):
     self.balance += amount
     return self.balance
  def withdraw(self, amount):
     self.balance -= amount
     return self.balance
  def display_balance(self):
    print( self.balance)

pierwszy = BankAccount("Piotr", "ZZZZ", 1,2,1234,0)


print( pierwszy.deposit(96))

print(pierwszy.withdraw(25))

pierwszy.display_balance()
