import requests
import pandas

data = {'id': []}

for i in range(2, 65):
    req = requests.get('https://covid19.ncsc.gov.vn/api/v3/covid/province/{}'.format(i))
    data['id'].append(req.json()['id'])
    print(i, len(req.json()['death_by_day']))
    for day, count in req.json()['death_by_day'].items():
        if day not in data:
            data[day] = [None for _ in range(63)]
        data[day][i - 2] = count

df = pandas.DataFrame(data)

df.to_csv('data/death.csv', index=False)