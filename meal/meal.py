# Main function
def main() -> None:
    # Ask the user for the current time
    user_time: str = input("What time is it? (HH:MM) ")

    # Convert user input into decimal hours
    converted_time: float = convert(user_time)

    # Determine meal time
    if 7 <= converted_time <= 8:
        print("Breakfast time")
    elif 12 <= converted_time <= 13:
        print("Lunch time")
    elif 18 <= converted_time <= 19:
        print("Dinner time")
    else:
        print("Not meal time")


# Function to convert time string "HH:MM" to decimal hours
def convert(time: str = "0:00") -> float:
    # Split the input string into hour and minute
    hour, minute = time.split(":")

    # Convert to decimal hours
    return int(hour) + int(minute) / 60


#

# Entry point
if __name__ == "__main__":
    main()
