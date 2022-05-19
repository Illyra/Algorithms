import os
import sys
from timeit import default_timer as timer
from time import perf_counter

print(os.getcwd()) #to return the working directory due to I had an issue where my .txt files wouldn't be read
file = input("Enter a file name: ") #asks the user to input the file name
print(file)
arr = []

with open(file.strip(), 'r') as textfile:
    for line in textfile:
        arr.extend((item) for item in line.split()) #in order to open as a string

#referenced https://www.geeksforgeeks.org/python-program-for-longest-common-subsequence/
def lcs(X, Y, m, n):

    if m == 0 or n == 0: #if m == 0 or n == 0 it returns the value
        return 0
    elif X[m-1] == Y[n-1]: #when it moves to the next number and subtracts
        return 1 + lcs(X, Y, m - 1, n - 1) #it would return the value and then add 1
    else:
        return max(lcs(X, Y, m, n-1), lcs(X, Y, m - 1, n)) #else it would return the maximum value

#referenced https://www.geeksforgeeks.org/python-program-for-longest-common-subsequence/
def dyLcs(X, Y):
    # find the length of the strings
    m = len(X)
    n = len(Y)
  
    # declaring the array for storing the dp values
    L = [[None]*(n + 1) for i in range(m + 1)]
  
    """Following steps build L[m + 1][n + 1] in bottom up fashion
    Note: L[i][j] contains length of LCS of X[0..i-1]
    and Y[0..j-1]"""
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0 :
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
  
    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    return L[m][n]

def readdyLcs(arr): #created this function in-order to create the lists 
    lcsRead = 0
    for i in range (len(arr)):
        temp = dyLcs(arr[i], "0123456789") #parameters thats to be read from the dyanmic array
        if temp > lcsRead:
            lcsRead = temp
    return lcsRead
"""
def timeEfficiencyA(func, *args): #create a parameter such that a function to a pointer
    start = timer() #start of the timer using the dictioanry above instead of writing out time.timeit()
    func (*args) #passing a variable number of arguements into the function
    end = timer() #creates the end of the program execution
    timeTaken = (end - start) #this would represent the time taken for the program

    print(f"The execution time for recursive lcs is: {timeTaken}")
"""
def timeEfficiencyB(args): #create a parameter such that a function to a pointer
    start = timer() #start of the timer using the dictioanry above instead of writing out time.timeit()
    run = readdyLcs(args) #passing a variable number of arguements into the function
    end = timer() #creates the end of the program execution
    timeTaken = (end - start) #this would represent the time taken for the program
    print(f"The execution time for Dynamic lcs is: {timeTaken}")
    return run

#print(type(arr[0])) #this is to test what type it is to see if its a string.
#print(arr)

lcsArr = []
Y = "0123456789"

start = perf_counter()
for num in arr:
    lcsArr.append(lcs(num, Y, len(num), 10)) #parameters for recursive lcs
end = perf_counter()
print(f"The execution time to run recursive Lcs: {end - start}")

readTime = timeEfficiencyB(arr)