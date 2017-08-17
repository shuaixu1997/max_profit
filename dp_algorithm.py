def Knapsack(capacity,name,weight,value):
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
