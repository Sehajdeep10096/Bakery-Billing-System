# Default bakery items stored in a dictionary
items = {
    1: ["Cake", 120],
    2: ["Bread", 40],
    3: ["Donut", 30],
    4: ["Cookie", 20]
}

while True:
    print("\n===== BAKERY MENU =====")
    for key in items:
        print(key, items[key][0], "- ₹", items[key][1])
    print("0. Finish & Show Bill")

    total = 0
    order_details = []

    while True:
        choice = int(input("\nEnter item number (0 to finish): "))

        if choice == 0:
            break

        if choice in items:
            qty = int(input("Enter quantity: "))
            name = items[choice][0]
            price = items[choice][1]
            cost = price * qty

            order_details.append([name, qty, cost])
            total += cost

            print("Added!\n")
        else:
            print("Invalid item number!")

    print("\n----- BILL -----")
    if len(order_details) == 0:
        print("No items purchased.")
    else:
        for x in order_details:
            print(x[0], "x", x[1], "= ₹", x[2])

    print("TOTAL BILL = ₹", total)

    again = input("\nOrder again? (y/n): ")
    if again.lower() != "y":
        print("Thank you!")
        break
