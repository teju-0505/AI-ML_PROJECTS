print("---Python OOP PROJECT: Employee Management system--- ")

while True:
    print("Choose an opration: ")
    print("1.create a person")
    print("2.create an Employee")
    print("3.create a Manager")
    print("4.Show Details")
    print("5.Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        print(f"Person created with name: {name} and Age: {age}.")
        print("---- Choose another operation ----")

    if choice == 2:
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        employee = str(input("Enter Employee ID: "))
        salary = int(input("Enter Salary: "))
        print(f"Employee created with Name: {name}, Age: {age}, Id: {employee}, and Salary: ${salary}.") 
        print("---- Choose another operation ----")

    if choice == 3:
         name = input("Enter Name: ")
         age = int(input("Enter Age: "))
         employee = str(input("Enter Employee ID: "))
         salary = int(input("Enter Salary: "))
         department = input("Enter Department: ")
         print(f"Employee created with Name: {name}, Age: {age}, Id: {employee}, and Salary: ${salary}, And Department: {department}.")
         print("---- Choose another operation ----")

    if choice == 4:
        print("Choose details to show: ")
        print("1. Person")
        print("2. Employee")
        print("3. Manager")
        choice = int(input("Enter your choice: "))

        print("Employee Details: ")
        print(f"Name:{name} ")
        print(f"age:{age} ")
        print(f"Employee ID: {employee}")
        print(f"Salary: ${salary}")
        print("---- Choose another operation ----")

    elif choice == 5:
        print("Exiting the system. All resources have been freed.")
        print("GOODBYE!")
        break