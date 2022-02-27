print("______________________________________________________________________________________________________________________________________________________________________________\nThe code:\n\n")

while(True):
    userInput = int(input("Enter a 5 digits number: "))
    if (userInput > 9999) and (userInput < 100000):
        break

print(str(userInput) + " / 3 = " + str(userInput/3))
print(str(userInput) + " // 3 = " + str(userInput//3))
print("The last digit of ur number is: " + str(userInput % 10))
print("The tens digit of ur number is: " + str((userInput // 10)%10))
print("The last digit in power of 5: " + str((userInput % 10)**5))