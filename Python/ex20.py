print("______________________________________________________________________________________________________________________________________________________________________________\nThe code:\n\n")



def findIdByName(name, lines):
    for i in range(len(lines)):
        startOfWord = 0         #the starting index of possible word
        endOfWord = 0
        stop = 0

        for j in range(len(lines[i])):
            if (lines[i][j] == ',') and (stop == 1):
                endOfWord = j - 1
                checkedName = lines[i][startOfWord:endOfWord + 1]
                stop = 2
                break
            if lines[i][j] == ',':
                startOfWord = j + 1
                stop += 1

        ## if we found the wanted name, quit!
        if (checkedName == name) and (stop == 2):
            finalID = lines[i][0:startOfWord - 1]
            return finalID
        
    print("The name has not been found. :C")
    return False


def getSum(cust_id, lines):
    totalSum = 0
    for i in lines:
        x = i.split(',')   # split the line by ','
        if x[1] == cust_id:
            totalSum += int(x[3])

        ## if we found the wanted cust_id, start calculate the sum
    return totalSum



## input
name = input("Enter your name please: ")


## Find the ID of the NAME
f = open('\FullStuck\Python\cust.csv')
lines = f.readlines()

## with the id founded, access the order.csv
cust_id = findIdByName(name, lines)
f = open('\FullStuck\Python\orders.csv')
lines = f.readlines()

if cust_id != False:
    totalSum = getSum(cust_id,lines)
    print(totalSum)


## return list of the orders for the id entered


## and sum all the cust_id SUM


