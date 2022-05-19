import os
import sys
import re
from timeit import default_timer as timer


print(os.getcwd()) #to return the working directory due to I had an issue where my .txt files wouldn't be read
#file = input("Enter a file name: ") #asks the user to input the file name
file = "rand1000000.txt"
a = [] #creates an empty array
print(file)

with open(file, 'r') as textfile:
    lines = textfile.read().splitlines()
    lines = [line.lstrip() for line in lines]
    realLine = lines[0:len(lines):2]
    a = [int(item) for line in realLine for item in line.split()]

#referenced https://stackoverflow.com/questions/39819878/quicksort-with-insertion-sort-python-not-working
def insertSort(arr, low, n): #function with the parameters
    for i in range(low + 1, n + 1):
        val = arr[i]
        j = i
        while j > low and arr[j - i] > val:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = val

#referenced https://www.geeksforgeeks.org/python-program-for-quicksort/
def part(arr, low, high):
    i = (low - 1) #index of smaller elements
    pivot = arr[high] #pivot to last element in the sublsit
    #i = j = low # i and j - lowest index
    for j in range(low, high): #iterates for every element in sublist
        if arr[j] <= pivot: #if sublist at index i is less than the last element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i] #swaps the elements in the index of i with element index
            #j += 1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = part(arr, low, high) #pi partions the index, arr[p] to correct place
        quickSort(arr, low, pi - 1) #to seperate sort elements before
        quickSort(arr, pi + 1, high) #to partition after the elements are sorted
        return arr

#referenced https://www.geeksforgeeks.org/advanced-quick-sort-hybrid-algorithm/
def hybridSortB(arr, subListLen):
    subArrays = []
    while subListLen < len(arr):
        subArr = arr[:subListLen] #partitions the array into different subbarays
        subArrays.append(subArr)
        arr = arr[subListLen:] #removes whatever is partitioned
    subArrays.append(arr) #so it doesnt remove the last 20 elements
    Response = hybridSortC(subArrays)
    print(f"Hybrid sort: {timeEfficiencyA(hybridSortC, subArrays)}")
    
    return Response

def hybridSortC(subArrays):
    Response = [] #creates an empty array to later recieve a response from the sorts
    for subArr in subArrays: #to later on create sub lists to sort
        insertSort(subArr, 0, len(subArr) - 1)
    list(map(Response.extend, subArrays))
    quickSort(Response, 0, len(Response) - 1)

    return Response

def timeEfficiencyA(func, *args): #create a parameter such that a function to a pointer
    start = timer() #start of the timer using the dictioanry above instead of writing out time.timeit()
    func (*args) #passing a variable number of arguements into the function
    end = timer() #creates the end of the program execution
    timeTaken = (end - start) #this would represent the time taken for the program
    
    print(f"The execution time for the k-value is: {timeTaken}")


k_val = [400000, 400005, 400010, 400015, 400020]
for k in k_val:
    arrayA = a
    print(k)
    hybridSortB(arrayA, k)
#print(f"Hybrid sort: {quickSort(arrayA, 0, len(arrayA) - 1)}")
#print(f"Quick sort: {quickSort(arrayA, 0, len(arrayA) - 1)}")
#print (arrayA)