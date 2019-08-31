import os
import matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numpy import linspace, hstack
from scipy.stats.kde import gaussian_kde

os.chdir("/home/user/PycharmProjects/Analysis_by _Python/")


# sep - задает символ разделмитель полей в файле (по умолчанию разделитель)
# names - список названий колонок
# index_col - номер калонки с индексом
# decimal - символ разделитель для знаков после запятой
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 1000)
file = pd.read_csv('test_sale1.csv', sep=',', index_col=0, delimiter=',')
print(file)
print('Кол-во строк, столбцов: ', file.shape)
print("Длина данного файла: ", len(file))
print("Типы данного файла: ", file.dtypes)

# Метод describe показывает основные статистические характеристики
# данных по каждому числовому признаку (типы int64 и float64):
# число непропущенных значений, среднее, стандартное отклонение, диапазон, медиану, 0.25 и 0.75 квартили.
describe_file = file.describe(include='all')
print('Describe file: ', describe_file)

# Построение гистограммы
matplotlib.style.use('bmh')
print("Стили гистограмм:\n", plt.style.available)
histogram_file = file["Общая стоимость"].hist(bins=60)
# print(histogram_file)
plt.show()

my_density = gaussian_kde(file['Общая стоимость'], bw_method=0.1)
x = linspace(min(file['Общая стоимость']), (max(file['Общая стоимость'])), 1000000)
new_hist = file['Общая стоимость'].hist(alpha=.3)
new_hist.plot(x, my_density(x), 'r')
plt.show()

file.groupby("Район")["Общая стоимость"].plot.hist(alpha=0.6)
plt.legend()