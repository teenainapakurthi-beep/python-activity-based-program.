
name = input("Enter patient name: ")
age = int(input("Enter patient age: "))

consultation = 500
diagnostic = 1000
treatment = float(input("Enter treatment charge: "))

if age < 0 or treatment < 0:
    print("Invalid input. Age and charges cannot be negative.")

else:
    subtotal = consultation + diagnostic + treatment
    concession = 0

    # Senior citizen concession
    if age >= 60:
        concession = subtotal * 0.10

    amount_after_concession = subtotal - concession

    # Additional concession for bills of Rs. 10000 or more
    if subtotal >= 10000:
        concession = concession + amount_after_concession * 0.05

    final_bill = subtotal - concession

    print("\n--- Hospital Bill ---")
    print("Patient name:", name)
    print("Consultation charge: Rs.", consultation)
    print("Diagnostic charge: Rs.", diagnostic)
    print("Treatment charge: Rs.", treatment)
    print("Subtotal: Rs.", round(subtotal, 2))
    print("Total concession: Rs.", round(concession, 2))
    print("Final bill: Rs.", round(final_bill, 2))

    paid = float(input("Enter amount paid: Rs. "))

    if paid < 0 or paid > final_bill:
        print("Invalid payment amount.")

    else:
        balance = final_bill - paid

        if paid == final_bill:
            status = "Paid"
        elif paid > 0:
            status = "Partially Paid"
        else:
            status = "Unpaid"

        print("Amount paid: Rs.", round(paid, 2))
        print("Balance due: Rs.", round(balance, 2))
        print("Payment status:", status)
