  #Write a Boolean function that checks if a string contains ‘@’ sign and at least one ‘.’ dot (disregard the order for the sake of 
#simplicity). Use that function to check if a user input is a valid e-mail or not.

email = input("Please enter your email:")

if (email.__contains__("@" and ".")):
  print ("valid email")
else:
  print ("invalid email")