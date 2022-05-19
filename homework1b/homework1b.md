NAME : KENNY DANG
STUDENT ID : 107156688
CLASS : CSCI 3412 003
HW # 1B
DUE DATE : FEBRUARY 7TH, 2021


    #description of the programs

    #HOMEWORK 1B PART 1:
    #This program was to create a number that was generated from 1-1000 which uses a 
    #binary search algorithm which allows the program to solve the specific number
    #The program is also looped 10,000 times and could be changed to have the max number
    #be solved from 1-1,000,000

    #Theres only the main program that it's run in

    #OUTPUT OF PROGRAM

    #10,000 tries from 1-1000 the progam also lists all the numbers and guesses so i will only post the important pieces of it

Random number is: 356
the total guesses is: 90104
count is: 10
The average amount for 10000 tries of guesses is : 9.0104

    #when the number is 1-1,000,000 with 10,000 tries the output is:

The computer guesses correctly: 793040
Random number is: 793040
the total guesses is: 189702
count is: 18
The average amount for 10000 tries of guesses is : 18.9702

    #HOMEWORK 1B PART 2:
    #this program has the user input an integer and the program solves how many prime numbers is within that set range of numbers that the user had inputted. This program also tests how fast the program runs from the start to the end and calculate the time taken it took to run the program

    #OUTPUT OF THE PROGRAM FOR PART 2

Enter a number for the list of prime numbers [0..your number]: 
50
The prime numbers between 0 and 50 are: 

1
2
3
5
7
11
13
17
19
23
29
31
37
41
43
47
the start time of function: 1.7233627
the end time of the function is: 1.7331555
The time taken for this function: 0.009792800000000046

    #HOMEWORK 1B PART 3:    
    #This program takes two different algorithms in-order to solve a specific number. If the number was for example 999 the program would be able to solve it. With the brute-force permutation algorithm it would keep looping within itself an keep incremeneting from 000, 001, 002, 003, 004, 005, etc until it reaches its destination of a specific number. With the random algorithm it would say create the random integer such as 659 and the program would guess random numbers such as 456, 832, 455, 658, 654, etc until it gets to the correct number

    #OUTPUT OF THE PROGRAM

Deterministic brute-force algorithm: 
Number of Tries: 10000
Highest number of guess in a try: 1000
The lowest number of tries: 1
Number of correct tries: 10000        
The average number of tries: 506.2236 

Complete pure random Algorithm: 
Number of tries: 10000
The highest number of guesses in a try: 47
The lowest number of tries: 47
Number of correct tries: 9953
The average number of tries: 47

    #HOMEWORK 1B PART 4:
    for this homework I actually didn't understand how to create keys or use specific commands such as splitting the empty spaces, or removing leading spaces and newline characters for the prompt so i actually had to use https://www.geeksforgeeks.org/python-count-occurrences-of-each-word-in-given-text-file-using-dictionary/ for some help. This program basically would read a text file and display n amount of words in descending order. 

    #OUTPUT of the program

Enter a file name: Kennedy.txt
How many words would you like to display? 20
 the: 32
 of: 24
 to: 20
 we: 19
 and: 15
 a: 12
 our: 10
 that: 8
 not: 7
 in: 7
 this: 6
 but: 5
 for: 5
 is: 5
 are: 5
 those: 5
 shall: 5
 any: 5
 president: 4
 as: 4

    #HOMEWORK 1B EXTRA CREDIT PART 1
    This program uses the same functions and coding from part 2 instead it would be wrapped around using another function in order for it to run

Enter a positive integer: 100
The prime numbers between 0 and 100 are: 
1
2
3
5
7
11
13
17
19
23
29
31
37
41
43
47
53
59
61
67
71
73
79
83
89
97
the start time of function: 3.4811084
the end time of the function is: 3.4919148
The time taken for this function: 0.010806399999999883
