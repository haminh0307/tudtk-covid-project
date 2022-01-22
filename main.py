import pandas
from matplotlib import pyplot as plt

POPULATION = 98694816
PERIOD = 3

vaccine_df = pandas.read_csv('vaccine.csv', index_col=0)

covid_df = pandas.read_csv('covid.csv', index_col=0)
covid_df.replace(-1, 0)
covid_df = covid_df.sum()

death_df = pandas.read_csv('death.csv', index_col=0)
death_df.replace(-1, 0)
death_df = death_df.sum()

X = []
Y = []

count = 0
cnt_death = 0
cnt_case = 0

for day in vaccine_df.columns.values:
    if day not in covid_df or day not in death_df:
        continue
    cnt_death += death_df[day]
    cnt_case += covid_df[day]
    count += 1
    if count == PERIOD:
        if cnt_case > 0:
            X.append(vaccine_df[day][2] / POPULATION)
            Y.append(cnt_death / cnt_case)
        count = 0
        cnt_case = 0
        cnt_death = 0

plt.scatter(X, Y)
plt.show()

