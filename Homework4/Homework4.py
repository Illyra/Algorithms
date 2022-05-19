import os
import sys
from timeit import default_timer as timer

print(os.getcwd()) #to return the working directory due to I had an issue where my .txt files wouldn't be read
file = input("Enter a file name: ") #asks the user to input the file name
print(file)
arr = []

with open(file.strip(), 'r') as textfile:
    for line in textfile:
        arr.extend(int(item) for item in line.split())

def splitList(List, sublength):
    tempList = [] #creating an empty array
    indexList = 0
    secondaryList = [] #creating another list in which it would could create another empty array
    for i in range (100): #from the values of 100 sub lists
        for j in range(sublength): #grabs the sublength of each one in which it would 10 or 10000
            tempList.append(List[indexList])
            indexList += 1
        secondaryList.append(tempList)
        tempList = []
    return secondaryList #returns the second list in which it would be splitted from

#referenced https://www.geeksforgeeks.org/radix-sort/
def CountRadix(arr, pres):
    n = len(arr)
    output = [0] * (n) #the output of the array elements that will be sorted
    count = [0] * (10) #initalize count array to 0

    for i in range (0, n): #store teh count of occurences in count[]
        index = (arr[i] / pres)
        count[int(index % 10)] += 1
    #changes count[i] so it would contain the actual position of the output array
    for i in range (1, 10):
        count[i] += count[i - 1]
    #builds the output array
    i = n - 1
    while i >= 0:
        index = (arr[i] / pres)
        output[count[int(index % 10)] - 1] = arr[i]
        count[int(index % 10)] -= 1
        i -= 1
    #copys the otuput array to arr[] so that it contains sorted arrays
    i = 0
    for i in range (0, len(arr)):
        arr[i] = output[i]

def radixSort(arr):
    maximum = max(arr) #finds the maximum number of digits
    #does a counting sort for every integer where i would be the current integer
    exp = 1
    while maximum / exp > 0:
        CountRadix(arr, exp)
        exp *= 10

def insertSort(arrayA): #function with the parameters
    for i in range(1, len(arrayA)): #this is to go through 1 to len(arrayA)
        currVal = arrayA[i] 
        currPos = i - 1 #this is to move the elements which would be greater than i to the position ahead of itself from their current position
        while currPos >= 0 and currVal <= arrayA[currPos]:
            arrayA[currPos + 1] = arrayA[currPos]
            currPos -= 1
        arrayA[currPos + 1]  = currVal

#referenced https://stackabuse.com/bucket-sort-in-python/
def bucketSort(input_list):
    # Find maximum value in the list and use length of the list to determine which value in the list goes into which bucket 
    max_value = max(input_list)
    size = max_value/len(input_list)

    # Create n empty buckets where n is equal to the length of the input list
    buckets_list= []
    for x in range(len(input_list)):
        buckets_list.append([]) 

    # Put list elements into different buckets based on the size
    for i in range(len(input_list)):
        j = int (input_list[i] / size)
        if j != len (input_list):
            buckets_list[j].append(input_list[i])
        else:
            buckets_list[len(input_list) - 1].append(input_list[i])

    # Sort elements within the buckets using Insertion Sort
    for z in range(len(input_list)):
        insertSort(buckets_list[z])
            
    # Concatenate buckets with sorted elements into a single list
    final_output = []
    for x in range(len (input_list)):
        final_output = final_output + buckets_list[x]
    return final_output

#referenced https://www.geeksforgeeks.org/heap-sort-for-decreasing-order-using-min-heap/
def heapify(arr, n, i):
    smallest = i #initializes the smallest root
    left = 2 * i + 1
    right = 2 * i + 2
#if the left child is smaller than the root
    if left < n and arr[left] < arr[smallest]:
        smallest = left
#if the right child is smaller than the smallest integer
    if right < n and arr[right] < arr[smallest]:
        smallest = right
#if the smallest is not root
    if smallest != i:
        (arr[i], arr[smallest]) = (arr[smallest], arr[i])
        heapify(arr, n, smallest) #will call heapify the affected sub-tree

def heapSorted(arr, n):
    for i in range(int(n/2) -1, -1, -1): #builds the heap
        heapify(arr, n, i)
    #extracts the element from the heap
    for i in range(n - 1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0] #moves the current root the the end of the number
        heapify(arr, i, 0) #calls the max heapify on the reduced heap
#allows to print the array of size n
def printArr(arr, n):
    for i in range(n):
        print(arr[i], end = " ")
    print()

def timeEfficiencyA(func, *args): #create a parameter such that a function to a pointer
    start = timer() #start of the timer using the dictioanry above instead of writing out time.timeit()
    func (*args) #passing a variable number of arguements into the function
    end = timer() #creates the end of the program execution
    timeTaken = (end - start) #this would represent the time taken for the program

    print(f"The execution time for the heap sort is: {timeTaken}")

length = int(len(arr))
sLength = length / 100
blist = splitList(arr, int(sLength))
emptylist = []

#print("The first 50 of the list using radix sort: ")
for i in range(0, 50): #from 0-49 which is 50 lists
    radixSort(blist[i])

#print("\n Sorting the last 50 lists of the bucket sort: ")    
for z in range(50, 100): #from 50 -99 which is the last 50 lists
    blist[z] = bucketSort(blist[z])

#print("\n the full min heap of the array when converted to a full array: ")

for i in range(0, 100):
    for j in range(0,int(sLength)):
        emptylist.append(blist[i][j])

#for a in range(0, 500):
    #heapSorted(blist[a], length)

heapSorted(arr, length)
timeEfficiencyA(heapSorted, arr, length)
#print(arr, length)

#print("\n the full sort of the radix sort and the bucket sort is from 0-100 is:")
#print(emptylist, len(blist))
