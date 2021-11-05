  #Guessing game! Pick a number randomly. While user does not guess the number correctly give an instruction about 
#the number and take another guess from user. 
  #Instruction:
   #If the guessed number is lower than the picked number print «increase your number»  else print  "decrease your number"

import random
number = int (random.randint(0, 25))
guessnumber = 0

while guessnumber < 10 :
    guessnumber += 1
    guess = int(input("guess which number i have on my mind from 0 to 25: "))
    if number < guess :
        print("Try again with a smaller number")
    if number > guess :
        print("Try again with a bigger number")
    if number == guess :
        break

if number == guess :
    print ("Yes, you guessed it right")
else :
    print("No, the number was" + str(number))