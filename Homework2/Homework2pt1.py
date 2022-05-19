import os
import sys
from math import factorial, sqrt
import numpy as np
from scipy.optimize import fsolve

def lognFunc(n, time):
    response = np.log2(n) - time #used numpy to do log2 subtracted by time as the original equation would np.log2(n) = time in which you would have to solve n when using fsolve
    return response

def sqrtnFunc(n, time):
    response = sqrt(n) - time #imported the square root to figure out n
    return response

def nFunc(n, time):
    response = n - time
    return response

def nlognFunc(n, time):
    response = np.log2(n) * n - time #used numpy to log n log n to figure out n later when using fsolve
    return response

def nsquaredFunc(n, time):
    response = n**2 - time
    return response

def ncubedFunc(n, time):
    response = n**3 - time
    return response

def twosquarednFunc(n, time):
    response = n - np.log2(time) 
    return response

def solveFactorial(time):
    n = 0
    nFact = 0
    while nFact < time: #if the factorial of n is less than the time we would continue. (trying to hold the value less than time due to if it was greater would cause an integer to be incorrect)
        nFact = factorial(n)
        n += 1 #increment 
    return n - 2

oneSec = 1000000
oneMinute = 60*oneSec
oneHour = 60*oneMinute
oneDay = 24*oneHour
oneMonth = 30*oneDay
oneYear = 365 * oneDay
oneCentury = 100 * oneYear

timeTaken = [oneSec, oneMinute, oneHour, oneDay, oneMonth, oneYear, oneCentury] #created an array for the time
secondaryList = ["one second", "one minute", "one hour", "one day", "one month", "one year", "one century"] #created a string array to hold the names so i won't have to copy and paste the code a lot of times
for val, time in zip(timeTaken, secondaryList): #used zip to create an iterator so when I place the values in the string it won't have to be repeated many times
    print(f"{time} for log n is: {fsolve(lognFunc,val, args = val)}") #
print("") 

for val, time in zip(timeTaken, secondaryList):
    print(f"{time} for the square root of n is: {fsolve(sqrtnFunc,val, args = val)}")  #created a new variable with val in-order for the arguments to pass to cause an error later
print("")

for val, time in zip(timeTaken, secondaryList):
    print(f"{time} for n is: {fsolve(nFunc,val, args = val)}")
print("")

for val, time in zip(timeTaken, secondaryList):
    print(f"{time} for n log n is: {fsolve(nlognFunc,val, args = val)}")
print("")

for val, time in zip(timeTaken, secondaryList):
    print(f"{time} for n squared is: {fsolve(nsquaredFunc,val, args = val)}")
print("")

for val, time in zip(timeTaken, secondaryList):
    print(f"{time} for n cubed is: {fsolve(ncubedFunc,val, args = val)}")
print("")

for val, time in zip(timeTaken, secondaryList):
    print(f"{time} for 2 to the power of n is: {fsolve(twosquarednFunc,val, args = val)}")
print("")

for val, time in zip(timeTaken, secondaryList):
    print(f"{time} for n! is: {solveFactorial(val)}") 