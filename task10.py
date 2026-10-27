
venue = float(input("Enter venue cost: Rs. "))
equipment = float(input("Enter equipment cost: Rs. "))
transport = float(input("Enter transport cost: Rs. "))

catering = float(input("Enter catering cost per participant: Rs. "))
certificate = float(input("Enter certificate cost per participant: Rs. "))

participants = int(input("Enter expected participants: "))
registration_fee = float(input("Enter registration fee per participant: Rs. "))
sponsorship = float(input("Enter sponsorship amount: Rs. "))

if (venue < 0 or equipment < 0 or transport < 0
        or catering < 0 or certificate < 0
        or participants < 0 or registration_fee < 0
        or sponsorship < 0):
    print("Invalid input. Values cannot be negative.")

else:
    fixed_cost = venue + equipment + transport
    variable_cost = catering + certificate

    total_variable_cost = variable_cost * participants
    total_expenses = fixed_cost + total_variable_cost

    registration_income = registration_fee * participants
    total_revenue = registration_income + sponsorship

    balance = total_revenue - total_expenses

    # Calculate funding shortfall
    if balance < 0:
        shortfall = -balance
        print("\nFunding shortfall: Rs.", round(shortfall, 2))
    else:
        shortfall = 0
        print("\nNo funding shortfall.")

    # Calculate break-even registrations
    contribution = registration_fee - variable_cost

    if fixed_cost <= sponsorship:
        break_even = 0
    elif contribution <= 0:
        break_even = -1
    else:
        remaining_fixed_cost = fixed_cost - sponsorship
        break_even = int(
            (remaining_fixed_cost + contribution - 0.01)
            // contribution
        )

    print("\n===== CAMPUS EVENT FINANCIAL REPORT =====")
    print("Venue cost: Rs.", round(venue, 2))
    print("Equipment cost: Rs.", round(equipment, 2))
    print("Transport cost: Rs.", round(transport, 2))
    print("Fixed costs: Rs.", round(fixed_cost, 2))
    print("Variable cost per participant: Rs.", round(variable_cost, 2))
    print("Total expenses: Rs.", round(total_expenses, 2))
    print("Registration income: Rs.", round(registration_income, 2))
    print("Sponsorship: Rs.", round(sponsorship, 2))
    print("Total revenue: Rs.", round(total_revenue, 2))

    if balance > 0:
        print("Surplus: Rs.", round(balance, 2))
    elif balance < 0:
        print("Deficit: Rs.", round(-balance, 2))
    else:
        print("The event breaks even.")

    if break_even == -1:
        print("Break-even is not possible with this registration fee.")
    else:
        print("Minimum registrations to break even:", break_even)

    print("=========================================")
