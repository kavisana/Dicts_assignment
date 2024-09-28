#user interface to the main menu
import data
import functions
def show_main_menu():
  while True:
    print("Keerthana Sai Avisana") #edit to show your name
    print("__________")
    print('N for a new order')
    print('X for close orders and print the check')
    print('Q for quit')
    user_menu_choice = input('Your choice: ')
    if user_menu_choice in 'Qq':
      break
    elif user_menu_choice in 'Xx':
      close_order(user_menu_choice())
    elif user_menu_choice in 'Nn':
      print('New order')
      make_order(user_menu_choice.upper())  #calls a function for adding to the orders
    else:
      print("Invalid choice. Please choose N, X, or Q.") 

def make_order(menu_choice):
  print('Functionality for menu choice ', menu_choice)
  orders=[]
  while True:
        user_selection = functions.get_item_number()  # Get item number and quantity
        item_code, quantity = user_selection.split()
        item_name, item_price = functions.get_item_information(item_code)
        
        if item_name:
            quantity = int(quantity)
            total_price = item_price * quantity
            orders.append((item_name, quantity, total_price))
            print(f"Item added: {item_name}, Quantity: {quantity}, Unit Price: ${item_price:.2f}, Total: ${total_price:.2f}")
        else:
            print("Invalid item code. Please try again.")
        
        more_items = input("Add more items? (Y/N): ").upper()
        if more_items != 'Y':
            break

  print(f"Order Summary: {orders}")
def close_order(menu_choice):
  print('Functionality for menu choice ', menu_choice)

def show_manager_menu():
    while True:
        print("Manager Menu")
        print("__________")
        print('1. Change item price')
        print('2. Change item description')
        print('3. Add a new item')
        print('4. Remove an item')
        print('Q. Return to main menu')
        manager_choice = input('Your choice: ')

        if manager_choice == '1':
            change_item_price()
        elif manager_choice == '2':
            change_item_description()
        elif manager_choice == '3':
            add_new_item()
        elif manager_choice == '4':
            remove_item()
        elif manager_choice in 'Qq':
            break
        else:
            print("Invalid choice. Please choose a valid option.")

# Function to change the price of an existing menu item
def change_item_price():
    item_code = input("Enter the item code you want to update the price for: ").upper()
    item_name, item_price = functions.get_item_information(item_code)
    
    if item_name:
        print(f"Current price of {item_name}: ${item_price:.2f}")
        new_price = float(input("Enter the new price: "))
        for item in data.menu_items_dict:
            if item['code'] == item_code:
                item['price'] = new_price
                print(f"Price for {item_name} updated to ${new_price:.2f}")
                break
    else:
        print("Invalid item code. Please try again.")

# Function to change the description/name of an existing menu item
def change_item_description():
    item_code = input("Enter the item code you want to update the description for: ").upper()
    item_name, item_price = functions.get_item_information(item_code)
    
    if item_name:
        print(f"Current description of {item_code}: {item_name}")
        new_description = input("Enter the new description: ")
        for item in data.menu_items_dict:
            if item['code'] == item_code:
                item['name'] = new_description
                print(f"Description for {item_code} updated to {new_description}")
                break
    else:
        print("Invalid item code. Please try again.")

# Function to add a new item to the menu
def add_new_item():
    new_code = input("Enter the code for the new item: ").upper()
    new_name = input("Enter the name/description of the new item: ")
    new_price = float(input("Enter the price of the new item: "))
    
    # Add the new item to the menu list
    new_item = {
        'code': new_code,
        'name': new_name,
        'price': new_price
    }

    # If it's not a drink, assign a random stock number
    if new_code not in data.drink_items:
        new_item['stock'] = random.randint(25, 50)
    
    data.menu_items_dict.append(new_item)
    print(f"New item {new_name} added to the menu.")

# Function to remove an existing item from the menu
def remove_item():
    item_code = input("Enter the item code you want to remove: ").upper()
    item_name, item_price = functions.get_item_information(item_code)
    
    if item_name:
        confirmation = input(f"Are you sure you want to remove {item_name}? (Y/N): ").upper()
        if confirmation == 'Y':
            data.menu_items_dict = [item for item in data.menu_items_dict if item['code'] != item_code]
            print(f"{item_name} has been removed from the menu.")
        else:
            print("Item not removed.")
    else:
        print("Invalid item code. Please try again.")

if __name__ == '__main__':
    show_main_menu()