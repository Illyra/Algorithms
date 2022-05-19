import os
import random
import sys



Title = "Hello CSCI 3412 | |\n"
print (Title)

userInput = int (input("Please enter a positive integer: \n"))

negativeNum = -1 * userInput

for i in range (negativeNum, userInput + 1, 2):
   print (f"Num: {i} {i**2} ")
