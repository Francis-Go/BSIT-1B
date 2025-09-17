print("Welcome to the Multiplicator!")

user=eval(input("What number would you like to multiply? " ))

print("\n Multiplication table for", user)

for times in range(1,11):
  product=user*times
  print("\n", user, "x", times, "=", product)