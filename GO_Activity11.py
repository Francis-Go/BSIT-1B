temp = eval(input("Enter the temperature => " ))


if temp <= 0:
	print("Temperature is considered as Below Freezing")
if temp >= 1 and temp <= 15:
	print("Temperature is considered as Extremely Cold")
if temp >= 16 and temp <= 30:
	print("Temperature is considered as Cold")
if temp >= 31 and temp <= 38:
	print("Temperature is considered as Lukewarm")
if temp >= 39 and temp <= 42:
	print("Temperature is considered as Warm")
if temp >= 43 and temp <= 50:
	print("Temperature is considered as Hot")
if temp >= 51 and temp <= 60:
	print("Temperature is considered as Extremely Hot")
if temp >= 60:
	print("Temperature is considered Burning")