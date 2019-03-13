class BankAccount:

	def __init__(self,balance=0.00):
		self.balance = balance


	def deposit(self, amount):
		""" make a deposit"""
		new_balance = self.balance + amount
		print(new_balance)


	def withdraw(self,amount):
		""" make a withdraw"""
		if amount > self.balance:
			raise ValueError("insufficient funds")
		self.balance -=amount



account1 = BankAccount()
account1.deposit(20000)
account1.withdraw(6000)



				