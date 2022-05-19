

#referenced https://www.wyzant.com/resources/answers/740658/python-program-to-output-a-given-amount-of-change-in-fewest-number-coins-po
#referenced https://www.geeksforgeeks.org/understanding-the-coin-change-problem-with-dynamic-programming/
#referenced https://stackoverflow.com/questions/3947867/find-the-least-number-of-coins-required-that-can-make-any-change-from-1-to-99-ce
#referenced https://stackoverflow.com/questions/58599737/how-to-output-the-actual-coin-combination-in-the-minimum-change-problem-using-re

num = float(input("Enter a currency: "))

def minChange(money):

    currency = [100.0, 50.0, 20.0, 10.0, 5.0, 1.0, 0.50, 0.25, 0.10, 0.05, 0.01] #creates the array for coin denom
    currencyUsed = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #there would be 11 0's due to the number of coins/bills being used
    printMoney = ["Hundred(s)", "Fifty(s)", "Twenty(s)", "Ten(s)", "Five(s)", "One(s)",
                "Half Quarter(s)", "Quarter(s)", "Dime(s)", "Nickle(s)", "Penny(s)"]

    temp = 0 #creating an empty temp (lowest index)
    for i in range(11): #returns the loop for number of denominations available
        while num >= temp: #while the sum of denominations is less than the amount
            if(temp + currency[i]) <= num: #checks if it adds to the new denominations
                temp += currency[i] 
                currencyUsed[i] += 1 #if its continues then it would include that denomination
            else:
                break #else it would move to the next denom
        if temp == num: #if they are equal to the amount it would break out of the loop
            break

    for i in range(11):
        if currencyUsed[i] != 0:
            print("{0}: {1}".format(currencyUsed[i], printMoney[i]))

minChange(num)


