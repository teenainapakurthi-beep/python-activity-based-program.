
material_qty = float(input("Enter material quantity: "))
material_rate = float(input("Enter material cost per unit: Rs. "))

wastage_percent = float(input("Enter wastage percentage: "))

workers = int(input("Enter number of workers: "))
hours = float(input("Enter working hours per worker: "))
wage = float(input("Enter hourly wage per worker: Rs. "))

machine_hours = float(input("Enter machine operating hours: "))
machine_rate = float(input("Enter machine cost per hour: Rs. "))

production_qty = float(input("Enter quantity produced: "))
selling_price = float(input("Enter selling price per unit: Rs. "))
target = float(input("Enter target profit percentage: "))

if (material_qty < 0 or material_rate < 0
        or wastage_percent < 0 or wastage_percent > 100
        or workers < 0 or hours < 0 or wage < 0
        or machine_hours < 0 or machine_rate < 0
        or production_qty <= 0 or selling_price < 0
        or target < 0):
    print("Invalid input. Check the entered values.")

else:
    material_cost = material_qty * material_rate
    wastage_cost = material_cost * wastage_percent / 100

    labour_cost = workers * hours * wage
    machine_cost = machine_hours * machine_rate

    total_cost = (
        material_cost + wastage_cost
        + labour_cost + machine_cost
    )

    revenue = production_qty * selling_price
    profit = revenue - total_cost

    if total_cost > 0:
        profit_percent = profit / total_cost * 100
    else:
        profit_percent = 0

    print("\n===== MANUFACTURING REPORT =====")
    print("Material cost: Rs.", round(material_cost, 2))
    print("Wastage cost: Rs.", round(wastage_cost, 2))
    print("Labour cost: Rs.", round(labour_cost, 2))
    print("Machine cost: Rs.", round(machine_cost, 2))
    print("Total production cost: Rs.", round(total_cost, 2))
    print("Total revenue: Rs.", round(revenue, 2))
    print("Profit/Loss: Rs.", round(profit, 2))
    print("Profit percentage:", round(profit_percent, 2), "%")

    if profit_percent >= target:
        print("Result: Target profit achieved.")
    else:
        print("Result: Target profit not achieved.")

    print("================================")
