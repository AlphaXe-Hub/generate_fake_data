import random
import calendar
import time

import fakedata as fd

if __name__ == '__main__':
    person_list = []
    for i in range(0, 100):
        person_list.append(fd.new_person())
