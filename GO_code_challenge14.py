import os
import json
os.system('cls')

print("Hello this is the STUDENT INFORMATION SYSTEM")
user_input = ""
student_info = {} 

while user_input != "G":
    print("\nA: Add Student Record")
    print("B: Print All Student Record")
    print("C: Search Student Record") 
    print("D: Delete Student Record")
    print("E: Edit Student Record")
    print("F: Export Student Record")
    print("G: Exit System")
    user_input = input("\nWhat action do you want to take? " ).upper()

    if user_input == "A":
        new_user = []
        add_id = eval(input("What is their ID NUMBER? " ))
        add_last = input("What is their LAST NAME? " )
        add_first = input("What is their FIRST NAME? " )
        add_age = input("What is their AGE? " )
        add_section = input("What is their SECTION? " )
        add_course = input("What is their COURSE? " )
        new_user = [add_last, add_first, add_age, add_course, add_section]
        student_info[add_id] = new_user
        continue
    elif user_input == "B":
        for key, value in student_info.items():
            print(f"{key}: {value}")   
        continue
    elif user_input == "C":
        search_input = eval(input("What is their ID NUMBER to SEARCH? \n" ))
        for each_id in student_info.keys():
            if search_input in student_info.keys():
                print("\nRecord Found")
                print(student_info[search_input])
            else:
                print("\nNo Record Found")
        continue
    elif user_input == "D":
        delete_input = eval(input("What ID NUMBER do you want to DELETE? " ))
        student_info.pop(delete_input)
        print("You have successfuly deleted", delete_input)
        continue
    elif user_input == "E":
        edit_input = eval(input("What ID NUMBER do you want to EDIT? " ))
        print("LAST NAME / FIRST NAME / AGE / SECTION / COURSE")
        what_to_edit = input("What will you EDIT? " ).upper()
        if what_to_edit == "LAST NAME":
            new_last = input("What is their new last name? " )
            student_info[edit_input].pop(0)
            student_info[edit_input].insert(0, new_last)
            print("You have updated their LAST NAME")
            continue
        if what_to_edit == "FIRST NAME":
            new_first = input("What is their new first name? " )
            student_info[edit_input].pop(1)
            student_info[edit_input].insert(1, new_first)
            print("You have updated their FIRST NAME")
            continue
        if what_to_edit == "AGE":
            new_age = input("What is their new age? " )
            student_info[edit_input].pop(2)
            student_info[edit_input].insert(2, new_age)
            print("You have updated their AGE")
            continue
        if what_to_edit == "SECTION":
            new_section = input("What is their new section? " )
            student_info[edit_input].pop(3)
            student_info[edit_input].insert(3, new_section)
            print("You have updated their SECTION")
            continue
        if what_to_edit == "COURSE":
            new_course = input("What is their new course? " )
            student_info[edit_input].pop(4)
            student_info[edit_input].insert(4, new_course)
            print("You have updated their COURSE")
            continue
        continue
    elif user_input == "F":
        print("Exporting all student records now...")
        with open('student_records.json', 'w') as new_file:
            json.dump(student_info, new_file, indent=3)
        continue
    print("\nThank you for using the STUDENT INFORMATION SYSTEM!!")
    break
