#https://www.geeksforgeeks.org/knapsack-problem/ ->knapsack problem
# I USED NOTES FROM A PREVIOUS CLASS, WILL UPLOAD THEM WHEN I FIND THEM

company = ['A','B','C','D','E','F','G','H','I','J'] #company names
amount = [1,2,3,4,5,6,7,8,9,10] 
price = [1,5,8,9,10,17,17,20,24,30]
length = len(company)
maxAmount = 30
wantthis = length
myList = [[0 for j in range(maxAmount+1)] for i in range(length+1)]
chosenCompanies = []

def test(am,pr, le, maxAm): #return maax value that can be returned
    for i in range(le+1):
        for j in range(maxAm+1):
            if i==0 or j == 0:     #if either is 0 then either the max price has been reached (so dontt go on), or there are no more elements
                myList[i][j] = 0
            elif am[i-1]  <= j:  
                myList[i][j] = max(pr[i-1]+myList[i-1][j-am[i-1]], myList[i-1][j])

            else:
                myList[i][j] = myList[i-1][j]
    return myList[wantthis][maxAm]
'''
        withIt = test(amount,price,length-1,maxPrice-price[length-1])
        withoutIt = price[length-1] + test(amount,price,length-1,maxPrice)
        if withIt > withoutIt:
            return withIt
        else:
            return withoutIt
            '''
def test2(am,pr, le, maxAm):
    list2 = [0 for w in range(maxAm+1)]
    for i in range(maxAm+1):
        for j in range(le):
            if am[j] <= i:
                list2[i] = max(pr[j]+list2[i-am[j]], list2[i])
    return list2[maxAm]






if __name__ == '__main__':
    #print("Enter the max amout that you want")
    maxStock  = int(input("Enter the max amout that you would like as a number:"))
    print("Enter if you would like to inlude a company multiple times in the calculation")
    responce = int(input("Enter 1 = Yes, 0 = No: "))
    if responce == 0:
        print(test(amount,price, length,  maxStock))
    else:
        print(test2(amount,price, length,  maxStock))
