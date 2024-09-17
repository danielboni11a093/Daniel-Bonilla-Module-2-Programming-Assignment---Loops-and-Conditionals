Small = input("Is it small?: True or False: ")
Green = input("Is it Green?: True or False: ")

if Small == "True":
    if Green == "True":
        print("It's a pea")
    else:
        print("It's a Cherry")
else:
    if Green == "True":
        print("It's a Watermelon")
    else:
        print("It's a pumpkin")