import os
import sys
from timeit import default_timer as timer

print(os.getcwd()) #to return the working directory due to I had an issue where my .txt files wouldn't be read
file = input("Enter a file name: ") #asks the user to input the file name
arr = [] #creates an empty array
print(file)

with open(file.strip(), 'r') as textfile:
    for line in textfile:
        arr.extend(int(item) for item in line.split())

#References : https://stackoverflow.com/questions/36699213/how-to-sort-numbers-in-ascending-order-in-a-file-in-python-by-insertion-sort
#https://www.geeksforgeeks.org/python-program-for-insertion-sort/
def insertSort(arrayA, count): #function with the parameters
    count[0] += 1 #creates a counter with an array and increments it every time it loops
    for i in range(1, len(arrayA)): #this is to go through 1 to len(arrayA)
        currVal = arrayA[i] 
        currPos = i - 1 #this is to move the elements which would be greater than i to the position ahead of itself from their current position
        while currPos >= 0 and currVal <= arrayA[currPos]:
            arrayA[currPos + 1] = arrayA[currPos]
            currPos -= 1
            count[0] += 1
        arrayA[currPos + 1]  = currVal

def mergeSort(arr,counter):
    #Reference : https://www.geeksforgeeks.org/python-program-for-merge-sort/
    if len(arr) > 1:
        counter[0] += 1
        midPoint = len(arr) // 2 #used to find the middle of the array
        leftSide = arr[:midPoint] #would divide the array elements to its respective counterparts
        rightSide = arr[midPoint:] #would place it in halfs
        mergeSort(leftSide, counter) #would sort the left(first half) of the array
        mergeSort(rightSide, counter)#would sort the right(second half) of the array
        i = 0 #initial indexes of subarrays that would traverse the two halves
        j = 0
        k = 0 #would be the iterator for the main lists
        while i < len(leftSide) and j < len(rightSide): #creating a temp arrays
            if leftSide[i] < rightSide[j]: #would be the value from the left half that has been used
                arr[k] = leftSide[i] #would continue to move the iterators forward
                i += 1
                counter[0] += 1
            else:
                arr[k] = rightSide[j]
                j += 1
                counter[0] += 1 
            k += 1 #would move to the next slots
        while i < len(leftSide): #these will check if there is any elements left 
            arr[k] = leftSide[i]
            i += 1
            k += 1
            counter[0] += 1
        while j < len(rightSide):
            arr[k] = rightSide[j]
            j += 1
            k += 1
            counter[0] += 1


def timeEfficiencyA(func, *args): #create a parameter such that a function to a pointer
    start = timer() #start of the timer using the dictioanry above instead of writing out time.timeit()
    func (*args) #passing a variable number of arguements into the function
    end = timer() #creates the end of the program execution
    timeTaken = (end - start) #this would represent the time taken for the program
    
    print(f"The execution time for insert sort is: {timeTaken}")

def timeEfficiencyB(func, *args): #create a parameter such that a function to a pointer
    start = timer() #start of the timer using the dictioanry above instead of writing out time.timeit()
    func (*args) #passing a variable number of arguements into the function
    end = timer() #creates the end of the program execution
    timeTaken = (end - start) #this would represent the time taken for the program
    
    print(f"The execution time for merge sort is: {timeTaken}")

count = [0]
counter = [0]
arrayA = arr
insertSort(arrayA, count) #calling the function
#print(f"Insert sort: {arrayA}") #was used to test if the sort went correctly
mergeSort(arr,counter) 
#print(f"Merge sort: {arr}") #used to see if the sort went correctly

print(f"The counter of merge sort is: {counter}")
print(f"the counter for insert sort is: {count}")

timeEfficiencyA(insertSort, arrayA, count) 
timeEfficiencyB(mergeSort, arr, counter)