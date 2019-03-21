import requests
import json
response = requests.get("http://www.metoffice.gov.uk/pub/data/"
                        "weather/uk/climate/stationdata/heathrowdata.txt")
# file = open("Heathrow_Air_Port.txt", mode='w+')
# file.write(response.text)
# file.close()
def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]


weather_data = response.text.splitlines()
weather_data_list = []

for line in weather_data:
    weather_data_list.append(line.split())

print(weather_data_list)

# s = 0
# for line in weather_data_list[7:7+12]:
#     avg = 0
#     x = list(map(float, line[2:4]))
#     avg = sum(x)/2.0
#     s += avg

#print(round(number= s/12.0, ndigits=2))

avg = []
for month in weather_data_list[7:]:
    data = list(map(float, month[2:4]))
    avg.append(round(number=sum(data)/2.0, ndigits=2))


avg_data = list(chunks(avg, 12))
final_avg = []
for avg in avg_data:
    final_avg.append(round(number=sum(avg)/12, ndigits=2))

result = [[x, y]for x, y in zip(range(1948, 2019), final_avg)]
print('Year and Avg')
for line in result:
    print(line)



