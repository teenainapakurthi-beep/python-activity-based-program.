
distance = float(input("Enter journey distance in km: "))
n = int(input("Enter number of passengers: "))

if distance <= 0 or n <= 0:
    print("Invalid distance or passenger count.")

else:
    print("\nTravel Classes:")
    print("1. Sleeper")
    print("2. AC 3 Tier")
    print("3. AC 2 Tier")

    choice = int(input("Select travel class (1-3): "))

    if choice == 1:
        class_name = "Sleeper"
        multiplier = 1.0
    elif choice == 2:
        class_name = "AC 3 Tier"
        multiplier = 1.5
    elif choice == 3:
        class_name = "AC 2 Tier"
        multiplier = 2.0
    else:
        class_name = ""
        multiplier = 0

    if multiplier == 0:
        print("Invalid travel class.")

    else:
        # Calculate fare using distance slabs
        if distance <= 100:
            base_fare = distance * 1
        elif distance <= 300:
            base_fare = 100 + (distance - 100) * 1.5
        else:
            base_fare = 100 + 200 * 1.5 + (distance - 300) * 2

        class_fare = base_fare * multiplier
        reservation_fee = 40

        for i in range(n):
            print("\nPassenger", i + 1)
            age = int(input("Enter passenger age: "))

            if age < 0:
                print("Invalid age.")
                continue

            fare = class_fare

            if age < 5:
                fare = 0
            elif age >= 60:
                fare = fare * 0.80

            total_fare = fare + reservation_fee

            print("Travel class:", class_name)
            print("Journey distance:", distance, "km")
            print("Fare after concession: Rs.", round(fare, 2))
            print("Reservation fee: Rs.", reservation_fee)
            print("Total ticket fare: Rs.", round(total_fare, 2))

            cancelled = input("Cancel ticket? (yes/no): ").lower()

            if cancelled == "yes":
                penalty = total_fare * 0.25
                refund = total_fare - penalty

                print("Cancellation penalty: Rs.",
                      round(penalty, 2))
                print("Refund amount: Rs.", round(refund, 2))
            else:
                print("Ticket confirmed.")
