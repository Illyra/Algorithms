import os 
import sys
from timeit import default_timer as timer



def timeEfficiencyDecorator(func): #instead of writing two parameters inside it would only have one
    def wrapper(*args): #wrapper that wraps the function around the decorator
        start = timer()
        func (*args) 
        end = timer()
        timeTaken = (end - start)

        print(f"the start time of function: {start}")
        print(f"the end time of the function is: {end}")
        print(f"The time taken for this function: {timeTaken}")
    return wrapper #returns the value of the wrapper

@timeEfficiencyDecorator #calls the first function again in-order for the program to run 
def listprimeNumbers(theMaxNum):
    print(f"The prime numbers between {0} and {theMaxNum} are: ")
    for i in range(0, theMaxNum + 1):
        if i > 0:
            for a in range (2, i):
                if (i % a) == 0:
                    break
            else:
                print (i)
listprimeNumbers(int(input("Enter a positive integer: ")))