import func

bank = func.bankSystem("users.json")
current_user = None
main_menu = True

while main_menu:
  try:
    choose = int(input("\nChoose one option:\n1.REGISTRATION\n2.ENTERANCE\nRight here: "))
    if choose == 1:
      while True:
        name = input("Write name to register: ")
        if bank.check_login(name):
          password = input("Write pass for register: ")
          if bank.check_pass(password):
            bank.registration(name, password)
            current_user = name
            flag = True
            break
          else:
            print("Try again, pass should be at least 5 characters")
            flag = False
    
    elif choose == 2:
      while True:
        name = input("Login: ")
        password = input("Password: ")
        if bank.enterance(name,password):
          print("You are entered!")
          while True:
            try:
              choice = int(input("\nChoose one option:\n1.Deposit money\n2.Send money\n3.Check money\n4.Exit:\nRight here: "))
              if choice == 1:
                summa = int(input("How much money do u want to put? "))
                bank.deposit_money(name, summa)
              elif choice == 2:
                bank.list_of_users(name)
                recipient = input("Choose recipient: ")
                summa = int(input("How much money do u want to send? "))
                bank.send_money(name,recipient,summa)
              elif choice == 3:
                bank.check_money(name)
              elif choice == 4:
                print("You are exited")
                main_menu = True
                break
            except:
              print("You chose incorrect option")
          break
        else:
          print("Login or pass incorrect, Try again")
  except:
    print("Choose correct option")