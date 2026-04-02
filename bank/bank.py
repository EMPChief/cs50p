# Initialize the main and start the program so we can program top down
def main() -> None:
    greeting: str = get_user_input()
    amount: int = classify_greeting(greeting)
    print(bank_answer(amount))


# Asking the user for input
def get_user_input() -> str:
    bank_customer: str = str(input("Greeting: ")).strip().lower()
    print(bank_customer)
    return bank_customer


# Run the greeting through if/elif conditions to decide the response value
def classify_greeting(bank_customer: str) -> int:
    if bank_customer == "hello" or bank_customer == "hello, newman":
        return 0
    elif bank_customer == "how you doing?":
        return 20
    else:
        return 100


# Separated the answer part to make it more modular and easier to check
def bank_answer(n: int) -> str:
    return f"${n}"


# Starts the program
main()
