#user inputs
monthly_income = float(input("Enter your monthly income:"))
monthly_expenses = float(input("Enter you total monthly expenses:"))

#monthly savings
monthly_savings = monthly_income - monthly_expenses

#projected annual savings
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

#output results
print(f"Your monthly savings are ${monthly_savings}")
print(f"Projected savings after one year, with interest, is: ${projected_savings}")