print("Welcome to the Amusement Park!")
x=int(input("Please enter your age: "))
print(x,type(x))

if x<18:
    print("The price of ticket is free")
    print("Welcome!!")
if x>=18:
    print("The price of ticket is 20$ please")
    print("Welcome!!")