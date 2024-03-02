'''
# Pseudo Code
1 - Create a List of items and named as menu = ["Coffee", "Pastries", "sandwich", "Cup Cakes"]
2 - Create dictionary stock with menu name as key and menu_item quantity as value.
3 - Create another dictionary price with menu_item name as key and menu_item price as value.
4 - Create a empty float variable total_stock = 0.0
5 - Run for loop on menu list - for item in menu:
6 - Get quantity = stock[item] & cost = price[item].
7 - Now apply formula total_stock = total_stock + quantity * cost
8 - Print total_stock_worth on screen.
''' 
# Menu_List
menu = ["Coffee",
        "Pastries",
        "sandwich",
        "Cup Cakes"
       ]

# Stock Dictionary.
stock = {'Coffee' : 20,
         'Pastries' : 30,
         'sandwich' : 35,
         'Cup Cakes' : 25
        }

# Price Dictionary.
price = {'Coffee' : 20.0,
         'Pastries' : 20.0,
         'sandwich' : 30.0,
         'Cup Cakes' : 30.0
        }

total_stock = 0.0

# Running for loop on menu_list.
for item in menu:
    quantity = stock[item]
    cost = price[item]
    total_stock = total_stock + quantity * cost # Calculating total worth of stock.

print('Total stock worth: £', total_stock)
 