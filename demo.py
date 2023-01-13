import threading
import time

import pandas as pd

import fakedata as fd


def gen_person(filename, num):
    # 运行时间计算
    locT = time.time()
    person_list = []
    # 在这里可以调整数据生成的总数
    for i in range(0, num):
        person_list.append(fd.new_person().split(","))

    # 数据有三列，列名分别为one,two,three
    name = ['idcard', 'name', 'gender', 'ethnic', 'province', 'city', 'area']
    test = pd.DataFrame(columns=name, data=person_list)
    test.to_csv('cvs/{}.csv'.format(filename), index=False)
    return 0


if __name__ == '__main__':
    new_thread1 = threading.Thread(target=gen_person('T1', 10000), name='T1')
    new_thread2 = threading.Thread(target=gen_person('T2', 10000), name='T2')
    new_thread3 = threading.Thread(target=gen_person('T3', 10000), name='T3')
    new_thread4 = threading.Thread(target=gen_person('T4', 10000), name='T4')
    new_thread5 = threading.Thread(target=gen_person('T5', 10000), name='T5')

    new_thread1.start()
    new_thread2.start()
    new_thread3.start()
    new_thread4.start()
    new_thread5.start()

    print("当前线程数量为", threading.active_count())
    print("所有线程的具体信息", threading.enumerate())
    print("当前线程具体信息", threading.current_thread())
