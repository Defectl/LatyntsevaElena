import numpy as np
import pandas as pd
import sqlite3

def get_sql_table():
    """
    Переводит введный csv-файл в таблицу sqlite.
    """
    df = pd.read_csv(input('Введите нужный csv-файл: '))
    conn = sqlite3.connect('valCurs.sqlite')
    df.to_sql('valCurs', conn, if_exists='replace', index=False)

vacancies = pd.read_csv(r'C:\Users\elena\PycharmProjects\LatyntsevaElena\vacancies_dif_currencies.csv')
conn = sqlite3.connect('valCurs.db')
vacancies = vacancies.fillna(0)
vacancies.loc[
    ((vacancies['salary_from'].astype(float) == 0) | (vacancies['salary_to'].astype(float) == 0)), 'salary_not_rur'] = \
    vacancies['salary_from'].astype(float) + vacancies['salary_to'].astype(float)
vacancies.loc[
    ((vacancies['salary_from'].astype(float) != 0) & (vacancies['salary_to'].astype(float) != 0)), 'salary_not_rur'] = \
    (vacancies['salary_from'].astype(float) + vacancies['salary_to'].astype(float)) / 2
vacancies['date'] = vacancies['published_at'].str[:7]

