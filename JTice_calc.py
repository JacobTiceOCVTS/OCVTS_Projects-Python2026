loopProgam = True
num1 = None
num2 = None
operator = None
result = None

print("Welcome to JTice Calculator App!")
while loopProgam:
    while num1 == None or num2 == None or operator == None:    
        if num1 == None:
            try:
                num1 = float(input("Input the first number:\n"))
            except Exception as e:
                num1 = None
                print("Invalid Number")
                break
        if operator == None:
            matchy = input("Input operator: (+, -, *, /, ^, sqrt, !)\n")
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
        if operator == "sqrt" or operator == "!":
            break
        if num2 == None:
            try:
                num2 = float(input("Input the Second number:\n"))
            except Exception as e:
                num2 = None
                print("Invalid Number")
                break
    
    def add(num1, num2):
        return num1 + num2
    
    def subtract(num1, num2):
        return num1 - num2
    
    def multiply(num1, num2):
        return num1 * num2
    
    def divide(num1, num2):
        return num1 / num2
    
    def exponent(num1, num2):
        return num1 ** num2

    def sqrt(num1):
        return num1 ** 0.5
    
    def factorial(num1):
        if type(num1) != int:
            print("Invalid input for factorial, must be integer greater than or equal to 0")
            return None
        facResult = num1 * factorial(int(num1 - 1))
    
    def percent(num1, num2):
        return (num1 / num2) * 100

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

    if result != None:
        print("Result: " + str(result))
        num1 = None
        num2 = None
        operator = None
        result = None