print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? \n$"))
tip = int(input("What percentage tip would you like to give? 10%, 12%, 15%\n"))
people = int(input("How many people to split the bill?\n"))

Total_bill_Amount_plus_tip = float(bill*(tip/100) + bill)
Final_Amount =float(Total_bill_Amount_plus_tip/people)
print (f"Each Person should pay:${round(Final_Amount,2)}.")