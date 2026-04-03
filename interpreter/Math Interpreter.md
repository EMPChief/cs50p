Purpose:
    Create a simple calculator that takes a user input expression 
    (like "50 / 5") and returns the result.

Inputs:
    - User enters an expression in the format:
        <number> <operator> <number>
      Example: 50 / 5

Process / Steps:
    1. Input Parsing:
        - Split the user input into three parts:
            a -> first number
            b -> operator (+, -, *, /)
            c -> second number
    2. Data Conversion:
        - Convert a and c from string to float for calculation.
    3. Operation Selection:
        - Use if-elif statements to determine the operator (b)
          and perform the corresponding calculation.
    4. Output Result:
        - Display the result to the user.
    5. Error Handling:
        - If the operator is invalid, show an error message.

Outputs:
    - The calculated result of the expression.
      Example: Input "50 / 5" -> Output: "Result: 10.0"