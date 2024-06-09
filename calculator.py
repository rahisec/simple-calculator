import math

class Colors:
    CYAN = '\033[96m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    RED = '\033[91m'
    MAGENTA = '\033[95m'
    RESET = '\033[0m'

calculator_art = r"""

 ██████╗ █████╗ ██╗      ██████╗██╗   ██╗██╗      █████╗ ████████╗ ██████╗ ██████╗ 
██╔════╝██╔══██╗██║     ██╔════╝██║   ██║██║     ██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
██║     ███████║██║     ██║     ██║   ██║██║     ███████║   ██║   ██║   ██║██████╔╝
██║     ██╔══██║██║     ██║     ██║   ██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗
╚██████╗██║  ██║███████╗╚██████╗╚██████╔╝███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║
 ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
   Author: Md. Fazle Rabbi
"""

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def modulus(x, y):
    return x % y

def exponentiate(x, y):
    return x ** y

def square_root(x):
    return math.sqrt(x)

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

print(Colors.CYAN + calculator_art + Colors.RESET)
print(Colors.YELLOW + "Welcome to The Calculator!" + Colors.RESET)

def print_menu():
    print(Colors.RED + "-"*50 + Colors.RESET)
    print(Colors.RED + "-"*50 + Colors.RESET)
    print(Colors.GREEN + ">> Select operation:" + Colors.RESET)
    print(Colors.MAGENTA + "-"*50 + Colors.RESET)
    print(Colors.BLUE + "1. Add           2. Subtract" + Colors.RESET)
    print(Colors.BLUE + "3. Multiply      4. Divide" + Colors.RESET)
    print(Colors.BLUE + "5. Modulus       6. Exponentiation" + Colors.RESET)
    print(Colors.BLUE + "7. Square Root   8. Sine" + Colors.RESET)
    print(Colors.BLUE + "9. Cosine        10. Tangent" + Colors.RESET)
    print(Colors.BLUE + "11. Clear Screen 12. View History" + Colors.RESET)
    print(Colors.BLUE + "13. Exit" + Colors.RESET)
    print(Colors.MAGENTA + "-"*50 + Colors.RESET)
    print(Colors.MAGENTA + "-"*50 + Colors.RESET)

def clear_screen():
    print("\033[H\033[J", end="")

history = []

while True:
    print_menu()
    choice = input(Colors.CYAN + "Enter choice(1-13): " + Colors.RESET)

    if choice == '13':
        print(Colors.YELLOW + "Goodbye!" + Colors.RESET)
        break

    if choice == '11':
        clear_screen()
        continue

    if choice == '12':
        if history:
            print(Colors.MAGENTA + "Calculation History:" + Colors.RESET)
            for record in history:
                print(record)
        else:
            print(Colors.MAGENTA + "No calculations yet." + Colors.RESET)
        continue

    if choice in ('1', '2', '3', '4', '5', '6'):
        try:
            num1 = float(input(Colors.CYAN + "Enter first number: " + Colors.RESET))
            num2 = float(input(Colors.CYAN + "Enter second number: " + Colors.RESET))
            print(Colors.MAGENTA + "-"*50 + Colors.RESET)
        except ValueError:
            print(Colors.RED + "Invalid input. Please enter a number." + Colors.RESET)
            continue
    elif choice in ('7', '8', '9', '10'):
        try:
            num1 = float(input(Colors.CYAN + "Enter number: " + Colors.RESET))
            print(Colors.MAGENTA + "-"*50 + Colors.RESET)
        except ValueError:
            print(Colors.RED + "Invalid input. Please enter a number." + Colors.RESET)
            continue

    if choice == '1':
        result = add(num1, num2)
        print(Colors.GREEN + f"{num1} + {num2} = {result}" + Colors.RESET)
        history.append(f"{num1} + {num2} = {result}")

    elif choice == '2':
        result = subtract(num1, num2)
        print(Colors.GREEN + f"{num1} - {num2} = {result}" + Colors.RESET)
        history.append(f"{num1} - {num2} = {result}")

    elif choice == '3':
        result = multiply(num1, num2)
        print(Colors.GREEN + f"{num1} * {num2} = {result}" + Colors.RESET)
        history.append(f"{num1} * {num2} = {result}")

    elif choice == '4':
        result = divide(num1, num2)
        print(Colors.GREEN + f"{num1} / {num2} = {result}" + Colors.RESET)
        history.append(f"{num1} / {num2} = {result}")

    elif choice == '5':
        result = modulus(num1, num2)
        print(Colors.GREEN + f"{num1} % {num2} = {result}" + Colors.RESET)
        history.append(f"{num1} % {num2} = {result}")

    elif choice == '6':
        result = exponentiate(num1, num2)
        print(Colors.GREEN + f"{num1} ^ {num2} = {result}" + Colors.RESET)
        history.append(f"{num1} ^ {num2} = {result}")

    elif choice == '7':
        result = square_root(num1)
        print(Colors.GREEN + f"√{num1} = {result}" + Colors.RESET)
        history.append(f"√{num1} = {result}")

    elif choice == '8':
        result = sin(num1)
        print(Colors.GREEN + f"sin({num1}) = {result}" + Colors.RESET)
        history.append(f"sin({num1}) = {result}")

    elif choice == '9':
        result = cos(num1)
        print(Colors.GREEN + f"cos({num1}) = {result}" + Colors.RESET)
        history.append(f"cos({num1}) = {result}")

    elif choice == '10':
        result = tan(num1)
        print(Colors.GREEN + f"tan({num1}) = {result}" + Colors.RESET)
        history.append(f"tan({num1}) = {result}")

    else:
        print(Colors.RED + "Invalid Input" + Colors.RESET)
        continue

    print(Colors.MAGENTA + "-"*50 + Colors.RESET)

    next_calculation = input(Colors.MAGENTA + "Let's do next calculation? (yes=Enter/no): " + Colors.RESET)
    if next_calculation.lower() == "no":
        print(Colors.RED + "Goodbye!" + Colors.RESET)
        break
