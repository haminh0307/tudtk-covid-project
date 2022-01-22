import pandas
import numpy as np

POPULATION = 98694816 # Vietnam population


def preprocess(df, denoise=False):
    """
    Preprocess dataframe
    :param df: dataframe
    :param denoise: if True, replace outlier by zero
    :return: new dataframe
    """
    df.fillna(0)
    if denoise:
        df[df > 3 * df.mean()] = np.nan
        df = df.fillna(method='ffill')
    return df


def get_data(vaccine='data/vaccine.csv', case='data/case.csv', death='data/death.csv', period=7):
    """
    Get data from vaccine, case and death dataframe
    :param vaccine: path to vaccine csv
    :param case: path to case csv
    :param death: path to death csv
    :param period: number of days per sample
    :return: sample X, Y
    """
    vaccine_df = pandas.read_csv(vaccine, index_col=0)
    vaccine_df = preprocess(vaccine_df)

    case_df = pandas.read_csv(case, index_col=0)
    case_df = case_df.loc[:, '13/9/2021':]
    case_df = case_df.sum() # sum case by day
    case_df = preprocess(case_df, denoise=True) # case dataframe has noise

    death_df = pandas.read_csv(death, index_col=0)
    death_df = death_df.loc[:, '13/9/2021':]
    death_df = death_df.sum() # sum death by day
    death_df = preprocess(death_df)

    X = []
    Y = []

    count = 0
    vaccinated = 0
    cnt_death = 0
    cnt_case = 0

    for day in vaccine_df.columns.values:
        if day not in case_df or day not in death_df:
            continue
        # number of twice injected in first day of period
        if count == 0:
            vaccinated = vaccine_df[day][2]
        # cummulative case and death
        cnt_case += case_df[day]
        cnt_death += death_df[day]
        count += 1
        # new sample
        if count == period:
            if cnt_case > 0:
                X.append(vaccinated / POPULATION)
                Y.append(cnt_death / cnt_case)
            count = 0
            cnt_case = 0
            cnt_death = 0

    return X, Y