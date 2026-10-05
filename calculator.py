# ============================================
# PROJECT: Simple Calculator
# AUTHOR: (Your Name)
# INTERNSHIP: Syntecxhub
# ============================================

# --------------------------------------------
# PART 1: CALCULATION FUNCTIONS
# These do the math. They just take numbers
# and give back a result. Easy to test!
# --------------------------------------------

def add(a, b):
    # This function adds two numbers
    # 'a' and 'b' are the inputs
    # 'return' sends the answer back
    return a + b


def subtract(a, b):
    # This function subtracts b from a
    return a - b


def multiply(a, b):
    # This function multiplies two numbers
    # Example: multiply(4, 5) gives 20
    return a * b


def divide(a, b):
    # This function divides a by b
    # But we must check: can we divide by zero?
    if b == 0:
        # If b is zero, math breaks!
        # So we raise a friendly error message
        raise ValueError("Cannot divide by zero!")
    # If b is not zero, do the division
    return a / b


# --------------------------------------------
# PART 2: INPUT HELPER FUNCTIONS
# These ask the user for input and make sure
# the input is valid (not letters, not symbols)
# --------------------------------------------

def get_number(prompt):
    # 'prompt' is the message we show the user
    # Example: "Enter a number: "
    while True:
        # 'while True' means: keep looping forever
        # until we hit a 'return' or 'break'
        try:
            # 'try' means: attempt this code
            # 'input()' asks the user to type something
            # 'float()' converts text to a decimal number
            # So if user types "5", float("5") = 5.0
            return float(input(prompt))
        except ValueError:
            # 'except' means: if the try block failed
            # 'ValueError' happens when float() can't convert
            # Example: float("hello") fails
            # So we print a friendly message
            print("❌ That's not a valid number. Try again.")


def get_operator():
    # This function asks the user for a math operator
    # Allowed operators: +, -, *, /, clear
    valid = ['+', '-', '*', '/', 'clear']
    # 'valid' is a list of allowed answers

    while True:
        # Keep asking until user gives a valid operator
        # 'input()' asks the user to type
        # '.strip()' removes extra spaces from start/end
        # '.lower()' turns "CLEAR" into "clear"
        op = input("Enter operator (+, -, *, /) or 'clear': ").strip().lower()

        # Check if what they typed is in our valid list
        if op in valid:
            # If yes, send it back
            return op

        # If not valid, show error and loop again
        print("❌ Invalid operator. Try again.")


# --------------------------------------------
# PART 3: MAIN FUNCTION
# This is the brain of the program.
# It shows the menu and runs the loop.
# --------------------------------------------

def main():
    # 'def main()' defines the main function
    # Greet the user with a nice message
    print("🧮 Welcome to the Simple Calculator!")

    # 'result' keeps the running answer
    # We start at 0
    result = 0

    while True:
        # Loop forever until user chooses to exit
        # Show the current result so far
        print(f"\nCurrent result: {result}")
        # '\n' means a blank line (new line)

        # Ask the user which operator they want
        op = get_operator()

        # If user typed 'clear', reset everything
        if op == 'clear':
            result = 0  # set result back to zero
            print("🧹 Cleared! Result is now 0.")
            continue
            # 'continue' means: skip the rest of the loop
            # and go back to the top (show result again)

        # Ask the user for a number
        num = get_number("Enter a number: ")

        # Now do the math based on the operator
        try:
            # 'try' because divide() might crash on zero
            if op == '+':
                # If user chose +, add the numbers
                result = add(result, num)
            elif op == '-':
                # If user chose -, subtract
                result = subtract(result, num)
            elif op == '*':
                # If user chose *, multiply
                result = multiply(result, num)
            elif op == '/':
                # If user chose /, divide
                result = divide(result, num)

            # Show the new result
            print(f"✅ Result: {result}")

        except ValueError as e:
            # If divide() raised an error, catch it here
            # 'e' holds the error message
            # Example: "Cannot divide by zero!"
            print(f"❌ Error: {e}")

        # Ask if user wants to continue
        again = input("Continue? (y/n): ").strip().lower()

        # If they didn't say yes, exit the loop
        if again != 'y':
            print("👋 Goodbye!")
            break
            # 'break' means: stop the while loop entirely


# --------------------------------------------
# PART 4: START THE PROGRAM
# This line says: only run main() if this file
# is being run directly (not imported).
# --------------------------------------------

if __name__ == "__main__":
    # If the file is run directly, call main()
    main()