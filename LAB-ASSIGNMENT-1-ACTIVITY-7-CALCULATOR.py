while True:
 
    print("\nARITHMETIC CALCULATOR")
    print("1. Addition          2. Subtraction       3. Multiplication")
    print("4. Division          5. Modulus           6. Increment")
    print("7. Decrement")

    while True:
        try:
            choice = int(input("\nSelect an arithmetic operation: "))

            if 1 <= choice <= 7:
                break
            else:
                print("Invalid menu option. Please select a number from 1 to 7.")
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 7.")
            
    if choice in [1, 2, 3, 4, 5]:

        while True:
            try:
                x = float(input("Enter the value of x: "))
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        while True:
            try:
                y = float(input("Enter the value of y: "))
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        print(f"\nVariable Values: x = {x}, y = {y}")

        if choice == 1:
            result = x + y
            print(f"Addition: x + y = {result}")

        elif choice == 2:
            result = x - y
            print(f"Subtraction: x - y = {result}")

        elif choice == 3:
            result = x * y
            print(f"Multiplication: x * y = {result}")

        elif choice == 4:
            if y == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = x / y
                print(f"Division: x / y = {result}")

        elif choice == 5:
            if y == 0:
                print("Error: Modulus by zero is not allowed.")
            else:
                result = x % y
                print(f"Modulus: x % y = {result}")

    elif choice == 6:

        while True:
            try:
                x = float(input("Enter the value of x: "))
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        result = x + 1

        print(f"\nVariable Values: x = {x}")
        print(f"Increment: x + 1 = {result}")
        
    elif choice == 7:

        while True:
            try:
                x = float(input("Enter the value of x: "))
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        result = x - 1

        print(f"\nVariable Values: x = {x}")
        print(f"Decrement: x - 1 = {result}")

    while True:
        continue_choice = input("\nDo you want to continue? (YES/NO): ").strip().upper()

        if continue_choice == "YES":
            break
        elif continue_choice == "NO":
            print("Program terminated. Thank you!")
            exit()
        else:
            print("Invalid input. Please enter YES or NO.")
    