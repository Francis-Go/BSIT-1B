#Part 1 
Person1 = "Bob"
Person2 = "Joe"
print(f"Do you know both {Person1} and {Person2} ?")

#Part2
big = 100
print("Input ten numbers to subract to the number 100")

for small in range(1, 11, 1):
    number = eval(input(f"({small}). Insert the subtrahend here > "))
    big -= number
print(f"This is the total, {big}")