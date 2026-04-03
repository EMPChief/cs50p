Goal:
    Check if the user knows the answer to the ultimate question.

Input:
    - User answer (string)
      Examples: "42", "forty-two", "forty two"

Output:
    - "Yes" or "No"

Process / Steps:
    1. Ask user the question:
        "What is the Answer to the Great Question of Life, the Universe, and Everything?"
    2. Receive input from user
    3. Normalize input:
        - Convert to lowercase
        - Remove leading/trailing spaces
    4. Check answer:
        - If input is:
            "42" OR "forty-two" OR "forty two"
            → print "Yes"
        - Otherwise
            → print "No"
    5. Display result

Example:
    42          → Yes
    forty-two   → Yes
    forty two   → Yes
    43          → No