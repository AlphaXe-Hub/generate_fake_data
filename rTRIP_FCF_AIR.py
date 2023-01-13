import numpy
import pandas


# Created by Mao on 2021/Jun/8
# Copyright © 2021 Reda Inc. All rights reserved.
# 参数积分算法，参数y 在 x 序列之上积分
# 输入：arr_x，间隔序列
# 输入：arr_y，被积分参数序列
# 输入：coff， 输入输出换算系数
# 例：地速按秒积分
#     arr_x：秒值序列，如[257, 258, 259]，单位秒
#     arr_y：GS序列，如 [149.2, 149.4, 149.5]，单位节
#     coff：0.514444，即 /3600*1852，输出单位为m
def get_integral_cal(arr_x, arr_y, coff):
    # 首先检查x和y序列长度是否一致
    if len(arr_x) != len(arr_y):
        return False

    # 以下为正式计算
    np = numpy
    rx = np.array(arr_x)
    ry = np.array(arr_y)

    val_sum = np.sum((rx[1:] - rx[:-1]) * ((ry[:-1] + ry[1:]) / 2)) * coff

    return val_sum


# Created by Mao on 2021/Jun/04
# Last Revision by Mao on 2022/Aug/03
# Copyright © 2021 Reda Inc. All rights reserved.
# 空中段耗油量（燃油流量积分）
# DP_PARAMS: FUEL_FLOW_1, FUEL_FLOW_2, FUEL_FLOW_3, FUEL_FLOW_4    1号发动机燃油流量
# DP_ROMS: pTKO, pTXI_START, rTOTAL_RATIO_FF_L2R       起飞阶段起始点（加油门起飞点）   滑入结束点   左右发燃油流量比例
# DP_HELPER_SCRIPTS: check_std_param_miss, check_kp_miss, get_integral_cal
def rTRIP_FCF_AIR_rom(info, result):
    # # 检查所需标准参数是否存在
    # LIST_PARAM = ['FUEL_FLOW_1', 'FUEL_FLOW_2']
    # flg_err, str_err = check_std_param_miss(LIST_PARAM)
    # if flg_err == True:
    #     result.error = str_err
    #     return result
    #
    # # 检查所需关键点是否存在
    # LIST_KP = ['pTKO', 'pTXI_START']
    # flg_err, str_err = check_kp_miss(LIST_KP)
    # if flg_err == True:
    #     result.error = str_err
    #     return result

    # # 数据质量检查
    # # 若左右发燃油量流量比例 <0.8 或 >1.2，认为至少1发燃油数据不可用，不进行计算
    # if rTOTAL_RATIO_FF_L2R:
    #     if rTOTAL_RATIO_FF_L2R.value < 0.8 or rTOTAL_RATIO_FF_L2R.value > 1.2:
    #         result.error = f"[E] Fuel Flow of one or both engine uncomplete. rTOTAL_RATIO_FF_L2R = {rTOTAL_RATIO_FF_L2R.value}"
    #         return result

    # 以下为主体逻辑

    return result


# 修订记录
# 2021-Jun-04 首次创建
# 2022-Aug-03 变更结束点为 pTXI_START


if __name__ == '__main__':
    # 设定起止点
    df = pandas.read_csv("cvs/FF.csv")
    FUEL_FLOW_1 = df.FF1
    FUEL_FLOW_2 = df.FF2

    # 计算油量
    LIST_FC = []
    LIST_FF = [FUEL_FLOW_1, FUEL_FLOW_2]
    for Px in LIST_FF:
        arr_FF = Px
        # 遍历每个发动机的燃油流量      通过get_integral_cal函数  时间+燃油流量  积分算得总油量
        LIST_FC.append(get_integral_cal(range(0, df.index.size), arr_FF, 1 / 3600))
    # 保留6位小数
    print(round(sum(LIST_FC), 6))
    # result.time = kp2.time


