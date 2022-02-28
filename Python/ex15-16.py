print("______________________________________________________________________________________________________________________________________________________________________________\nThe code:\n\n")

array = []
num = int(input("$$$$$$$$$$$$ Enter a number: "))

## push the numbers into the array
for i in range(num):
    newNum = int(input("Enter a number: "))
    array.append(newNum)

## calculate the average of these numbers that are in the array
sum = 0
for item in array:
    sum += item

## print the average
average = sum/len(array)
print(average)



############################################################################################################
x = int(input("Enter a number: "))
while(x != -999):
    n = 0
    while(x != 0):
        n += 1
        x //= 10
    print("Your number has",n,"digits.")
    x = int(input("To quit, type -999\nOtherwise, Enter a number: "))
