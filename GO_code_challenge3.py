name = input("What is your name? " )
studentinput = input("Are you a student? " ).lower()
feeinput = eval(input("How much is your fare fee? " ))
eligible = 'yes'

discountedfare = ""
fee = feeinput

discount = fee * 0.2
discountfare = fee - discount

if (studentinput == eligible):
	print("Your name is", name)
	print("Your total is:", discountfare)
	print("As you are a student you have discount")
	
else:
	print("Your name is", name)
	print("Your total is", fee)
	print("As you are not a student, no discount for you")