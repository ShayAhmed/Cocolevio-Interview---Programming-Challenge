# https://www.geeksforgeeks.org/knapsack-problem/ ->knapsack problem
# I USED NOTES FROM A PREVIOUS CLASS, WILL UPLOAD THEM WHEN I FIND THEM
# https://en.wikipedia.org/wiki/Knapsack_problem


'''
GIVIN INITIAL CONDITIONS
    -USER MUST INPUT EXACTLY AS THE PROMPT STATES
    -USER DOES NOT REQUEST NAMES OF COMPANIES
    -INPUT IS POSTIVE AND NOT FRACTIONAL
'''



company = ['A','B','C','D','E','F','G','H','I','J']     #company names
amount = [1,2,3,4,5,6,7,8,9,10]     #amounts given by companies
price = [1,5,8,9,10,17,17,20,24,30]     #prices given by companies
length = len(company)      #length of company arraay
#maxAmount = 30      #default value for testing
#wantthis = length
#myList = [[0 for j in range(maxAmount+1)] for i in range(length+1)]
#chosenCompanies = []    #company names to be chosen

#This is when the user wants a single instance of a company
def test(am,pr, le, maxAm):     #return maax value that can be returned
    myList = [[0 for j in range(maxAm+1)] for i in range(length+1)]
    for i in range(le+1):
        for j in range(maxAm+1):
            if i==0 or j == 0:     #either zero price or zero amount
                myList[i][j] = 0

            elif am[i-1]  <= j:  
                myList[i][j] = max(pr[i-1]+myList[i-1][j-am[i-1]], myList[i-1][j])      #finds max of including this element or not

                #if pr[i-1]+myList[i-1][j-am[i-1]] > myList[i-1][j]:
                 #   chosenCompanies.append(company[i-1])

            else:
                myList[i][j] = myList[i-1][j]   #goes there if amount is larger than the max at that point

    return myList[le][maxAm]

#THis is when the user wants multiple instances of a company
def test2(am,pr, le, maxAm):
    list2 = [0 for w in range(maxAm+1)]
    for i in range(maxAm+1):
        for j in range(le):
            if am[j] <= i: 
                list2[i] = max(pr[j]+list2[i-am[j]], list2[i])      #same concept as before, find max of with it or without it
                #chosenCompanies.append(company[i-1])
    return list2[maxAm]     #last element has answer because it is calculated with maxAm, the one requested by the user






if __name__ == '__main__':
    print("Hello, welcome to my solution of the CocoLevio programming challenge!")
    looper = 'y'
    while looper == 'y':
        maxStock  = int(input("Enter the maximum amount that you would like (as a number):"))
        print("Enter if you would like to inlude a company multiple times in the calculation")
        responce = int(input("Enter 1 = Yes, 0 = No: "))
        if responce == 0:
            print(test(amount,price, length,  maxStock))
            #print(chosenCompanies)
        else:
            print(test2(amount,price, length,  maxStock))
            #print(chosenCompanies)
        looper = input("Would you like to continue? y/n ")
    print("Bye!")
