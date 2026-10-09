# Joey Strada
# 10/4/2026
# Homework 2

# the inputs
principal = float(input("Enter the loan amount ($): "))
annual_rate_percent = float(input("Enter the annual interest rate (%): "))
years = int(input("Enter the loan term (years) : "))

# processing
annual_rate = annual_rate_percent / 100
monthly_rate = annual_rate / 12
num_payments = years * 12

if monthly_rate == 0:
    monthly_payment = principal / num_payments
else:
    monthly_payment = (
        principal
        * (monthly_rate * (1 + monthly_rate) ** num_payments)
        / ((1 + monthly_rate) ** num_payments - 1)
    )

# the output
# monthly payment
print()
print(f"Monthly Payment: ${monthly_payment:.2f}")
print()

# the table headers
print(
    f"{'Month':>5} {'Payment':>10} {'Principal':>12} {'Interest':>10} {'Balance':>12}"
)

# the table rows
balance = principal
for month in range(1, num_payments + 1):
    interest = balance * monthly_rate
    principal_paid = monthly_payment - interest
    balance = balance - principal_paid

    if month == num_payments or abs(balance) < 0.005:
        balance = 0.0

    print(
        f"{month:>5} {monthly_payment:>10,.2f} {principal_paid:>12,.2f} "
        f"{interest:>10,.2f} {balance:>12,.2f}"
    )

print()
print("Done! Let's go!")
