print("\nWelcome to Sam\'s Mortgage Calculator!\n")

# Input house purchase price
purchase_price = float(input("Please enter the price of the house you are purchasing:\n"))

# Calculate stamp duty
stamp_duty = 0
if purchase_price > 550000:
    stamp_duty = 28070 + ((purchase_price - 550000) * 0.06)
elif purchase_price > 440000 and purchase_price <= 550000:
    stamp_duty = 18370 + ((purchase_price - 440000) * 0.06)
else:
    stamp_duty = 2870 + ((purchase_price - 130000) * 0.05)

# Print stamp duty
print("\nYour stamp duty is: ${:.2f}\n".format(stamp_duty))

# Calculate profit from sale of house
sale_price = 470000
brad_commission = sale_price * 0.02
marketing_and_conveyancing = 5500
money_owed_on_campbell = 228000
sale_profit = sale_price - brad_commission - marketing_and_conveyancing - money_owed_on_campbell
car_loans = 53000
balance_after_car_loans = sale_profit - car_loans

# Amount needed to borrow considering profit from sale of house
borrow_amount = purchase_price + stamp_duty - balance_after_car_loans
print("You need to borrow: ${:.2f}\n".format(borrow_amount))

# Accept input of any extra cash needed
extra_cash = float(input("Please enter the amount of extra money you would like to borrow on top of the above amount:\n"))

# Update total borrow amount
borrow_amount = borrow_amount + extra_cash
print("\nYou need to borrow a total of: ${:.2f}\n".format(borrow_amount))

# Accept interest rate input
interest_rate = float(input("Please enter the interest rate:\n"))

# Accept loan duration input
loan_duration = float(input("\nPlease enter the loan duration in years:\n"))

# Total number of repayments
number_of_payments = loan_duration * 52

# Adjusted interest rate
interest_rate = interest_rate / 100 / 52

# Calculate weekly payment
weekly_payment = borrow_amount * ((interest_rate * ((1 + interest_rate) ** number_of_payments)) / ((1 + interest_rate) ** number_of_payments - 1))

# Print results
print("\nYour annual payment is: ${:.2f}\n".format(weekly_payment * 52))
print("Your monthly payment is: ${:.2f}\n".format(weekly_payment * 52 / 12))
print("Your weekly payment is: ${:.2f}\n".format(weekly_payment))
print("Given that you currently pay $632.50 a week on mortgage and car loans, this will cost an extra ${:.2f} a week\n".format(weekly_payment - 632.50))

