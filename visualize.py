import pandas
from matplotlib import pyplot as plt
from data import preprocess

vaccine_df = pandas.read_csv('data/vaccine.csv', index_col=0)
vaccine_df = preprocess(vaccine_df)

covid_df = pandas.read_csv('data/covid.csv', index_col=0)
covid_df = covid_df.sum()
covid_df = preprocess(covid_df, denoise=True)

death_df = pandas.read_csv('data/death.csv', index_col=0)
death_df = death_df.sum()
death_df = preprocess(death_df)

days = []
vaccinated = []
case = []
death = []

for day in vaccine_df.columns.values:
    if day not in covid_df or day not in death_df:
        continue
    days.append(day)
    vaccinated.append(vaccine_df[day][2])
    case.append(covid_df[day])
    death.append(death_df[day])

# visualize twice injected
# plt.bar(days, vaccinated)
# plt.xticks([])
# plt.xlabel('Day')
# plt.ylabel('Twice injected')
# plt.title('Twice injected by day, from 13/9/2021 to 21/1/2022')
# plt.savefig('plot/twice_injected.pdf', format='pdf')

# visualize case and death
plt.bar(days, death, color='red')
plt.bar(days, case, color='orange', bottom=death)
plt.xticks([])
plt.xlabel('Day')
plt.ylabel('Case')
plt.title('Case and death by day, from 13/9/2021 to 21/1/2022')
colors = {'case': 'orange', 'death': 'red'}
labels = list(colors.keys())
handles = [plt.Rectangle((0, 0), 1, 1, color=colors[label]) for label in labels]
plt.legend(handles, labels)
plt.savefig('plot/case_and_death.pdf', format='pdf')
