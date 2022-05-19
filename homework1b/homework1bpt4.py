import sys
import os
import string

file = input("Enter a file name: ") #has the user input the file name
d = dict() #creates an empty dictioanry 
wordCount = int(input("How many words would you like to display? ")) #asks the user to input the number of words that they'd like to display

with open (file, "r") as textFile: #has the file
    for line in textFile: #to loop through each line of the file
        line = line.strip() #this is to remove the spaces of the lines and new lines of the characters
        line = line.lower() #it would avoid specific mismatches throughout the case
        words = line.split(" ") #to split each of the lines into specific words
        if line == "":
            continue
        for word in words:
            if word in d: #basically to check if the words in each of the dictioanry is already in the dictioanry
                d[word] = d[word] + 1
            else:
                d[word] = 1
d = dict(sorted(d.items(), key=lambda item: item[1], reverse = True)) #sorts the items with the key have a set number of any arguements within the items, and the reverse allows the characters to go to descending order
counter = 0
while counter != wordCount: #uses this loop just in case the characters is mismatched incorrectly and to also print the characters
    for key, value in d.items():
        print(f" {key}: {value}")
        counter += 1

        if counter == wordCount:
            break
