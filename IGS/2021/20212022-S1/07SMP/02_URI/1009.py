name = input()
fix_salary = float(input())
product_sold = float(input())

total_salary = fix_salary + (0.15 * product_sold)

print(f"TOTAL = R$ {total_salary:.2f}")