#this module will be where most functionality will be stored
#create your def blocks for the assignment in this module
#Use this  function that will return the item name and price for a given item code
# for example, find_menu_item('D2') should return Lemonade, and integer 3 as the result
import data

def display_items():
  pass

def get_item_number():
 order_item = input("Enter dish number and quantity (e.g., D1 2): ")
 if order_item.split()[0] in data.all_items:
        return order_item
 else:
      print("Invalid item code. Please try again.")
      return get_item_number()
def get_item_information(item_code):
    # Search for the item in the menu_items_dict
    for item in data.menu_items_dict:
        if item['code'] == item_code:
            return item['name'], item['price'], item.get('stock', 'Unlimited')
    return None, None, None

