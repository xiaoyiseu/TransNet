# -*- coding: utf-8 -*-
from datetime import datetime

class VitalSigns2Digital(object):
    def Gender(self,gender):
        if gender == '男':
            state = 1
        elif gender == '女':
            state = 2
        else:
            state = 0
        return state


    def Age(self, birth):
        if birth != '空值' and birth != '':
            if "/" in birth:
                birth_d = datetime.strptime(birth, "%Y/%m/%d")
            else:
                birth_d = datetime.strptime(birth, "%Y-%m-%d").date()

            today_d = datetime.now()
            age = today_d.year - birth_d.year
            if 18 <= age <= 65:
                state = 1  # 青年
            elif 66 <= age <= 79:
                state = 2  # 中年
            elif 0 <= age <= 17:
                state = 3  # 未成年
            elif age >= 80:
                state = 4  # 老年
            else:
                state = 0
        else:
            state = 0
        return state

    def Arr_way(self, arr_way):
        if arr_way in ['步入', '扶走']:
            state = 1 #'Walk'
        elif arr_way == '轮椅':
            state = 2 #'Wheelchair'
        elif '120' in arr_way or '999' in arr_way:
            state = 3 #'Ambulance'
        else:
            state = 0
        return state

    def Temperature(self,temp):
        if temp != '空值' and temp != '':
            if 36 <= float(temp) <= 37:
                state = 1 #'normal'
            else:
                state = 2 #'unnormal'
        else:
            state = 0
        return state

    def Pulse(self, pulse):
        if pulse != '空值'and pulse != '':
            if 60 <= float(pulse) <= 100:
                state = 1 #'normal'
            else:
                state = 2 #'unnormal'
        else:
            state = 0
        return state

    def Respiration(self, resp):
        if resp != '空值' and resp != '':
            if 12 <= float(resp) <= 20:
                state = 1 #'normal'
            else:
                state = 2 #'unnormal'
        else:
            state = 0
        return state

    # def BloodPressure(self, i):
    #     if i != '' and '/' in i:
    #         f1, f2 = i.split('/')
    #         if f1.isdigit() and f2.isdigit():
    #             if 90 <= float(f1) <= 140 and 60 <= float(f2) <= 90:
    #                 state = 1  # 'normal'
    #             else:
    #                 state = 2  # 'unnormal'
    #         elif f1.isdigit() and not f2.isdigit():
    #             if 90 <= float(f1) <= 140:
    #                 state = 1  # 'normal'
    #             else:
    #                 state = 2  # 'unnormal'
    #         elif not f1.isdigit() and f2.isdigit():
    #             if 60 <= float(f2) <= 90:
    #                 state = 1  # 'normal'
    #             else:
    #                 state = 2  # 'unnormal'
    #         else:
    #             state = 0
    #     else:
    #         state = 0
    #     return state
    def BloodPressure(self, bp):
        if bp != '空值' and '/' in bp:
            h, l = bp.split('/')
            if h.isdigit() and l.isdigit():
                if 90 <= float(h) <= 140 and 60 <= float(l) < 90:
                    state = 1  # 'normal'
                elif 140 <= float(h) <= 159 or 90 <= float(l) <= 99:
                    state = 2 # '1级高血压'
                elif 160 <= float(h) <= 179 or 100 <= float(l) <= 109:
                    state = 3  # '2级高血压'
                elif 500 > float(h) >= 180 or 500 > float(l) >= 110:
                    state = 4 # '3级高血压'
                elif 0 < float(h) <= 90 or 0 < float(l) <= 60:
                    state = 5  # '低血压'
                else:
                    state = 0  # 'others'

            elif h.isdigit() and not l.isdigit():
                if 90 <= float(h) <= 140:
                    state = 1  # 'normal'
                elif 140 <= float(h) <= 159:
                    state = 2  # 'normal'
                elif 160 <= float(h) <= 179:
                    state = 3  # 'normal'
                elif float(h) >= 180:
                    state = 4 # 'normal'
                elif 0 < float(h) <= 90:
                    state = 5 # 'normal'
                else:
                    state = 0  # 'unnormal'

            elif not h.isdigit() and l.isdigit():
                if 60 <= float(l) < 90:
                    state = 1  # 'normal'

                elif 90 <= float(l) <= 99:
                    state = 2 # 'normal'
                elif 100 <= float(l) <= 109:
                    state = 3  # 'normal'
                elif float(l) >= 110:
                    state = 4  # 'normal'
                elif 0 < float(l) <= 60:
                    state = 5 # 'normal'
                else:
                    state = 0 # 'unnormal'
        else:
            state = 0  # 'unnormal'
        return state

    def SpO2(self, spo2):
        if spo2 != '空值'and spo2 != '':
            if 95 <= float(spo2) <= 100:
                state = 1 #'normal'
            else:
                state = 2 #'unnormal'
        else:
            state =0
        return state


class VitalSigns2TXT(object):
    def Gender(self, gender):
        if gender == '男':
            state = '男'
        elif gender == '女':
            state = '女'
        else:
            state = 'others'
        return state

    def Age(self, birth):
        if birth != '空值' and birth != '':
            if "/" in birth:
                birth_d = datetime.strptime(birth, "%Y/%m/%d")
            else:
                birth_d = datetime.strptime(birth, "%Y-%m-%d").date()

            today_d = datetime.now()
            age = today_d.year - birth_d.year
            if 18 <= age <= 65:
                state = '青年'  # 青年
            elif 66 <= age <= 79:
                state = '中年'  # 中年
            elif 0 <= age <= 17:
                state = '未成年'  # 未成年
            elif age >= 80:
                state = '老年'  # 老年
            else:
                state = 'others'
        else:
            state = 'others'
        return state

    def Arr_way(self, arr_way):
        if arr_way in ['步入', '扶走']:
            state = 'Walk'
        elif arr_way == '轮椅':
            state = 'Wheelchair'
        elif '120' in arr_way or '999' in arr_way:
            state = 'Ambulance'
        else:
            state = 'others'
        return state

    def Temperature(self, temp):
        if temp != '空值' and temp != '':
            if 36 <= float(temp) <= 37:
                state = '正常'  # 'normal'
            else:
                state = 'fever' #'unnormal'
        else:
            state = 'others'
        return state

    def Pulse(self, pulse):
        if pulse != '空值' and pulse != '':
            if 60 <= float(pulse) <= 100:
                state = 'normal'  # 'normal'
            else:
                state = 'unnormal'  # 'unnormal'
        else:
            state = 'others'
        return state

    def Respiration(self, resp):
        if resp != '空值' and resp != '':
            if 12 <= float(resp) <= 20:
                state = 'normal'  #'normal'
            else:
                state = 'unnormal'  #'unnormal'
        else:
            state = 'others'
        return state

    def BloodPressure(self, bp):
        if bp != '空值' and '/' in bp:
            h, l = bp.split('/')
            if h.isdigit() and l.isdigit():
                if 90 <= float(h) <= 140 and 60 <= float(l) < 90:
                    state = '正常'  # 'normal'

                elif 140 <= float(h) <= 159 or 90 <= float(l) <= 99:
                    state = '1级高血压'  # 'normal'
                elif 160 <= float(h) <= 179 or 100 <= float(l) <= 109:
                    state = '2级高血压'  # 'normal'
                elif 500 > float(h) >= 180 or 500 > float(l) >= 110:
                    state = '3级高血压'  # 'normal'
                elif 0 < float(h) <= 90 or 0 < float(l) <= 60:
                    state = '低血压'  # 'normal'
                else:
                    state = 'others'  # 'unnormal'

            elif h.isdigit() and not l.isdigit():
                if 90 <= float(h) <= 140:
                    state = '正常'  # 'normal'
                elif 140 <= float(h) <= 159:
                    state = '1级高血压'  # 'normal'
                elif 160 <= float(h) <= 179:
                    state = '2级高血压'  # 'normal'
                elif float(h) >= 180:
                    state = '3级高血压'  # 'normal'
                elif 0 < float(h) <= 90:
                    state = '低血压'  # 'normal'
                else:
                    state = 'others'  # 'unnormal'

            elif not h.isdigit() and l.isdigit():
                if 60 <= float(l) < 90:
                    state = '正常'  # 'normal'

                elif 90 <= float(l) <= 99:
                    state = '1级高血压'  # 'normal'
                elif 100 <= float(l) <= 109:
                    state = '2级高血压'  # 'normal'
                elif float(l) >= 110:
                    state = '3级高血压'  # 'normal'
                elif 0 < float(l) <= 60:
                    state = '低血压'  # 'normal'
                else:
                    state = 'others'  # 'unnormal'
        else:
            state = 'others'  # 'unnormal'
        return state

    def SpO2(self, spo2):
        if spo2 != '空值':
            if 95 <= float(spo2) <= 100:
                state = 'normal'  # 'normal'
            else:
                state = 'unnormal'  # 'unnormal'
        else:
            state = 'others'
        return state