import random
import calendar


# 加载字典,若有字典更新,手动更新area_fix,area_fix2文件
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
    dic = area_dict_gen()     # 加载字典
    p = dic[str[:-4] + '0000']   # 获取省份
    try:
        c = dic[str[:-2] + '00']   # 获取城市
    except:
        c = p                   # 首都,直辖市,特区  特殊情况处理
    a = dic[str]              # 获取区/县
    str = "{},{},{}".format(p, c, a) # 字符串拼接
    return str


# 得到随机身份证前缀
def getAreaId():
    with open("area_fix", encoding='utf-8') as area:   # 加载区号字典
        num = area.read()
    num_list = num.split('\n')
    while True:                                       # 区号生成
        res = num_list[random.randint(0, len(num_list)-3)]
        if res[4:] != '00':                                 # 防止抽取到省号和城市号
            return res


# 校验系数  前置要求:身份证前缀+生日+后三位
# 算法 : https://zhidao.baidu.com/question/42349442.html
def verify_tail(id):
    temp_num = 0
    verify_list = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    tail_num_index = [1, 0, "X", 9, 8, 7, 6, 5, 4, 3, 2]
    for i in range(0, 17):
        temp_num += verify_list[i] * int(id[i])
    return tail_num_index[temp_num % 11]


# 生日生成
def gen_birthday():
    birthday = ''
    # 在这里修改年份范围
    year = random.randint(1940, 2023)
    month = random.randint(1, 13)
    # 31天的月份
    if month == 1 and month == 3 and month == 5 and month == 7 and month == 8 and month == 10 and month == 12:
        day = random.randint(1, 31)
    # 2月份 和 闰年判定
    elif month == 2:
        if calendar.isleap(year):
            day = random.randint(1, 29)
        else:
            day = random.randint(1, 28)
    # 30天的月份
    else:
        day = random.randint(1, 30)
    # 字符串拼接
    birthday = "{}{:0>2d}{:0>2d}".format(year, month, day)
    return birthday


# 生日后三位  无规律
def gen_after_bir():
    i = random.randint(0, 999)
    return i


# 判断性别
# 根据 生日后三位的最后一位判定男女
def judge_gender(i):
    if i % 2 == 0:
        return "女"
    else:
        return "男"


# 生成一条人  工程模式  将以上函数组合
def new_person():
    id_prefix = getAreaId()
    # 以下print均为测试探针
    # print("id_prefix = " + id_prefix)
    area = id_to_area(id_prefix)
    # print("area = " + area)
    birthday = gen_birthday()
    # print("birthday = " + birthday)
    after_bir = gen_after_bir()
    # print("after_bir = {}".format(after_bir))
    gender = judge_gender(after_bir)
    # {:0>3d}用来格式化数据 不满三位数的补零
    id = '{}{}{:0>3d}'.format(id_prefix, birthday, after_bir)
    # 加上最后以为校验码
    verify_tail_num = verify_tail(id)
    # print("verify_tail = {}".format(verify_tail_num))
    id += str(verify_tail_num)
    # print(id)
    # print(gender)
    return "{},{},{},{},{}".format(id, random_name(gender), gender, gen_ethnic(), area)


# 随机生成名字
def random_name(sex):
    # 删减部分小众姓氏
    firstName = "赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻水云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳鲍史唐费岑薛雷贺倪汤滕殷罗毕郝邬安常乐于时傅卞齐康伍余元卜顾孟平" \
                "黄和穆萧尹姚邵湛汪祁毛禹狄米贝明臧计成戴宋茅庞熊纪舒屈项祝董粱杜阮席季麻强贾路娄危江童颜郭梅盛林刁钟徐邱骆高夏蔡田胡凌霍万柯卢莫房缪干解应宗丁宣邓郁单杭洪包诸左石崔吉" \
                "龚程邢滑裴陆荣翁荀羊甄家封芮储靳邴松井富乌焦巴弓牧隗山谷车侯伊宁仇祖武符刘景詹束龙叶幸司韶黎乔苍双闻莘劳逄姬冉宰桂牛寿通边燕冀尚农温庄晏瞿茹习鱼容向古戈终居衡步都耿满弘国文东殴沃曾关红游盖益桓公晋楚闫"
    # 百家姓姓氏
    # firstName = "赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐费廉岑薛雷贺倪汤滕殷罗毕郝邬安常乐于时傅皮卞齐康伍余元卜顾孟平" \
    #             "黄和穆萧尹姚邵湛汪祁毛禹狄米贝明臧计伏成戴谈宋茅庞熊纪舒屈项祝董粱杜阮蓝闵席季麻强贾路娄危江童颜郭梅盛林刁钟徐邱骆高夏蔡田樊胡凌霍虞万支柯昝管卢莫经房裘缪干解应宗丁宣贲邓郁单杭洪包诸左石崔吉钮" \
    #             "龚程嵇邢滑裴陆荣翁荀羊於惠甄麴家封芮羿储靳汲邴糜松井段富巫乌焦巴弓牧隗山谷车侯宓蓬全郗班仰秋仲伊宫宁仇栾暴甘钭厉戎祖武符刘景詹束龙叶幸司韶郜黎蓟薄印宿白怀蒲邰从鄂索咸籍赖卓蔺屠蒙池乔阴欎胥能苍" \
    #             "双闻莘党翟谭贡劳逄姬申扶堵冉宰郦雍舄璩桑桂濮牛寿通边扈燕冀郏浦尚农温别庄晏柴瞿阎充慕连茹习宦艾鱼容向古易慎戈廖庾终暨居衡步都耿满弘匡国文寇广禄阙东殴殳沃利蔚越夔隆师巩厍聂晁勾敖融冷訾辛阚那简饶空" \
    #             "曾毋沙乜养鞠须丰巢关蒯相查後荆红游竺权逯盖益桓公晋楚闫法汝鄢涂钦归海帅缑亢况后有琴梁丘左丘商牟佘佴伯赏南宫墨哈谯笪年爱阳佟言福百家姓终"
    # 百家姓中双姓氏
    firstName2 = "万俟司马上官欧阳夏侯诸葛闻人东方赫连皇甫尉迟公羊澹台公冶宗政濮阳淳于单于太叔申屠公孙仲孙轩辕令狐钟离宇文长孙慕容鲜于闾丘司徒司空亓官司寇仉督子颛孙端木巫马公西漆雕乐正壤驷公良拓跋夹谷宰父谷梁段干百里东郭南门呼延羊舌微生梁丘左丘东门西门南宫南宫"
    # 女孩名字
    girl = '秀娟英华慧巧美娜静淑惠珠翠雅芝玉萍红娥玲芬芳燕彩春菊兰凤洁梅琳素云莲真环雪荣爱妹霞香月莺媛艳瑞凡佳嘉琼勤珍贞莉桂娣叶璧璐娅琦晶妍茜秋珊莎锦黛青倩婷姣婉娴瑾颖露瑶怡婵雁蓓纨仪荷丹蓉眉君琴蕊薇菁梦岚苑婕馨瑗琰韵融园艺咏卿聪澜纯毓悦昭冰爽琬茗羽希宁欣飘育滢馥筠柔竹霭凝晓欢霄枫芸菲寒伊亚宜可姬舒影荔枝思丽'
    # 男孩名字
    boy = '伟刚勇毅俊峰强军平保东文辉力明永健世广志义兴良海山仁波宁贵福生龙元全国胜学祥才发武新利清飞彬富顺信子杰涛昌成康星光天达安岩中茂进林有坚和彪博诚先敬震振壮会思群豪心邦承乐绍功松善厚庆磊民友裕河哲江超浩亮政谦亨奇固之轮翰朗伯宏言若鸣朋斌梁栋维启克伦翔旭鹏泽晨辰士以建家致树炎德行时泰盛雄琛钧冠策腾楠榕风航弘'
    # 名
    name = '中笑贝凯歌易仁器义礼智信友上都卡被好无九加电金马钰玉忠孝'

    # 10%的机遇生成双数姓氏
    if random.choice(range(100)) > 10:
        firstName_name = firstName[random.choice(range(len(firstName)))]
    else:
        i = random.choice(range(len(firstName2)))
        firstName_name = firstName2[i:i + 2]

    name_1 = ""
    # 生成并返回一个名字
    if sex == "女":
        girl_name = girl[random.choice(range(len(girl)))]
        if random.choice(range(2)) > 0:
            name_1 = name[random.choice(range(len(name)))]
        return firstName_name + name_1 + girl_name
    else:
        boy_name = boy[random.choice(range(len(boy)))]
        if random.choice(range(2)) > 0:
            name_1 = name[random.choice(range(len(name)))]
        return firstName_name + name_1 + boy_name


def gen_ethnic():
    mes = [
        "汉族", "壮族", "满族", "回族",
        "苗族", "维吾尔族", "彝族", "土家族",
        "蒙古族", "藏族", "布依族", "侗族",
        "瑶族", "朝鲜族", "白族", "哈尼族",
        "黎族", "哈萨克族", "傣族", "畲族",
        "傈僳族", "仡佬族", "拉祜族", "东乡族",
        "佤族", "水族", "纳西族", "羌族",
        "土族", "锡伯族", "仫佬族", "柯尔克孜族",
        "达斡尔族", "景颇族", "撒拉族", "布朗族",
        "毛南族", "塔吉克族", "普米族", "阿昌族",
        "怒族", "鄂温克族", "京族", "基诺族",
        "德昂族", "乌孜别克族", "俄罗斯族",
        "裕固族", "保安族", "门巴族", "鄂伦春族",
        "独龙族", "塔塔尔族", "赫哲族", "高山族", "珞巴族"
    ]
    i = random.randint(0, 155)
    if i > 55:
        return mes[0]
    else:
        return mes[i]

