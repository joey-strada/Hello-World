# Joey Strada
# 9/13/2026
# homework 1

# Exercise 1

# The sales tax
sales_tax_rate = 0.075

# The items price
item_price = float(input("Enter the item's price: $"))

# Asking for the quantity
quantity = int(input("Enter the quantity: "))

# Calculating subtotal
subtotal = item_price * quantity
tax_amount = subtotal * sales_tax_rate
total = subtotal + tax_amount

# The receipt
print("\n--- Receipt ---")
print(f"Subtotal:  ${round(subtotal, 2):.2f}")
print(f"Tax (7.5%): ${round(tax_amount, 2):.2f}")
print(f"Total:     ${round(total, 2):.2f}")            

# ----------------------------------------------------------------

# Exercise 2

regular_hours_limit = 40
overtime_multiplier = 1.5

# Hourly wage and hours worked
hourly_wage = float(input("Enter the employee's hourly wage: $"))
hours_worked = float(input("Enter total hours worked this week: "))

# Is there overtime
if hours_worked >regular_hours_limit:
    regular_hours = regular_hours_limit
    overtime_hours = hours_worked - regular_hours_limit
else:
    regular_hours = hours_worked
    overtime_hours = 0
    
 # Calculate base pay and overtime   
base_pay = regular_hours * hourly_wage
overtime_pay = overtime_hours * hourly_wage * overtime_multiplier
total_pay = base_pay + overtime_pay

# Pay summary
print("\n--- Weekly Pay Summary ---")
print(f"Base Pay:     ${round(base_pay, 2):.2f}")
print(f"Overtime Pay: ${round(overtime_pay, 2):.2f}")
print(f"Total Pay:    ${round(total_pay, 2):.2f}")

# --------------------------------------------------------------

# Exercise 3

# Ask what their grade is
numeric_grade = float(input("Enter your numeric grade (0-100): "))

# Calculate letter grade
if numeric_grade >= 90:
        letter_grade = "A"
elif numeric_grade >= 80:
        letter_grade = "B"
elif numeric_grade >= 70:
        letter_grade = "C"
elif numeric_grade >= 60:
        letter_grade = "D"
else:
        letter_grade = "F"
        
# Number and Letter Grade      
print(f"\nNumeric Grade: {numeric_grade}")
print(f"Letter Grade:  {letter_grade}")
        
# -----------------------------------------------------------------

# Exercise 4

hours_required = 35
score_required = 85
bonus_amount = 100

# Asking for hours and performance score
hours_worked = float(input("Enter hours worked: "))
performance_score = float(input("Enter performance score: "))

# Elgibility of bonus
is_eligible = hours_worked > hours_required and performance_score > score_required

# What happens if their elgible
if is_eligible:
    print(f"\nCongratulations! You qualify for a ${bonus_amount} bonus!")
else:
    print("\nSorry, you don't qualify for the bonus yet.")
    
if hours_worked <= hours_required:
            hours_needed = ( hours_required - hours_worked) + 0.01
            print(f"You need {round(hours_needed, 2)} more hours to qualify")
            
if performance_score <= score_required:
    points_needed = (score_required - performance_score) + 0.01
    print(f"You need {round(points_needed, 2)} more points to qualify.")
    
