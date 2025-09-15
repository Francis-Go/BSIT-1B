print("THE FACTORIAL PROGRAM")
z = eval(input("Enter your desired number > "))
y = 1

for x in range(z, 0, -1):
    # print(x)
    y *= x

print("The Factorial of", z, "is", y)