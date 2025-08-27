input1 = input("input your number 1: " )
input2 = input("input your operation: " )
input3 = input("input your number 2: " )

print("This is your operation: ", input1, input2, input3)

number1 = ""
operation = ""
number2 = ""

number1 = eval(input1)
number2 = eval(input3)
operation = (input2)

if operation == '+':
	answer_plus = int(number1 + number2)
	print("This is your answer", answer_plus)

if operation == '-':
	answer_minus = int(number1 - number2)
	print("This is your answer", answer_minus)

if operation == '*':
	answer_times = int(number1 * number2)
	print("This is your answer", answer_times)

if operation == '/':
	answer_divide = float(number1 / number2)
	print("This is your answer", answer_divide)
