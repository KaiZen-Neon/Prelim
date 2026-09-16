user_input = input("Enter a multiple of 5 between 1 and 100: ")

if user_input.isdigit():
    number = int(user_input)
    
    if 1 <= number <= 100 and number % 5 == 0:
        print(f"Valid! {number} is a multiple of 5 between 1 and 100.")
    else:
        print(f"Invalid! {number} is not a valid multiple of 5 within the range.")
else:
    print("Invalid input! Please enter a whole number.")
