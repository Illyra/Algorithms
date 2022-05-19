import os
import sys

#referenced https://www.educative.io/edpresso/how-to-implement-quicksort-in-python
def quickSort(arr):
    
    elements = len(arr)
    
    if elements < 2:
        return arr
    
    curr_Pos = 0 

    for i in range(1, elements):
        if arr[i] <= arr[0]:
            curr_Pos += 1
            temp = arr[i]
            arr[i] = arr[curr_Pos]
            arr[curr_Pos] = temp

    temp = arr[0]
    arr[0] = arr[curr_Pos] 
    arr[curr_Pos] = temp 
    
    leftSide = quickSort(arr[0:curr_Pos]) 
    rightSide = quickSort(arr[curr_Pos+1:elements]) 

    arr = leftSide + [arr[curr_Pos]] + rightSide 
    
    return arr

def insertSort(arrayA): #function with the parameters
    for i in range(1, len(arrayA)): #this is to go through 1 to len(arrayA)
        currVal = arrayA[i] 
        currPos = i - 1 #this is to move the elements which would be greater than i to the position ahead of itself from their current position
        while currPos >= 0 and currVal <= arrayA[currPos]:
            arrayA[currPos + 1] = arrayA[currPos]
            currPos -= 1
        arrayA[currPos + 1]  = currVal



randomArr = [10,12,51,23,16,1,2,5,24,18,26,58,100,43,77,68,8,9,98,88]
randomArr2 = [10,12,51,23,16,1,2,5,24,18,26,58,100,43,77,68,8,9,98,88]
insertSort(randomArr2)
print(f"Quick Sort array: {quickSort(randomArr)}")
print(f"Insert Sorted array is: {randomArr2}")
