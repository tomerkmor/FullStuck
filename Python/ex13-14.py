from random import choice
## notes:
## תרגיל קצת חופר ומשעמם, ההבא יהיה קשה יותר

## import sys for the second exercise
import sys

print("______________________________________________________________________________________________________________________________________________________________________________\nThe code:\n\n")

number = int(input("Enter a number please: "))

####### first and fifth question:
if number > 0:
    print("Your number is positive!")
elif number == 0:
    print("You typed 0.")
else:
    print("Your number is negative!")


####### second question:
x = int(input("Enter a number please: "))
y = int(input("Enter a number please: "))
decision = int(input("Please choose 1 or 2: "))

if decision == 1:
    print("The sum of these 2 numbers is: ", x + y)
elif decision == 2:
    print("The sub of these 2 numbers is: ", x - y)
else:
    print("!!WRONG CHOICE!!")
    sys.exit()


####### third question:
firstName = input("Enter your first name please: ")
lastName = input("Enter your last name please: ")
sex = input("Are you man / woman ? \n TYPE: \n m - for man \n w - for woman \n")

if sex == "m":
    txt = "Mr."
elif sex =="w":
    txt = "Mrs."

print("Hello,", txt, firstName, lastName, "Nice To Meet You")


####### forth question:
x = int(input("Enter a number: "))
if x >= 0:
    print("The number in it's absolute value is:", x)
else:
    print("The number in it's absolute value is:", -x)


###### sixth question:
## ze kvar hofer...
