class Product():

	def __init__(self,total_amount):
		self.total_amount = total_amount
		self.all_customers = [] 

	def add_customer(self,company):
		self.all_customers.append(company)

	def get_maximum_profits(self):
		capacity = self.total_amount
		name = [x.name for x in self.all_customers]
		weight = [x.amount for x in self.all_customers]
		value = [x.price for x in self.all_customers]
		assert len(name) == len(weight) == len(value)
		# two dimentional map
		res_json = Knapsack(name,capacity,weight,value)
		print(res_json)
		return res_json['total_value']

class Company():

	def __init__(self,name,amount,price):
		self.name = name
		self.amount = amount
		self.price = price

def Knapsack(name,capacity,weight,value):
	# dp algorithm
	n = len(name)
	res = [[] for x in range(n)]
	divide = min(weight[-1], capacity)
	res[-1] = [0 for x in range(divide)]
	res[-1].extend(value[-1] for x in range(divide, capacity+1))
	for i in reversed(list(range(1,n-1))):
		divide = min(weight[i],capacity)
		for j in range(divide):
			res[i].append(res[i+1][j])
		for j in range(divide,capacity+1):
			res[i].append(max(res[i+1][j],res[i+1][j-weight[i]]+value[i]))
	res[0] = {capacity: res[1][capacity]}
	if weight[0] <= capacity:
		res[0][capacity] = max(res[1][capacity],res[1][capacity-weight[0]]+value[0])
	vector = [0 for x in range(n)]
	capacity_temp = capacity
	for i in range(n-1):
		if res[i][capacity_temp] != res[i+1][capacity_temp]:
			vector[i] = 1
			capacity_temp -= weight[i]
	vector[-1] = 0 if capacity_temp == 0 else 1
	name_vector = [name[x] for x,v in enumerate(vector) if v == 1]
	return {'total_value': res[0][capacity], 'select':name_vector}

def test1():
	banana = Product(10)
	sample_price = [1,5,8,9,10,17,17,20,24,30]
	for i in range(10):
		# generate the test sample
		banana.add_customer(Company('c'+str(i+1),i+1,sample_price[i]))
	assert banana.get_maximum_profits() == 30

def test2():
	banana = Product(10)
	sample_price = [1,5,8,9,10,17,17,20,240,30]
	for i in range(10):
		# generate the test sample
		banana.add_customer(Company('c'+str(i+1),i+1,sample_price[i]))
	assert banana.get_maximum_profits() == 241

def main():
	test1()
	test2()

if __name__ == '__main__':
	main()