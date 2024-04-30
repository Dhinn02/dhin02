
stock = {
    "pen": 50,
    "pencil": 50,
    "eraser": 50,
    "sharpener": 50,
    "a4": 100,
    "note": 100,
    "ruler": 50,
    "tape": 50,
    "exampad": 50
}

def displayShopItems():
    print("Available Items in Shop:")
    for item, quantity in stock.items():
        print(f"{item.capitalize()}: {quantity}")

def addProductToReceipt(receipt, product_name, quantity):
    if product_name in stock:
        if quantity > stock[product_name]:
            print(f"Insufficient quantity for {product_name.capitalize()}. Available stock: {stock[product_name]}")
        else:
            receipt.append((product_name, quantity))
            stock[product_name] -= quantity
            print(f"{quantity} {product_name.capitalize()} added to receipt.")
    else:
        print(f"{product_name.capitalize()} is not available in the shop.")

def generateReceipt(customerName, receipt):
    print("====================================")
    print("Supermarket Receipt")
    print("Customer Name:", customerName)
    print("====================================")
    print("Products Purchased:")
    total_cost = 0
    for product_name, quantity in receipt:
        cost = quantity  # Assuming each item costs 1 unit for simplicity
        print(f"{product_name.capitalize()}: {quantity} x {cost} = {quantity * cost}")
        total_cost += quantity * cost
    print("------------------------------------")
    print("Total Cost: Rs.", total_cost)
    print("====================================")

def main():
    while True:
        customerName = input("Enter customer name (or 'exit' to exit): ")

        if customerName.lower() == 'exit':
            print("Exiting...")
            break

        receipt = []
        print(f"\nWelcome {customerName} to the Shop!")
        displayShopItems()

        while True:
            print("\nOptions:")
            print("1. Add Product to Receipt")
            print("2. Generate Receipt")
            print("3. Finish and Serve Next Customer")
            choice = input("Enter your choice: ")

            if choice == '1':
                product_name = input("Enter product name: ").lower()
                if product_name in stock:
                    quantity = int(input(f"Enter quantity (Available: {stock[product_name]}): "))
                    addProductToReceipt(receipt, product_name, quantity)
                else:
                    print("Invalid product name. Please try again.")

            elif choice == '2':
                generateReceipt(customerName, receipt)

            elif choice == '3':
                print(f"Finishing transaction for {customerName}...")
                break

            else:
                print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()
