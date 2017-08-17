# max_profit

Run python max_profit.py to see test results.

A little bit documentation:

# max_profit.py contains the main classes, 'Product' and 'Company'
[Product]
- Product is what we sell to companies. Initialize with the total amount we have.
- Three methods are implemented here: add_customer(Company),get_customer_by_name(str) and get_maximum_profits()

[Company]
- Company is the customer instance. A company comes with a name and the amount/price it offers.
- Two simple methods: set_amount(int) and set_price(int). I did this in case the company changes the offer. Well this seems unneccessary though :(

# test.py contains 4 test cases.

# dp_algorithm.py has the classic 0/1 Knapsack algorithm. I wrote this function a few month ago when i learned dynamic programming. The scenario in this problem happens to be the same, so i integrated that part.
