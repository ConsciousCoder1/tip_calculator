from typing import final


print("Welcome to the Tip & Total Calculator Application.\n\nPlease follow the prompts below to calculate tip and total amount.\n\n")

# 1. Asks user to provide bill total.
bill_total = float(input("Please enter the total bill amount: "))

# 2. Asks user to select tip amount to apply to bill total.
tip_amount = float(input("What percentage of tip money would you like to leave - 15%, 18%, 20%?: "))

# 3. Asks user to determine and enter number of people to split bill between.
num_of_people = float(input("How many people do you wish to split the bill between?: "))

# 4. Calculates tip based on user input.
final_tip = float((bill_total) * ((tip_amount / 100) * 1)) + bill_total 
final_tip = "{:.2f}".format(final_tip / num_of_people)
    
print(f"Each person will pay ${final_tip}.")
