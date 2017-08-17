from dp_algorithm import Knapsack
import test

class Product():

	def __init__(self,total_amount):
		self.total_amount = total_amount
		self.all_customers = [] 

	def add_customer(self,company):
		self.all_customers.append(company)

	def get_customer_by_name(self,name):
		for i in self.all_customers:
			if i.name == name:
				print ('Customer Found: ',i.__dict__)
				return i
		print('No Customer Found')
		return None

	def get_maximum_profits(self):
		if len(self.all_customers)<1:
			print('No Customer')
			return 0

		capacity = self.total_amount
		name = [x.name for x in self.all_customers]
		weight = [x.amount for x in self.all_customers]
		value = [x.price for x in self.all_customers]
		assert len(name) == len(weight) == len(value)

		if len(self.all_customers)==1:
			print('Only One Customer: ',self.all_customers[0].__dict__)
			return value[0] if weight[0]<=capacity else 0	

		res_json = Knapsack(capacity,name,weight,value)
		print(res_json)
		return res_json['total_value']

class Company():

	def __init__(self,name,amount,price):
		self.name = name
		self.amount = amount
		self.price = price

	def set_amount(self,amount):
		self.amount = amount

	def set_price(self,price):
		self.price = price

def main():
	test.test0()
	test.test1()
	test.test2()
	test.test3()

if __name__ == '__main__':
	main()