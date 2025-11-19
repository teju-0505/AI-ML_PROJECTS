print("Welcome to the Student Data Organizer!\n")

students = []
all_subjects = set()

while True:
    print("Select an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nEnter student details:")
        sid = input("Student ID: ").strip()
        name = input("Name: ").strip()
        age = int(input("Age: ").strip())
        grade = input("Grade: ").strip()
        dob = input("Date of Birth (YYYY-MM-DD): ").strip()

        subj_line = input("Subjects (comma-separated): ").strip()
        subjects = [s.strip() for s in subj_line.split(",")]


        for s in subjects:
            duplicate_found = False
            for exist in all_subjects:   
                if s == exist:
                    duplicate_found = True
                    break
            if not duplicate_found:
                all_subjects.add(s)

        unique_info = (sid, dob)

        student_dict = {
            "id": sid,
            "name": name,
            "age": age,
            "grade": grade,
            "dob": dob,
            "subjects": subjects,
            "unique": unique_info
        }

        students.append(student_dict)

        print("\nStudent added successfully!\n")


    elif choice == "2":
        print("\n--- Display All Students ---")

        if len(students) == 0:
            print("No student records found.\n")
        else:
            for stu in students:                  
                subjects_str = ""
                for sub in stu["subjects"]:         
                    subjects_str += sub + ", "
                subjects_str = subjects_str.rstrip(", ")

                print(
                    f"Student ID: {stu['id']} | Name: {stu['name']} | "
                    f"Age: {stu['age']} | Grade: {stu['grade']} | "
                    f"Subjects: {subjects_str}"
                )
            print()


    elif choice == "3":
        sid = input("Enter Student ID to update: ")
        found = False

        for stu in students:
            if stu["id"] == sid:
                found = True
                print("\nWhat do you want to update?")
                print("1. Age")
                print("2. Subjects")
                opt = input("Enter choice: ")

                if opt == "1":
                    new_age = int(input("Enter new age: "))
                    stu["age"] = new_age
                    print("Age updated successfully!\n")

                elif opt == "2":
                    new_subj = input("Enter new subjects (comma-separated): ")
                    subs_list = [x.strip() for x in new_subj.split(",")]

                    for s in subs_list:             
                        exists = False
                        for a in all_subjects:      
                                exists = True
                                break
                        if not exists:
                            all_subjects.add(s)

                    stu["subjects"] = subs_list
                    print("Subjects updated successfully!\n")
                break

        if not found:
            print("Student ID not found.\n")


    elif choice == "4":
        sid = input("Enter Student ID to delete: ")

        index = -1
        for i, stu in enumerate(students):
            if stu["id"] == sid:
                index = i
                break

        if index != -1:
            del students[index]
            print("Student deleted successfully!\n")
        else:
            print("Student ID not found.\n")


    elif choice == "5":
        print("\n--- Unique Subjects Offered ---")
        if len(all_subjects) == 0:
            print("No subjects available.")
        else:
            for s in all_subjects:
                for char in s: 
                    pass
                print(s, end=", ")
        print("\n")


    elif choice == "6":
        print("\nThank you for using the Student Data Organizer!")
        break

    else:
        print("Invalid choice. Try again.\n")
