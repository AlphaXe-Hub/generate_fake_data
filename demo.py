import pandas as pd

import fakedata as fd

if __name__ == '__main__':
    person_list = []
    # 在这里可以调整数据生成的总数
    for i in range(0, 10000):
        person_list.append(fd.new_person().split(","))

    # 数据有三列，列名分别为one,two,three
    name = ['id', 'name', 'gender', 'province', 'city', 'area']
    test = pd.DataFrame(columns=name, data=person_list)
    print(test)
    test.to_csv('cvs/A3.csv',index=False)
