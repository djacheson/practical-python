#pcost.py
#
#Exercise 1.27
import sys

def portfolio_cost(filename):
	total_cost = 0
	with open(filename, 'rt') as f:
		headers = next(f)
		for row in f:
			row = row.split(',')
			shares = int(row[1])
			cost = float(row[-1].strip())
			total_cost += shares * cost
	return total_cost

if len(sys.argv) == 2:
	filename = sys.argv[1]
else:
	filename = 'Data/portfolio.csv'
total_cost = portfolio_cost(filename)
print(f'Total cost {total_cost:0.2f}')
