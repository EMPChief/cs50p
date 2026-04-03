Goal:
    Determine the current meal time based on input time.

Input:
    - Time in "HH:MM" format
      Example: 07:30, 12:15, 18:00

Output:
    - "Breakfast time", "Lunch time", "Dinner time", or "Not meal time"

Process / Steps:
    1. Receive time input from user
    2. Validate format:
        - Must be HH:MM
    3. Convert time:
        - Split into hours and minutes
        - Convert into decimal:
            time = hours + (minutes / 60)
    4. Compare time ranges:
        - Breakfast: 7.0 ≤ time ≤ 8.0
        - Lunch:     12.0 ≤ time ≤ 13.0
        - Dinner:    18.0 ≤ time ≤ 19.0
    5. Return result:
        - If within range → return corresponding meal
        - Otherwise → "Not meal time"
    6. Handle errors:
        - Invalid format → return error message

Example:
    07:30 → Breakfast time
    12:15 → Lunch time
    18:00 → Dinner time
    15:00 → Not meal time