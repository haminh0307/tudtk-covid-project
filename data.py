import pandas
from matplotlib import pyplot as plt

POPULATION = 98694816


def preprocess(df, denoise=False):
    df.fillna(0)
    if denoise:
        df[df > 10 * df.mean()] = 0
    return df


def get_data(vaccine='data/vaccine.csv', covid='data/covid.csv', death='data/death.csv', period=7):
    vaccine_df = pandas.read_csv(vaccine, index_col=0)
    vaccine_df = preprocess(vaccine_df)

    covid_df = pandas.read_csv(covid, index_col=0)
    covid_df = covid_df.sum()
    covid_df = preprocess(covid_df, denoise=True)

    death_df = pandas.read_csv(death, index_col=0)
    death_df = death_df.sum()
    death_df = preprocess(death_df)

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
        if count == period:
            if cnt_case > 0:
                X.append(vaccine_df[day][2] / POPULATION)
                Y.append(cnt_death / cnt_case)
            count = 0
            cnt_case = 0
            cnt_death = 0

    return X, Y