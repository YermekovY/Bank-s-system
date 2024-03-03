import json


class bankSystem:
  def __init__(self, data_file):
    self.data_file = data_file
    with open (self.data_file,"r") as f:
      self.bank = json.load(f)

  def save_data(self):
    with open (self.data_file,"w") as f:
      json.dump(self.bank,f)

  def registration (self, username, password):
    for user in self.bank["users"]:
      new_user = {
        "username":username.strip(),
        "password":password,
        "money":0
      }
    self.bank["users"].append(new_user)
    print("OK! You are registred")
    self.save_data()

  def enterance (self, username, password):
    for user in self.bank["users"]:
      if user["username"] == username and user["password"] == password:
        return True
    return False

  def deposit_money(self, username, summa):
    if summa <= 0:
      return print("Incorrect input")
    for user in self.bank.get("users"):
      if user.get("username") == username:
        user["money"] += summa
        self.save_data()
        return print("You are deposed! Ok! ")
      
  
  def send_money(self, username, recipient, summa):
    if summa <= 0:
      return print("Can not be under or equal to 0 or inccorect data")
    if username == recipient:
        return print("Cannot send yourself")
    sender = None
    recip = None
    for user in self.bank.get("users"):
      if user.get("username") == username and user.get("money") >= summa:
          sender = user
      if user.get("username") == recipient:
          recipient_user = user
    if sender and recipient_user:
      sender["money"] -= summa
      recipient_user["money"] += summa
      print(f"You are sent money {summa}")
      self.save_data()
    else:
      print("Not found this recip")
    


  def check_money(self, username):
    for user in self.bank["users"]:
      if user["username"] == username:
        money = user.get("money")
        print(f"You balance is {money}")
        
      
  

  def check_pass(self, password):
    if len(password.strip()) >= 5:
      return True
    else:
      return False

  def check_login(self,username): 
    for user in self.bank["users"]:
      if user["username"] == username:
        print("Login already exists")
        return False
      elif len(username.strip()) <= 0:
        print("at least 1 symbol")
        return False
    return True

  def list_of_users(self, username):
    for user in self.bank["users"]:
      if user.get("username") != username:
        print(user.get("username"))
