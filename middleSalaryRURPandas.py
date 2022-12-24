# import pandas as pd
#
# vacancies = pd.read_csv('C:\\Users\\elena\\PycharmProjects\\LatyntsevaElena\\CSV_files_years_new\\2022.csv')
# val_curs = pd.read_csv('C:\\Users\\elena\\PycharmProjects\\LatyntsevaElena\\currencyRate.csv')
# vacancies = vacancies.fillna(0)
# vacancies.loc[((vacancies['salary_from'].astype(float) == 0) | (vacancies['salary_to'].astype(float) == 0)), 'salary_not_rur'] = \
#     vacancies['salary_from'].astype(float) + vacancies['salary_to'].astype(float)
# vacancies.loc[((vacancies['salary_from'].astype(float) != 0) & (vacancies['salary_to'].astype(float) != 0)), 'salary_not_rur'] = \
#     (vacancies['salary_from'].astype(float) + vacancies['salary_to'].astype(float)) / 2
# vacancies.loc[vacancies['salary_currency'] == 0, 'coef'] = 0
# vacancies.loc[vacancies['salary_currency'] == 'RUR', 'coef'] = 1
# print(vacancies)

