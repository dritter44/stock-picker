from multiprocessing.sharedctypes import Value


def picker(prices):

#initialize the values for index holding variables
    low_day = 0             #the value of this variable is a loop index from i
    high_day = 1            #the value of this variable is a loop index from j
    greatest_diff = 0
    strat = []

    #set up a loop through the list for any amount of values
    for i in range(len(prices)):           #start initial loop at i = 0
        for j in range (i+1,len(prices)):    #start follow on loop at j=i+1  
            #print(i,j, greatest_diff, prices[i], prices[j])
            if (prices[j] - prices[i]) > 0 and (prices[j] - prices[i]) > greatest_diff:
                greatest_diff = prices[j] - prices[i]
                low_day = i 
                high_day = j
    strat.append(low_day)
    strat.append(high_day)
    
    return strat
print(picker([19,17,6,9,8,15,6,3,1]))

#[1,17,6,9,8,15,6,3,19]