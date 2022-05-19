import os
import sys
from time import perf_counter
import plotly
import plotly_express as px
import plotly.graph_objs as go
from plotly import offline as ply
import matplotlib.pyplot as plt

print(os.getcwd()) #to return the working directory due to I had an issue where my .txt files wouldn't be read
file = input("Enter a file name: ") #asks the user to input the file name
print(file)
arr = []

with open(file.strip(), 'r') as textfile:
    for line in textfile:
        arr.extend((item) for item in line.split()) #in order to open as a string

#referenced https://www.geeksforgeeks.org/hash-map-in-python/
class Hash_Node:  #created a class in order to name the key and values.
    def __init__(self, key, val):
        self.key = key
        self.val = val
    
class hashTable:
    def __init__(self):
        self.size = 10000 #sets the table size to 10k
        self.hash_table = [] #creates an empty table with 10k variance
        for i in range(0, self.size):
            self.hash_table.append(Hash_Node(i, [])) #creates the empty bucket list


    """
    What Set_val is going to do is insert the values into the hash map
    """
    def set_val(self, Node): 
        self.hash_table[Node.key].val.append(Node.val)

    def re_Hash(self, oldNode):
        self.set_val(oldNode) % self.size
        

#referenced https://www.geeksforgeeks.org/python-program-for-longest-common-subsequence/
Y = "0123456789"
class lcsRecursive: #created a class in-order to keep track of the number of counts
    def __init__(self):
        self.count = 0 

    def lcs(self, X, Y, m, n):
        
        if m == 0 or n == 0:
            return 0
        elif X[m-1] == Y[n-1]:
            self.count += 1
            return 1 + self.lcs(X, Y, m - 1, n - 1)
        else:
            self.count += 1
            return max(self.lcs(X, Y, m, n-1), self.lcs(X, Y, m - 1, n))

    def driver(self, num):
        long_common = self.lcs(num, Y, len(num), 10) #what this does is that calls the recursive lcs function
        response = self.count
        self.count = 0 #resets the count
        return response, long_common #returns the values of the count and the value

h = hashTable()
readLcs = lcsRecursive()
for i in arr: #calling the functions
    count, lcs = readLcs.driver(i)
    node = Hash_Node(count, lcs)
    h.set_val(node)

trace = go.Bar(x = [x for x in range(0, len(h.hash_table))],
                y = [len(y.val) for y in h.hash_table])
ply.plot({
    "data": [trace]

}, filename = 'Homework5Q3.html')

