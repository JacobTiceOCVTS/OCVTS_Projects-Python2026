# Initialize variables for the calculator loop
loopProgam = True
num1 = None  # First operand
num2 = None  # Second operand
operator = None  # Operation to perform
result = None  # Result of the operation

print("Welcome to JTice Calculator App!")
# Main loop - continues until user exits
while loopProgam:
    # Keep looping until all required inputs are provided
    while num1 == None or num2 == None or operator == None:    
        # Get first number from user
        if num1 == None:
            try:
                num1 = float(input("Input the first number:\n"))
            except Exception as e:
                num1 = None
                print("Invalid Number")
                break
        # Get operator from user
        if operator == None:
            matchy = input("Input operator: (+, -, *, /, ^, sqrt, !)\n")
            # Match operator input to valid operators
            match matchy:
                case "+":
                    operator = "+"
                case "-":
                    operator = "-"
                case "*":
                    operator = "*"
                case "/":
                    operator = "/"
                case "^":
                    operator = "^"
                case "sqrt":
                    operator = "sqrt"
                case "!":
                    operator = "!"
                case "%":
                    operator = "%"
                case _:
                    operator == None
        # Skip second number input for single-operand operations (sqrt and factorial)
        if operator == "sqrt" or operator == "!":
            break
        # Get second number from user
        if num2 == None:
            try:
                num2 = float(input("Input the Second number:\n"))
            except Exception as e:
                num2 = None
                print("Invalid Number")
                break
    
    # Define calculator operation functions
    def add(num1, num2):
        return num1 + num2
    
    def subtract(num1, num2):
        return num1 - num2
    
    def multiply(num1, num2):
        return num1 * num2
    
    def divide(num1, num2):
        return num1 / num2
    
    def exponent(num1, num2):
        # Calculate num1 raised to the power of num2
        return num1 ** num2

    def sqrt(num1):
        # Calculate square root using exponent of 0.5
        return num1 ** 0.5
    
    def factorial(num1):
        # Calculate factorial (n!)
        if type(num1) != int:
            print("Invalid input for factorial, must be integer greater than or equal to 0")
            return None
        facResult = num1 * factorial(int(num1 - 1))
    
    def percent(num1, num2):
        # Calculate what percentage num1 is of num2
        return (num1 / num2) * 100

    # Execute the operation based on the selected operator
    match operator:
        case "+":
            result = add(num1, num2)
        case "-":
            result = subtract(num1, num2)
        case "*":
            result = multiply(num1, num2)
        case "/":
            result = divide(num1, num2)
        case "^":
            result = exponent(num1, num2)
        case "sqrt":
            result = sqrt(num1)
        case "!":
            result = factorial(num1)
        case "%":
            result = percent(num1, num2)
        case _:
            result == None

    # Display result if calculation was successful
    if result != None:
        print("Result: " + str(result))
    # Reset all variables for the next calculation
    num1 = None
    num2 = None
    operator = None
    result = None