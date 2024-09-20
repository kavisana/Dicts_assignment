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
      print('This option prints the list of items ordered, extended price, total, Taxes, and Grand total ')
    elif user_menu_choice in 'Nn':
      print('New order')
      make_order(user_menu_choice.upper())  #calls a function for adding to the orders
    else:
      print("Invalid choice. Please choose N, X, or Q.") 

def make_order(menu_choice):
  print('Functionality for menu choice ', menu_choice)
  user_selection = functions.get_item_number()
  item_code, quantity = user_selection.split()
  print(functions.get_item_information(item_code))
  item_name, item_price = functions.get_item_information(item_code)
  if item_name:
            print(f"Item added: {item_name}, Quantity: {quantity}, Unit Price: ${item_price}")
            # Store the item and quantity (implement how you want to store orders)
            # Example: orders.append((item_name, int(quantity), item_price * int(quantity)))
  else:
      print("Invalid item code. Please try again.")
  more_items = input("Add more items? (Y/N): ").upper()


def close_order(menu_choice):
  print('Functionality for menu choice ', menu_choice)



if __name__ == '__main__':
    #initialize the lists
    drinks = []
    appetizers = []
    salads = []
    entrees = []
    dessert= []
    #print(functions.get_item_information('D1'))
    show_main_menu()