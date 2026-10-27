
plans = [
    ["Plan A", 199, 2, 200, 28],
    ["Plan B", 299, 5, 500, 28],
    ["Plan C", 399, 10, 1000, 56]
]

data_needed = float(input("Enter required data in GB: "))
calls_needed = int(input("Enter required calling minutes: "))
days_needed = int(input("Enter required validity in days: "))
budget = float(input("Enter your budget: Rs. "))

best_plan = ""
lowest_cost = float("inf")

print("\n--- Mobile Plan Comparison ---")

for plan in plans:
    name = plan[0]
    price = plan[1]
    data = plan[2]
    calls = plan[3]
    validity = plan[4]

    extra_data = 0
    extra_calls = 0

    if data_needed > data:
        extra_data = (data_needed - data) * 20

    if calls_needed > calls:
        extra_calls = (calls_needed - calls) * 0.50

    total_cost = price + extra_data + extra_calls

    print("\nPlan:", name)
    print("Base price: Rs.", price)
    print("Excess data charge: Rs.", round(extra_data, 2))
    print("Excess call charge: Rs.", round(extra_calls, 2))
    print("Total cost: Rs.", round(total_cost, 2))

    if validity >= days_needed and total_cost <= budget:
        if total_cost < lowest_cost:
            lowest_cost = total_cost
            best_plan = name

print("\n--- Best Plan ---")

if best_plan != "":
    print("Recommended plan:", best_plan)
    print("Total cost: Rs.", round(lowest_cost, 2))
else:
    print("No plan satisfies all your requirements.")
