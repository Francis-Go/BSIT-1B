name = input("What is your name? " )
studentinput = input("Are you a student? " ).lower()
feeinput = input(float("How much is your fare fee? " ))
discount = 'yes'

discountedfare = ""
totalfare = feeinput
feefare = eval(feeinput)

discount2 = feeinput * 0.2
discountfare -= discount2

if (studentinput == discount):
	print("Your name is", name)
	print("Your total is:", discountfare)
	print("As you are a student you have discount")
	
else:
	print("Your name is", name)
	print("Your total is", feeinput)
	print("As you are not a student, no discount for you")