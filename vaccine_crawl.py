import requests
import pandas

data = dict()

index = ['total_injected_by_time', 'once_injected_by_time', 'twice_injected_by_time']

for i in range(2, 65):
    req = requests.get('https://covid19.ncsc.gov.vn/api/v3/vaccine/province/{}'.format(i))

    for idx, key in enumerate(index):
        for day, count in req.json()[key].items():
            if day not in data:
                data[day] = [0 for _ in range(3)]
            data[day][idx] += count

df = pandas.DataFrame(data)
df.to_csv('data/vaccine.csv', index=index)