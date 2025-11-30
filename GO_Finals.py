import os
import time

def Menu():
    print("\nWhat would you like to learn about?")
    print("1. Print Statements")
    print("2. Variables")
    print("3. Operators")
    print("4. Conditionals")
    print("5. Loops")
    print("6. Lists")
    print("7. Functions")
    print("0. Exit")

def Submenu():
    print("1. Definition")
    print("2. Example")
    print("3. Try your own")
    print("0. Exit")

user_name = input("Hello user! What is your name? " ).title()
print(f"Welcome {user_name}, this is a walkthrough about the coding language of Python!")
time.sleep(1)

user_menu = ""
user_submenu = ""

while user_menu != 0:
    Menu()
    user_menu = eval(input("\nInsert the number of your choice --> " ))
    if user_menu == 1:
        time.sleep(1)
        print("\nYou have chosen to learn about the PRINT STATEMENTS")
        Submenu()
        user_submenu = eval(input("\nInsert the number of your choice --> " ))
        if user_submenu == 1:
            print("\nPRINT STATEMENTS \nPrint statements are commands used to show text, numbers, or results on the screen.")
            print("They help you see what your program is doing.")
            time.sleep(1)
            continue
        elif user_submenu == 2:
            print("\nThere are two types of PRINTING STATEMENTS: for texts and for numbers")
            time.sleep(1)
            print("\nprint(“Hello, world!”)")
            print("This tells the computer to display the text “Hello, world!” on the screen.")
            time.sleep(1)
            print("\nprint(5 + 3)")
            print("Before printing, the computer solves the math expression 5 + 3. \nThe result is 8, so the screen shows: 8")
            time.sleep(1)
            continue
        elif user_submenu == 3:
            print("\nYou will now try to input what you want to PRINT \n")
            time.sleep(1)
            user_print_input = input("Enter your text here: ")
            print("You typed:")
            print(user_print_input)
            time.sleep(1)
            print("\nReminder: To display something on the screen, type it inside the print() like this: print(“Your text here”)")
            time.sleep(1)
            continue
        elif user_submenu == 0:
            print("\nReturning to main menu")
            time.sleep(1)
            continue
        else:
            print("\nYou have entered an invalid choice, try again. Returning to main menu")
            time.sleep(1)
            continue

    elif user_menu == 2:
        time.sleep(1)
        print("\nYou have chosen to learn about the VARIABLES")
        Submenu()
        user_submenu = eval(input("\nInsert the number of your choice --> " ))
        if user_submenu == 1:
            print("\nVARIABLES \nVariables are names that store values.")
            print("They let you save information and use it later in the program.")
            time.sleep(1)
            continue
        elif user_submenu == 2:
            print("\nname = “Joe” \nage = 13")
            time.sleep(1)
            print("\nname = “Joe”. This stores the word “Joe” inside a container called name.")
            print("If you use name later, it gives you “Joe”.")
            time.sleep(1)
            print("\nage = 13. This stores the number 13 inside the variable age.")
            print("The computer remembers this value until changed.")
            time.sleep(1)
            continue
        elif user_submenu == 3:
            print("\nYou will now try to name your own VARIABLE.")
            print("Think of a name for your variable and what you want to store in it.\n")
            time.sleep(1)
            variable_name = input("Enter your variable name: ")
            variable_value = input(f"Enter the value you want to store in '{variable_name}': ")
            print("\nYou created a variable like this:")
            print(f"{variable_name} = \"{variable_value}\"")
            time.sleep(1)
            print("\nRemember: to display the value, use a print statement like this:")
            print("variable name")
            time.sleep(1)
            print("\nReminder: To create a variable, type the name, then =, then the value.")
            print("Example: my_variable = 13 or name = “Joe”)")
            time.sleep(1)
            continue
        elif user_submenu == 0:
            print("\nReturning to main menu")
            time.sleep(1)
            continue
        else:
            print("\nYou have entered an invalid choice, try again. Returning to main menu")
            time.sleep(1)
            continue

    elif user_menu == 3:
        time.sleep(1)
        print("\nYou have chosen to learn about the OPERATORS")
        Submenu()
        user_submenu = eval(input("\nInsert the number of your choice --> " ))
        if user_submenu == 1:
            print("\nOPERATORS \nOperators are symbols that let the computer perform actions like math, comparisons, or logic.")
            print("They usually use symbols like +, -, >, ==.")
            time.sleep(1)
            continue
        elif user_submenu == 2:
            print("\n10 + 5   # addition \n8 > 3    # True \nTrue and False")
            time.sleep(1)
            print("\n10 + 5 \nUses the + operator to add two numbers. The result is 15.")
            time.sleep(1)
            print("\n8 > 3 \nUses the > operator to compare numbers. Since 8 is bigger than 3, the result is True.")
            time.sleep(1)
            print("\nTrue and False \nUses the logical operator AND.\n AND only returns True if both sides are True. Since one is False, the result is False.")
            time.sleep(1)
            continue
        elif user_submenu == 3:
            print("\nYou will now try using OPERATORS")
            time.sleep(1)
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            print("\nLet's try some calculations using operators.")
            time.sleep(1)
            addition = num1 + num2
            subtraction = num1 - num2
            multiplication = num1 * num2
            division = num1 / num2
            print(f"\n{num1} + {num2} = {addition}")
            print(f"{num1} - {num2} = {subtraction}")
            print(f"{num1} * {num2} = {multiplication}")
            print(f"{num1} / {num2} = {division}")
            time.sleep(1)
            print("\nNow let's compare the two numbers using comparison operators:")
            print(f"{num1} > {num2} : {num1 > num2}")
            print(f"{num1} < {num2} : {num1 < num2}")
            print(f"{num1} == {num2} : {num1 == num2}")
            time.sleep(1)
            print("\nReminder: To perform calculations or comparisons, use operators like +, -, *, /, >, <, == between numbers or variables")
            time.sleep(1)
            continue
        elif user_submenu == 0:
            print("\nReturning to main menu")
            time.sleep(1)
            continue
        else:
            print("\nYou have entered an invalid choice, try again. Returning to main menu")
            time.sleep(1)
            continue

    elif user_menu == 4:
        time.sleep(1)
        print("\nYou have chosen to learn about the CONDITIONALS")
        Submenu()
        user_submenu = eval(input("\nInsert the number of your choice --> " ))
        if user_submenu == 1:
            print("\nCONDITIONALS \nStatements that make the program choose what to do based on a condition (using if, else).")
            print("They check if something is true or false, then run the correct block of code.")
            time.sleep(1)
            continue
        elif user_submenu == 2:
            print("\ngrade = 90 \nif grade >= 75: \n\tprint(“Passed”) \nelse: \n\tprint(“Failed”)")
            time.sleep(1)
            print("\nThe variable grade stores 90.")
            print("The if statement checks the condition: Is 90 greater than or equal to 75?")
            time.sleep(1)
            print("\nYes, it is true → so the computer runs the code inside the if block: \nprint(“Passed”)")
            print("The else block is ignored because the condition was true.")
            time.sleep(1)
            continue
        elif user_submenu == 3:
            print("\nYou will now try to create a CONDITIONAL STATEMENT.")
            time.sleep(1)
            user_number = input("Enter a number: ")
            user_number = int(user_number) 
            print("\nLet's check your number using a conditional:")
            time.sleep(1)
            if user_number > 0:
                result = "positive"
            elif user_number < 0:
                result = "negative"
            else:
                result = "zero"
            print(f"\nYour number is {result}!")
            time.sleep(1)
            print("\nReminder: To make decisions, use if, elif, else statements with a condition.")
            print("\nExample:\nif x > 0:\n    print(“Positive”)\nelse:\n    print(“Not positive”)")
            time.sleep(1)
            continue
        elif user_submenu == 0:
            print("\nReturning to main menu")
            time.sleep(1)
            continue
        else:
            print("\nYou have entered an invalid choice, try again. Returning to main menu")
            time.sleep(1)
            continue

    elif user_menu == 5:
        time.sleep(1)
        print("\nYou have chosen to learn about the LOOPS")
        Submenu()
        user_submenu = eval(input("\nInsert the number of your choice --> " ))
        if user_submenu == 1:
            print("\nLOOPS \nLoop commands that make the program repeat actions automatically.")
            print("It lets your program repeat actions without writing the same code over and over.")
            time.sleep(1)
            continue
        elif user_submenu == 2:
            print("\nThere are two types of loops: For Loop and While Loop")
            print("\nFor Loop Example:")
            print("\nfor i in range(3):\n\tprint(“Hello”)")
            time.sleep(1)
            print("\nrange(3) means the loop runs 3 times. Each time it runs, it prints “Hello”.")
            print("\nOutput:\nHello\nHello\nHello")
            time.sleep(1)
            print("\nWhile Loop Example:")
            print("\ncount = 0\nwhile count < 3:\n\tprint(“Hello”)\n\tcount += 1")
            time.sleep(1)
            print("\nThe loop starts with count = 0.")
            print("\nIt checks: Is count less than 3?")
            time.sleep(1)
            print("\nYes → print “Hello”")
            print("\nThen increase count by 1 (count += 1)")
            print("\nThis repeats until count becomes 3. It prints “Hello” 3 times.")
            time.sleep(1)
            continue
        elif user_submenu == 3:
            print("\nYou will now try using LOOPS.")
            time.sleep(1)
            times = int(input("Enter the number of times you want to repeat a message: "))
            message = input("Enter the message you want to repeat: ")
            print("\nLet's see the loop in action!")
            time.sleep(1)
            for i in range(times):
                print(f"{message}")
                time.sleep(0.5)
            print("\nReminder: To repeat code, use a loop like for or while. Example: for i in range(5): print(i)  # prints 0 to 4")
            time.sleep(1)
            continue
        elif user_submenu == 0:
            print("\nReturning to main menu")
            time.sleep(1)
            continue
        else:
            print("\nYou have entered an invalid choice, try again. Returning to main menu")
            time.sleep(1)
            continue

    elif user_menu == 6:
        time.sleep(1)
        print("\nYou have chosen to learn about the LISTS")
        Submenu()
        user_submenu = eval(input("\nInsert the number of your choice --> " ))
        if user_submenu == 1:
            print("\nLISTS \nCollections that store multiple items in a single variable.")
            print("It is like an array of values, and you can access items one by one.")
            time.sleep(1)
            continue
        elif user_submenu == 2:
            print("\nfruits = [“apple”, “banana”, “mango”]\nprint(fruits[1])")
            time.sleep(0.5)
            print("\nThe list fruits contains three items:")
            time.sleep(1)
            print("\n\tindex 0 → “apple”\n\tindex 1 → “banana”\n\tindex 2 → “mango”")
            time.sleep(1)
            print("\nprint(fruits[1])")
            print("\nThis asks the computer to show the item at index 1.")
            print("\nLists start counting from 0, so index 1 is “banana”.")
            time.sleep(1)
            print("\nfruits.append(“orange”)\nprint(fruits)")
            print("\n['apple', 'banana', 'mango', 'orange']")
            time.sleep(0.5)
            print("\n\tappend() adds a new item at the end of the list.")
            time.sleep(1)
            print("\nfruits.append(“orange”)\nprint(fruits)")
            print("\n['apple', 'banana', 'mango', 'orange']")
            time.sleep(0.5)
            print("\n\tappend() adds a new item at the end of the list.")
            time.sleep(1)
            print("\nfruits.remove(“banana”)\nprint(fruits)")
            print("\n['apple', 'mango', 'orange']")
            time.sleep(0.5)
            print("\n\tremove() deletes the first occurrence of the specified item.")
            time.sleep(1)
            print("\nlast_item = fruits.pop()\nprint(last_item)\nprint(fruits)")
            print("\norange\n['apple', 'mango']")
            time.sleep(0.5)
            print("\n\tpop() removes the last item by default and can store it in a variable.")
            print("\n\tYou can also use fruits.pop(0) to remove by index.")
            time.sleep(1)
            print("\nfruits.insert(1, “kiwi”)\nprint(fruits)")
            print("\n['apple', 'kiwi', 'mango']")
            time.sleep(0.5)
            print("\n\tinsert(index, item) adds an item at the specified position.")
            time.sleep(1)
            print("\nfruits.sort()\nprint(fruits)")
            print("\n['apple', 'kiwi', 'mango'] (alphabetical order)")
            time.sleep(0.5)
            print("\n\tsort() arranges the list items in ascending order (alphabetical for strings, numerical for numbers).")
            continue
        elif user_submenu == 3:
            print("\nYou will now try using LISTS.")
            time.sleep(1)
            items = input("Enter several items separated by commas (e.g., apple, banana, mango): ")
            my_list = [item.strip() for item in items.split(",")]
            print("\nHere is the list you created:")
            print(my_list)
            time.sleep(1)
            index = int(input(f"\nEnter the index of the item you want to see (0 to {len(my_list)-1}): "))
            print(f"The item at index {index} is: {my_list[index]}")
            time.sleep(1)
            print("\nReminder: To store multiple items, use a list inside brackets [].")
            print("Example: fruits = [“apple”, “banana”, “mango”]. To access items: print(fruits[0])  # prints 'apple'")
            print("To add: fruits.append(“orange”), remove: fruits.remove(“banana”), pop: fruits.pop(), insert: fruits.insert(1, “kiwi”), sort: fruits.sort()")

            time.sleep(1)
            continue
        elif user_submenu == 0:
            print("\nReturning to main menu")
            time.sleep(1)
            continue
        else:
            print("\nYou have entered an invalid choice, try again. Returning to main menu")
            time.sleep(1)
            continue

    elif user_menu == 7:
        time.sleep(1)
        print("\nYou have chosen to learn about the FUNCTIONS")
        Submenu()
        user_submenu = eval(input("\nInsert the number of your choice --> " ))
        if user_submenu == 1:
            print("\nFUNCTIONS \nReusable blocks of code that perform a specific task when called.")
            print("They help make programs organized and efficient.")
            time.sleep(1)
            continue
        elif user_submenu == 2:
            print("\ndef greet(name):\n\tprint(“Hello, ” + name + “!”)")
            print("\ngreet(“Joe”)")
            time.sleep(0.5)
            print("\ndef greet(name):")
            print("\nThis creates a function called greet with one input (parameter) called name.")
            time.sleep(0.5)
            print("\nInside the function:")
            print("\nprint(“Hello, ” + name + “!”)")
            print("\nThis prints a greeting using the name provided.")
            time.sleep(0.5)
            print("\ngreet(“Joe”)")
            print("\nCalls the function and gives it the value “Joe”.")
            print("\nSo it prints:\nHello, Joe!")
            continue
        elif user_submenu == 3:
            print("\nYou will now try using FUNCTIONS.")
            time.sleep(1)
            user_name = input("Enter your name: ")
            def greet(name):
                print(f"Hello, {name}! Welcome to the function workshop.")
            print("\nLet's see the function in action:")
            greet(user_name)
            time.sleep(1)
            def add_numbers(a, b):
                return a + b
            num1 = float(input("\nEnter the first number to add: "))
            num2 = float(input("Enter the second number to add: "))
            result = add_numbers(num1, num2)
            print(f"The sum of {num1} and {num2} is: {result}")
            time.sleep(1)
            print("\nReminder: To create reusable code, define a function using def.")
            print("Example:\ndef greet(name):\n    print(“Hello, ” + name)\nCall it using: greet(“Joe”)")
            time.sleep(1)
            continue
        elif user_submenu == 0:
            print("\nReturning to main menu")
            time.sleep(1)
            continue
        else:
            print("\nYou have entered an invalid choice, try again. Returning to main menu")
            time.sleep(1)
            continue
    elif user_menu == 0:
        print("\nThank you for using the Python Walkthrough Program!")
        break
    else:
        print("\nYou have entered an invalid choice, try again. Returning to main menu")
        time.sleep(1)
        continue