Goal:
    Evaluate a simple mathematical expression.

Input:
    - Expression in format: <number> <operator> <number>
      Example: 50 / 5

Output:
    - Result of calculation OR error message

Process / Steps:
    1. Receive expression from user
    2. Split input into 3 parts:
        a → first number
        b → operator (+, -, *, /)
        c → second number
    3. Validate input:
        - Ensure exactly 3 parts exist
    4. Convert numbers:
        - Convert a and c to numeric values (float)
    5. Perform operation:
        - + → addition
        - - → subtraction
        - * → multiplication
        - / → division (check division by zero)
    6. Handle errors:
        - Invalid operator → show error
        - Division by zero → show error
        - Invalid format → show error
    7. Return result

Example:
    50 / 5 → Result: 10.0
    10 * 3 → Result: 30.0