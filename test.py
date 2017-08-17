from max_profit import Product,Company

def test0():
	banana = Product(1)
	banana.add_customer(Company('c1',1,1))
	assert banana.get_maximum_profits() == 1
	c1 = banana.get_customer_by_name('c1')

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

def test3():
	banana = Product(2)
	banana.add_customer(Company('c1',1,1))
	banana.add_customer(Company('c2',2,5))
	assert banana.get_maximum_profits() == 5
	c2 = banana.get_customer_by_name('c2')
	c2.set_price(15)
	print(c2.price)