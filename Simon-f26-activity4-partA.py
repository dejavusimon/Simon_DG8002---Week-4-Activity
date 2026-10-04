# DG8002 - F26 - Activity 4
# Author Name: Simon Su
# Date: Oct.04.2026


savings_goal = float(input("Enter your desired savings goal ($): "))
base_investment = float(input("Enter your base investment ($): "))
annual_rate = float(input("Enter the annual interest rate (%): "))
monthly_deposit = float(input("Enter your monthly deposit ($, 0 if none): "))

# Converting to a monthly decimal rate
monthly_rate = annual_rate / 100 / 12

months = 0
balance = base_investment

if balance < savings_goal and monthly_rate <= 0 and monthly_deposit <= 0:
    print("With no interest and no monthly deposits, your balance will never reach your goal.")
else:
    while balance < savings_goal:
        balance += monthly_deposit
        interest_earned = balance * monthly_rate
        balance += interest_earned
        months += 1

    print(f"\nFinal balance: ${balance:,.2f}")
    if months > 12:
        years = months / 12
        print(f"It will take about {years:.1f} years to reach your goal of ${savings_goal:,.2f}.")
    else:
        print(f"It will take {months} month(s) to reach your goal of ${savings_goal:,.2f}.")