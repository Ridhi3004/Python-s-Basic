while True:
    n = int(input("Enter first number: "))
    m = int(input("Enter second number: "))

    print("Choose operation:")
    print("+ for Addition")
    print("- for Subtraction")
    print("* for Multiplication")
    print("/ for Division")
    print("% for Modulus")

    operation = input("Enter operation: ")

    if operation == "+":
        print("Result:", n + m)
    elif operation == "-":
        print("Result:", n - m)
    elif operation == "*":
        print("Result:", n * m)
    elif operation == "/":
        print("Result:", n / m)
    elif operation == "%":
        print("Result:", n % m)
    else:
        print("Invalid operation")

    again=input("Wanna Continue? (yes/no):")
    if again == "no":
        print("The End")
        break
    elif again == "yes":
         print("Let's do it again")
    else:
        print("Invalid")
        



