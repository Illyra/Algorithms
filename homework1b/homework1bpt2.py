import os
import sys
from timeit import default_timer as timer #import from dictionary of time to use later instead of writing out a variable that goes somefunction = time.timeit()

theMaxNum = 0

def listprimeNumbers(theMaxNum): 
    for i in range(0, theMaxNum + 1): #from this range of if the user inputs a number such as 10 it would have a range from 0 - 10
        if i > 0: #such that if i would be greater than 0
            for a in range (2, i): #would return the value of the prime number through another for-if loop
                if (i % a) == 0: #compares the value to zero
                    break
            else:
                print (i) #then prints the values of the prime numbers

theMaxNum = int(input("Enter a number for the list of prime numbers [0..your number]: \n"))
print(f"The prime numbers between {0} and {theMaxNum} are: \n")

def timeEfficiency(func, *args): #create a parameter such that a function to a pointer
    start = timer() #start of the timer using the dictioanry above instead of writing out time.timeit()
    func (*args) #passing a variable number of arguements into the function
    end = timer() #creates the end of the program execution
    timeTaken = (end - start) #this would represent the time taken for the program

    print(f"the start time of function: {start}")
    print(f"the end time of the function is: {end}")
    print(f"The time taken for this function: {timeTaken}")

timeEfficiency(listprimeNumbers, theMaxNum) #calling the function to allow how long it took for the program to run x of time
