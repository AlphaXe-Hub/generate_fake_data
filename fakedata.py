import random
import calendar


# 加载字典
def area_dict_gen():
    with open("area_fix", encoding='utf-8') as area:
        num = area.read()
    with open("area_fix2", encoding='utf-8') as area:
        name = area.read()

    num_list = num.split('\n')
    name_list = name.split('\n')

    dic = dict(zip(num_list, name_list))
    return dic


# 从id得到地区
def id_to_area(str):
    dic = area_dict_gen()
    return "{},{},{}".format([str[:-4] + '0000'], dic[str[:-2] + '00'], dic[str])


# 得到随机身份证前缀
def getAreaId():
    with open("area_fix", encoding='utf-8') as area:
        num = area.read()
    num_list = num.split('\n')
    while True:
        res = num_list[random.randint(0, len(num_list))]
        if res[4:] != '00':
            return res


# 校验系数  前置要求:身份证前缀+生日+后三位
def verify_tail(id):
    sum = 0
    verify_list = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    tail_num_index = [1, 0, "X", 9, 8, 7, 6, 5, 4, 3, 2]
    for i in range(0, 17):
        sum += verify_list[i] * int(id[i])
    return tail_num_index[sum % 11]


# 生日生成
def gen_birthday():
    birthday = ''
    year = random.randint(1940, 2023)
    month = random.randint(1, 13)
    if month == 1 and month == 3 and month == 5 and month == 7 and month == 8 and month == 10 and month == 12:
        day = random.randint(1, 31)
    elif month == 2:
        if calendar.isleap(year):
            day = random.randint(1, 29)
        else:
            day = random.randint(1, 28)
    else:
        day = random.randint(1, 30)
    birthday = "{}{:0>2d}{:0>2d}".format(year, month, day)
    return birthday


# 生日后三位
def gen_after_bir():
    i = random.randint(0, 999)
    return i


# 判断性别
def judge_gender(i):
    if i % 2 == 0:
        return "女"
    else:
        return "男"


# 生成一条人
def new_person():
    id_prefix = getAreaId()
    print("id_prefix = " + id_prefix)
    area = id_to_area(id_prefix)
    print("area = " + area)
    birthday = gen_birthday()
    print("birthday = " + birthday)
    after_bir = gen_after_bir()
    print("after_bir = {}".format(after_bir))
    gender = judge_gender(after_bir)
    id = '{}{}{}'.format(id_prefix, birthday, after_bir)
    verify_tail_num = verify_tail(id)
    print("verify_tail = {}".format(verify_tail_num))
    id += str(verify_tail_num)
    print(id)
    print(gender)
    return "{},{},{}".format(id, gender, area)
