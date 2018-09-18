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
