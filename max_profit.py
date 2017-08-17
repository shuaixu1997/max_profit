class Product():

	def __init__(self,total_amount):
		self.total_amount = total_amount
		self.all_customers = [] 

	def add_customer(self,company):
		self.all_customers.append(company)

	def get_maximum_profits(self):
		capacity = self.total_amount-1
		name = [x.name for x in self.all_customers]
		weight = [x.amount for x in self.all_customers]
		value = [x.price for x in self.all_customers]
		assert len(name) == len(weight) == len(value)
		# two dimentional map
		result = Knapsack(capacity,name,weight,value)

class Company():

	def __init__(self,name,amount,price):
		self.name = name
		self.amount = amount
		self.price = price

def Knapsack(name,capacity,weight,value):
	# dp algorithm
	# print(name,capacity,weight,value)

	pass

def test1():
	banana = Product(10)
	sample_price = [1,5,8,9,10,17,17,20,24,30]
	for i in range(10):
		# generate the test sample
		banana.add_customer(Company('c'+str(i+1),i+1,sample_price[i]))
	banana.get_maximum_profits()

def main():
	test1()

if __name__ == '__main__':
	main()