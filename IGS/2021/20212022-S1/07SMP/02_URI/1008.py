employee_number = int(input())
worked_hours = int(input())
salary_per_hour = float(input())

total_salary = worked_hours * salary_per_hour

print(f"NUMBER = {employee_number}")
print(f"SALARY = U$ {total_salary:.2f}")