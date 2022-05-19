NAME : KENNY DANG
STUDENT ID : 107156688
CLASS : CSCI 3412 003
HW # 2
DUE DATE : FEBRUARY 21ST, 2021


    #DESCRIPTION OF THE PROGRAMs
    
    #PART 1
    What the program does is that it uses the equation to solve n for each of the big o notations by either using the inverse of said equation or by using a specific libraries from python to allow the program to solve n. The program runs through an array of the time from 1 second, 1 minute, 1 hour, 1 day, 1 month, 1 year, and 1 century to see how many milliseconds it would take for it to run during that time period. The outputs are then placed into HTML code to make a table of the data.

    References : https://stackoverflow.com/questions/36699213/how-to-sort-numbers-in-ascending-order-in-a-file-in-python-by-insertion-sort

    https://www.geeksforgeeks.org/python-program-for-insertion-sort/


    #PART 2
    What this program does is it uses two different sorts for multiple files to sort the files in different sorts. The first use in this program would be the insert sort in which it would move the value of a number over to get to a point in which it would end up being sorted. The second sort is a merge sort in which it would break the numbers in half to make multiple array and repeats that process over and over again until it sorts itself. The last process of this program is to see how long the execution of the program takes to run each of the sorts when compiled, and how many iterations of comparisons it takes when going through a loop.

    Reference : https://www.geeksforgeeks.org/python-program-for-merge-sort/
    #PART 3
    1. A loop invariant is a logical assertion in which it would represent when a loop would be true before and after every single iteration of a loop. Usually with a loop invariant it would be considered inductive.

    2. The loop invariant in my merge() function would start with my while loop of i < len(leftSide) and j < len(rightSide). Thos would be true for every single iteration in the loop. The initialization step would be the intial indexes of my variables which would be i = 0, j = 0, k = 0. The maintenance step is every time that i or j gets incremented within the loop. The termination step would be when the list finally finds the last elements in the list on both the left and right sides of the array. 

    3.The intialization step would be the definitions of variables before the program runs. 
    
    4.THe maintenance step is what maintains a loop variation condition for every iteration that is stepped into after every loop. 
    
    5. Termination step would be what causes the program to end the loop.

    #OUTPUT OF PART 1
one second for log n is: [1.2901e+10]
one minute for log n is: [7.7406e+11]
one hour for log n is: [9.19836e+13]
one day for log n is: [2.2076064e+15]
one month for log n is: [6.6228192e+16]
one year for log n is: [8.05776336e+17]
one century for log n is: [8.05776336e+19]

one second for the square root of n is: [1.e+12]
one minute for the square root of n is: [3.6e+15]
one hour for the square root of n is: [1.296e+19]
one day for the square root of n is: [4.4237664e+15]
one month for the square root of n is: [1.32712992e+17]
one year for the square root of n is: [1.61467474e+18]
one century for the square root of n is: [1.61467474e+20]

one second for n is: [1000000.]
one minute for n is: [60000000.]
one hour for n is: [3.6e+09]
one day for n is: [8.64e+10]
one month for n is: [2.592e+12]
one year for n is: [3.1536e+13]
one century for n is: [3.1536e+15]

one second for n log n is: [62746.12646969]
one minute for n log n is: [2801417.88324151]
one hour for n log n is: [1.33378059e+08]
one day for n log n is: [2.75514751e+09]
one month for n log n is: [7.18708564e+10]
one year for n log n is: [7.97633893e+11]
one century for n log n is: [6.86109568e+13]

one second for n squared is: [1000.]
one minute for n squared is: [7745.96669241]
one hour for n squared is: [60000.]
one day for n squared is: [293938.76913398]
one month for n squared is: [1609968.94379985]
one year for n squared is: [5615692.29926284]
one century for n squared is: [56156922.99262843]

one second for n cubed is: [100.]
one minute for n cubed is: [391.48676412]
one hour for n cubed is: [1532.61886479]
one day for n cubed is: [4420.83779837]
one month for n cubed is: [13736.57091064]
one year for n cubed is: [31593.82456903]
one century for n cubed is: [146645.54333072]

one second for 2 to the power of n is: [19.93156857]
one minute for 2 to the power of n is: [25.83845916]
one hour for 2 to the power of n is: [31.74534976]
one day for 2 to the power of n is: [36.33031226]
one month for 2 to the power of n is: [41.23720286]
one year for 2 to the power of n is: [44.84206492]
one century for 2 to the power of n is: [51.4859211]

one second for n! is: 9
one minute for n! is: 11
one hour for n! is: 12
one day for n! is: 13
one month for n! is: 15
one year for n! is: 16
one century for n! is: 17



    #OUTPUT OF PART 2

rand1000.txt
The counter of merge sort is: 10975
the counter for insert sort is: 246374
The execution time for insert sort is: 0.0003353999999999857
The execution time for merge sort is: 0.003947300000000098

rand10000.txt
The counter of merge sort is: 143615
the counter for insert sort is: 24982804
The execution time for insert sort is: 0.0031479999999994845
The execution time for merge sort is: 0.06172059999999924

rand100000.txt
The counter of merge sort is: 1768927
the counter for insert sort is: 2505224364
The execution time for insert sort is: 0.041170399999941765
The execution time for merge sort is: 0.9273881999999958

rand250000.txt
The counter of merge sort is: 4737855
the counter for insert sort is: 15644836370
The execution time for insert sort is: 0.08671049999975367
The execution time for merge sort is: 1.8120498999996926

rand500000.txt
The counter of merge sort is: 9975711
the counter for insert sort is: 62475768537
The execution time for insert sort is: 0.134402499999851
The execution time for merge sort is: 2.6934293000012985

rand1000000.txt
The counter of merge sort is: [20951423]
the counter for insert sort is: [249926367342]
The execution time for insert sort is: 0.33598490000440506
The execution time for merge sort is: 5.530451500002528