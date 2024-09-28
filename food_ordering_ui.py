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



if __name__ == '__main__':
    #initialize the lists
    drinks = []
    appetizers = []
    salads = []
    entrees = []
    dessert= []
    #print(functions.get_item_information('D1'))
    show_main_menu()