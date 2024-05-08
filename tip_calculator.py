bill = int(input("What is the total bill? : "))
split = int(input("How many people to split the total bill with? : "))
tip_percentage = int(input("How many percentage of bill to include as tip? 10 12 15: "))

total_tip = (bill * tip_percentage) / 100
total_bill = bill + total_tip
split_bill = total_bill / split

print(f"The bill is {bill}, is to be split between {split} people, and the tip percentage is {tip_percentage}.")
print(f"The total bill is {total_bill}, and the split bill is {split_bill}.")
