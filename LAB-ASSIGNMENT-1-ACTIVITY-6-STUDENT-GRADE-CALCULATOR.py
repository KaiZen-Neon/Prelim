print("STUDENT GRADE CALCULATOR:\n")

while True:

    while True:
        try:
            java_score = float(input("Enter your Java Programming Score: "))
            if 0 <= java_score <= 100:
                break
            else:
                print("Invalid score. Please enter a score from 0 to 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric score.")


    while True:
        try:
            c_score = float(input("Enter your C Programming Score: "))
            if 0 <= c_score <= 100:
                break
            else:
                print("Invalid score. Please enter a score from 0 to 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric score.")

    while True:
        try:
            database_score = float(input("Enter your Database Handling Score: "))
            if 0 <= database_score <= 100:
                break
            else:
                print("Invalid score. Please enter a score from 0 to 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric score.")

    average = (java_score + c_score + database_score) / 3

    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 75:
        grade = "C"
    else:
        grade = "F"

    print("\nAverage:", f"{average:.2f}")
    print("Grade:", grade)
    print(f"Explanation: The average is {average:.2f}, so the student's grade is {grade}.")

    while True:
        continue_choice = input("\nDo you want to continue? (YES/NO): ").strip().upper()

        if continue_choice == "YES":
            print("\n" + "=" * 40)
            break
        elif continue_choice == "NO":
            print("Program terminated. Thank you!")
            exit()
        else:
            print("Invalid input. Please enter YES or NO.")
