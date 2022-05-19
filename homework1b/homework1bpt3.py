import os 
import sys
import time
from statistics import mean #importing a stats function for later to calculate the average of the each algorithm
from random import randrange, seed #basically like in c++ when you use a seed. It's to use a set random of numbers in a variable

seed(time.time()) #creating the random seed generator

def bruteForce():
    randomList = [randrange(0, 10) for i in range(3)] #passing through an array such that if the number was from 0-9 it would pass the value of i three times
    tries = 0
    guessString = "" #passing a variable into an empty string
    for i in range(0, 1000): #the maximum number you can possibly have from 000 - 999 which would be equivalent to 1000 numbers in between 000 - 999
        if i < 10: 
            guessString = f"00{i}" #such that if the value is 000 it would create 000 or it would keep incrememnting to 001, 002, 003, etc
        elif i < 100:
            guessString = f"0{i}" 
        else:
            guessString = f"{i}"
        tries += 1 #incrememnts the number of tries the program takes
        guess = [int(digit)for digit in guessString] #basically passing an integer into the empty string
        if guess == randomList:
            return tries

def randomAlgorithm():
    randomList = [randrange(0, 10) for i in range(3)] 
    tries = [0]
    guess = []  #passing the variable into an empty array
    while guess != randomList:
        guess = [randrange(0, 10) for i in range(3)] #continues to guess the random number such that if your number was 876 it would state 834 or 142 and continues that until it solves the value
        tries[0] += 1 #increments the value of number of tries
    return tries


loop = 10000 #loops the function 10000 times to be used in a for loop later instead of writing a value of 10000
bruteForceGuesses = []
for j in range(loop):
    bruteForceGuesses.append(bruteForce()) #creates a new item into the array to be used later during prints statements

print(f"Deterministic brute-force algorithm: ")
print(f"Number of Tries: {loop}")
print(f"Highest number of guess in a try: {max(bruteForceGuesses)}") #using {max(bruteForceGuesses)} allows for the program to calculate the maximum number
print(f"The lowest number of tries: {min(bruteForceGuesses)}") #min is used to calculate the minimum number of tries it took
print(f"Number of correct tries: {loop}")
print(f"The average number of tries: {mean(bruteForceGuesses)}\n") #had to import mean from the dictionary in order to find the average number of tries

randomAlgorithmGuess = 0
for a in range(loop):
    randomAlgorithmGuess = randomAlgorithm() #calling the function basically to be able to use values such as tries from random algorithm

print(f"Complete pure random Algorithm: ")
print(f"Number of tries: {loop}")
print(f"The highest number of guesses in a try: {max(randomAlgorithmGuess)}") 
print(f"The lowest number of tries: {min(randomAlgorithmGuess)}")
print(f"Number of correct tries: {loop - randomAlgorithmGuess[0]}") #subtracted the number of times by the number of tries it took to get the correct number of tries the program took to get the value
print(f"The average number of tries: {mean(randomAlgorithmGuess)}")

