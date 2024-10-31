A = int(input("Enter First Number = "))
B = int(input("Enter Second Number = "))
C = int(input("Enter Third Number = "))

if (A>=B) and (A >= C):
    print ("The largest number is", A)
elif (B>=A) and (B>=C):
    print ("The largest number is ", B)
else:
    print ("The largest number is ", C)