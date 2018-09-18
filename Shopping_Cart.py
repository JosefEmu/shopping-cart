"""
#####################################################################################
############################# Test Objectives #######################################
#####################################################################################

Create a class called ShoppingCart.

Create a constructor that takes no arguments and sets the total attribute to zero, 
and initializes an empty dict attribute named items.

Create a method add_item that requires item_name, quantity and price arguments.
This method should add the cost of the added items to the current value of total.
It should also add an entry to the items dict such that the key is the item_name and 
the value is the quantity of the item.

Create a method remove_item that requires similar arguments as add_item. It should
remove items that have been added to the shopping cart and are not required. 
This method should deduct the cost of the removed items from the current total
and also update the items dict accordingly.

If the quantity of an item to be removed exceeds the current quantity of that 
item in the cart, assume that all entries of that item are to be removed.

Create a method checkout that takes in cash_paid and returns the value of balance 
from the payment. If cash_paid is not enough to cover the total, 
return "Cash paid not enough".

Create a class called Shop that has a constructor which takes no arguments and 
initializes an attribute called quantity at 100. 
Make sure Shop inherits from ShoppingCart.

In the Shop class, override the remove_item method, 
such that calling Shop's remove_item with no arguments decrements quantity by one.

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

core functions
-add items (cost of each/ quantity) [done]
-calculate total [done]
-calculate tax

extras:
-present receipt in a friendly form
-make more human friendly to read/use

"""
class ShoppingCart:
	"""Basic shopping cart app- that adds items to cart, calculates total and tracks stock"""
	def __init__(self):
		self.items= {} #reciept with item names and quantity
		self.total= 0 #initial total variable

	def add_item(self, item_name, quantity, price):
		#add cost of added items to total
		if item_name in self.items:
			self.items[item_name] += quantity
		else:
			self.items[item_name]= quantity

		self.total += (price * quantity)
		print(self.total, self.items)


	def remove_item(self, item_name, quantity, price):
		#removes cost of removed items from total
		if quantity <= self.items.get(item_name):
			self.items[item_name] -= quantity
			if self.items.get(item_name) == 0:
				self.items.pop(item_name)
			self.total -= (price * quantity)
			print(self.total, self.items)
		else:
			print("\nQuantity entered exceeds quantity in cart.\nRe-enter correct quantity to continue\n")
	def checkout(self, cash_paid):
		if cash_paid> self.total:
			print("Your change is ", cash_paid- self.total)
		else:
			print("\nCash paid is not enough. \nAdd ",self.total- cash_paid, "shillings to continue\n")


class Shop(ShoppingCart):
	"""Inherits from ShoppingCart class."""
	def __init__(self):
		super(Shop, self).__init__()
		self.quantity = 100

	def remove_item(self):
		self.quantity -= 1

#random tests		
cust1 = ShoppingCart()
cust1.add_item("Bread", 1, 50)
cust1.add_item("Bread", 1, 50)
cust1.add_item("Bread", 1, 50)
cust1.add_item("Peanut Butter", 2, 120)
cust1.remove_item("Bread", 3, 50)
cust1.checkout(100)

today= Shop()
print(today.quantity)
today.remove_item()
today.remove_item()
today.remove_item()
today.remove_item()
print(today.quantity)