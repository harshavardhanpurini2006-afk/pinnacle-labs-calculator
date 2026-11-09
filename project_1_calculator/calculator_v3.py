while True:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Choose an operation (1-5): ")

    if choice == "1":
        print("Addition:", num1 + num2)

    elif choice == "2":
        print("Subtraction:", num1 - num2)

    elif choice == "3":
        print("Multiplication:", num1 * num2)

    elif choice == "4":
        if num2 != 0:
            print("Division:", num1 / num2)
        else:
            print("Cannot divide by zero")

    elif choice == "5":
        print("Calculator Closed")
        break

    else:
        print("Invalid choice")