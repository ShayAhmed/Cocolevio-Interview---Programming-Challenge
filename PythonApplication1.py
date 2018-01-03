#https://www.geeksforgeeks.org/knapsack-problem/ ->knapsack problem
# I USED NOTES FROM A PREVIOUS CLASS, WILL UPLOAD THEM WHEN I FIND THEM

company = ['A','B','C','D','E','F','G','H','I','J']
amount = [1,2,3,4,5,6,7,8,9,10]
price = [1,5,8,9,10,17,17,20,24,30]
length = len(company)
maxPrice = 30

def test(amount,price, length, maxPrice):
    if length == 0 or maxPrice == 0: #if either is 0 then either the max price has been reached (so dontt go on), or there are no more elements
        return 0
    if price[length-1]>maxPrice: #if price 
        test(amount,price,length-1,maxPrice)
    else:
        withIt = test(amount,price,length-1,maxPrice-price[length-1])
        withoutIt = price[length-1] + test(amount,price,length-1,maxPrice)
        if withIt > withoutIt:
            return withIt
        else:
            return withoutIt



print(test(amount,price, length, maxPrice))
