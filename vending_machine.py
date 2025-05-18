items = {
    "1": {"name": "Cola", "catagory": "Drink", "price": 1.50, "stock": 3},
    "2": {"name": "Pepsi", "catagory": "Drink", "price": 1.50, "stock":2},
    "3": {"name": "Water", "catagory": "Drink", "price": 1.00, "stock": 3},
    "4": {"name": "Americano", "catagory": "Hot Drinks", "price": 2.5, "stock":2},
    "5": {"name": "Chips", "catagory": "Snack", "price": 1.20, "stock": 2},
    "6": {"name": "Snickers", "catagory": "Snack", "price": 1.30, "stock": 1}
}

def show_menu():
    print("===== VENDING MACHINE MENU =====")
    for code in items:
        item = items[code]
        print(code + ": " + item["name"] + " (" + item["catagory"] + ") - $" + str(item["price"]) + ("[OUT OF STOCK]" if item["stock"] == 0 else ""))

def get_selection():
    code = input("Enter item number: ").upper()
    if code in items:
        if items[code]["stock"] > 0:
            return code
        else:
            print("That item out of stock")
            return get_selection()
    else:
        print("Invalid number. Try again")
        return get_selection()
    
def take_payment(cost):
    print("Please insert $" + str(cost))
    inserted = 0.0
    while inserted < cost:
        try:
            money = float(input("Insert amount: "))
            inserted = inserted + money
        except:
            print("Invalid input")
    change = inserted - cost
    return change

def dispense_item(code):
    item = items[code]
    print("You chose: ", item["name"])
    change = take_payment(item["price"])
    items[code]["stock"] -= 1
    print("Dispensing: ", item["name"])
    print("Your change is: $" + str(round(change, 2)))
    print("Thank you")

def main():
    while True:
        show_menu()
        selected = get_selection()
        dispense_item(selected)
        again = input("Would you like to buy another item? (Y/N): ").lower()

        if again != "y":
            print("Thank you for using the vending machine!")
            break

main()