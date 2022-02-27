print("______________________________________________________________________________________________________________________________________________________________________________\nThe code:\n\n")
## meir stopped here
##
##
##


ls1 = [10,20,30,40,50,60] 
ls2 = [3,4,5,3,7,5,9,10,20,10]


print(set(ls1))
############################
print(set(ls1) & set(ls2))
print(set(ls1).intersection(set(ls2)))

############################
print(list(set(ls1) - {20,40}))
## why ls1 is covered with set?

ls1.remove(20)
ls1.remove(40)
print(ls1)


print(set(ls1) - set(ls2))