
name = input("Enter employee name: ")
basic = float(input("Enter basic pay: Rs. "))
hours = float(input("Enter overtime hours: "))
incentive = float(input("Enter incentive: Rs. "))

if basic < 0 or hours < 0 or incentive < 0:
    print("Invalid input. Values cannot be negative.")

else:
    allowance = basic * 0.20
    overtime = hours * 200

    gross = basic + allowance + overtime + incentive

    # Calculate progressive deductions
    if gross <= 20000:
        deduction = 0
    elif gross <= 40000:
        deduction = (gross - 20000) * 0.05
    else:
        deduction = 20000 * 0.05 + (gross - 40000) * 0.10

    net_salary = gross - deduction

    print("\n========== SALARY STATEMENT ==========")
    print("Employee Name:", name)
    print("--------------------------------------")
    print("Basic Pay:       Rs.", round(basic, 2))
    print("Allowances:      Rs.", round(allowance, 2))
    print("Overtime Pay:    Rs.", round(overtime, 2))
    print("Incentive:       Rs.", round(incentive, 2))
    print("--------------------------------------")
    print("Gross Salary:    Rs.", round(gross, 2))
    print("Total Deduction: Rs.", round(deduction, 2))
    print("Net Salary:      Rs.", round(net_salary, 2))
    print("======================================")
