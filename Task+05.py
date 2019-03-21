file = open('temp_data_pipes_00a.csv', mode='r')
result = []

for line in file:
    result.append(line.strip().split())
print(result)
print(result[0][0])
