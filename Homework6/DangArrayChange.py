



#referenced https://www.geeksforgeeks.org/understanding-the-coin-change-problem-with-dynamic-programming/



def getNumberArr(N, coins):
    ways = [0 for i in range(N +1)] #create the ways array to 1 plus the amount to stop the overflow
    ways[0] = 1 #sets the first way to 1 because its 0 and there is 1 way to make 0 with 0 coins

    #goes through all of the coins
    for i in range(len(coins)):
        for j in range(len(ways)): #makes a comparison to each index value of ways with the coin value
            if(coins[i] <= j):
                ways[j] += ways[j - coins[i]] #would update the ways array
    return ways[N] #returns the nth position of the array

def printArr(coins):
    for i in coins:
        print(i)
    
if __name__ == '__main__':
    currency = [1, 3, 4]
    print("The coins array is: ")
    printArr(currency)

    print("The number of ways is: ", end = '')

    x = int(input("Enter the coins amount to put into the array: "))
    print(getNumberArr(x, currency))