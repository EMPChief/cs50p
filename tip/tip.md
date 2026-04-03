Goal:
Calculate the tip amount based on meal cost and desired tip percentage.

Input: - Meal cost (string with optional "$")
Example: "$50", "25" - Tip percentage (string with optional "%")
Example: "15%", "20"

Output: - Tip amount formatted as a dollar string
Example: "Leave $7.50"

Process / Steps: 1. Ask user for meal cost - Remove "$" if present - Convert to float 2. Ask user for tip percentage - Remove "%" if present - Convert to decimal (divide by 100) 3. Calculate tip: - tip = meal cost × tip percentage 4. Display result: - Format tip to 2 decimal places - Print as "Leave $<tip>"

Example:
Meal: $50, Tip: 15% → Leave $7.50
Meal: 25, Tip: 20% → Leave $5.00
