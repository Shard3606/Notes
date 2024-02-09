import time
Username = ""
Password = ""
UsernameGuess = ""
PasswordGuess = ""

def createaccount():
  global Username
  global Password
  Username = input("Please create a username.")
  Password = input("Please create a password.")

def signintoaccount():
  global Username
  global Password
  global UsernameGuess
  global PasswordGuess
  UsernameGuess = input("Please input your username.")
  PasswordGuess = input("Please input your password.")
  if UsernameGuess == Username and PasswordGuess == Password
    print("Welcome...")
    time.sleep(3)
  else
    print("Incorrect username or password. Please try again.")
    time.sleep(3)
    signintoaccount():
