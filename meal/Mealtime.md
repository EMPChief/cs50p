Purpose:
    Determine whether the current time falls into breakfast, lunch, or dinner time.

Inputs:
    - User enters the current time in "HH:MM" format.
      Example: 07:30, 12:15, 18:00

Process / Steps:
    1. Input:
        - Prompt user to enter the current time.
    2. Conversion:
        - Use the convert() function to split "HH:MM" into hours and minutes.
        - Convert it into decimal hours: hours + (minutes / 60)
    3. Time Checking:
        - Compare the converted time against predefined meal time ranges:
            Breakfast: 7 <= time <= 8
            Lunch:     12 <= time <= 13
            Dinner:    18 <= time <= 19
    4. Output:
        - Display the corresponding meal message.
        - If the time does not fall into any meal range, display "Not meal time".

Outputs:
    - A printed message indicating the current meal time or "Not meal time".
      Example: Input "07:30" -> Output: "Breakfast time"