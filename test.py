# Initialize the starting amount and number of days
starting_amount = 2
days = 30

# Initialize total earnings
total = 0

# Loop through each day
for day in range(1, days + 1):
    total += starting_amount
    print(f"Day {day}: {starting_amount} rupees")  # Display daily earnings
    starting_amount *= 2  # Double the amount for the next day

# Display total earnings after 30 days
print("\nTotal earnings after 30 days:", total, "rupees")
