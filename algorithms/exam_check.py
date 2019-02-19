students = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
match = { '1': { 'correct':0}, '2' : {'correct':0}, '3' : {'correct':0} }

match['1']['correct'] += 2

print(match['1']['correct'])
