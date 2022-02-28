print("______________________________________________________________________________________________________________________________________________________________________________\nThe code:\n\n")

## def function(*target)
## function(10,20,30,40)
## it's a tuple: (10, 20, 30, 40)

## def function(**target)
## function(1=10, 2=marko, 3=polo)
## it's a dictionary: {'1': 10, '2': 'marko','3': 'polo}


## First question:
def mislahat(x):
    if x % 2 == 0:
        return 0
    return 1

num = int(input("Enter a number: "))
print(mislahat(num))



## Second question:
def power(a,b):
    result = 1
    while(b > 0):
        result *= a
        b -= 1
    return result

print(power(4,3))



## Third question:
def function(price):
    discount = 0.1
    if price > 1000:
        return function2(price)
    else:
        return price - price*discount

def function2(price):
    discount = int(input("Enter discount amount(%): "))
    return price - price*discount



## forth question:
## too lazy to type it out..
## next question can be done wity if statements
## and with object notations, which is shown in the answers

## fifth question:
#while(True):
if True:
    print("a -  the biggest divider")
    print("b -  the smallest divider")
    print("c -  the result of pow(a,b)")
    print("d -  the reuslt of sqrt(a)-sqrt(b)")
    print("e -  exit")
    
    answer = input("")
    if(answer == "e"):
        #break
        print("quit!")