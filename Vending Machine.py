# Constructing a function to show the products that the vending machine has to offer.
def Display(items):
    print("\nWelcome to my Vending Machine")
    # Repeat for every item category.
    for category, products in items.items():
        print(f"\n{category}:\n")
        print("Code\tProduct\t\t\tPrice\tQuantity")
        # Go over each item in the category one by one.
        for code, product in products.items():
            # Showing product details: code, name, price, and quantity
            print(f"{code}\t{product['name']}\t\t${product['price']:.2f}\t{product['quantity']}")

# Establishing a function that allows you to choose an item from the vending machine.
def ItemSelectiom(items, balance):
    while True:
        # Request that the user input a product code.
        code = input("\nEnter the product code (or 'exit' to quit): ")
        if code.lower() == 'EXIT':
            return None, None
        # Verify whether the code you entered matches any product in the items dictionary.
        for category, products in items.items():
            if code in products:
                product = products[code]
                # Verify that the product you have chosen is stocked.
                if product['quantity'] == 0:
                    print("\nSorry, this product is out of stock.")
                # Verify that the user has sufficient balance to buy the item.    
                elif balance < product['price']:
                    print("\nInsufficient balance. Please insert more money.")
                # Subtract the cost from the balance if the product is available and the user has sufficient balance.
                else:
                    balance -= product['price']
                    #decrease in quantity of product
                    product['quantity'] -= 1
                    print(f"\nDispensing {product['name']}...")
                    print(f"Remaining Balance: ${balance:.2f}")
                    print(f"Remaining {product['name']} quantity: {product['quantity']}")
                    return category, code
                break
        else:
            print("\nInvalid choice. Please enter a valid product code.")

# Specifying the primary use of the vending machine.
def VendingMachine(items):
    #showing item which are available in vending machine
    Display(items)
    balance = 0 # start balance with zero
    total_spent = 0
    while True:
        if balance <= 0:
            while True:
                #request user to insert money
                money_input = input("\nInsert money (in dollars) or type 'exit' to quit: ")
                if money_input.lower() == 'exit':
                    print("Thank you for using the Vending Machine")
                    return
                if money_input.replace('.', '', 1).isdigit():
                    money = float(money_input)
                    if money > 0:
                        #adding inserted money in balance
                        balance += money
                        print(f"Current Balance: ${balance:.3f}")
                        break
                    else:
                        print("Invalid amount. Please insert a positive amount.")
                else:
                    print("Invalid input. Please enter a numeric amount.")
        #select an item form machine
        selected_category, selected_code = ItemSelectiom(items, balance)
        if selected_category and selected_code:
            #subtract the price of purchased product form balance
            total_spent += items[selected_category][selected_code]['price']
            balance -= items[selected_category][selected_code]['price']
            more_purchase = input("\nDo you want to make another purchase? (yes/no): ")
            if more_purchase == 'no':
                # Calculate the change and display the total spent amou
                change = balance if balance >= 0 else 0
                print(f"Total spent: ${total_spent:.3f}")
                print(f"Change: ${change:.3f}")
                print("Thank you for using the Vending Machine.")
                return

# displaying Samples product for the vending machine 
items = {
    'Snacks': {
        'BIS1': {'name': 'Biscuits', 'price': 1.75, 'quantity': 20},
        'CHOC2': {'name': 'Chocolate', 'price': 2.40, 'quantity': 5},
        'POP3': {'name': 'Lollipop', 'price': 1.82, 'quantity': 7}
    },
    'Drinks': {
        'DRINK1': {'name': 'Dr.Pep\t', 'price': 3.11, 'quantity': 22},
        'C2': {'name': 'Coke\t', 'price': 2.58, 'quantity': 9},
        'P3': {'name': 'Pepsi\t', 'price': 1.41, 'quantity': 33}
    }
}
#intiate the vending machine
VendingMachine(items)
