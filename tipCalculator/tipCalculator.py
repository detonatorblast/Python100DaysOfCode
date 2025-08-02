# This is a simple tip calculator program.
print ("Welcome to the Tip Calculator!")
print ("What was the total bill? $", end="")
total_bill = float(input())
print ("What percentage tip would you like to give? 10, 12, or 15? ", end="")
tip_percentage = int(input())
tip_amount = total_bill * (tip_percentage / 100)
print ("How many people to split the bill? ", end="")
num_people = int(input())
total_amount = total_bill + tip_amount
amount_per_person = total_amount / num_people
print ("Total bill: $", total_bill)
print ("Tip amount: $", tip_amount)
print ("Total amount: $", total_amount)
print ("Amount per person: $", amount_per_person, end="$\n")
print ("Thank you for using the Tip Calculator!")