# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# =============================================================================
#
# TASK: Console-Based Simple Calculator
#
# Build a calculator program that runs in the console and performs basic
# arithmetic operations based on the user's input.
#
# -----------------------------------------------------------------------------
# OPERATIONS YOUR CALCULATOR MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Addition          ( + )    e.g.  10 + 3  =  13
#   2. Subtraction       ( - )    e.g.  10 - 3  =  7
#   3. Multiplication    ( * )    e.g.  10 * 3  =  30
#   4. Division          ( / )    e.g.  10 / 3  =  3.33
#   5. Modulus           ( % )    e.g.  10 % 3  =  1  (remainder)
#   6. Exponentiation    ( ** )   e.g.  2 ** 8  =  256
#   7. Quit
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        SIMPLE CALCULATOR
#   ============================
#   1. Addition
#   2. Subtraction
#   3. Multiplication
#   4. Division
#   5. Modulus
#   6. Exponentiation
#   7. Quit
#   Select an operation (1-7):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Select an operation (1-7): 4
#   Enter first number : 10
#   Enter second number: 3
#   Result: 10 / 3 = 3.33
#
#   Select an operation (1-7): 4
#   Enter first number : 5
#   Enter second number: 0
#   Error: Cannot divide by zero.
#
#   Select an operation (1-7): 7
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Each arithmetic operation MUST be written as its own function.
# - Use a loop so the calculator keeps running until the user selects Quit.
# - Division by zero must be caught and handled with a clear error message
#   (do NOT let the program crash).
# - Division results should be rounded to 2 decimal places.
# - Handle invalid menu choices gracefully.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return round(a / b, 2)

def modulus(a, b):
    if b == 0:
        return "Error: Cannot calculate modulus with zero."
    # Return int if it's a whole number, else float, to match standard calculator behavior
    result = a % b
    return int(result) if result.is_integer() else result

def exponentiate(a, b):
    return a ** b

def get_number(prompt):
    """Bulletproof numeric input handler. Trust no user."""
    while True:
        user_input = input(prompt).strip()
        try:
            return float(user_input)
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")

def main():
    """Main execution loop. Runs until terminated."""
    operations = {
        '1': ('Addition', '+', add),
        '2': ('Subtraction', '-', subtract),
        '3': ('Multiplication', '*', multiply),
        '4': ('Division', '/', divide),
        '5': ('Modulus', '%', modulus),
        '6': ('Exponentiation', '**', exponentiate)
    }
    
    while True:
        print("============================")
        print("     SIMPLE CALCULATOR")
        print("============================")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Exponentiation")
        print("7. Quit")
        
        choice = input("Select an operation (1-7): ").strip()
        
        if choice == '7':
            print("Goodbye!")
            break
            
        if choice not in operations:
            print("Error: Invalid choice. Please enter 1-7.\n")
            continue
            
        op_name, op_symbol, op_func = operations[choice]
        
        num1 = get_number("Enter first number : ")
        num2 = get_number("Enter second number: ")
        
        result = op_func(num1, num2)
        
        # Format output to match expected interaction
        if isinstance(result, str): # Catches the error messages
            print(result)
        else:
            # Format numbers: remove .0 for clean display if they are whole numbers
            n1_display = int(num1) if num1.is_integer() else num1
            n2_display = int(num2) if num2.is_integer() else num2
            res_display = int(result) if isinstance(result, float) and result.is_integer() else result
            print(f"Result: {n1_display} {op_symbol} {n2_display} = {res_display}")
        print()

if __name__ == "__main__":
    main()
