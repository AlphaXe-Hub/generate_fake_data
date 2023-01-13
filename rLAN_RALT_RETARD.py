# Created by Mao on 2021/Jun/11
# Copyright © 2021 Reda Inc. All rights reserved.
# 着陆前收油门时刻无线电高度
# DP_PARAMS: ALTITUDE, ALT_RADIO, ENG_THR_VAL_1, ENG_THR_VAL_2, ENG_THR_VAL_3, ENG_THR_VAL_4
# DP_ROMS: pTD, pAPP_1000FT
# DP_HELPER_SCRIPTS: check_std_param_miss, check_kp_miss
def rLAN_RALT_RETARD_rom(info, result):
    # # 检查所需标准参数是否存在
    # LIST_STD_PARAM = ['ALTITUDE', 'ALT_RADIO', 'ENG_THR_VAL_1', 'ENG_THR_VAL_2']
    # flg_miss, err_miss = check_std_param_miss(LIST_STD_PARAM)
    # if flg_miss == True:
    #     result.error = err_miss
    #     return result
    #
    # # 检查所需关键点是否存在
    # LIST_KP = ['pTD', 'pAPP_1000FT']
    # flg_miss, err_miss = check_kp_miss(LIST_KP)
    # if flg_miss == True:
    #     result.error = err_miss
    #     return result

    # 以下为主体逻辑
    # 采集 接地 和 1000FT 时刻
    time_td = pTD.time
    time_1000FT = pAPP_1000FT.time

    # 找到场压高150FT时刻
    time_150FT = None
    for i in range(time_td, time_1000FT, -1):

        if ALTITUDE[i] > 300:
            result.error = '[E] Cannot find ALTITUDE 150FT between 300FT and TD.'
            return result

        if ALTITUDE[i] > 150 and ALTITUDE[i + 1] <= 150:
            time_150FT = i
            break

    if time_150FT is None:
        result.error = '[E] Cannot find ALTITUDE 150FT.'
        return result

    # 记录各台发动机各自判断的收油门时机
    # time_Retract：各台发动机各自判断的收油门无线电高度
    list_time_Retard = []

    LIST_ENG = [ENG_THR_VAL_1, ENG_THR_VAL_2, ENG_THR_VAL_3, ENG_THR_VAL_4]
    for Px in LIST_ENG:
        if Px:
            # 以150FT 时刻油门杆角度值为参考值
            val_ref = Px[time_150FT]
            # 加20是考虑有的航班在接地后才收油门
            for i in range(time_150FT, time_td + 20):
                # 收油门判断条件
                # T0秒比 val_ref 小 1
                # T1秒比 val_ref 小 2
                if Px[i] - val_ref <= -1 and Px[i + 1] - val_ref <= -2:
                    list_time_Retard.append(i)
                    break

    # 采集到的收油门time值，取最早值
    if len(list_time_Retard) == 0:
        result.error = '[E] Cannot find Retract Time on any engine.'
        return result
    else:
        time_retard = min(list_time_Retard)
        # 无线电高度小于0的情况，修正为0
        if ALT_RADIO[time_retard] >= 0:
            result.value = ALT_RADIO[time_retard]
        else:
            result.value = 0
        result.time = time_retard
        return result
