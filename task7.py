
products = []
n = int(input("Enter number of products: "))

if n <= 0:
    print("Invalid number of products.")

else:
    subtotal = 0

    for i in range(n):
        print("\nProduct", i + 1)

        name = input("Enter product name: ")
        category = input(
            "Enter category (Food/Clothing/Electronics): "
        ).lower()
        price = float(input("Enter price: Rs. "))
        quantity = int(input("Enter quantity: "))

        if price < 0 or quantity <= 0:
            print("Invalid price or quantity.")
            continue

        if category == "food":
            tax_rate = 5
        elif category == "clothing":
            tax_rate = 12
        elif category == "electronics":
            tax_rate = 18
        else:
            print("Invalid category. Product skipped.")
            continue

        amount = price * quantity
        subtotal = subtotal + amount

        products.append(
            [name, category, price, quantity, amount, tax_rate]
        )

    if subtotal == 0:
        print("No valid products entered.")

    else:
        # Calculate overall discount
        if subtotal >= 5000:
            discount_rate = 15
        elif subtotal >= 2000:
            discount_rate = 10
        else:
            discount_rate = 0

        discount = subtotal * discount_rate / 100

        if discount > 1000:
            discount = 1000

        total_tax = 0
        final_total = 0

        print("\n========== ITEMIZED INVOICE ==========")
        print("Subtotal: Rs.", round(subtotal, 2))
        print("Discount: Rs.", round(discount, 2))
        print("--------------------------------------")

        for product in products:
            name = product[0]
            category = product[1]
            quantity = product[3]
            amount = product[4]
            tax_rate = product[5]

            # Allocate discount proportionally
            item_discount = discount * amount / subtotal
            discounted_amount = amount - item_discount

            tax = discounted_amount * tax_rate / 100
            item_total = discounted_amount + tax

            total_tax = total_tax + tax
            final_total = final_total + item_total

            print("\nProduct:", name)
            print("Category:", category)
            print("Quantity:", quantity)
            print("Amount: Rs.", round(amount, 2))
            print("Discount: Rs.", round(item_discount, 2))
            print("Tax:", tax_rate, "%")
            print("Tax amount: Rs.", round(tax, 2))
            print("Item total: Rs.", round(item_total, 2))

        print("\n--------------------------------------")
        print("Subtotal: Rs.", round(subtotal, 2))
        print("Total discount: Rs.", round(discount, 2))
        print("Total tax: Rs.", round(total_tax, 2))
        print("Final amount: Rs.", round(final_total, 2))
        print("======================================")
