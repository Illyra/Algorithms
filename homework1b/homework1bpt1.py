import os
import random
import sys

#global variables
global totalGuess
totalGuess = 0

#class
def binaryGuess(x, maxNum, randomNum1):
    count = 1
    mid = int((x + maxNum) / 2) #when the value is at the mid point x would be added to the maxNum(1000) and then be divided by 2 so its at its mid point
    pcGuess = mid
    high = maxNum #high end of the value is = to the maximum number
    low = x #x being equal to 1 would be the lowest number on the end
    while pcGuess != randomNum1: #if the number guesses the number correctly it just moves on with the program
        if pcGuess == randomNum1: 
            pass 
        elif low == 999 and high == 1000: #having the low 999 and high 1000 it would allow the program to run to the designated point without errors and being stuck at finding a number such as 1001
            count += 1 #incrementation
            break
        elif pcGuess < randomNum1: #if the number is less than the randomnumber the program guess would loop
            count += 1
            low = pcGuess
        else:
            count += 1
            high = pcGuess
        pcGuess = int((high - low) // 2 + low) #represents how the program guesses the random number

    return count, pcGuess

loop = 10000 #loop represents how many times to loop through the program
for i in range (loop): #for loop within the range of 10k or 1 million
    randomNum1 = random.randint(1, 1000) #allows the numbers to be randomly generated from 1-1000
    count, pcGuess = binaryGuess(1, 1000, randomNum1)
    print (f"The computer guesses correctly: {pcGuess}")
    print ("Random number is:" , randomNum1)
    totalGuess += count
    print (f"the total guesses is: {totalGuess}")
    print (f"count is: {count}")

averageGuess = totalGuess / loop #to figure out the number of average guesses
print (f"The average amount for 10000 tries of guesses is : {averageGuess}")



