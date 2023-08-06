data = [[1, 2], [3, 4], [1, 2], [5, 6], [3, 4]]
unique_data = [list(x) for x in set(tuple(x) for x in data)]

print(unique_data)