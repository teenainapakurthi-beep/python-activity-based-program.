
months = ["January", "February", "March", "April"]
consumption = []
bills = []

for month in months:
    units = float(input("Enter units for " + month + ": "))
    consumption.append(units)

    # Calculate energy charges
    if units <= 100:
        energy = units * 2
    elif units <= 200:
        energy = 100 * 2 + (units - 100) * 3
    elif units <= 300:
        energy = 100 * 2 + 100 * 3 + (units - 200) * 5
    else:
        energy = 100 * 2 + 100 * 3 + 100 * 5 + (units - 300) * 7

    fixed_charge = 50
    surcharge = energy * 0.05
    rebate = 0

    if units < 100:
        rebate = energy * 0.10

    total = energy + fixed_charge + surcharge - rebate
    bills.append(total)

print("\n--- Electricity Bill Report ---")

for i in range(len(months)):
    print("\nMonth:", months[i])
    print("Units consumed:", consumption[i])
    print("Total bill: Rs.", round(bills[i], 2))

    if i > 0:
        increase = consumption[i] - consumption[i - 1]

        if consumption[i - 1] > 0:
            percentage = increase / consumption[i - 1] * 100

            if percentage > 30:
                print("Warning: Unusual consumption increase!")
                print("Increase:", round(percentage, 2), "%")
            else:
                print("No unusual increase detected.")
        elif consumption[i] > 0:
            print("Warning: Consumption increased from zero units.")
