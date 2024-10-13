print("Welcome to assessment evaluation system!")
x=float(input("Please input your mark:"))
print(x,type(x))

if 90<= x <= 100:
    print("the mark iS EXCELLENT!")

elif 70<= x <90:
    print("the mark is GOOD!")

elif 50 <= x< 70:
    print("the mank iS NORMAL!")

elif 0<= x< 50:
    print("the mark is BAD!")

else:
    print("the data is ERROR!!!")