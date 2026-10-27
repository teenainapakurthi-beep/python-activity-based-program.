
rates = {
    "USD": 84,
    "EUR": 92,
    "GBP": 110,
    "INR": 1
}

budget = float(input("Enter travel budget in INR: Rs. "))
n = int(input("Enter number of expense categories: "))

expenses = []
total_spending = 0
largest_category = ""
largest_amount = -1

if budget < 0 or n <= 0:
    print("Invalid budget or number of categories.")

else:
    for i in range(n):
        print("\nExpense", i + 1)

        category = input("Enter category name: ")
        currency = input(
            "Enter currency (USD/EUR/GBP/INR): "
        ).upper()
        amount = float(input("Enter expense amount: "))

        if amount < 0:
            print("Invalid amount. Expense skipped.")
            continue

        if currency not in rates:
            print("Unsupported currency. Expense skipped.")
            continue

        converted = amount * rates[currency]

        if currency != "INR":
            fee = converted * 0.02
        else:
            fee = 0

        final_amount = converted + fee

        expenses.append(
            [category, currency, amount, converted, fee, final_amount]
        )

        total_spending += final_amount

        if final_amount > largest_amount:
            largest_amount = final_amount
            largest_category = category

    print("\n===== TRAVEL BUDGET REPORT =====")

    for expense in expenses:
        print("\nCategory:", expense[0])
        print("Original amount:", expense[2], expense[1])
        print("Converted amount: Rs.", round(expense[3], 2))
        print("Conversion fee: Rs.", round(expense[4], 2))
        print("Total expense: Rs.", round(expense[5], 2))

    print("\nTotal spending: Rs.", round(total_spending, 2))
    print("Travel budget: Rs.", round(budget, 2))
    print("Largest expense category:", largest_category)
    print("Largest expense: Rs.", round(largest_amount, 2))

    if total_spending > budget:
        print("Status: Budget exceeded.")
        print("Extra amount: Rs.", round(total_spending - budget, 2))
    else:
        print("Status: Within budget.")
        print("Remaining budget: Rs.", round(budget - total_spending, 2))

    print("================================")
