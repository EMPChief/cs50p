Goal:
    Determine a dollar amount based on the user's greeting.

Input:
    - Greeting (string)
      Examples: "hello", "how you doing?", "good morning"

Output:
    - Dollar amount (string)
      Examples: "$0", "$20", "$100"

Process / Steps:
    1. Receive greeting from user
    2. Normalize input:
        - Remove leading/trailing spaces
        - Convert to lowercase
    3. Check greeting:
        - If greeting is "hello" or "hello, newman"
            → return 0
        - Else if greeting is "how you doing?"
            → return 20
        - Otherwise
            → return 100
    4. Format result:
        - Add "$" in front of the number
    5. Display result

Example:
    hello              → $0
    how you doing?    → $20
    good morning      → $100