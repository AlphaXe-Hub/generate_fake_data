import random
import calendar
import time

import pandas as pd

import fakedata as fd

if __name__ == '__main__':
    person_list = []
    for i in range(0, 100):
        person_list.append(fd.new_person().split(","))

    # 数据有三列，列名分别为one,two,three
    name = ['id', 'name', 'gender', 'province', 'city', 'area']
    test = pd.DataFrame(columns=name, data=person_list)
    print(test)
    test.to_csv('./test.csv',index=False)
