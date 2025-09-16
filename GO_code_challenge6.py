print("ODD NUMBER CALCULATOR")

odd = 0
for number in range(7):
	user = eval(input("What are your numbers? " ))
	check = user % 2
	if check != 0:
		odd += user
if odd != 0:
	print("The total sum of your odd numbers are:", odd)
else:
	print("You entered all even numbers")