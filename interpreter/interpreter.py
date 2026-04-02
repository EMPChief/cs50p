# Main function that starts the calculator program
def main():
    interpreter()


# Function to interpret and calculate the user's math expression
def interpreter():
    # Prompt user to enter a mathematical expression like "50 / 5"
    get_user_math_question = input("Expression (e.g., 50 / 5): ")

    # Split the input into three parts: first number, operator, second number
    a, b, c = get_user_math_question.split(" ")

    # Convert the numbers from string to float for calculations
    a = float(a)
    c = float(c)

    # Determine the operation based on the operator and perform calculation
    if b == "+":
        print("Result:", a + c)
    elif b == "-":
        print("Result:", a - c)
    elif b == "/":
        print("Result:", a / c)
    elif b == "*":
        print("Result:", a * c)
    else:
        # Handle invalid operator input
        print("Invalid operator. Please use +, -, *, or /.")


# Run the program
main()
