# Get the initial deposit from the user
initial_deposit = float(input("Enter the initial deposit amount: $"))

# Define the annual interest rate
interest_rate = 0.04  # 4 percent

# Calculate the balance after 1, 2, and 3 years
balance_after_1_year = initial_deposit * (1 + interest_rate)
balance_after_2_years = balance_after_1_year * (1 + interest_rate)
balance_after_3_years = balance_after_2_years * (1 + interest_rate)

# Display the results rounded to 2 decimal places
print("Balance after 1 year: ${:.2f}".format(balance_after_1_year))
print("Balance after 2 years: ${:.2f}".format(balance_after_2_years))
print("Balance after 3 years: ${:.2f}".format(balance_after_3_years))
