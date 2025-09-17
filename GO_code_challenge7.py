print("Welcome to the countdown!")
user=eval(input("What is the duration of the countdown? " ))

print("\n Starting countdown in:")

for time in range(user, 0, -1):
  print("\n", time)
 
print("\n Liftoff!")