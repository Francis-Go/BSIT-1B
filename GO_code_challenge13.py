name = input("What is your name? " )
print("Welcome to the ODD NUMBER SUMMATION", name)
user = ""
total = 0
all = ""
while user != 0:
    user = eval(input("\nInsert your number here > " ))
    check = user % 2
    if check == 1:
        print("Your Number is ODD, continue code...")
        total += user
        user = str(user)
        all += user + " "
    elif check == 0:
        print("Your Number is EVEN, continue code...")
print("number inserted is equal to zero, CODE STOPS...")
print("\n",name, "the SUMMATION of your ODD NUMBER is equal to:", total)
print("The numbers include:", all)