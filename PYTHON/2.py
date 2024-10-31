list1 = [1, 2, 3, 4, 5]
list2 = [6,7,8,9,10]
C=[(x,y) for x in list1 for y in list2]
print(C)
if ((list1[1],list2[1]) and (list1[1],list2[2])) :
    print("yes")