 ##Write a program that asks for a number N as a user input, and calculates the sum of odd numbers, and the average of even numbers 
#starting from 1 up to and including N.
 ##Sum of first x odd numbers = x**2

N = int(input ("Please enter a number: "))
if N%2==0 :
    numberofoddnumbers = int (N/2)
    print("the sum of the odd numbers: ", (numberofoddnumbers**2))
    print("avarege of the even numbers: ", (numberofoddnumbers))
else :
    numberofoddnumbers = (N+1)/2
    print("the sum of the odd numbers: ", (numberofoddnumbers**2))
    print("avarege of the even numbers: ", (numberofoddnumbers))