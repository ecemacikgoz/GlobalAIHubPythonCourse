#User login application
"""
The boolean variables used for infinity loops to check correct operation request or login attempt, usable username, valid e-mail address and password matching.
Registered users are defined in the users dictionary. Two sets are defined to control user-specified informations.
It basically works as follows;
The user selects the sign in or sign up option.

To sign in:
- Pre-registered username and password check from the users dictionary
- This query continues until the information is entered correctly or three incorrect login attempts(after that it goes back to beginning).

To sign up, it checks:
- If the chosen username is unique, it goes to next step. Otherwise it stays in the same loop until a unique name is chosen. 
- the e-mail address has not been used before and the format of the e-mail address. It stays in the same loop until an appropriate e-mail address is entered.
- whether the password is appropriate or not
After these queries are made, the new user is added to the users dictionary.
"""

doubleCheckID = False
doubleCheckMail = False
loginLoop = False
signInLoop = False
passwordCheckLoop = False

users = { #userID: [password, name, surname, mail]
    "jfkennedy":["20nov1961", "John Fitzgerald", "Kennedy", "jfk@usa.gov"],
    "teslarati":["elonM", "Tesla", "Motors", "motor@tesla.com"],
    "maryPop":["Supercallifragilisticexpialidocious!", "Mary", "Poppins", "marythelady@gmail.com"],
    "theRabbit": ["whatsupDOC", "Bugs", "Bunny", "therabbit@looney.com"],
    "iceiceBABY": ["yoVIP", "Vanilla", "Ice", "toocold@baby.com"]
}

userID_check = ({i for i in users.keys()})
userMail_check = ({k[-1] for k in users.values()})

print("Welcome to Global AI Hub")
while not loginLoop:
  quit = 0
  loginOption = str(input("Sign in (I), Sign up(U): "))

  if loginOption.upper() == "I" :
    while not signInLoop and quit != 3:
      userID = str(input("Please enter your ID: "))
      password = str(input("Please enter your password: "))

      if userID in users.keys() and password == users[userID][0]:
        print("Successfully logged in!")
        print("Welcome", users[userID][1], users[userID][2])
        print("Here you go..")
        print("loading..")
        signInLoop = True
        loginLoop = True

      else:
        print("Used ID or Password is wrong. Please try again.")
        quit += 1

  elif loginOption.upper() == "U":
    while not doubleCheckID:
      userID = str(input("Enter user ID: "))

      if userID in userID_check:
        print("This user name already taken.")
      else:
        doubleCheckID = True

    while not doubleCheckMail:
      mail = str(input("Mail: "))

      if "@" in mail and ".com" in mail and not ".gov" in mail and not ".edu" in mail or not ".com" in mail and ".gov" in mail and not ".edu" in mail or not ".com" in mail and not ".gov" in mail and ".edu" in mail: #just a few musts for e-mail correction
        doubleCheckMail = True
      elif mail in userMail_check:
        print("Already used...")
      else:
        print("Invalid mail account..")

    name = str(input("Name: "))
    surname = str(input("Surname: "))

    while not passwordCheckLoop:
      password = str(input("Password: "))

      if len(password) < 8:
        print("too short..") 
      elif len(password) > 16:
        print("too long..")  
      else:
        passwordCheck = str(input("Confirm your password: "))
        if not passwordCheck == password:
          print("Not matched!!")
        else:  
          passwordCheckLoop = True

    print("Creating your account...")
    users.update({userID: [password, name, surname, mail]})

    print("Your account successfully created.")
    print("Welcome", users[userID][1], users[userID][2])
    print("Here you go..")
    print("loading..")
    loginLoop = True

  else:
    print("Wrong login attempt")


print("!!! Finished !!!")
