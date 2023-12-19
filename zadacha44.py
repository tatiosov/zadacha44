import pandas as pd  # Импорт библиотеки pandas и использование псевдонима pd
import numpy as np   # Импорт библиотеки numpy и использование псевдонима np
import random        # Импорт модуля random

lst = ['robot'] * 10       # Создание списка из 10 элементов со значением 'robot'
lst += ['human'] * 10      # Добавление к списку 10 элементов со значением 'human'
random.shuffle(lst)        # Перемешивание элементов списка случайным образом
data = pd.DataFrame({'whoAmI': lst})  # Создание DataFrame из списка lst с колонкой 'whoAmI'
print(data)  # Вывод DataFrame на экран

#==================================================#

data['tmp'] = 1  # Добавление временной колонки 'tmp' со всеми значениями равными 1
data.set_index([data.index, 'whoAmI'], inplace=True)  # Установка индексов, включая существующий индекс и 'whoAmI'
data = data.unstack(level=-1, fill_value=0).astype(int)  # Преобразование DataFrame с мультииндексами, заполняя пропущенные значения 0, и преобразование к целочисленному типу данных
data.columns = data.columns.droplevel()  # Удаление уровня индекса в заголовках столбцов
data.columns.name = None  # Удаление имени колонок
print(data)  # Вывод измененного DataFrame на экран