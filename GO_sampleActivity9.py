print("Type your username:")
username = input()

print("Type your password:")
password = input()

if (username == 'Francis') and (password == 'Go123'):
	print("Login succesfully")

if (username != 'Francis') or (password != 'Go123'):
	print("Login failed")