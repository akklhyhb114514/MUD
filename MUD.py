'''
此为新版爽文修真
只适合在window上运行
'''
# v1.0.6正式版
# 更新版本时别忘了改更新日期和版本说明!!!
# 子文件列表(运行前请检查):
# |python.exe(解释器,必须要!!!(3.8版本以上!!!))
# |MUD.py(本体)
# |hunshou.py(战斗模块)
# |save.py(初始数据)
# |MUD_SAVE.json(数据)
# |SWXZ.py(开发中文件)
# |爽文修真.py(测试文件)
# |存档(存档文件夹)
# |TabMake.py(列表及表格管理模块)
# |Go.py(五子棋模块)
# |100619552281_00063.ico(封面图片)
# |__pycache__(加载模块模块)
# |os.py(访问系统模块(python.exe自带))
# |time.py(管理时间模块(python.exe自带))
# |json.py(加载数据及存档模块(python.exe自带))
# |re.py(管理列表模块(python.exe自带))
# |random.py(随机模块(python.exe自带))
# 打包:pyinstaller --icon=icon.ico -F MUD.py


import json
import os
import random
import re
from tkinter import messagebox as mbox

from Go import *
from Save import *
from TabMake import *


def Debug(a, mod=None):
    global colormod
    global Debugmod
    global dum
    Debugmod = a
    if a == True:
        if mod == 'color':
            colormod = False
        elif mod == 'name':
            dum.name = 'Debuger'
        elif mod == 'xb':
            dum.xb = '2'
        elif mod == 'dr':
            dum.dr = 'Debug'
        else:
            colormod = False
            dum.name = 'Debuger'
            dum.xb = '2'
            dum.dr = 'Debug'
        print('[Debug ON]')
    elif a == False:
        colormod = True
        print('[Debug OFF]')


def clean_up():
    # DOS/Windows
    os.system('CLS')


def check_system():
    if os.name not in ("nt", "dos", "ce"):
        # Fallback for other operating systems.
        mbox.showerror('error', '不兼容此系统!')
        exit()


class MUD():
    # __init__
    def __init__(self):
        listall = dir(Save)
        listall = listall[26:-1]
        for i in listall:
            try:
                exec('self.' + str(i) + ' = Save.' + str(i))
            except:
                pass

    # time
    def time_now(self):
        a = self.timeh
        b = self.timemin
        if a < 10:
            a = '0' + str(a)
        if b < 10:
            b = '0' + str(b)
        return str(self.timey) + '年 ' + str(self.timem) + '月 ' + str(self.timed) + '日 ' + str(a) + '时 ' + str(
            b) + '分'

    def new_time(self, date=0, mouth=0, year=0, hour=0, min=0):
        self.timemin = self.timemin + min
        if self.timemin >= 61:
            self.timemin = self.timemin + 1
        self.timeh = self.timeh + self.timemin // 61 + hour
        self.timemin = self.timemin % 61
        if self.timeh >= 25:
            self.timeh = self.timeh + 1
        self.timed = self.timed + self.timeh // 25 + date
        self.timeh = self.timeh % 25
        if self.timed >= 31:
            self.timed = self.timed + 1
        self.timem = self.timem + self.timed // 31 + mouth
        self.timed = self.timed % 31
        if self.timem >= 13:
            self.timem = self.timem + 1
        self.timey = self.timey + self.timem // 13 + year
        self.timem = self.timem % 13

    # all
    def import_save():
        listall = dir(Save)
        listall = listall[26:-1]
        for i in listall:
            a = 'self.' + str(i) + ' = Save.' + str(i)
            print(a)

    def tab_pd(str1, qs=-4, tn=24):
        str1 = str(str1)
        tn = tn + qs
        a = len(str1)
        if MUD.is_Chinese(str1) == True:
            n = MUD.number_of_Chinese(str1)
            a = n + len(str1) + (qs + 8) - 3
        b = tn - a - 1
        b = max(b, 0)
        return ' ' * b + '\t'

    def colorful_word(a='', b='', c='', d='', e='', f='', g='', h='', i='', j='', k='', l='', m='', n='', sep=' '):
        global colormod
        name = str(a) + sep + str(b) + sep + str(c) + sep + str(d) + sep + str(e) + sep + str(f) + sep + str(
            g) + sep + str(h) + sep + str(i) + sep + str(j) + sep + str(k) + sep + str(l) + sep + str(m) + sep + str(n)
        color = ''
        gh = ''
        if colormod == True:
            if '★★★★★★★' in name:
                color = '\033[5;31m'
                gh = '\033[0m'
            elif '★★★★★' in name:
                color = '\033[1;33m'
                gh = '\033[0m'
            elif '★★★★' in name:
                color = '\033[1;35m'
                gh = '\033[0m'
            elif '★★★' in name:
                color = '\033[1;34m'
                gh = '\033[0m'
            elif '★★' in name:
                color = '\033[1;32m'
                gh = '\033[0m'
            elif '★' in name:
                color = '\033[1;40m'
                gh = '\033[0m'
        print(color + name + gh)

    def save_save(self):
        global cv
        if self.sm < self.cmsx or self.living == True:
            list1 = []
            listall = MUD.listdeef(dir(dum), dir(MUD))
            for i in listall:
                list1 = list1 + [eval('dum.' + str(i))]
            with open(cv + '\\' + str(self.save_name) + '.json', 'w') as f:
                json.dump([listall, list1], f)

    def jqzsint(number):
        number = str(number)
        nu = len(number)
        if nu <= 5:
            return str(number)
        elif nu <= 8:
            str1 = number[0:(nu - 4)]
            str1 = str1 + '.' + number[(nu - 4):(nu - 2)] + '万'
        else:
            str1 = number[0:(nu - 8)]
            str1 = str1 + '.' + number[(nu - 8):(nu - 6)] + '亿'
        return str1

    def jqzsset(self):
        if self.jq != '---':
            self.jq = int(round(self.jq, 0))
            self.jqshow = MUD.jqzsint(self.jq)
        if self.zs != '---':
            self.zs = int(round(self.zs, 0))
            self.zsshow = MUD.jqzsint(self.zs)
        if self.plgx != '---':
            self.plgx = int(round(self.plgx))
            self.plgxshow = MUD.jqzsint(self.plgx)

    def wgmgset(self):
        self.xl = int(round(self.xl, 0))
        self.wg = int(round(self.wg, 0))
        self.gj_mg = int(round(self.gj_mg, 0))
        self.wf = int(round(self.wf, 0))
        self.mf = int(round(self.mf, 0))
        self.jsl = int(round(self.jsl, 0))
        self.wgshow = MUD.jqzsint(int(round(self.wg * self.wgxs * self.sxxs, 0)))
        self.jg_mgshow = MUD.jqzsint(int(round(self.gj_mg * self.gj_mgxs * self.sxxs, 0)))
        self.wfshow = MUD.jqzsint(int(round(self.wf * self.wfxs * self.sxxs, 0)))
        self.mfshow = MUD.jqzsint(int(round(self.mf * self.mfxs * self.sxxs, 0)))
        self.xlshow = MUD.jqzsint(int(round(self.xl * self.xlxs * self.sxxs, 0)))
        self.real_xlshow = MUD.jqzsint(int(round(self.real_xl * self.xlxs * self.sxxs, 0)))
        self.jslshow = MUD.jqzsint(self.jsl)
        self.zlsx()
        self.zhzlshow = MUD.jqzsint(self.zhzl)
        self.xpshow = MUD.jqzsint(self.xp)
        self.levelshow = MUD.jqzsint(self.level)
        self.levelsxshow = MUD.jqzsint(self.levelsx)
        self.soul_coreshow = MUD.jqzsint(self.soul_core)
        self.soul_coresxshow = MUD.jqzsint(self.soul_coresx)

    def jysxset(self):
        self.jy = int(round(self.jy, 0))
        self.sx = int(round(self.sx, 0))
        self.jyshow = MUD.jqzsint(self.jy)
        self.sxshow = MUD.jqzsint(self.sx)

    def damage(self, damage_):
        self.real_xl -= damage_ / self.xlsx / self.sxxs
        if self.real_xl <= 0:
            self.living = False
            self.smpd()
        else:
            self.real_xlshow = MUD.jqzsint(int(round(self.real_xl * self.xlxs * self.sxxs, 0)))

    def color(self):
        global colormod
        if colormod == True:
            os.system(self.yc)

    def check_level(self):
        self.level = int(round((self.xp ** (1 / 3)), 0)) + 1
        self.levelsx = int(round((self.level + 1) ** (3), 0))

    def check_core(self):
        self.soul_core = min(self.soul_core, 6561)
        self.soul_core_dess = int(round((self.soul_core ** (1 / 4)), 0))
        self.soul_coresx = int(round((self.soul_core_dess + 10) ** (3), 0))
        self.soul_coresx = min(self.soul_coresx, 6561)
        if self.soul_core_dess == 0:
            self.soul_core_des = '无'
        elif self.soul_core_dess == 1:
            self.soul_core_dess = '一阶'
        elif self.soul_core_dess == 2:
            self.soul_core_des = '二阶'
        elif self.soul_core_dess == 3:
            self.soul_core_des = '三阶'
        elif self.soul_core_dess == 4:
            self.soul_core_des = '四阶'
        elif self.soul_core_dess == 5:
            self.soul_core_des = '五阶'
        elif self.soul_core_dess == 6:
            self.soul_core_des = '六阶'
        elif self.soul_core_dess == 7:
            self.soul_core_des = '七阶'
        elif self.soul_core_dess == 8:
            self.soul_core_des = '八阶'
        elif self.soul_core_dess == 9:
            self.soul_core_des = '九阶'

    def djpd(self, a=True):
        if self.jy >= 99 ** 3 and self.jsl < 50000:
            self.jsl = self.jsl + int(round((self.jy - 98 ** 3 + 1) / 100, 0))
            self.jy = 98 ** 3 - 1
        self.dj = int(round((self.jy ** (1 / 3)), 0)) + 1
        self.sx = int(round((self.dj + 1) ** (3), 0))
        self.zhzl = self.zhzl + self.dj * 10
        while self.dj >= self.djjs:
            self.sxxs = self.sxxs + ((self.djjs ** 2) / 10000)
            self.djjs = self.djjs + 1
        if 1 <= self.dj < 10 and self.jys <= 0:
            self.djxr = '魂士'
            self.jys = 1
            self.xlxs = self.xlxs + 0.05
            self.wgxs = self.wgxs + 0.03
            self.wfxs = self.wfxs + 0.02
            self.gj_mgxs = self.gj_mgxs + 0.01
            self.mfxs = self.mfxs + 0
            self.cmsx = self.cmsx + 5
            self.famous += random.randint(1, 2)
        if 10 <= self.dj and self.jys <= 1:
            self.djxr = '魂师'
            self.jys = 2
            self.xlxs = self.xlxs + 0.3
            self.wgxs = self.wgxs + 0.2
            self.wfxs = self.wfxs + 0.1
            self.gj_mgxs = self.gj_mgxs + 0.05
            self.mfxs = self.mfxs + 0.02
            self.cmsx = self.cmsx + 5
            self.famous += random.randint(1, 2)
        if 20 <= self.dj and self.jys <= 2:
            self.djxr = '大魂师'
            self.jys = 3
            self.xlxs = self.xlxs + 0.5
            self.wgxs = self.wgxs + 0.4
            self.wfxs = self.wfxs + 0.3
            self.gj_mgxs = self.gj_mgxs + 0.1
            self.mfxs = self.mfxs + 0.08
            self.cmsx = self.cmsx + 5
            self.famous += random.randint(2, 3)
        if 30 <= self.dj and self.jys <= 3:
            self.djxr = '魂尊'
            self.jys = 4
            self.xlxs = self.xlxs + 0.7
            self.wgxs = self.wgxs + 0.6
            self.wfxs = self.wfxs + 0.5
            self.gj_mgxs = self.gj_mgxs + 0.12
            self.mfxs = self.mfxs + 0.1
            self.cmsx = self.cmsx + 10
            self.famous += random.randint(2, 3)
        if 40 <= self.dj and self.jys <= 4:
            self.djxr = '魂宗'
            self.jys = 5
            self.xlxs = self.xlxs + 0.9
            self.wgxs = self.wgxs + 0.8
            self.wfxs = self.wfxs + 0.7
            self.gj_mgxs = self.gj_mgxs + 0.24
            self.mfxs = self.mfxs + 0.1
            self.cmsx = self.cmsx + 10
            self.famous += random.randint(3, 4)
        if 50 <= self.dj and self.jys <= 5:
            self.djxr = '魂王'
            self.jys = 6
            self.xlxs = self.xlxs + 1.1
            self.wgxs = self.wgxs + 1.0
            self.wfxs = self.wfxs + 0.9
            self.gj_mgxs = self.gj_mgxs + 0.4
            self.mfxs = self.mfxs + 0.3
            self.cmsx = self.cmsx + 10
            self.famous += random.randint(3, 4)
        if 60 <= self.dj and self.jys <= 6:
            self.djxr = '魂帝'
            self.jys = 7
            self.xlxs = self.xlxs + 1.3
            self.wgxs = self.wgxs + 1.2
            self.wfxs = self.wfxs + 1.1
            self.gj_mgxs = self.gj_mgxs + 0.9
            self.mfxs = self.mfxs + 0.8
            self.cmsx = self.cmsx + 10
            self.famous += random.randint(4, 5)
        if 70 <= self.dj and self.jys <= 7:
            self.djxr = '魂圣'
            self.jys = 8
            self.xlxs = self.xlxs + 1.0
            self.wgxs = self.wgxs + 0.9
            self.wfxs = self.wfxs + 0.8
            self.gj_mgxs = self.gj_mgxs + 1.2
            self.mfxs = self.mfxs + 1.0
            self.cmsx = self.cmsx + 15
            self.famous += random.randint(4, 5)
        if 80 <= self.dj and self.jys <= 8:
            self.djxr = '魂斗罗'
            self.jys = 9
            self.xlxs = self.xlxs + 1.2
            self.wgxs = self.wgxs + 1.1
            self.wfxs = self.wfxs + 1.0
            self.gj_mgxs = self.gj_mgxs + 1.5
            self.mfxs = self.mfxs + 1.2
            self.cmsx = self.cmsx + 15
            self.famous += random.randint(5, 6)
        if 90 <= self.dj and self.jys <= 9:
            if self.dr != 'Debug':
                if a == True:
                    print('恭喜突破"封号斗罗"!')
                    dr = input('请取封号(sj随机):')
                    if dr == 'sj':
                        self.dr = MUD.random_fh()
                else:
                    self.dr = MUD.random_fh()
            self.djxr = self.dr + '斗罗'
            self.dlfh = '(' + self.djxr + ')'
            self.jys = 10
            self.xlxs = self.xlxs + 1.5
            self.wgxs = self.wgxs + 1.4
            self.wfxs = self.wfxs + 1.3
            self.gj_mgxs = self.gj_mgxs + 1.5
            self.mfxs = self.mfxs + 1.2
            self.cmsx = self.cmsx + 15
            self.famous += random.randint(6, 7)
        if 100 <= self.dj and self.jys <= 10:
            print('即将突破并遭受天劫...')
            input('任意键继续...')
            self.szsx = min(self.szsx, 10)
            ra = random.randint(self.szsx, 10)
            print('一道天雷从天而降...')
            import time
            time.sleep(1)
            if ra == self.szsx:
                print('渡劫成功!')
                self.jys = 11
                self.djxr = '神祗' + self.dlfh
                self.xlxs = self.xlxs + 2
                self.wgxs = self.wgxs + 1.9
                self.wfxs = self.wfxs + 1.8
                self.gj_mgxs = self.gj_mgxs + 2
                self.mfxs = self.mfxs + 1.8
                self.cmsx = self.cmsx + 100
                self.szsx = 1
                self.famous += random.randint(7, 8)
            else:
                print('渡劫失败!')
                self.szsx = self.szsx + 1
                self.jy = 98 ** 3
                self.djpd()
            input()
        if 110 <= self.dj and self.jys <= 11:
            self.djxr = '大神祗' + self.dlfh
            self.jys = 12
            self.xlxs = self.xlxs + 1
            self.wgxs = self.wgxs + 1
            self.wfxs = self.wfxs + 1
            self.gj_mgxs = self.gj_mgxs + 1
            self.mfxs = self.mfxs + 1
            self.cmsx = self.cmsx + 100
            self.famous += random.randint(7, 8)
        if 120 <= self.dj and self.jys <= 12:
            self.djxr = '神尊' + self.dlfh
            self.jys = 13
            self.xlxs = self.xlxs + 2
            self.wgxs = self.wgxs + 2
            self.wfxs = self.wfxs + 2
            self.gj_mgxs = self.gj_mgxs + 2
            self.mfxs = self.mfxs + 2
            self.cmsx = self.cmsx + 100
            self.famous += random.randint(8, 9)
        if 130 <= self.dj and self.jys <= 13:
            self.djxr = '神宗' + self.dlfh
            self.jys = 14
            self.xlxs = self.xlxs + 2
            self.wgxs = self.wgxs + 2
            self.wfxs = self.wfxs + 2
            self.gj_mgxs = self.gj_mgxs + 2
            self.mfxs = self.mfxs + 2
            self.cmsx = self.cmsx + 100
            self.famous += random.randint(8, 9)
        if 140 <= self.dj and self.jys <= 14:
            self.djxr = '神王' + self.dlfh
            self.jys = 15
            self.xlxs = self.xlxs + 2
            self.wgxs = self.wgxs + 2
            self.wfxs = self.wfxs + 2
            self.gj_mgxs = self.gj_mgxs + 2
            self.mfxs = self.mfxs + 2
            self.cmsx = self.cmsx + 100
            self.famous += random.randint(9, 10)
        if 150 <= self.dj and self.jys <= 15:
            self.djxr = '神帝' + self.dlfh
            self.jys = 16
            self.xlxs = self.xlxs + 2.5
            self.wgxs = self.wgxs + 2.5
            self.wfxs = self.wfxs + 2.5
            self.gj_mgxs = self.gj_mgxs + 2.5
            self.mfxs = self.mfxs + 2.5
            self.cmsx = self.cmsx + 500
            self.famous += random.randint(9, 10)
        if 160 <= self.dj and self.jys <= 16:
            self.djxr = '神圣' + self.dlfh
            self.jys = 17
            self.xlxs = self.xlxs + 3
            self.wgxs = self.wgxs + 3
            self.wfxs = self.wfxs + 3
            self.gj_mgxs = self.gj_mgxs + 3
            self.mfxs = self.mfxs + 3
            self.cmsx = self.cmsx + 800
            self.famous += random.randint(10, 11)
        if 170 <= self.dj and self.jys <= 17:
            self.djxr = '神斗罗' + self.dlfh
            self.jys = 18
            self.xlxs = self.xlxs + 3.5
            self.wgxs = self.wgxs + 3.5
            self.wfxs = self.wfxs + 3.5
            self.gj_mgxs = self.gj_mgxs + 3.5
            self.mfxs = self.mfxs + 3.5
            self.cmsx = self.cmsx + 1200
            self.famous += random.randint(10, 11)
        if 180 <= self.dj and self.jys <= 18:
            print('恭喜突破"封号之神"!')
            self.sm = input('请取封号(sj随机):')
            if self.sm == 'sj':
                self.sm = self.random_fh()
            self.djxr = self.sm + '之神' + self.dlfh
            self.jys = 19
            self.xlxs = self.xlxs + 4
            self.wgxs = self.wgxs + 4
            self.wfxs = self.wfxs + 4
            self.gj_mgxs = self.gj_mgxs + 4
            self.mfxs = self.mfxs + 4
            self.cmsx = self.cmsx + 1500
            self.famous += random.randint(11, 12)

        if self.jsl >= 500000000:
            self.jsl = 500000000

        if 50 > self.jsl >= 1 and self.jys2 <= 0:
            self.jslxr = '灵元境'
            self.jslsx = '50'
            self.jys2 = 1
            self.famous += random.randint(1, 2)
        if 500 > self.jsl >= 50 and self.jys2 <= 1:
            self.jslxr = '灵海境'
            self.jslsx = '500'
            self.jys2 = 2
            self.famous += random.randint(1, 2)
        if 5000 > self.jsl >= 500 and self.jys2 <= 2:
            self.jslxr = '灵渊境'
            self.jslsx = '5000'
            self.jys2 = 3
            self.famous += random.randint(2, 3)
        if 50000 > self.jsl >= 5000 and self.jys2 <= 3:
            self.jslxr = '灵域境'
            self.jslsx = '50000'
            self.jys2 = 4
            self.famous += random.randint(2, 3)
        if 500000 > self.jsl >= 50000 and self.jys2 <= 4:
            self.jslxr = '神元境'
            self.jslsx = '50万'
            self.jys2 = 5
            self.famous += random.randint(3, 4)
        if 5000000 > self.jsl >= 500000 and self.jys2 <= 5:
            self.jslxr = '神海境'
            self.jslsx = '500万'
            self.jys2 = 6
            self.famous += random.randint(3, 4)
        if 50000000 > self.jsl >= 5000000 and self.jys2 <= 6:
            self.jslxr = '神渊境'
            self.jslsx = '5000万'
            self.jys2 = 7
            self.famous += random.randint(4, 5)
        if self.jsl >= 50000000 and self.jys2 <= 7:
            self.jslxr = '神域境'
            self.jslsx = '5亿'
            self.jys2 = 8
            self.famous += random.randint(5, 6)

        self.famous = min(self.famous, 100)

        if self.famous <= 10:
            self.famousxr = '无名鼠辈'
        elif self.famous <= 20:
            self.famousxr = '鲜为人知'
        elif self.famous <= 30:
            self.famousxr = '默默无闻'
        elif self.famous <= 40:
            self.famousxr = '小有名气'
        elif self.famous <= 50:
            self.famousxr = '大名鼎鼎'
        elif self.famous <= 60:
            self.famousxr = '名噪一时'
        elif self.famous <= 70:
            self.famousxr = '声名远扬'
        elif self.famous <= 80:
            self.famousxr = '名扬中外'
        elif self.famous <= 90:
            self.famousxr = '人尽皆知'
        elif self.famous <= 100:
            self.famousxr = '名垂青史'

        if self.xb == '114514':
            self.sxxs = 114514

    def zlsx(self):
        self.zhzl = int(round((
                                      self.xl * self.xlxs + self.wg * self.wgxs + self.gj_mg * self.gj_mgxs + self.wf * self.wfxs + self.mf * self.mfxs) * (
                                      self.yz * 0.8) * self.sxxs + self.jsl + self.soul_core, 0))

    # random
    def random_name():
        d1g = random.randint(0, 40)
        d2g = random.randint(0, 43)
        d3g = random.randint(0, 32)
        nms = random.randint(1, 6)
        if d1g == 1:
            d1g = '张'
        elif d1g == 2:
            d1g = '李'
        elif d1g == 3:
            d1g = '王'
        elif d1g == 4:
            d1g = '周'
        elif d1g == 5:
            d1g = '蔡'
        elif d1g == 6:
            d1g = '蓝'
        elif d1g == 7:
            d1g = '唐'
        elif d1g == 8:
            d1g = '吴'
        elif d1g == 9:
            d1g = '沈'
        elif d1g == 10:
            d1g = '司马'
        elif d1g == 11:
            d1g = '诸葛'
        elif d1g == 12:
            d1g = '上官'
        elif d1g == 13:
            d1g = '麻'
        elif d1g == 14:
            d1g = '马'
        elif d1g == 15:
            d1g = '陈'
        elif d1g == 16:
            d1g = '何'
        elif d1g == 17:
            d1g = '孙'
        elif d1g == 18:
            d1g = '郑'
        elif d1g == 19:
            d1g = '小'
        elif d1g == 20:
            d1g = '丁'
        elif d1g == 21:
            d1g = '徐'
        elif d1g == 22:
            d1g = '余'
        elif d1g == 23:
            d1g = '俞'
        elif d1g == 24:
            d1g = '赵'
        elif d1g == 25:
            d1g = '刘'
        elif d1g == 26:
            d1g = '习'
        elif d1g == 27:
            d1g = '毛'
        elif d1g == 28:
            d1g = '邓'
        elif d1g == 29:
            d1g = '柳'
        elif d1g == 30:
            d1g = '章'
        elif d1g == 31:
            d1g = '江'
        elif d1g == 32:
            d1g = '史'
        elif d1g == 33:
            d1g = '罗'
        elif d1g == 34:
            d1g = '钱'
        elif d1g == 35:
            d1g = '阮'
        elif d1g == 36:
            d1g = '慕容'
        else:
            d1g = '*'
        if d2g == 1:
            d2g = '三'
        elif d2g == 2:
            d2g = '四'
        elif d2g == 3:
            d2g = '亿'
        elif d2g == 4:
            d2g = '泰'
        elif d2g == 5:
            d2g = '卓'
        elif d2g == 6:
            d2g = '成'
        elif d2g == 7:
            d2g = '诚'
        elif d2g == 8:
            d2g = '开'
        elif d2g == 9:
            d2g = '鑫'
        elif d2g == 10:
            d2g = '亮'
        elif d2g == 11:
            d2g = '迁'
        elif d2g == 12:
            d2g = '光'
        elif d2g == 13:
            d2g = '聪'
        elif d2g == 14:
            d2g = '丽'
        elif d2g == 15:
            d2g = '晨'
        elif d2g == 16:
            d2g = '曦'
        elif d2g == 17:
            d2g = '建'
        elif d2g == 18:
            d2g = '坚'
        elif d2g == 19:
            d2g = '好'
        elif d2g == 20:
            d2g = '婉'
        elif d2g == 21:
            d2g = '发'
        elif d2g == 22:
            d2g = '屌'
        elif d2g == 23:
            d2g = '保'
        elif d2g == 24:
            d2g = '明'
        elif d2g == 25:
            d2g = '吱'
        elif d2g == 26:
            d2g = '晓'
        elif d2g == 27:
            d2g = '志'
        elif d2g == 28:
            d2g = '凤'
        elif d2g == 29:
            d2g = '红'
        elif d2g == 30:
            d2g = '强'
        elif d2g == 31:
            d2g = '佳'
        elif d2g == 32:
            d2g = '如'
        elif d2g == 33:
            d2g = '帅'
        elif d2g == 34:
            d2g = '五'
        elif d2g == 35:
            d2g = '六'
        elif d2g == 36:
            d2g = '七'
        elif d2g == 37:
            d2g = '八'
        elif d2g == 38:
            d2g = '九'
        elif d2g == 39:
            d2g = '近'
        elif d2g == 40:
            d2g = '郑'
        elif d2g == 41:
            d2g = '珍'
        elif d2g == 42:
            d2g = '冬'
        else:
            d2g = '*'
        if d3g == 1:
            d3g = '明'
        elif d3g == 2:
            d3g = '国'
        elif d3g == 3:
            d3g = '飞'
        elif d3g == 4:
            d3g = '人'
        elif d3g == 5:
            d3g = '阳'
        elif d3g == 6:
            d3g = '刚'
        elif d3g == 7:
            d3g = '悦'
        elif d3g == 8:
            d3g = '宇'
        elif d3g == 9:
            d3g = '儿'
        elif d3g == 10:
            d3g = '丝'
        elif d3g == 11:
            d3g = '浩'
        elif d3g == 12:
            d3g = '然'
        elif d3g == 13:
            d3g = '强'
        elif d3g == 14:
            d3g = '杰'
        elif d3g == 15:
            d3g = '钰'
        elif d3g == 16:
            d3g = '正'
        elif d3g == 17:
            d3g = '气'
        elif d3g == 18:
            d3g = '轩'
        elif d3g == 19:
            d3g = '涌'
        elif d3g == 20:
            d3g = '俪'
        elif d3g == 21:
            d3g = '丽'
        elif d3g == 22:
            d3g = '娟'
        elif d3g == 23:
            d3g = '宣'
        elif d3g == 24:
            d3g = '成'
        elif d3g == 25:
            d3g = '妮'
        elif d3g == 26:
            d3g = '军'
        elif d3g == 27:
            d3g = '冬'
        elif d3g == 28:
            d3g = '蛋'
        elif d3g == 29:
            d3g = '平'
        elif d3g == 30:
            d3g = '香'
        elif d3g == 31:
            d3g = '梅'
        else:
            d3g = '*'
        if 1 <= nms <= 3:
            nm = d1g + d2g
        elif 3 < nms <= 6:
            nm = d1g + d2g + d3g
        return nm

    def random_yz(xb):
        yz = random.randint(1, 12)
        if xb == '1':
            xb = '男'
            if yz <= 3:
                yzxr = '丑男'
            elif 3 < yz <= 5:
                yzxr = '一般'
            elif 5 < yz <= 8:
                yzxr = '英俊'
            elif 8 < yz <= 10:
                yzxr = '帅哥'
            elif 10 < yz <= 12:
                yzxr = '绝世'
            else:
                yzxr = '...'
        elif xb == '2':
            xb = '女'
            if yz <= 3:
                yzxr = '丑女'
            elif 3 < yz <= 5:
                yzxr = '一般'
            elif 5 < yz <= 7:
                yzxr = '漂亮'
            elif 7 < yz <= 10:
                yzxr = '美女'
            elif yz == 11:
                yzxr = '沉鱼落雁'
            elif yz == 12:
                yzxr = '倾国倾城'
            else:
                yzxr = '...'
        elif xb == '114514':
            xb = '114514'
            yzxr = 'homo'
            yz = -1
        else:
            print('居然是—不男不女!')
            xb = '不男不女!'
            yzxr = '人妖'
        return yz, yzxr, xb

    def yzpd(self, yz, xb):
        xb = str(xb)
        if self.xb == '1':
            self.xb = '男'
            if self.yz <= 3:
                self.yzxr = '丑男'
            elif 3 < self.yz <= 5:
                self.yzxr = '一般'
            elif 5 < self.yz <= 8:
                self.yzxr = '英俊'
            elif 8 < self.yz <= 10:
                self.yzxr = '帅哥'
            elif 10 < self.yz <= 12:
                self.yzxr = '绝世'
            else:
                self.yzxr = '...'
        elif self.xb == '2':
            self.xb = '女'
            if self.yz <= 3:
                self.yzxr = '丑女'
            elif 3 < self.yz <= 5:
                self.yzxr = '一般'
            elif 5 < self.yz <= 7:
                self.yzxr = '漂亮'
            elif 7 < self.yz <= 10:
                self.yzxr = '美女'
            elif self.yz == 11:
                self.yzxr = '沉鱼落雁'
            elif self.yz == 12:
                self.yzxr = '倾国倾城'
            else:
                self.yzxr = '...'
        else:
            self.xb = '不男不女!'
            self.yzxr = '人妖'

    def random_fh():
        d1g = random.randint(0, 25)
        d2g = random.randint(0, 30)
        if d1g == 1:
            d1g = '张'
        elif d1g == 2:
            d1g = '李'
        elif d1g == 3:
            d1g = '王'
        elif d1g == 4:
            d1g = '周'
        elif d1g == 5:
            d1g = '蔡'
        elif d1g == 6:
            d1g = '蓝'
        elif d1g == 7:
            d1g = '唐'
        elif d1g == 8:
            d1g = '吴'
        elif d1g == 9:
            d1g = '沈'
        elif d1g == 10:
            d1g = '司马'
        elif d1g == 11:
            d1g = '诸葛'
        elif d1g == 12:
            d1g = '上官'
        elif d1g == 13:
            d1g = '麻'
        elif d1g == 14:
            d1g = '马'
        elif d1g == 15:
            d1g = '陈'
        elif d1g == 16:
            d1g = '何'
        elif d1g == 17:
            d1g = '孙'
        elif d1g == 18:
            d1g = '郑'
        elif d1g == 19:
            d1g = '小'
        else:
            d1g = '*'
        if d2g == 1:
            d2g = '三'
        elif d2g == 2:
            d2g = '四'
        elif d2g == 3:
            d2g = '亿'
        elif d2g == 4:
            d2g = '泰'
        elif d2g == 5:
            d2g = '卓'
        elif d2g == 6:
            d2g = '成'
        elif d2g == 7:
            d2g = '诚'
        elif d2g == 8:
            d2g = '开'
        elif d2g == 9:
            d2g = '鑫'
        elif d2g == 10:
            d2g = '亮'
        elif d2g == 11:
            d2g = '迁'
        elif d2g == 12:
            d2g = '光'
        elif d2g == 13:
            d2g = '聪'
        elif d2g == 14:
            d2g = '丽'
        elif d2g == 15:
            d2g = '晨'
        elif d2g == 16:
            d2g = '曦'
        elif d2g == 17:
            d2g = '建'
        elif d2g == 18:
            d2g = '坚'
        elif d2g == 19:
            d2g = '好'
        elif d2g == 20:
            d2g = '婉'
        elif d2g == 21:
            d2g = '发'
        elif d2g == 22:
            d2g = '屌'
        elif d2g == 23:
            d2g = '保'
        elif d2g == 24:
            d2g = '明'
        elif d2g == 25:
            d2g = '吱'
        else:
            d2g = '*'
        nm = d1g + d2g
        return nm

    # zm
    def choosezm(self):
        a = True
        while a == True:
            print('选择宗门：')
            print('青龙宗(1) | 华山派(2) | 玄灵宗(3) | 昊天宗(4) |')
            print('唐门(5)   | 海神阁(6) |  神界(7)  | 返回(8)  |')
            xz = str(input('：'))
            if xz == '1':
                print('成功加入青龙宗!')
                a = False
                self.zm = '青龙宗'
                self.zmdj = 1
            elif xz == '2' and self.dj * self.famous>= 500:
                print('成功加入华山派!')
                a = False
                self.zm = '华山派'
                self.zmdj = 4
            elif xz == '3' and self.dj * self.famous>= 800:
                print('成功加入玄灵宗!')
                a = False
                self.zm = '玄灵宗'
                self.zmdj = 6
            elif xz == '4' and self.dj * self.famous >= 1800:
                print('成功加入昊天宗!')
                a = False
                self.zm = '昊天宗'
                self.zmdj = 8
            elif xz == '5' and self.dj * self.famous >= 2800:
                print('成功加入唐门!')
                a = False
                self.zm = '唐门'
                self.zmdj = 10
            elif xz == '6' and self.dj * self.famous >= 4300:
                print('成功加入海神阁!')
                a = False
                self.zm = '海神阁'
                self.zmdj = 12
            elif xz == '7' and self.dj >= 101:
                print('成功加入神界!')
                a = False
                self.zm = '神界'
                self.zmdj = 20
            elif xz == '8':
                a = False
            else:
                print('未开放或等级不够!')
            input()

    def jdz(a):
        if a >= 0:
            return a
        else:
            return -a

    def slcspd(self):
        if self.slcs <= 10 and self.jys3 <= 0:
            self.dy = '坚韧黑铁'
            self.jys3 = 1
        if 10 < self.slcs <= 30 and self.jys3 <= 1:
            self.dy = '倔强青铜'
            self.jys3 = 2
            self.famous += random.randint(1, 2)
        if 30 < self.slcs <= 70 and self.jys3 <= 2:
            self.dy = '不屈白银'
            self.jys3 = 3
            self.famous += random.randint(1, 2)
        if 70 < self.slcs <= 150 and self.jys3 <= 3:
            self.dy = '英勇黄金'
            self.jys3 = 4
            self.famous += random.randint(2, 3)
        if 150 < self.slcs <= 240 and self.jys3 <= 4:
            self.dy = '坚韧铂金'
            self.jys3 = 5
            self.famous += random.randint(2, 3)
        if 240 < self.slcs <= 380 and self.jys3 <= 5:
            self.dy = '永恒钻石'
            self.jys3 = 6
            self.famous += random.randint(3, 4)
        if 380 < self.slcs <= 460 and self.jys3 <= 6:
            self.dy = '超级王牌'
            self.jys3 = 7
            self.famous += random.randint(3, 4)
        if 460 < self.slcs and self.jys3 <= 7:
            self.dy = '无敌战神'
            self.jys3 = 8
            self.famous += random.randint(4, 5)

    def defzm(self):
        am = True
        while am and self.zm != '无':
            clean_up()
            if self.zmgxe <= 1000:
                self.zy = '外门弟子'
            elif 1000 < self.zmgxe <= 3000:
                self.zy = '内门弟子'
            elif 3000 < self.zmgxe <= 7500:
                self.zy = '长老'
            elif 7500 < self.zmgxe <= 16000:
                if self.zm == '唐门':
                    self.zy = '副门主'
                elif self.zm == '海神阁':
                    self.zy = '副阁主'
                else:
                    self.zy = '副宗主'
            elif 16000 < self.zmgxe:
                if self.zm == '唐门':
                    self.zy = '门主'
                elif self.zm == '海神阁':
                    self.zy = '阁主'
                else:
                    self.zy = '宗主'

            self.jqzsset()
            self.wgmgset()
            self.jysxset()
            print('----------------------------宗门----------------------------')
            pljx = 0
            self.zmdj = int(self.zmdj + int(self.zmgxd // self.zmdjsx))
            self.zmdjsx = int(round((self.zmdj ** 2) * 1000, 0))
            self.zmgxd = self.zmgxe % self.zmdjsx
            print('宗门：', self.zm, sep='')
            print('宗门大厅(1) | 宗门比武(2) | 宗门商店(3) | 宗门任务(4) | 返回(5)')
            su = input('')
            if su == '1':
                print('-----------------------宗门大厅-----------------------')
                print('宗门：', self.zm, '\t\t等级：', self.zmdj, '(', self.zmgxd, '/', self.zmdjsx, ')')
                print('成员：权限不足无法查看', '\t职位：', self.zy)
                print('金币:', self.jqshow, '\t\t钻石:', self.zsshow)
                print('金币捐献(1) | 钻石捐献(2) | 退出宗门(3)')
                sr1 = str(input(''))
                if sr1 == '1' or sr1 == '2':
                    pljx = input('捐献数：')
                    try:
                        pljx = MUD.jdz(int(round(float(pljx), 0)))
                        if (sr1 == '1' and self.jq - pljx >= 0) or self.jq != '---':
                            if self.jq != '---':
                                self.jq = self.jq - pljx
                            print('感谢你的捐赠!')
                            print('金币-', pljx)
                            print('贡献度+', 0.1 * pljx)
                            self.zmgxd = self.zmgxd + (0.1 * pljx)
                            self.zmgxe = self.zmgxe + (0.1 * pljx)
                            self.plgx = self.plgx + (0.1 * pljx)
                        elif (sr1 == '2' and self.zs - pljx >= 0) or self.zs != '---':
                            if self.zs != '---':
                                self.zs = self.zs - pljx
                            print('感谢你的捐赠!')
                            print('钻石-', pljx)
                            print('贡献度+', pljx)
                            self.zmgxd = self.zmgxd + 10 * pljx
                            self.zmgxe = self.zmgxe + 10 * pljx
                            self.plgx = self.plgx + 10 * pljx
                        input('')
                    except:
                        print('输入有误!')
                elif sr1 == '3':
                    print('是否退出(贡献将会清零)？')
                    print('是(1) | 否(2)')
                    tc = str(input(':'))
                    if tc == '1':
                        print('已退出', self.zm)
                        self.zm = '无'
                        self.zmgxe = 0
                        self.slcs = 0
                        self.jys3 = 0
                        self.famous = max(self.famous - 20, 0)
                        self.dy = '坚韧黑铁'
                elif sr1 == '':
                    pass
                else:
                    print('金币或钻石不足')
                    input('')
            elif su == '2':
                running = True
                print('----------------------宗门比武场----------------------')
                while running == True:
                    clean_up()
                    self.information()
                    self.aiallzb()
                    print('开始匹配(1) | 返回(2)')
                    sr2 = input('')
                    if sr2 == '1' or sr2 == '':
                        zdz = input('请下赌注：')
                        try:
                            clean_up()
                            ai = MUD()
                            if zdz == '':
                                zdz = 0
                            zdz = MUD.jdz(int(round(float(zdz), 0)))
                            if zdz >= 32000:
                                print('赌注上限为32000$!')
                                zdz = 32000
                            if self.jq - zdz >= 0:
                                dum.new_time(0, 0, 0, 0, random.randint(1, 30))
                                ai.create_AI(self, zdz)
                                print('匹配成功!')
                                print('对手：')
                                ai.information()
                                ai.aiallzb()
                                print('----------------------------------------')
                                print('你的信息:见上')
                                input('任意键开始战斗...')
                                jg = ai.fight()
                                if jg == 1 or jg == 0:
                                    print('你赢了!')
                                    print('金钱 +', zdz)
                                    print('经验 +', ai.dj * 10)
                                    self.jq = self.jq + zdz
                                    self.jy = self.jy + ai.dj * 10
                                    self.slcs = self.slcs + 1
                                    self.lscs = self.lscs + 1
                                else:
                                    print('你输了!')
                                    print('金钱 -', zdz)
                                    self.jq = self.jq - zdz
                                    self.lscs = 0
                                input()
                            else:
                                print('赌注不足!')
                                input()

                        except:
                            print('输入赌注有误!')
                            input('')

                    elif sr2 == '2':
                        running = False
                    else:
                        print('未开放!')
                        input()

            elif su == '3':
                run = True
                while run == True:
                    clean_up()
                    print('---------------------------宗门商店---------------------------')
                    dum.new_time(0, 0, 0, 0, 5)
                    print('欢迎!', self.name)
                    print('由于您是', self.zy, '您可以前往:')
                    print('第', end='')
                    print('1', end='')
                    if 1000 < self.zmgxe:
                        print('、2', end='')
                    if 3000 < self.zmgxe:
                        print('、3', end='')
                    if 7500 < self.zmgxe:
                        print('、4', end='')
                    if self.zmgxe > 16000:
                        print('、5', end='')
                    print('层')
                    print('宗门贡献(@):', self.plgxshow)
                    print('金钱:', self.jqshow, '\t\t钻石:', self.zsshow)
                    print('------------------------------------------------------------')
                    print('| 第(1)层 | 第(2)层 | 第(3)层 | 第(4)层 | 第(5)层 |')
                    print('------------------------------------------------------------')
                    print('返回(6)')
                    sr4 = input('')
                    if sr4 == '1':
                        dum.new_time(0, 0, 0, 0, 5)
                        print('---------------------------第 1 层---------------------------')
                        print('铁矛★★\t\t\t50@(1)')
                        print('钢剑★★\t\t\t50@(2)')
                        print('蒙德拉贡★★\t\t100@(3)')
                        print('AK-47★★★\t\t450@(4)')
                        print('UNP9★★★\t\t400@(5)')
                        print('M4★★★★\t\t1100@(6)')
                        print('Kar98★★★★\t\t2800@(7)')
                        print('匕首(β-钛合金)★★★★\t1400@(8)')
                        sr5 = input('')
                        if sr5 == '1' and self.plgx - 50 >= 0:
                            self.plgx = self.plgx - 50
                            self.tm = self.tm + 1
                        elif sr5 == '2' and self.plgx - 50 >= 0:
                            self.plgx = self.plgx - 50
                            self.gj = self.gj + 1
                        elif sr5 == '3' and self.plgx - 100 >= 0:
                            self.plgx = self.plgx - 100
                            self.mdlg = self.mdlg + 1
                        elif sr5 == '4' and self.plgx - 450 >= 0:
                            self.plgx = self.plgx - 450
                            self.ak47 = self.ak47 + 1
                        elif sr5 == '5' and self.plgx - 400 >= 0:
                            self.plgx = self.plgx - 400
                            self.unp9 = self.unp9 + 1
                        elif sr5 == '6' and self.plgx - 1100 >= 0:
                            self.plgx = self.plgx - 1100
                            self.m4 = self.m4 + 1
                        elif sr5 == '7' and self.plgx - 2800 >= 0:
                            self.plgx = self.plgx - 2800
                            self.kar98 = self.kar98 + 1
                        elif sr5 == '8' and self.plgx - 1400 >= 0:
                            self.plgx = self.plgx - 1400
                            self.bsba = self.bsba + 1
                        else:
                            print('未开放或宗门贡献(@)不足!')
                            input()
                    elif sr4 == '2' and self.zmgxe > 3000:
                        dum.new_time(0, 0, 0, 0, 5)
                        print('---------------------------第 2 层---------------------------')
                        print('魂环1000年\t\t\t200@(1)')
                        print('魂环2000年\t\t\t400@(2)')
                        print('魂环4000年\t\t\t800@(3)')
                        print('魂环6000年\t\t\t1200@(4)')
                        print('魂环8000年\t\t\t1600@(5)')
                        print('魂环10000年\t\t\t2000@(6)')
                        print('魂环20000年\t\t\t4000@(7)')
                        print('魂环40000年\t\t\t8000@(8)')
                        sr5 = input('')
                        if sr5 == '1' and self.plgx - 200 >= 0:
                            self.plgx = self.plgx - 200
                            self.listhh = self.listhh + [1000]
                        elif sr5 == '2' and self.plgx - 400 >= 0:
                            self.plgx = self.plgx - 400
                            self.listhh = self.listhh + [2000]
                        elif sr5 == '3' and self.plgx - 800 >= 0:
                            self.plgx = self.plgx - 800
                            self.listhh = self.listhh + [4000]
                        elif sr5 == '4' and self.plgx - 1200 >= 0:
                            self.plgx = self.plgx - 1200
                            self.listhh = self.listhh + [6000]
                        elif sr5 == '5' and self.plgx - 1600 >= 0:
                            self.plgx = self.plgx - 1600
                            self.listhh = self.listhh + [8000]
                        elif sr5 == '6' and self.plgx - 2000 >= 0:
                            self.plgx = self.plgx - 2000
                            self.listhh = self.listhh + [10000]
                        elif sr5 == '7' and self.plgx - 4000 >= 0:
                            self.plgx = self.plgx - 4000
                            self.listhh = self.listhh + [20000]
                        elif sr5 == '8' and self.plgx - 8000 >= 0:
                            self.plgx = self.plgx - 8000
                            self.listhh = self.listhh + [40000]
                        else:
                            print('未开放或宗门贡献(@)不足!')
                            input()
                    elif sr4 == '6' or sr4 == '':
                        run = False
                    else:
                        print('未开放或贡献不足!')
                        input()

            elif su == '4':
                dum.new_time(0, 0, 0, 0, 5)
                print('---------------------------宗门任务----------------------------')
                print('宗门例行巡逻(1)')
                print('管理宗门禁地(2)')
                print('辅导宗门弟子(3)')
                print('外出宗门历练(4)')
                print('防卫外部据点(5)')
                print('宗门外部防御(6)')
                der = input('')
                if der == '1':
                    self.new_time(1)
                    self.zmgxd = self.zmgxd + 10
                    self.zmgxe = self.zmgxe + 10
                    self.plgx = self.plgx + 10
                    self.jy = self.jy + 10
                elif der == '2':
                    self.new_time(5)
                    self.zmgxd = self.zmgxd + 60
                    self.zmgxe = self.zmgxe + 60
                    self.plgx = self.plgx + 60
                    self.jy = self.jy + 60
                elif der == '3':
                    self.new_time(15)
                    self.zmgxd = self.zmgxd + 200
                    self.zmgxe = self.zmgxe + 200
                    self.plgx = self.plgx + 200
                    self.jy = self.jy + 200
                elif der == '4':
                    self.new_time(30)
                    self.zmgxd = self.zmgxd + 420
                    self.zmgxe = self.zmgxe + 420
                    self.plgx = self.plgx + 420
                    self.jy = self.jy + 420
                elif der == '5':
                    self.new_time(90)
                    self.zmgxd = self.zmgxd + 1400
                    self.zmgxe = self.zmgxe + 1400
                    self.plgx = self.plgx + 1400
                    self.jy = self.jy + 1400
                elif der == '6':
                    self.new_time(360)
                    self.zmgxd = self.zmgxd + 6400
                    self.zmgxe = self.zmgxe + 6400
                    self.plgx = self.plgx + 6400
                    self.jy = self.jy + 6400
            elif su == '5' or su == '':
                am = False
            else:
                print('未开放!')
                input()

    def create_AI(self, dum, zdz):
        # use "self" = MUD() before create_AI to create an aiself
        self.name = MUD.random_name()
        self.famous = random.randint(1, 25)
        self.xl = random.randint(80, 150)
        self.wg = random.randint(5, 13)
        self.gj_mg = random.randint(1, 7)
        self.wf = random.randint(4, 12)
        self.mf = random.randint(0, 6)
        self.jq = random.randint(zdz, zdz + 10000)
        self.zs = random.randint(0, dum.zs + 120)
        if dum.slcs <= 20:
            self.slcs = 0
        else:
            self.slcs = random.randint(dum.slcs - 20, dum.slcs + zdz)
        self.slcspd()
        if (dum.zmdj + 20 + dum.lscs) <= (dum.dj + 15 + dum.lscs) <= 99:
            self.dj = random.randint(dum.zmdj + 10 + dum.lscs, dum.dj + 5 + dum.lscs)
        elif (dum.zmdj + 20 + dum.lscs) <= 99 <= (dum.dj + 15 + dum.lscs):
            self.dj = random.randint(dum.zmdj + 10 + dum.lscs, 99)
        elif (dum.zmdj + 20 + dum.lscs) >= (dum.dj + 15 + dum.lscs) >= 99:
            self.dj = random.randint(99, dum.dj + 5 + dum.lscs)
        else:  # (dum.dj+15+dum.lscs)<=(dum.zmdj+20+dum.lscs)<=99
            self.dj = random.randint(dum.dj + 5 + dum.lscs, dum.zmdj + 10 + dum.lscs)
        self.jy = random.randint(self.dj ** 3 + 1, (self.dj + 1) ** 3 - 1)
        self.jsl = random.randint(self.dj, self.dj ** 2)
        self.level = random.randint(max(dum.level - 10, 5), (dum.level + 10))
        self.xp = random.randint(self.level ** 3 + 1, (self.level + 1) ** 3 - 1)
        self.check_level()
        self.random_core()
        self.check_core()
        self.jslxr = '灵元境'
        self.jslsx = 50
        self.jy = self.jy + zdz + (self.slcs * 100)
        self.zz = '人族'
        self.random_zb()
        self.random_hh()
        xb = random.randint(1, 2)
        self.yz, self.yzxr, self.xb = MUD.random_yz(str(xb))
        self.zlsx()
        self.djpd(False)
        self.zlsx()

    def aiallzb(self):
        t1 = MUD.tab_pd(self.zbhead)
        t2 = MUD.tab_pd(self.zbxb)
        t3 = MUD.tab_pd(self.zbleg)
        t4 = MUD.tab_pd(self.zbfoot)
        t5 = MUD.tab_pd(self.zszb, -6)
        t6 = MUD.tab_pd(self.fszb, -6)
        print('装备列表:', end='')
        print('\t\t魂骨列表:')
        print('头:', self.zbhead, end='')
        print(t1, '头部:', self.hgt)
        print('胸:', self.zbxb, end='')
        print(t2, '躯干:', self.hgqg)
        print('腿:', self.zbleg, end='')
        print(t3, '左臂:', self.hgzb)
        print('脚:', self.zbfoot, end='')
        print(t4, '右臂:', self.hgyb)
        print('主手:', self.zszb, end='')
        print(t5, '左腿:', self.hgzt)
        print('副手:', self.fszb, end='')
        print(t6, '右腿:', self.hgyt)
        print()
        t1 = MUD.tab_pd(self.hh1, -7)
        t2 = MUD.tab_pd(self.hh2, -7)
        t3 = MUD.tab_pd(self.hh3, -7)
        t4 = MUD.tab_pd(self.hh4, -7)
        t5 = MUD.tab_pd(self.hh5, -7)
        t6 = MUD.tab_pd(self.hh6, -7)
        t7 = MUD.tab_pd(self.hh7, -7)
        t8 = MUD.tab_pd(self.hh8, -7)
        t9 = MUD.tab_pd(self.hh9, -7)
        print('魂环列表:', end='')
        print('\t\t魂灵列表:')
        print('一:', self.hh1, '' if self.hh1 == '无' else '年', end='')
        print(t1, '一:', self.hl1)
        print('二:', self.hh2, '' if self.hh2 == '无' else '年', end='')
        print(t2, '二:', self.hl2)
        print('三:', self.hh3, '' if self.hh3 == '无' else '年', end='')
        print(t3, '三:', self.hl3)
        print('四:', self.hh4, '' if self.hh4 == '无' else '年', end='')
        print(t4, '四:', self.hl4)
        print('五:', self.hh5, '' if self.hh5 == '无' else '年', end='')
        print(t5, '五:', self.hl5)
        print('六:', self.hh6, '' if self.hh6 == '无' else '年', end='')
        print(t6, '六:', self.hl6)
        print('七:', self.hh7, '' if self.hh7 == '无' else '年', end='')
        print(t7, '七:', self.hl7)
        print('八:', self.hh8, '' if self.hh8 == '无' else '年', end='')
        print(t8, '八:', self.hl8)
        print('九:', self.hh9, '' if self.hh9 == '无' else '年', end='')
        print(t9, '九:', self.hl9)
        print()

    def aihg(self):
        print('魂骨列表:')
        print('头部:', self.hgt)
        print('躯干:', self.hgqg)
        print('左臂:', self.hgzb)
        print('右臂:', self.hgyb)
        print('左腿:', self.hgzt)
        print('右腿:', self.hgyt)

    def aizb(self):
        print('装备列表:')
        print('头:', self.zbhead)
        print('胸:', self.zbxb)
        print('腿:', self.zbleg)
        print('脚:', self.zbfoot)
        print('主手:', self.zszb)
        print('副手:', self.fszb)

    def aihh(self):
        print('魂环列表:')
        print('一:', self.hh1, '年')
        print('二:', self.hh2, '年')
        print('三:', self.hh3, '年')
        print('四:', self.hh4, '年')
        print('五:', self.hh5, '年')
        print('六:', self.hh6, '年')
        print('七:', self.hh7, '年')
        print('八:', self.hh8, '年')
        print('九:', self.hh9, '年')

    def aihl(self):
        print('魂灵列表:')
        print('一:', self.hl1)
        print('二:', self.hl2)
        print('三:', self.hl3)
        print('四:', self.hl4)
        print('五:', self.hl5)
        print('六:', self.hl6)
        print('七:', self.hl7)
        print('八:', self.hl8)
        print('九:', self.hl9)

    def random_core(self):
        if self.dj >= 70:
            a = min(10, 100 - self.dj)
            r = random.randint(a, 10)
            if r == 10:
                if 1 <= min(9, int(self.dj - 70) / 2):
                    self.soul_core_des = random.randint(1, min(9, int((self.dj - 70) / 2)))
                else:
                    self.soul_core_des = random.randint(min(9, int((self.dj - 70) / 2)), 1)
                if (self.soul_core_des ** 3) <= ((self.soul_core_des - 1) ** 3):
                    self.soul_core = random.randint(self.soul_core_des ** 3, (self.soul_core_des - 1) ** 3)
                else:
                    self.soul_core = random.randint((self.soul_core_des - 1) ** 3, self.soul_core_des ** 3)

    def random_hh(self):
        dj = (self.dj / 10) // 1
        listH = []
        i = 1
        while i <= 10:
            hhmax = self.hhmax()
            q = random.randint(0, 100)
            if i <= dj:
                if q <= self.dj * 1.2:
                    a = (hhmax * 0.4) // 1
                    b = hhmax - (10 ** (len(str(hhmax)) - 1))
                    if a <= b:
                        year = random.randint(a, b)
                    else:
                        year = random.randint(b, a)
                    year = self.zbhhpd(year, i, 1, mod='ai')
                    listH = listH + [year]
                else:
                    listH += ['无']
            else:
                listH += ['无']
            i = i + 1
        try:
            self.hh1 = listH[0]
            self.hh2 = listH[1]
            self.hh3 = listH[2]
            self.hh4 = listH[3]
            self.hh5 = listH[4]
            self.hh6 = listH[5]
            self.hh7 = listH[6]
            self.hh8 = listH[7]
            self.hh9 = listH[8]
        except:
            pass

    def random_zb(self):
        xb = random.randint(0, 1)
        leg = random.randint(0, 1)
        r = random.randint(0, 1)
        l = random.randint(0, 1)
        if xb == 1:
            xb = random.randint(0, 1)
            self.zbxb = list_xb[xb]
        if leg == 1:
            leg = random.randint(0, 2)
            self.zbleg = list_leg[leg]
        t = self.dj // 2
        if self.dj >= 60:
            t = 30
        elif self.dj <= 8:
            t = 4
        if r == 1:
            r = random.randint(0, t)
            self.zszb = list_r[r]
        if l == 1:
            l = random.randint(0, t - 4)
            self.zszb = list_r[l]
        self.zbpd(self.zbxb, 1)
        self.zbpd(self.zbleg, 1)
        self.zbpd(self.zszb, 1)
        self.zbpd(self.fszb, 1)

    def fight(self):
        global dum
        plxl = int(round(dum.xl * dum.xlxs * dum.sxxs, 0))
        plwg = int(round(dum.wg * dum.wgxs * dum.sxxs, 0))
        plmg = int(round(dum.gj_mg * dum.gj_mgxs * dum.sxxs, 0))
        plwf = int(round(dum.wf * dum.wfxs * dum.sxxs, 0))
        plmf = int(round(dum.mf * dum.mfxs * dum.sxxs, 0))
        hjcs = 0
        aics = 0

        aixl = int(round(self.xl * self.xlxs * self.sxxs, 0))
        aiwg = int(round(self.wg * self.wgxs * self.sxxs, 0))
        aimg = int(round(self.gj_mg * self.gj_mgxs * self.sxxs, 0))
        aiwf = int(round(self.wf * self.wfxs * self.sxxs, 0))
        aimf = int(round(self.mf * self.mfxs * self.sxxs, 0))
        i = 0
        while aixl > 0 and plxl > 0:
            plxl = int(round(plxl, 0))
            aixl = int(round(aixl, 0))
            plxlshow = MUD.jqzsint(plxl)
            aixlshow = MUD.jqzsint(aixl)
            i = i + 1
            print('第', i, '回合:')
            print('你 的血量:', plxlshow)
            print('你 的护甲:', MUD.jqzsint(max(0, plwf + plmf)), '(物防:', MUD.jqzsint(max(0, plwf)), '魔防:',
                  MUD.jqzsint(plmf), ')')
            print('----------------------------------------------------------')
            print(self.name, '的血量:', aixlshow)
            print(self.name, '的护甲:', MUD.jqzsint(max(aiwf + aimf, 0)), '(物防:', MUD.jqzsint(max(0, aiwf)), '魔防:',
                  MUD.jqzsint(aimf), ')')
            dumwg = random.randint(int(round((plwg + dum.jsl) * 0.3, 0)), int(round(plwg * 2 + dum.jsl, 0)))
            dummg = random.randint(0, int(round(plmg * 3 + dum.jsl, 0)))
            wgxr = ''
            mgxr = ''
            if dumwg >= (plwg * 1.5):
                wgxr = '(暴击)'
            elif dumwg <= (plwg * 0.5):
                wgxr = '(免疫)'
            if dummg >= (plmg * 2):
                mgxr = '(暴击)'
            elif dummg <= (plmg * 0.3):
                mgxr = '(免疫)'
            print('你 :物攻:', MUD.jqzsint(dumwg), wgxr, '魔攻:', MUD.jqzsint(dummg), mgxr)
            if aiwf > 0:
                aiwf = aiwf - dumwg
            else:
                aixl = aixl - dumwg
            if aimf > 0:
                aimf = aimf - dummg
            else:
                aixl = aixl - dummg * 1.5
            if (aiwf + aimf) <= 0 and aics == 0:
                aics = 1
                print('破甲!')
                if aixl + aiwf + aimf <= 0 and self.dj - dum.dj <= -20:
                    aixl = 0
                aiwf = 0
                aimf = 0

            selfwg = random.randint(int(round((aiwg + self.jsl) * 0.3, 0)), int(round(aiwg * 2 + self.jsl, 0)))
            selfmg = random.randint(0, int(round(aimg * 3 + self.jsl, 0)))
            wgxr = ''
            mgxr = ''
            if selfwg >= (aiwg * 1.5):
                wgxr = '(暴击)'
            elif selfwg <= (aiwg * 0.5):
                wgxr = '(免疫)'
            if selfmg >= (aimg * 2):
                mgxr = '(暴击)'
            elif selfmg <= (aimg * 0.3):
                mgxr = '(免疫)'
            print(self.name, ':物攻:', MUD.jqzsint(selfwg), wgxr, '魔攻:', MUD.jqzsint(selfmg), mgxr)
            if plwf > 0:
                plwf = plwf - selfwg
            else:
                plxl = plxl - selfwg
            if plmf > 0:
                plmf = plmf - selfmg
            else:
                plxl = plxl - selfmg * 1.5
            if plwf + plmf <= 0 and hjcs == 0:
                hjcs = 1
                print('你的护甲为你挡住了最后一击...')
                if plxl + plwf + plmf <= 0 and self.dj - dum.dj >= 20:
                    plxl = 0
                plwf = 0
                plmf = 0

            dum.new_time(0, 0, 0, 0, 10)
            print('----------------------------------------------------------')

        print('')
        plxl = int(round(plxl, 0))
        aixl = int(round(aixl, 0))
        q = MUD.zfpd(plxl)
        p = MUD.zfpd(aixl)
        print('你 的血量:', MUD.jqzsint(q))
        print('你 的护甲:', MUD.jqzsint(plwf + plmf), '(物防:', MUD.jqzsint(plwf), '魔防:', MUD.jqzsint(plmf), ')')
        print('----------------------------------------------------------')
        print(self.name, '的血量:', MUD.jqzsint(p))
        print(self.name, '的护甲:', MUD.jqzsint(aiwf + aimf), '(物防:', MUD.jqzsint(aiwf), '魔防:', MUD.jqzsint(aimf),
              ')')
        if aixl <= 0 and plxl <= 0:
            print('你们同归于尽!')
            a = 0
            dum.jsl = int(round(dum.jsl * 1.01, 0))
        elif aixl <= 0:
            a = 1
            if dum.xb == '114514':
                print('哈哈，野兽先辈是不可战胜的!')
            print(self.name, '死了!')
            dum.jsl = dum.jsl + random.randint(int(round(dum.jsl / 100, 0)), int(round(dum.jsl / 10, 0))) * 8
        else:
            a = 2
            if dum.xb == '114514':
                print('哼~哼~哼~啊啊啊啊啊啊啊啊！！！')
            print('你 死了!')
            if max(dum.dj - self.dj, self.dj - dum.dj) <= dum.dj:
                dum.jsl = dum.jsl + random.randint(max(dum.dj - self.dj, self.dj - dum.dj), dum.dj) * 5
            else:
                dum.jsl = dum.jsl + random.randint(dum.dj, max(dum.dj - self.dj, self.dj - dum.dj)) * 5
        input()
        return a

    def zfpd(a):
        if a < 0:
            return 0
        else:
            return a

    # zb
    def zbpd(self, name, xs):
        dum.new_time(0, 0, 0, 0, 2)
        if name == '屎★':
            self.s = self.s - xs
            self.gj_mg = self.gj_mg + (xs * 1)
        elif name == '铁剑★':
            self.tj = self.tj - xs
            self.wg = self.wg + (xs * 5)
        elif name == '匕首★':
            self.bs = self.bs - xs
            self.wg = self.wg + (xs * 3)
        elif name == '木弓★':
            self.mg = self.mg - xs
            self.wg = self.wg + (xs * 7)
        elif name == '铁矛★★':
            self.tm = self.tm - xs
            self.wg = self.wg + (xs * 16)
            self.gj_mg = self.gj_mg + (xs * 2)
        elif name == '钢剑★★':
            self.gj = self.gl - xs
            self.wg = self.wg + (xs * 12)
            self.gj_mg = self.gj_mg + (xs * 4)
        elif name == '蒙德拉贡★★':
            self.mdlg = self.mdlg - xs
            self.wg = self.wg + (xs * 23)
        elif name == 'AK-47★★★':
            self.ak47 = self.ak47 - xs
            self.wg = self.wg + (xs * 45)
        elif name == 'UZI★★★':
            self.uzi = self.uzi - xs
            self.wg = self.wg + (xs * 26)
            self.gj_mg = self.gj_mg + (xs * 5)
        elif name == 'unp9':
            self.unp9 = self.unp9 - xs
            self.wg = self.wg + (34 * xs)
            self.gj_mg = self.gj_mg + (xs * 3)
        elif name == '杀猪刀★★★':
            self.szd = self.szd - xs
            self.wg = self.wg + (24 * xs)
            self.gj_mg = self.gj_mg + (xs * 10)
        elif name == '爪刀★★★':
            self.zd = self.zd - xs
            self.wg = self.wg + (44 * xs)
            self.gj_mg = self.gj_mg + (2 * xs)
        elif name == '铁丝棒球棍★★★':
            self.tsbq = self.tsbq - xs
            self.wg = self.wg + (xs * 54)
        elif name == '[无名刀]木偶★★★':
            self.mo = self.mo - xs
            self.wg = self.wg + (xs * 10)
            self.gj_mg = self.gj_mg + (xs * 20)
        elif name == '铁弓★★★':
            self.mo += -xs
            self.wg += xs * 20
            self.gj_mg += xs * 5
        elif name == '复合弓★★★★':
            self.mo += -xs
            self.wg += xs * 40
            self.gj_mg += xs * 10
        elif name == '麒麟臂★★★★':
            self.qlb = self.qlb - xs
            self.wg = self.wg + (xs * 58)
            self.gj_mg = self.gj_mg + (xs * 12)
        elif name == 'AK-74★★★★':
            self.ak74 = self.ak74 - xs
            self.wg = self.wg + (xs * 65)
            self.gj_mg = self.gj_mg + (xs * 2)
        elif name == 'M4★★★★':
            self.m4 = self.m4 - xs
            self.wg = self.wg + (xs * 64)
            self.gj_mg = self.gj_mg + (xs * 2)
        elif name == '匕首(β-钛合金)★★★★':
            self.bsba = self.bsba - xs
            self.wg = self.wg + (xs * 60)
            self.gj_mg = self.gj_mg + (xs * 16)
        elif name == 'YJ★★★★':
            self.yj = self.yj - xs
            self.wg = self.wg + (xs * 63)
            self.gj_mg = self.gj_mg + (xs * 22)
        elif name == 'Kar98★★★★':
            self.kar98 = self.kar98 - xs
            self.wg = self.wg + (102 * xs)
            self.gj_mg = self.gj_mg + (xs * 10)
        elif name == '[妖刀]芈月★★★★★':
            self.my = self.my - xs
            self.wg = self.wg + (65 * xs)
            self.gj_mg = self.gj_mg + (40 * xs)
        elif name == 'AK-12★★★★★':
            self.ak12 = self.ak12 - xs
            self.wg = self.wg + (xs * 87)
            self.gj_mg = self.gj_mg + (xs * 12)
        elif name == 'M416★★★★★':
            self.m416 = self.m416 - xs
            self.wg = self.wg + (xs * 92)
            self.gj_mg = self.gj_mg + (xs * 14)
        elif name == 'M82A1★★★★★':
            self.m82a1 = self.m82a1 - xs
            self.wg = self.wg + (xs * 222)
            self.gj_mg = self.gj_mg + (xs * 24)
        elif name == 'RPG★★★★★':
            self.rpg = self.rpg - xs
            self.wg = self.wg + (xs * 250)
            self.gj_mg = self.gj_mg + (xs * 50)
        elif name == 'AUG★★★★★':
            self.aug = self.aug - xs
            self.wg = self.wg + (xs * 97)
            self.gj_mg = self.gj_mg * (xs * 8)
        elif name == '凶霖之爪★★★★★':
            self.xlzz = self.xlzz - xs
            self.wg = self.wg + (xs * 65)
            self.gj_mg = self.gj_mg + (xs * 54)
        elif name == '死亡笔记★★★★★':
            self.swbj = self.swbj - xs
            self.gj_mg = self.gj_mg + (xs * 1000)
        elif name == '龙鳞剑★★★★★':
            self.llj = self.llj - xs
            self.wg = self.wg + (xs * 98)
            self.gj_mg = self.gj_mg + (xs * 35)
            self.wf = self.wf + (xs * 1)
        elif name == '神之YJ★★★★★':
            self.szyj = self.szjy - xs
            self.wg = self.wg + (xs * 45)
            self.gj_mg = self.gj_mg + (xs * 100)
        elif name == 'CR神器★★★★★':
            self.crsq = self.crsq - xs
            self.wg = self.wg + (xs * 74)
            self.gj_mg = self.gj_mg + (xs * 45)
        elif name == '愚公铲★★★★★':
            self.ygc = self.ygc - xs
            self.wg = self.wg + (xs * 105)
            self.gj_mg = self.gj_mg + (xs * 25)
        elif name == '光焰龙枪★★★★★':
            self.gylc = self.gylc - xs
            self.wg = self.wg + (xs * 120)
            self.gj_mg = self.gj_mg + (xs * 50)
            self.wf = self.wf + (xs * 20)
            self.mf = self.mf + (xs * 5)
        elif name == '木胸甲★':
            self.mxj = self.mxj - xs
            self.wf = self.wf + (xs * 20)
            self.mf = self.mf + (xs * 2)
            self.xl = self.xl + (xs * 25)
        elif name == '铁胸甲★★':
            self.txj = self.txj - xs
            self.wf = self.wf + (xs * 60)
            self.mf = self.mf + (xs * 10)
            self.xl = self.xl + (xs * 80)
        elif name == '钢胸甲★★★':
            self.gxj = self.gxj - xs
            self.wf = self.wf + (xs * 150)
            self.mf = self.mf + (xs * 20)
            self.xl = self.xl + (xs * 200)
        elif name == '七彩神龙甲★★★★★':
            self.qcslj = self.qcslj - xs
            self.wf = self.wf + (xs + 1000)
            self.mf = self.mf(xs * 200)
            self.xl = self.xl + (xs * 1500)
        elif name == '木腿甲★':
            self.mtj = self.mtj - xs
            self.wf = self.wf + (xs * 15)
            self.mf = self.mf + (xs * 1)
            self.xl = self.xl + (xs * 20)
        elif name == '铁腿甲★★':
            self.ttj = self.ttj - xs
            self.wf = self.wf + (xs * 40)
            self.mf = self.mf + (xs * 6)
            self.xl = self.xl + (xs * 60)
        elif name == '钢腿甲★★★':
            self.gxj = self.gxj - xs
            self.wf = self.wf + (xs * 100)
            self.mf = self.mf + (xs * 12)
            self.xl = self.xl + (xs * 120)

    def hhmax(self):
        year = int(round(10 ** ((self.dj / 10)), 0))
        year = min(year, 1000000)
        a = 0
        if self.hh1 != '无':
            a += self.hh1
        if self.hh2 != '无':
            a += self.hh2
        if self.hh3 != '无':
            a += self.hh3
        if self.hh4 != '无':
            a += self.hh4
        if self.hh5 != '无':
            a += self.hh5
        if self.hh6 != '无':
            a += self.hh6
        if self.hh7 != '无':
            a += self.hh7
        if self.hh8 != '无':
            a += self.hh8
        if self.hh9 != '无':
            a += self.hh9
        year = min(int((self.jsl * self.dj / 2) - a), year, self.jy // 9)
        year = max(year, 10)
        return year

    def zbhhpd(self, year, n, xs, mod='player'):
        year = int(year)
        if year <= self.hhmax():
            if mod == 'player':
                self.new_time(0, 0, 0, 0, 20)
            zjj = ((year * n) ** (1 / 3)) / 6 * xs
            self.gj_mg = self.gj_mg + zjj
            self.wg = self.wg + 2 * zjj
            if mod == 'ai':
                return year
        elif year > self.hhmax and mod == 'ai':
            return '无'
        else:
            print('魂环年份过高!')

    def zbwq(self):
        global dum
        print('背包武器：')
        listb = []
        a = 0
        if dum.s > 0:
            a = a + 1
            print('  屎★*', dum.s, '\t\t(', a, ')')
            listb = listb + ['屎★']
        if dum.tj > 0:
            a = a + 1
            print('  铁剑★*', dum.tj, '\t\t(', a, ')')
            listb = listb + ['铁剑★']
        if dum.bs > 0:
            a = a + 1
            print('  匕首★*', dum.bs, '\t\t(', a, ')')
            listb = listb + ['匕首★']
        if dum.mg > 0:
            a = a + 1
            print('  木弓★*', dum.mg, '\t\t(', a, ')')
            listb = listb + ['木弓★']
        if dum.tm > 0:
            a = a + 1
            print('  铁矛★★*', dum.tm, '\t\t(', a, ')')
            listb = listb + ['铁矛★★']
        if dum.gj > 0:
            a = a + 1
            print('  钢剑★★*', dum.gj, '\t\t(', a, ')')
            listb = listb + ['钢剑★★']
        if dum.mdlg > 0:
            a = a + 1
            print('  蒙德拉贡★★*', dum.mdlg, '\t\t(', a, ')')
            listb = listb + ['蒙德拉贡★★']
        if dum.ak47 > 0:
            a = a + 1
            print('  AK-47★★★*', dum.ak47, '\t\t(', a, ')')
            listb = listb + ['AK-47★★★']
        if dum.uzi > 0:
            a = a + 1
            print('  UZI★★★*', dum.uzi, '\t\t(', a, ')')
            listb = listb + ['UZI★★★']
        if dum.unp9 > 0:
            a = a + 1
            print('  UNP9★★★*', dum.unp9, '\t\t(', a, ')')
            listb = listb + ['UNP9★★★']
        if dum.szd > 0:
            a = a + 1
            print('  杀猪刀★★★*', dum.szd, '\t\t(', a, ')')
            listb = listb + ['杀猪刀★★★']
        if dum.zd > 0:
            a = a + 1
            print('  爪刀★★★*', dum.zd, '\t\t(', a, ')')
            listb = listb + ['爪刀★★★']
        if dum.tsbq > 0:
            a = a + 1
            print('  铁丝棒球棍★★★*', dum.tsbq, '\t\t(', a, ')')
            listb = listb + ['铁丝棒球棍★★★']
        if dum.wsd > 0:
            a = a + 1
            print('  武士刀★★★*', dum.wsd, '\t\t(', a, ')')
            listb = listb + ['武士刀★★★']
        if dum.mo > 0:
            a = a + 1
            print('  [无名刀]木偶★★★*', dum.mo, '\t\t(', a, ')')
            listb = listb + ['[无名刀]木偶★★★']
        if dum.tieg > 0:
            a += 1
            print('  铁弓★★★*', dum.tieg, '\t\t(', a, ')')
            listb += ['铁弓★★★']
        if dum.qlb > 0:
            a = a + 1
            print('  麒麟臂★★★★*', dum.qlb, '\t\t(', a, ')')
            listb = listb + ['麒麟臂★★★★']
        if dum.ak74 > 0:
            a = a + 1
            print('  AK-74★★★★*', dum.ak74, '\t\t(', a, ')')
            listb = listb + ['AK-74★★★★']
        if dum.m4 > 0:
            a = a + 1
            print('  M4★★★★*', dum.m4, '\t\t(', a, ')')
            listb = listb + ['M4★★★★']
        if dum.bsba > 0:
            a = a + 1
            print('  匕首(β-钛合金)★★★★*', dum.bsba, '\t\t(', a, ')')
            listb = listb + ['匕首(β-钛合金)★★★★']
        if dum.yj > 0:
            a = a + 1
            print('  YJ★★★★*', dum.yj, '\t\t(', a, ')')
            listb = listb + ['YJ★★★★']
        if dum.fhg > 0:
            a += 1
            print('  复合弓★★★★*', dum.fhg, '\t\t(', a, ')')
            listb += ['复合弓★★★★']
        if dum.kar98 > 0:
            a = a + 1
            print('  Kar98★★★★*', dum.kar98, '\t\t(', a, ')')
            listb = listb + ['Kar98★★★★']
        if dum.my > 0:
            a = a + 1
            print('  [妖刀]芈月★★★★★*', dum.my, '\t\t(', a, ')')
            listb = listb + ['[妖刀]芈月★★★★★']
        if dum.ak12 > 0:
            a = a + 1
            print('  AK-12★★★★★*', dum.ak12, '\t\t(', a, ')')
            listb = listb + ['AK-12★★★★★']
        if dum.m416 > 0:
            a = a + 1
            print('  M416★★★★★*', dum.m416, '\t\t(', a, ')')
            listb = listb + ['M416★★★★★']
        if dum.m82a1 > 0:
            a = a + 1
            print('  M82A1★★★★★*', dum.m82a1, '\t\t(', a, ')')
            listb = listb + ['M82A1★★★★★']
        if dum.aug > 0:
            a = a + 1
            print('  AUG★★★★★*', dum.aug, '\t\t(', a, ')')
            listb = listb + ['AUG★★★★★']
        if dum.rpg > 0:
            a = a + 1
            print('  RPG★★★★★*', dum.rpg, '\t\t(', a, ')')
            listb = listb + ['RPG★★★★★']
        if dum.xlzz > 0:
            a = a + 1
            print('  凶霖之爪★★★★★*', dum.xlzz, '\t\t(', a, ')')
            listb = listb + ['凶霖之爪★★★★★']
        if dum.swbj > 0:
            a = a + 1
            print('  死亡笔记★★★★★*', dum.swbj, '\t\t(', a, ')')
            listb = listb + ['死亡笔记★★★★★']
        if dum.llj > 0:
            a = a + 1
            print('  龙鳞剑★★★★★*', dum.llj, '\t\t(', a, ')')
            listb = listb + ['龙鳞剑★★★★★']
        if dum.szyj > 0:
            a = a + 1
            print('  神之YJ★★★★★*', dum.szyj, '\t\t(', a, ')')
            listb = listb + ['神之YJ★★★★★']
        if dum.crsq > 0:
            a = a + 1
            print('  CR神器★★★★★*', dum.crsq, '\t\t(', a, ')')
            listb = listb + ['CR神器★★★★★']
        if dum.ygc > 0:
            a = a + 1
            print('  愚公铲★★★★★*', dum.ygc, '\t\t(', a, ')')
            listb = listb + ['愚公铲★★★★★']
        if dum.gylq > 0:
            a = a + 1
            print('  光焰龙枪★★★★★*', dum.gylq, '\t\t(', a, ')')
            listb = listb + ['光焰龙枪★★★★★']
        if a == 0:
            print('无')
        return listb

    def zbhjhead(self):
        global dum
        print('背包防具：')
        listb = []
        a = 0
        print('无')

    def zbhjxb(self):
        global dum
        print('背包防具：')
        listb = []
        a = 0
        if dum.mxj > 0:
            a = a + 1
            print('  木胸甲★*', dum.mxj, '\t\t(', a, ')')
            listb = listb + ['木胸甲★']
        if dum.txj > 0:
            a = a + 1
            print('  铁胸甲★★*', dum.txj, '\t\t(', a, ')')
            listb = listb + ['铁胸甲★★']
        if dum.gxj > 0:
            a = a + 1
            print('  钢胸甲★★★*', dum.gxj, '\t\t(', a, ')')
            listb = listb + ['钢胸甲★★★']
        if dum.qclsj > 0:
            a = a + 1
            print('  七彩神龙甲★★★★★*', dum.qclsj, '\t\t(', a, ')')
            listb = listb + ['七彩神龙甲★★★★★']
        if a == 0:
            print('无')
        return listb

    def zbhjleg(self):
        global dum
        print('背包防具：')
        listb = []
        a = 0
        if dum.mtj > 0:
            a = a + 1
            print('  木腿甲★*', dum.mtj, '\t\t(', a, ')')
            listb = listb + ['木腿甲★']
        if dum.ttj > 0:
            a = a + 1
            print('  铁腿甲★★*', dum.ttj, '\t\t(', a, ')')
            listb = listb + ['铁腿甲★★']
        if dum.gtj > 0:
            a = a + 1
            print('  钢腿甲★★★*', dum.gtj, '\t\t(', a, ')')
            listb = listb + ['钢腿甲★★★']
        if a == 0:
            print('无')
        return listb

    def zbhjfoot(self):
        global dum
        print('背包防具：')
        listb = []
        a = 0
        print('无')

    def zbhh(self):
        print('魂环:')
        i = 0
        for a in self.listhh:
            i = i + 1
            print(a, '年(', i, ')')
        if i == 0:
            print('无')
        print('你的等级为:', self.dj, '最多可使用上限为', self.hhmax(), '年的魂环')

    def zb(self):
        ert = True
        print('装备列表(1) | 魂环列表(2) | 魂骨列表(3) | 魂灵列表(4) | 返回(5)')
        print('------------------------------------------------------------')
        sr = input('')
        if sr == '1':
            sr3 = 1
            while sr3 != '0' and sr3 != '':
                print('装备列表:')
                print('头:', self.zbhead, '\t\t(1)')
                print('胸:', self.zbxb, '\t\t(2)')
                print('腿:', self.zbleg, '\t\t(3)')
                print('脚:', self.zbfoot, '\t\t(4)')
                print('主手:', self.zszb, '\t(5)')
                print('副手:', self.fszb, '\t(6)')
                print('返回(0)')
                sr3 = input('')
                if sr3 == '1':
                    if self.zbhead == '无':
                        listb = self.zbhjhead()
                        sr = input()
                        try:
                            zb = listb[int(sr) - 1]
                            self.zbhead = zb
                            dum.zbpd(zb, 1)
                        except:
                            if sr != '':
                                print('输入有误!')
                                input()
                    else:
                        dum.zbpd(self.zbhead, -1)
                        self.zbhead = '无'
                        print('已卸下!')
                        input()
                elif sr3 == '2':
                    if self.zbxb == '无':
                        listb = self.zbhjxb()
                        sr = input()
                        try:
                            zb = listb[int(sr) - 1]
                            self.zbxb = zb
                            dum.zbpd(zb, 1)
                        except:
                            if sr != '':
                                print('输入有误!')
                                input()
                    else:
                        dum.zbpd(self.zbxb, -1)
                        self.zbxb = '无'
                        print('已卸下!')
                        input()
                elif sr3 == '3':
                    if self.zbleg == '无':
                        listb = self.zbhjleg()
                        sr = input()
                        try:
                            zb = listb[int(sr) - 1]
                            self.zbleg = zb
                            dum.zbpd(zb, 1)
                        except:
                            if sr != '':
                                print('输入有误!')
                                input()
                    else:
                        dum.zbpd(self.zbleg, -1)
                        self.zbleg = '无'
                        print('已卸下!')
                        input()
                elif sr3 == '4':
                    if self.zbfoot == '无':
                        listb = self.zbhjfoot()
                        sr = input()
                        try:
                            zb = listb[int(sr) - 1]
                            self.zbfoot = zb
                            dum.zbpd(zb, 1)
                        except:
                            if sr != '':
                                print('输入有误!')
                                input()
                    else:
                        dum.zbpd(self.zbfoot, -1)
                        self.zbfoot = '无'
                        print('已卸下!')
                        input()
                elif sr3 == '5':
                    if self.zszb == '无':
                        listb = self.zbwq()
                        sr = input()
                        try:
                            zb = listb[int(sr) - 1]
                            self.zszb = zb
                            dum.zbpd(zb, 1)
                        except:
                            if sr != '':
                                print('输入有误!')
                                input()
                    else:
                        dum.zbpd(self.zszb, -1)
                        self.zszb = '无'
                        print('已卸下!')
                        input()
                elif sr3 == '6':
                    if self.fszb == '无':
                        listb = self.zbwq()
                        sr = input()
                        try:
                            zb = listb[int(sr) - 1]
                            self.fszb = zb
                            dum.zbpd(zb, 1)
                        except:
                            if sr != '':
                                print('输入有误!')
                                input()
                    else:
                        dum.zbpd(self.fszb, -1)
                        self.fszb = '无'
                        print('已卸下!')
                        input()
                elif sr3 == '0' or sr3 == '':
                    pass
                else:
                    print('未开放!')
                    input()
        elif sr == '2':
            sr3 = 1
            while sr3 != '0' and sr3 != '':
                print('魂环列表:')
                print('一:', self.hh1, '' if self.hh1 == '无' else '年', '\t(1)')
                print('二:', self.hh2, '' if self.hh2 == '无' else '年', '\t(2)')
                print('三:', self.hh3, '' if self.hh3 == '无' else '年', '\t(3)')
                print('四:', self.hh4, '' if self.hh4 == '无' else '年', '\t(4)')
                print('五:', self.hh5, '' if self.hh5 == '无' else '年', '\t(5)')
                print('六:', self.hh6, '' if self.hh6 == '无' else '年', '\t(6)')
                print('七:', self.hh7, '' if self.hh7 == '无' else '年', '\t(7)')
                print('八:', self.hh8, '' if self.hh8 == '无' else '年', '\t(8)')
                print('九:', self.hh9, '' if self.hh9 == '无' else '年', '\t(9)')
                print('返回(0)')
                sr3 = input('')
                if sr3 == '1' and self.dj >= 10:
                    if self.hh1 == '无':
                        self.zbhh()
                        su = input('')
                        try:
                            hh = self.listhh[int(su) - 1]
                            self.listhh = TabMake.listdel(self.listhh, int(su))
                            self.zbhhpd(hh, 1, 1)
                            self.hh1 = hh
                        except:
                            if su != '':
                                print('输入有误!')
                                input()
                    else:
                        self.zbhhpd(self.hh1, 1, -1)
                        self.listhh = self.listhh + [self.hh1]
                        self.listhh = TabMake.px(self.listhh, sx=False)
                        self.hh1 = '无'
                        print('已卸下!')
                        input()
                elif sr3 == '2' and self.dj >= 20:
                    if self.hh2 == '无':
                        self.zbhh()
                        su = input('')
                        try:
                            hh = self.listhh[int(su) - 1]
                            self.listhh = TabMake.listdel(self.listhh, int(su))
                            self.zbhhpd(hh, 2, 1)
                            self.hh2 = hh
                        except:
                            if su != '':
                                print('输入有误!')
                                input()
                    else:
                        self.zbhhpd(self.hh2, 2, -1)
                        self.listhh = self.listhh + [self.hh2]
                        self.listhh = TabMake.px(self.listhh, sx=False)
                        self.hh2 = '无'
                        print('已卸下!')
                        input()
                elif sr3 == '3' and self.dj >= 30:
                    if self.hh3 == '无':
                        self.zbhh()
                        su = input('')
                        try:
                            hh = self.listhh[int(su) - 1]
                            self.listhh = TabMake.listdel(self.listhh, int(su))
                            self.zbhhpd(hh, 3, 1)
                            self.hh3 = hh
                        except:
                            if su != '':
                                print('输入有误!')
                                input()
                    else:
                        self.zbhhpd(self.hh3, 3, -1)
                        self.listhh = self.listhh + [self.hh3]
                        self.listhh = TabMake.px(self.listhh, sx=False)
                        self.hh3 = '无'
                        print('已卸下!')
                        input()
                elif sr3 == '4' and self.dj >= 40:
                    if self.hh4 == '无':
                        self.zbhh()
                        su = input('')
                        try:
                            hh = self.listhh[int(su) - 1]
                            self.listhh = TabMake.listdel(self.listhh, int(su))
                            self.zbhhpd(hh, 4, 1)
                            self.hh4 = hh
                        except:
                            if su != '':
                                print('输入有误!')
                                input()
                    else:
                        self.zbhhpd(self.hh4, 4, -1)
                        self.listhh = self.listhh + [self.hh4]
                        self.listhh = TabMake.px(self.listhh, sx=False)
                        self.hh4 = '无'
                        print('已卸下!')
                        input()
                elif sr3 == '5' and self.dj >= 50:
                    if self.hh5 == '无':
                        self.zbhh()
                        su = input('')
                        try:
                            hh = self.listhh[int(su) - 1]
                            self.listhh = TabMake.listdel(self.listhh, int(su))
                            self.zbhhpd(hh, 5, 1)
                            self.hh5 = hh
                        except:
                            if su != '':
                                print('输入有误!')
                                input()
                    else:
                        self.zbhhpd(self.hh5, 5, -1)
                        self.listhh = self.listhh + [self.hh5]
                        self.listhh = TabMake.px(self.listhh, sx=False)
                        self.hh5 = '无'
                        print('已卸下!')
                        input()
                elif sr3 == '6' and self.dj >= 60:
                    if self.hh6 == '无':
                        self.zbhh()
                        su = input('')
                        try:
                            hh = self.listhh[int(su) - 1]
                            self.listhh = TabMake.listdel(self.listhh, int(su))
                            self.zbhhpd(hh, 6, 1)
                            self.hh6 = hh
                        except:
                            if su != '':
                                print('输入有误!')
                                input()
                    else:
                        self.zbhhpd(self.hh6, 6, -1)
                        self.listhh = self.listhh + [self.hh6]
                        self.listhh = TabMake.px(self.listhh, sx=False)
                        self.hh6 = '无'
                        print('已卸下!')
                        input()
                elif sr3 == '7' and self.dj >= 70:
                    if self.hh7 == '无':
                        self.zbhh()
                        su = input('')
                        try:
                            hh = self.listhh[int(su) - 1]
                            self.listhh = TabMake.listdel(self.listhh, int(su))
                            self.zbhhpd(hh, 7, 1)
                            self.hh7 = hh
                        except:
                            if su != '':
                                print('输入有误!')
                                input()
                    else:
                        self.zbhhpd(self.hh7, 7, -1)
                        self.listhh = self.listhh + [self.hh7]
                        self.listhh = TabMake.px(self.listhh, sx=False)
                        self.hh7 = '无'
                        print('已卸下!')
                        input()
                elif sr3 == '8' and self.dj >= 80:
                    if self.hh8 == '无':
                        self.zbhh()
                        su = input('')
                        try:
                            hh = self.listhh[int(su) - 1]
                            self.listhh = TabMake.listdel(self.listhh, int(su))
                            self.zbhhpd(hh, 8, 1)
                            self.hh8 = hh
                        except:
                            if su != '':
                                print('输入有误!')
                                input()
                    else:
                        self.zbhhpd(self.hh8, 8, -1)
                        self.listhh = self.listhh + [self.hh8]
                        self.listhh = TabMake.px(self.listhh, sx=False)
                        self.hh8 = '无'
                        print('已卸下!')
                        input()
                elif sr3 == '9' and self.dj >= 90:
                    if self.hh9 == '无':
                        self.zbhh()
                        su = input('')
                        try:
                            hh = self.listhh[int(su) - 1]
                            self.listhh = TabMake.listdel(self.listhh, int(su))
                            self.zbhhpd(hh, 9, 1)
                            self.hh9 = hh
                        except:
                            if su != '':
                                print('输入有误!')
                                input()
                    else:
                        self.zbhhpd(self.hh9, 9, -1)
                        self.listhh = self.listhh + [self.hh9]
                        self.listhh = TabMake.px(self.listhh, sx=False)
                        self.hh9 = '无'
                        print('已卸下!')
                        input()
                elif sr3 == '0' or sr3 == '':
                    pass
                else:
                    print('未开放或等级不足!')
                    input()
        elif sr == '3':
            sr3 = 1
            while sr3 != '0' and sr3 != '':
                print('魂骨列表:')
                print('头部:', self.hgt, '\t(1)')
                print('躯干:', self.hgqg, '\t(2)')
                print('左臂:', self.hgzb, '\t(3)')
                print('右臂:', self.hgyb, '\t(4)')
                print('左腿:', self.hgzt, '\t(5)')
                print('右腿:', self.hgyt, '\t(6)')
                print('返回(0)')
                sr3 = input('')
                if sr3 != '' or sr3 != '0':
                    print('未开放或等级不足!')
                    input()
        elif sr == '4':
            sr3 = 1
            while sr3 != '0' and sr3 != '':
                print('魂灵列表:')
                print('一:', self.hl1, '\t(1)')
                print('二:', self.hl2, '\t(2)')
                print('三:', self.hl3, '\t(3)')
                print('四:', self.hl4, '\t(4)')
                print('五:', self.hl5, '\t(5)')
                print('六:', self.hl6, '\t(6)')
                print('七:', self.hl7, '\t(7)')
                print('八:', self.hl8, '\t(8)')
                print('九:', self.hl9, '\t(9)')
                print('返回(0)')
                sr3 = input('')
                if sr3 != '' or sr3 != '0':
                    print('未开放或等级不足!')
                    input()

        elif sr == '5' or sr == '':
            ert = False
        else:
            print('未开放或等级不足!')
            input()
        return ert

    # fb
    def fb(self):
        print('----------------------------历练----------------------------')
        print('落日森林:  外围(1) | 中间(2) | 核心(3)')
        print('龙虎山脉:  外围(4) | 中间(5) | 核心(6)')
        print('星斗大森林:外围(7) | 中间(8) | 核心(9)')
        print('返回(0)')
        sr3 = input()
        op = 1
        if (sr3 == '3' and self.dj >= 20) or (sr3 == '2' and self.dj >= 10) or (sr3 == '1' and self.dj >= 1):
            while op != '2':
                i = 0
                while i <= 100:
                    self.sunrise(mod=int(sr3))
                    i = i + 1
                op = input('按2退出:')
                self.sm = self.sm + 0.25
                self.timecy = self.timecy + 0.25
                self.new_time(mouth=3)
            return True
        elif sr3 == '0' or sr3 == '':
            return True
        else:
            print('未开放或等级不足!')
            input()
            return False

    def sunrise(self, mod):
        a = random.randint(0, 40000)
        blood = self.xl
        if mod >= 1:
            if a <= 2500:
                print('经验*1')
                self.xp = self.xp + 1
            elif 2500 < a <= 3000:
                print('经验*10')
                self.xp = self.xp + 10
            elif 3000 < a <= 3500:
                print('经验*100')
                self.xp = self.xp + 100
            elif 3500 < a <= 4000:
                print('获得“铁剑★”*1!')
                self.tj = self.tj + 1
            elif 4000 < a <= 4500:
                print('获得“木弓★”*1!')
                self.mg = self.mg + 1
            elif 4500 < a <= 4650:
                print('获得“铁矛★★”*1！')
                self.tm = self.tm + 1
            elif 4750 < a <= 4800:
                print('获得“钢剑★★”*1！')
                self.gj = self.gj + 1
            elif 4800 < a <= 5600:
                print('获得“木胸甲★”*1!')
                self.mxj = self.mxj + 1
            elif 5600 < a <= 5700:
                print('获得“木腿甲★”*1!')
                self.mtj = self.mtj + 1
            elif 8100 < a <= 10100:
                print('金钱*1')
                self.jq = self.jq + 1
            elif 10100 < a <= 12000:
                print('金钱*10')
                self.jq = self.jq + 10
            elif 12750 < a <= 13500:
                print('钻石*1')
                self.zs = self.zs + 1
            elif 13500 < a <= 13750:
                print('钻石*10')
                self.zs = self.zs + 10
            elif a == 13751:
                print('获得“CR神器★★★★★”*1!')
                input('')
                self.crsq = self.crsq + 1
            elif 13752 < a <= 14000:
                print('获得"匕首★"*1！')
                self.bs = self.bs + 1
            elif 14000 < a <= 14200:
                print('获得“杀猪刀★★★”*1!')
                self.szd = self.szd + 1
            elif 14200 < a <= 15500:
                print('获得“屎★”*1!')
                self.s = self.s + 1
            elif 15500 < a <= 16500:
                print('获得"树枝★"*1!')
                self.shz = self.shz + 1
            elif 16500 < a <= 17500:
                print('获得"石头★"*1!')
                self.st = self.st + 1
            elif 17500 < a <= 18500:
                print('获得"橡木★"*1!')
                self.xm = self.xm + 1
            elif 18500 < a <= 20000:
                print('获得"线★"*1!')
                self.xian += 1
            elif 20000 < a <= 20500:
                print('战斗中受伤,血量-5')

        if mod >= 2:
            if 20500 < a <= 21500:
                print('经验*200')
                self.xp = self.xp + 200
            elif 21500 < a <= 22000:
                print('获得“AK-47★★★”*1!')
                self.ak47 = self.ak47 + 1
            elif 22000 < a <= 23000:
                print('获得“铁胸甲★★”*1!')
                self.txj = self.txj + 1
            elif 23000 < a <= 24000:
                print('获得“铁腿甲★★”*1!')
                self.ttj = self.ttj + 1
            elif 24000 < a <= 25000:
                print('金钱*100')
                self.jq = self.jq + 100
            elif 25000 < a <= 25500:
                print('金钱*500')
                self.jq = self.jq + 500
            elif a == 25501:
                print('获得"死亡笔记★★★★★"*1!')
                input('')
                self.swbj = self.swbj + 1
            elif 26500 < a <= 27500:
                print('获得"蒙德拉贡★★"*1！')
                self.mdlg = self.mdlg + 1
            elif 28500 < a <= 29500:
                print('获得"果木★★"*1!')
                self.gm = self.gm + 1
            elif 29500 < a <= 30500:
                print('获得"皮革★★"*1!')
                self.pg = self.pg + 1
            elif 30500 < a <= 31500:
                print('获得"铁块★★"*1!')
                self.cltk = self.cltk + 1
            elif 31500 < a <= 32500:
                print('获得"螺钉★★"*1!')
                self.ls = self.ls + 1
        if mod == 3:
            if 32500 < a <= 33000:
                print('经验*500')
                self.xp = self.xp + 500
            elif 33000 < a <= 33500:
                print('经验*1000')
                self.xp = self.xp + 1000
            elif 33500 < a <= 34000:
                print('获得"UNP9★★★"*1!')
                self.nup9 = self.unp9 + 1
            elif a == 34501:
                print('获得"龙鳞剑★★★★★"*1!')
                input('')
                self.llj = self.llj + 1
            elif 34501 < a <= 35000:
                print('获得“铁丝棒球棍★★★”*1!')
                self.tsbq = self.tsbq + 1
            elif 35000 < a <= 35500:
                print('获得“武士刀★★★”*1!')
                self.wsd = self.wsd + 1
            elif 35500 < a <= 36000:
                print('获得“桃木★★★”*1!')
                self.tm = self.tm + 1
            elif 36000 < a <= 36500:
                print('获得“呢绒布★★★”*1!')
                self.nrb = self.nrb + 1
            elif 36500 < a <= 37000:
                print('获得“钢块★★★”*1!')
                self.gk = self.gk + 1
            elif 37000 < a <= 37500:
                print('获得“树脂★★★”*1!')
                self.szh = self.szh + 1
            elif 37500 < a <= 38000:
                print('获得“[无名刀]木偶★★★”*1!')
                self.mo = self.mo + 1
            elif 38000 < a <= 38500:
                print('获得“麒麟臂★★★★”*1!')
                self.qlb = self.qlb + 1
            elif 38500 < a <= 39000:
                print('获得“AK-74★★★★”*1!')
                self.ak74 = self.ak74 + 1
            elif 39000 < a <= 39500:
                print('获得“M4★★★★”*1!')
                self.m4 = self.m4 + 1

    #
    def bag_zb(self):
        global dum
        print('装备：')
        if dum.s > 0:
            print('  屎★*', dum.s)
        if dum.tj > 0:
            print('  铁剑★*', dum.tj)
        if dum.bs > 0:
            print('  匕首★*', dum.bs)
        if dum.mg > 0:
            print('  木弓★*', dum.mg)
        if dum.tm > 0:
            print('  铁矛★★*', dum.tm)
        if dum.gj > 0:
            print('  钢剑★★*', dum.gj)
        if dum.mdlg > 0:
            print('  蒙德拉贡★★*', dum.mdlg)
        if dum.ak47 > 0:
            print('  AK-47★★★*', dum.ak47)
        if dum.uzi > 0:
            print('  UZI★★★*', dum.uzi)
        if dum.unp9 > 0:
            print('  UNP9★★★*', dum.unp9)
        if dum.szd > 0:
            print('  杀猪刀★★★*', dum.szd)
        if dum.zd > 0:
            print('  爪刀★★★*', dum.zd)
        if dum.tsbq > 0:
            print('  铁丝棒球棍★★★*', dum.tsbq)
        if dum.wsd > 0:
            print('  武士刀★★★*', dum.wsd)
        if dum.mo > 0:
            print('  [无名刀]木偶★★★*', dum.mo)
        if dum.tieg > 0:
            print('  铁弓★★★*', dum.tieg)
        if dum.qlb > 0:
            print('  麒麟臂★★★★*', dum.qlb)
        if dum.ak74 > 0:
            print('  AK-74★★★★*', dum.ak74)
        if dum.m4 > 0:
            print('  M4★★★★*', dum.m4)
        if dum.bsba > 0:
            print('  匕首(β-钛合金)★★★★*', dum.bsba)
        if dum.yj > 0:
            print('  YJ★★★★*', dum.yj)
        if dum.fhg > 0:
            print('  复合弓★★★★*', dum.fhg)
        if dum.kar98 > 0:
            print('  Kar98★★★★*', dum.kar98)
        if dum.my > 0:
            print('  [妖刀]芈月★★★★★*', dum.my)
        if dum.ak12 > 0:
            print('  AK-12★★★★★*', dum.ak12)
        if dum.m416 > 0:
            print('  M416★★★★★*', dum.m416)
        if dum.m82a1 > 0:
            print('  M82A1★★★★★*', dum.m82a1)
        if dum.aug > 0:
            print('  AUG★★★★★*', dum.aug)
        if dum.rpg > 0:
            print('  RPG★★★★★*', dum.rpg)
        if dum.xlzz > 0:
            print('  凶霖之爪★★★★★*', dum.xlzz)
        if dum.swbj > 0:
            print('  死亡笔记★★★★★*', dum.swbj)
        if dum.llj > 0:
            print('  龙鳞剑★★★★★*', dum.llj)
        if dum.szyj > 0:
            print('  神之YJ★★★★★*', dum.szyj)
        if dum.crsq > 0:
            print('  CR神器★★★★★*', dum.crsq)
        if dum.ygc > 0:
            print('  愚公铲★★★★★*', dum.ygc)
        if dum.gylq > 0:
            print('  光焰龙枪★★★★★*', dum.gylq)
        if dum.mxj > 0:
            print('  木胸甲★*', dum.mxj)
        if dum.mtj > 0:
            print('  木腿甲★*', dum.mtj)
        if dum.txj > 0:
            print('  铁胸甲★★*', dum.txj)
        if dum.ttj > 0:
            print('  铁腿甲★★*', dum.ttj)
        if dum.gxj > 0:
            print('  钢胸甲★★★*', dum.gxj)
        if dum.gtj > 0:
            print('  钢腿甲★★★*', dum.gtj)
        if dum.qclsj > 0:
            print('  七彩神龙甲★★★★★*', dum.qclsj)

    def bag_cl(self):
        global dum
        print('材料：')
        if dum.shz > 0:
            print('  树枝★*', dum.shz)
        if dum.clmg > 0:
            print('  木棍★*', dum.clmg)
        if dum.st > 0:
            print('  石头★*', dum.st)
        if dum.xm > 0:
            print('  橡木★*', dum.xm)
        if dum.mt > 0:
            print('  木炭★★*', dum.mt)
        if dum.gm > 0:
            print('  果木★★*', dum.gm)
        if dum.pg > 0:
            print('  皮革★★*', dum.pg)
        if dum.cltk > 0:
            print('  铁块★★*', dum.cltk)
        if dum.ls > 0:
            print('  螺钉★★*', dum.ls)
        if dum.taom > 0:
            print('  桃木★★★*', dum.taom)
        if dum.nrb > 0:
            print('  呢绒布★★★*', dum.nrb)
        if dum.gk > 0:
            print('  钢块★★★*', dum.gk)
        if dum.szh > 0:
            print('  树脂★★★*', dum.szh)
        if dum.bm > 0:
            print('  柏木★★★★*', dum.bm)
        if dum.wfb > 0:
            print('  无纺布★★★★*', dum.wfb)
        if dum.lhj > 0:
            print('  铝合金★★★★*', dum.lhj)
        if dum.nam > 0:
            print('  楠木★★★★★*', dum.nam)
        if dum.thj > 0:
            print('  钛合金★★★★★*', dum.thj)
        if dum.gfz > 0:
            print('  高分子材料★★★★★*', dum.gfz)
        if dum.gcsl > 0:
            print('  工程塑料★★★★★*', dum.gcsl)

    def bag_hh(self):
        print('魂环:')
        for i in self.listhh:
            print(i, '年')

    def bag_hg(self):
        print('魂骨:')
        for i in self.listhg:
            print(i)

    # information
    def information(self):
        self.jqzsset()
        self.wgmgset()
        self.jysxset()
        a = '\t'
        t = '\t\t'
        if self.xb == '女' and self.yz <= 11:
            a = '\t\t'
        if len(str(self.zhzlshow)) >= 6 and ('万' not in str(self.zhzlshow) or '亿' not in str(self.zhzlshow)):
            t = '\t'
        elif ('万' in str(self.zhzlshow) or '亿' in str(self.zhzlshow)) and len(str(self.zhzlshow)) >= 5:
            t = '\t'
        print('姓名：', self.name, '\t\t 种族:', self.zz)
        print('性别:', self.xb, '\t\t 年龄:', int(round(self.sm, 0)), '岁/', self.cmsx, '岁')
        print('颜值:', self.yz, '(', self.yzxr, ') ' + a + '宗门：', self.zm)
        print('魂力:', self.djxr, '(', self.dj, '/', (self.dj // 10) * 10 + 10, ')(', self.jyshow, '/', self.sxshow,
              ')')
        print('精神力:', self.jslxr, '(', self.jslshow, '/', self.jslsx, ')')
        print('魂核：', self.soul_core_des, '(', self.soul_coreshow, '/', self.soul_coresxshow, ')')
        print('等级:', self.levelshow, '(', self.xpshow, '/', self.levelsxshow, ')')
        print('综合战力:', self.zhzlshow, t, '血量：', self.xlshow)
        print('物攻：', self.wgshow, '\t\t 魔攻：', self.jg_mgshow)
        print('物防：', self.wfshow, '\t\t 魔防：', self.mfshow)
        print('金钱($):', self.jqshow, '\t\t 钻石(&):', self.zsshow)
        print('宗门贡献(@):', self.plgxshow, '\t\t 比武场获胜次数：', self.slcs)
        print('段位:', self.dy, '\t\t 知名度:', str(self.famous) + '(' + self.famousxr + ')')
        if self.dj >= 10:
            print('魂环上限:', self.hhmax(), '年')

    # start
    def start(self):
        # 初始化
        global inal
        print(inal, '爽文修真', inal)
        print(' -' + inal, '正式', '-' + inal)
        print('\n')
        print('"呯！！！"')
        print('公元', self.timey, '年，随着一声巨响你穿越到了CR大陆...')
        print('\n')
        print('你意外获得了系统')
        print('开启了修仙之路...')
        print('\n')
        if self.name != 'Debuger':
            nm = str(input('你的名字(随机:(sj))：'))
            if nm == 'sj':
                name = MUD.random_name()
                self.name = name
            else:
                self.name = nm
        print('')
        print('你的名字:', self.name)
        print('')
        if self.xb != '2':
            print('性别:男(1) | 女(2)')
            xb = str(input(':'))
            if xb == '114514':
                self.name = '野兽先辈'
                print('由于你的性别是114514，你的名字被强制改为', self.name)
                input()
            yz, yzxr, xb = MUD.random_yz(xb)
            self.yz = yz
            self.yzxr = yzxr
            self.xb = xb
        self.zz = '人族'
        print('正在创建系统...')
        print('正在创建背包...')
        self.xl = random.randint(80, 150)
        self.real_xl = self.xl
        self.wg = random.randint(5, 13)
        self.gj_mg = random.randint(1, 7)
        self.wf = random.randint(4, 12)
        self.mf = random.randint(0, 6)
        self.zhzl = int(round((self.xl + self.wg + self.gj_mg + self.wf + self.mf) * (self.yz * 0.8), 0))
        print('正在创建世界...')
        print('正在创建人物...')
        print('-恭喜开局获得“铁剑★”')
        self.tj = 1
        self.sd = '10'
        self.qwe = 1
        self.zb1 = 1
        self.timecy = 0
        self.cltime = self.timey * 360 + self.timem * 30 + self.timed
        self.jsl = random.randint(1, 30)
        self.jy = random.randint(0, 728)
        self.date = 0
        self.famous = random.randint(1, 25)

        if self.xb == '114514':
            self.sxxs = 114514

    # xl
    def xlhl(self):
        print('修炼魂力:')
        print('当前修炼速度:', self.dj, '经验/时')
        print('当前魂力:', self.djxr, '(', self.dj, '/', (self.dj // 10) * 10 + 10, ')(', self.jyshow, '/', self.sxshow,
              ')')
        print('年龄：', int(round(self.sm, 0)), '/', self.cmsx)
        a = self.cmsx - self.sm
        print('以目前年龄上限最多可修炼:', int((a * 12) // 1), '月/', int((a * 360) // 1), '天/',
              int((a * 103680) // 1), '时')
        print('请输入修炼天数:')
        xltimeh = input('时:')
        xltimed = input('日:')
        xltimem = input('月:')
        try:
            if xltimed == '':
                xltimed = 0
            if xltimem == '':
                xltimem = 0
            if xltimeh == '':
                xltimeh = 0
            xltimed = MUD.jdz(int(round(float(xltimed), 0)))
            xltimem = MUD.jdz(int(round(float(xltimem), 0)))
            xltimeh = MUD.jdz(int(round(float(xltimeh), 0)))
            print('闭关:', xltimem, '月', xltimed, '日', xltimeh, '时')
            sr = input('返回请按2:')
            if sr != '2':
                self.new_time(xltimed, xltimem, 0, xltimeh)
                xltimez = xltimeh + (24 * xltimed) + (720 * xltimem)
                self.jy = self.jy + (self.dj * xltimez)
                print('经验+', self.dj * xltimez)
                input('')
        except:
            print('输入错误!')
            input('')

    def xlhh(self):
        s = int(round(self.soul_core ** 0.25, 0))
        print('修炼魂核:')
        print('当前修炼速度:', s, '经验/时')
        print('当前魂核：', self.soul_core_des, '(', self.soul_coreshow, '/', self.soul_coresxshow, ')')
        print('年龄：', int(round(self.sm, 0)), '/', self.cmsx)
        a = self.cmsx - self.sm
        print('以目前年龄上限最多可修炼:', int((a * 12) // 1), '月/', int((a * 360) // 1), '天/',
              int((a * 103680) // 1), '时')
        print('请输入修炼天数:')
        xltimeh = input('时:')
        xltimed = input('日:')
        xltimem = input('月:')
        try:
            if xltimed == '':
                xltimed = 0
            if xltimem == '':
                xltimem = 0
            if xltimeh == '':
                xltimeh = 0
            xltimed = MUD.jdz(int(round(float(xltimed), 0)))
            xltimem = MUD.jdz(int(round(float(xltimem), 0)))
            xltimeh = MUD.jdz(int(round(float(xltimeh), 0)))
            print('闭关:', xltimem, '月', xltimed, '日', xltimeh, '时')
            sr = input('返回请按2:')
            if sr != '2':
                self.new_time(xltimed, xltimem, 0, xltimeh)
                xltimez = xltimeh + (24 * xltimed) + (720 * xltimem)
                self.soul_core = self.soul_core + (s * xltimez)
                print('经验+', s * xltimez)
                input('')
        except:
            print('输入错误!')
            input('')

    def xljsl(self):
        s = int(round(self.jsl ** 0.25, 0))
        print('修炼精神力:')
        print('当前修炼速度:', s, '精神力/时')
        print('当前精神力：', self.jslxr, '(', self.jslshow, '/', self.jslsx, ')')
        print('年龄：', int(round(self.sm, 0)), '/', self.cmsx)
        a = self.cmsx - self.sm
        print('以目前年龄上限最多可修炼:', int((a * 12) // 1), '月/', int((a * 360) // 1), '天/',
              int((a * 103680) // 1), '时')
        print('请输入修炼天数:')
        xltimeh = input('时:')
        xltimed = input('日:')
        xltimem = input('月:')
        try:
            if xltimed == '':
                xltimed = 0
            if xltimem == '':
                xltimem = 0
            if xltimeh == '':
                xltimeh = 0
            xltimed = MUD.jdz(int(round(float(xltimed), 0)))
            xltimem = MUD.jdz(int(round(float(xltimem), 0)))
            xltimeh = MUD.jdz(int(round(float(xltimeh), 0)))
            print('闭关:', xltimem, '月', xltimed, '日', xltimeh, '时')
            sr = input('返回请按2:')
            if sr != '2':
                self.new_time(xltimed, xltimem, 0, xltimeh)
                xltimez = xltimeh + (24 * xltimed) + (720 * xltimem)
                self.jsl = self.jsl + (s * xltimez)
                print('精神力+', s * xltimez)
                input('')
        except:
            print('输入错误!')
            input('')

    def bj(self):
        if self.dj < 70:
            self.xlhl()
        else:
            while 1:
                print('修炼魂力(1) | 修炼魂核(2) | 修炼精神力(3)| 返回(4)')
                u = input('')
                if u == '1':
                    self.xlhl()
                elif u == '2':
                    self.xlhh()
                elif u == '3':
                    self.xljsl()
                elif u == '4' or u == '':
                    break
                else:
                    print('未开放!')
                    input()

    # sz
    def number_of_Chinese(word):
        i = 0
        for ch in word:
            if '\u4e00' <= ch <= '\u9fff':
                i = i + 1
        return i

    def is_Chinese(word):
        for ch in word:
            if '\u4e00' <= ch <= '\u9fff' or ch == '★':
                return True
        return False

    def is_English(word):
        my_re = re.compile(r'[A-Za-z]', re.S)
        res = re.findall(my_re, word)
        if len(res):
            return True
        else:
            return False

    def mep(str1):
        listT = []
        listR = []
        a = ''
        ch = False
        dh = False
        for i in str1:
            if i == '\n':
                if ch == True:
                    a = a + '"'
                listT = listT + [a]
                a = ''
                ch = False
                dh = False
            else:
                if i == '=':
                    dh = True
                if dh == True:
                    if MUD.is_Chinese(i) == True or MUD.is_English(i) == True:
                        if ch == False:
                            a = a + '"' + i
                            ch = True
                        else:
                            a = a + i
                    else:
                        a = a + i
                else:
                    a = a + i
        listT = listT + [a]
        for i in listT:
            if i != '':
                listR = listR + [i]
        return listR

    def mop(str1):
        listT = []
        listR = []
        a = ''
        ch = False
        dh = False
        for i in str1:
            if i == ' ' or i == '\n' or i == '\t' or i == ',' or i == '?' or i == '!' or i == ':':
                if ch == True:
                    a = a + '"'
                listT = listT + [a]
                a = ''
                ch = False
                dh = False
            else:
                if i == '=':
                    dh = True
                if dh == True:
                    if MUD.is_Chinese(i) == True or MUD.is_English(i) == True:
                        if ch == False:
                            a = a + '"' + i
                            ch = True
                        else:
                            a = a + i
                    else:
                        if ch == True:
                            a = a + i + '"'
                            ch = False
                        else:
                            a = a + i
                else:
                    a = a + i
        listT = listT + [a]
        for i in listT:
            if i != '':
                listR = listR + [i]
        return listR

    def listdeef(list1, list2):
        listT = []
        for i in list1:
            if i not in list2:
                listT = listT + [i]
        return listT

    def chongzhi():
        global dum
        print('确定重置存档?')
        print('是(1) | 否(2)')
        su = input('')
        if su == '1':
            MUD.import_save()
            dum = MUD()
            dum.start()

    def varhelp(b='\n'):
        global dum
        a = ''
        listall = MUD.listdeef(dir(dum), dir(MUD))
        for i in listall:
            a = a + 'dum.' + i + '=' + str(eval('dum.' + i)) + b
        print(a)

    def zsgg(self):
        global dum
        global cv
        running = True
        while running:
            clean_up()
            print('----------------------------设置----------------------------')
            print('颜色(1) | 命令(2) | 关于(3) | 返回(4)')
            sr = input('')
            if sr == '1':
                print('默认模式(1) | 修仙模式(2) | 爽文模式(3) | 夜间模式(4)')
                sr2 = str(input(':'))
                if sr2 == '1':
                    self.yc = 'color F1'
                    print('-默认模式已开启!')
                elif sr2 == '2':
                    self.yc = 'color 1F'
                    print('-修仙模式已开启!')
                elif sr2 == '3':
                    self.yc = 'color F0'
                    print('-爽文模式已开启!')
                elif sr2 == '4':
                    self.yc = 'color 0F'
                    print('-夜间模式已开启!')
            elif sr == '2':
                print('命令系统不稳定请慎用,可能导致游戏闪退或无响应!')
                print('       ^^^^^^                 ^^^^ ^^^^^^')
                print('修改变量时要在前方加上"dum."!')
                command = input('请输入命令:')
                try:
                    try:
                        if command == 'varhelp()':
                            print('所有可更改变量:')
                            MUD.varhelp()
                            print('部分变量受算法关联可能更改无效!')
                            print('其中中文或英文为str型,请在更改时以以上相应类型输入,否则后果自负!')
                        elif command == 'chongzhi()':
                            MUD.chongzhi()
                        elif command == 'help()':
                            print('函数列表:')
                            print('varhelp()')
                            print('chongzhi()')
                            print('save()')
                        elif command == 'save()':
                            dum.save_save()
                        else:
                            print(eval(command))
                    except SyntaxError or TypeError:
                        exec(command)
                        print('已更改!')
                    except:
                        print('找不到', command, '的命令或命令格式错误!')
                except:
                    print('         ', len(MUD.mop(command)[0]) * '^', '(此处)')
                    print('找不到', MUD.mop(command)[0], '的命令或命令格式错误!')
                try:
                    dum.yzpd(dum.yz, dum.xb)
                except:
                    print('变量名中出现未知错误!')
                input()
            elif sr == '3':
                print('关于:')
                print('爽文修真v1.0.6正式版')
                print('存档版本:', dum.var)
                print('存档名称:', dum.save_name)
                print('存档路径:', cv + '\\' + dum.save_name + '.json')
                print('版本说明:')
                print('现已开放存档功能!')
                print('修复了一些bug')
                print('优化了显示和输入')
                input()
            elif sr == '4' or sr == '':
                running = False
            else:
                print('未开放!')
                input()

    # others
    def smpd(self):
        global running
        global listyy
        global cv
        global save_number
        global color
        self.date = self.timey * 360 + self.timem * 30 + self.timed - self.cltime
        self.sm = round(self.date / 360, 4) + 14
        if self.sm > self.cmsx or self.living == False:
            self.living = False
            self.sm = min(self.sm, self.cmsx)
            print('九泉之下，众生平等')
            print('你死了')
            yy = input('说点遗言吧:')
            print('是否下葬?')
            print('是(1) | 否(2)')
            b = input(':')
            if b == '1':
                b = '已下葬'
            elif b == '2':
                b = '未下葬'
            else:
                b = '未知'
            a = str(self.name) + '\t享年:' + str(self.sm) + '\\' + str(self.cmsx) + '岁\t' + str(self.djxr) + '(' + str(
                self.dj) + ')\t遗言:' + str(yy) + '\t' + b
            listyy = listyy + [a]
            running = False
            with open(loc + '\\MUD_SAVE.json', 'w') as f_load:
                json.dump([cv, save_number, color, listyy], f_load)
            try:
                os.remove(cv + '\\' + str(self.save_name) + '.json')
            except:
                pass

    # shop
    def shoppd_tjp(self, sr):
        global dum
        jg = 0
        if sr == '1':
            jg = 3000
        elif sr == '2':
            jg = 5000
        elif sr == '3':
            jg = 4000
        elif sr == '4':
            jg = 4000
        elif sr == '5':
            jg = 6000
        elif sr == '6':
            jg = 6000
        elif sr == '7':
            jg = 7000
        elif sr == '8':
            jg = 8000
        elif sr == '9':
            jg = 10000
        elif sr == '10':
            jg = 12000
        elif sr == '11':
            jg = 20000
        elif sr == '12':
            jg = 30000
        elif sr == '13':
            jg = 50000
        elif sr == '14':
            jg = 120000
        elif sr == '15':
            jg = 8000
        elif sr == '16':
            jy = 7500
        else:
            jg = 0.1
        if jg != 0.1 and self.jq - jg >= 0:
            if self.jq != '---':
                self.jq = self.jq - jg
            print('购买成功!')
            dum.new_time(0, 0, 0, 0, 10)
            if sr == '1':
                dum.szd = dum.szd + 1
            elif sr == '2':
                dum.ak47 = dum.ak47 + 1
            elif sr == '3':
                dum.uzi = dum.uzi + 1
            elif sr == '4':
                dum.zd = dum.zd + 1
            elif sr == '5':
                dum.tsbq = dum.tsbq + 1
            elif sr == '6':
                dum.wsd = dum.wsd + 1
            elif sr == '7':
                dum.mo = dum.mo + 1
            elif sr == '8':
                dum.qlb = dum.qlb + 1
            elif sr == '9':
                dum.ak74 = dum.ak74 + 1
            elif sr == '10':
                dum.m4 = dum.m4 + 1
            elif sr == '11':
                dum.yj = dum.yj + 1
            elif sr == '12':
                dum.kar98 = dum.kar98 + 1
            elif sr == '13':
                dum.my = dum.my + 1
            elif sr == '14':
                dum.rpg = dum.rpg + 1
            elif sr == '15':
                dum.gxj = dum.gxj + 1
            elif sr == '16':
                dum.gtj = dum.gtj + 1
        else:
            print('购买失败!')

    def shoppd_zyt(self, sr):
        global dum
        jg = 0
        if sr == '1':
            jg = 1000
        elif sr == '2':
            jg = 5000
        elif sr == '3':
            jg = 10000
        elif sr == '4':
            jg = 20000
        elif sr == '5':
            jg = 40000
        elif sr == '6':
            jg = 80000
        elif sr == '7':
            jg = 100000
        elif sr == '8':
            jg = 150000
        elif sr == '9':
            jg = 200000
        elif sr == '10':
            jg = 10000000
        elif sr == '11':
            jg = 10000000
        elif sr == '12':
            jg = 1000000000
        else:
            jg = 0.1
        if jg != 0.1 and self.jq - jg >= 0:
            if self.jq != '---':
                self.jq = self.jq - jg
            print('购买成功!')
            dum.new_time(0, 0, 0, 0, 10)
            if sr == '1':
                print('  经验+1000')
                dum.jy = dum.jy + 1000
            elif sr == '2':
                print('  经验+6000')
                dum.jy = dum.jy + 6000
            elif sr == '3':
                print('  经验+14000')
                dum.jy = dum.jy + 14000
            elif sr == '4':
                print('  经验+30000')
                dum.jy = dum.jy + 30000
            elif sr == '5':
                print('  经验+48000')
                dum.jy = dum.jy + 48000
            elif sr == '6':
                print('  经验+70000')
                dum.jy = dum.jy + 70000
            elif sr == '7':
                print('  经验+300000')
                dum.jy = dum.jy + 300000
            elif sr == '8':
                print('  经验+400000')
                dum.jy = dum.jy + 4000000
            elif sr == '9':
                print('  经验+1000000')
                dum.jy = dum.jy + 1000000
            elif sr == '10':
                print('  寿命+1000年')
                dum.cmsx = dum.cmsx + 1000
            elif sr == '11':
                print('  你已重返18岁')
                dum.sm = 18
            elif sr == '12':
                print('...')
                dum.jy = 1000000
        else:
            print('购买失败!')

    def shoppd_clt(self, sr):
        global dum
        jg = 0
        if sr == '1':
            jg = 100
        elif sr == '2':
            jg = 1000
        elif sr == '3':
            jg = 10000
        elif sr == '4':
            jg = 50000
        elif sr == '5':
            jg = 100000
        else:
            jg = 0.1
        if jg != 0.1 and self.jq - jg >= 0:
            if self.jq != '---':
                self.jq = self.jq - jg
            print('购买成功!')
            dum.new_time(0, 0, 0, 0, 20)
            if sr == '1':
                year = random.randint(10, 99)
                dum.listhh = dum.listhh + [year]
                print('获得魂环(', year, '年)！')
            elif sr == '2':
                year = random.randint(100, 999)
                dum.listhh = dum.listhh + [year]
                print('获得魂环(', year, '年)！')
            elif sr == '3':
                year = random.randint(1000, 9999)
                dum.listhh = dum.listhh + [year]
                print('获得魂环(', year, '年)！')
            elif sr == '4':
                year = random.randint(10000, 49999)
                dum.listhh = dum.listhh + [year]
                print('获得魂环(', year, '年)！')
            elif sr == '5':
                year = random.randint(50000, 99999)
                dum.listhh = dum.listhh + [year]
                print('获得魂环(', year, '年)！')
        else:
            print('购买失败!')

    def shoppd_zs(self):
        if self.zs - 100 >= 0:
            if self.zs != '---':
                self.zs = self.zs - 100
            print('兑换成功！')
            print('金钱+10000')
            dum.new_time(0, 0, 0, 0, 10)
            self.jq = self.jq + 10000
        else:
            print('购买失败!')

    def shoppd_hsz(self, name, sr):
        try:
            exec('self.' + name + '=self.' + name + '-1')
            if name == 's':
                self.jq = self.jq + 1
            elif name == 'tj':
                self.jq = self.jq + 20
            elif name == 'mg':
                self.jq = self.jq + 30
            elif name == 'tm':
                self.jq = self.jq + 200
            elif name == 'gj':
                self.jq = self.jq + 200
            elif name == 'mdlg':
                self.jq = self.jq + 500
            elif name == 'ak47':
                self.jq = self.jq + 3000
            elif name == 'szd':
                self.jq = self.jq + 2000
            elif name == 'uzi':
                self.jq = self.jq + 2500
            elif name == 'tieg':
                self.jq += 5000
            elif name == 'fhg':
                self.jq += 20000
            elif name == 'unp9':
                self.jq = self.jq + 2500
            elif name == 'zd':
                self.jq = self.jq + 2500
            elif name == 'tsbq':
                self.jq = self.jq + 2500
            elif name == 'wsd':
                self.jq = self.jq + 5000
            elif name == 'mo':
                self.jq = self.jq + 5500
            elif name == 'qlb':
                self.jq = self.jq + 7000
            elif name == 'ak74':
                self.jq = self.jq + 9000
            elif name == 'm4':
                self.jq = self.jq + 10000
            elif name == 'bsba':
                self.jq = self.jq + 12000
            elif name == 'yj':
                self.jq = self.jq + 20000
            elif name == 'kar98':
                self.jq = self.jq + 25000
            elif name == 'my':
                self.jq = self.jq + 48000
            elif name == 'ak12':
                self.jq = self.jq + 70000
            elif name == 'm416':
                self.jq = self.jq + 80000
            elif name == 'm82a1':
                self.jq = self.jq + 120000
            elif name == 'aug':
                self.jq = self.jq + 95000
            elif name == 'rpg':
                self.jq = self.jq + 100000
            elif name == 'xlzz':
                self.jq = self.jq + 160000
            elif name == 'swbj':
                self.jq = self.jq + 500000
            elif name == 'llj':
                self.jq = self.jq + 400000
            elif name == 'szyj':
                self.jq = self.jq + 1000000
            elif name == 'ygc':
                self.jq = self.jq + 120000
            elif name == 'gylq':
                self.jq = self.jq + 800000
            elif name == 'mxj':
                self.jq = self.jq + 60
            elif name == 'txj':
                self.jq = self.jq + 600
            elif name == 'gxj':
                self.jq = self.jq + 6000
            elif name == 'mtj':
                self.jq = self.jq + 55
            elif name == 'ttj':
                self.jq = self.jq + 550
            elif name == 'gtj':
                self.jq = self.jq + 5500
            else:
                print('输入错误!')
                input()
        except TypeError:
            year = self.listhh[sr - 1]
            self.jq = self.jq + year
            self.listhh = TabMake.listdel(self.listhh, sr)
        except:
            print('输入错误!')
            input()

    def hs(self):
        global dum
        print('背包武器：')
        listb = []
        a = 0
        if dum.s > 0:
            a = a + 1
            print('  屎★*', dum.s, '\t\t1$(', a, ')')
            listb = listb + ['s']
        if dum.tj > 0:
            a = a + 1
            print('  铁剑★*', dum.tj, '\t\t20$(', a, ')')
            listb = listb + ['tj']
        if dum.bs > 0:
            a = a + 1
            print('  匕首★*', dum.bs, '\t\t20$(', a, ')')
            listb = listb + ['bs']
        if dum.mg > 0:
            a = a + 1
            print('  木弓★*', dum.mg, '\t\t30$(', a, ')')
            listb = listb + ['mg']
        if dum.tm > 0:
            a = a + 1
            print('  铁矛★★*', dum.tm, '\t\t200$(', a, ')')
            listb = listb + ['tm']
        if dum.gj > 0:
            a = a + 1
            print('  钢剑★★*', dum.gj, '\t\t200$(', a, ')')
            listb = listb + ['gj']
        if dum.mdlg > 0:
            a = a + 1
            print('  蒙德拉贡★★*', dum.mdlg, '\t500$(', a, ')')
            listb = listb + ['mdlg']
        if dum.ak47 > 0:
            a = a + 1
            print('  AK-47★★★*', dum.ak47, '\t3000$(', a, ')')
            listb = listb + ['ak47']
        if dum.uzi > 0:
            a = a + 1
            print('  UZI★★★*', dum.uzi, '\t2500$(', a, ')')
            listb = listb + ['uzi']
        if dum.unp9 > 0:
            a = a + 1
            print('  UNP9★★★*', dum.unp9, '\t2500$(', a, ')')
            listb = listb + ['unp9']
        if dum.szd > 0:
            a = a + 1
            print('  杀猪刀★★★*', dum.szd, '\t2000$(', a, ')')
            listb = listb + ['szd']
        if dum.zd > 0:
            a = a + 1
            print('  爪刀★★★*', dum.zd, '\t\t2500$(', a, ')')
            listb = listb + ['zd']
        if dum.tsbq > 0:
            a = a + 1
            print('  铁丝棒球棍★★★*', dum.tsbq, '\t2500$(', a, ')')
            listb = listb + ['tsbq']
        if dum.wsd > 0:
            a = a + 1
            print('  武士刀★★★*', dum.wsd, '\t5000$(', a, ')')
            listb = listb + ['wsd']
        if dum.mo > 0:
            a = a + 1
            print('  [无名刀]木偶★★★*', dum.mo, '\t5500$(', a, ')')
            listb = listb + ['mo']
        if dum.tieg > 0:
            a += 1
            print('  铁弓★★★*', dum.tieg, '\t5000$(', a, ')')
            listb += ['tieg']
        if dum.qlb > 0:
            a = a + 1
            print('  麒麟臂★★★★*', dum.qlb, '\t7000$(', a, ')')
            listb = listb + ['qlb']
        if dum.ak74 > 0:
            a = a + 1
            print('  AK-74★★★★*', dum.ak74, '\t9000$', a, ')')
            listb = listb + ['ak74']
        if dum.m4 > 0:
            a = a + 1
            print('  M4★★★★*', dum.m4, '\t\t10000$(', a, ')')
            listb = listb + ['m4']
        if dum.bsba > 0:
            a = a + 1
            print('  匕首(β-钛合金)★★★★*', dum.bsba, '\t\t12000$(', a, ')')
            listb = listb + ['bsba']
        if dum.yj > 0:
            a = a + 1
            print('  YJ★★★★*', dum.yj, '\t\t20000$(', a, ')')
            listb = listb + ['yj']
        if dum.fhg > 0:
            a += 1
            print('  复合弓★★★★*', dum.fhg, '\t\t20000$(', a, ')')
            listb += ['fhg']
        if dum.kar98 > 0:
            a = a + 1
            print('  Kar98★★★★*', dum.kar98, '\t\t25000$(', a, ')')
            listb = listb + ['kar98']
        if dum.my > 0:
            a = a + 1
            print('  [妖刀]芈月★★★★★*', dum.my, '\t\t48000$(', a, ')')
            listb = listb + ['my']
        if dum.ak12 > 0:
            a = a + 1
            print('  AK-12★★★★★*', dum.ak12, '\t\t70000$(', a, ')')
            listb = listb + ['ak12']
        if dum.m416 > 0:
            a = a + 1
            print('  M416★★★★★*', dum.m416, '\t\t80000$(', a, ')')
            listb = listb + ['m416']
        if dum.m82a1 > 0:
            a = a + 1
            print('  M82A1★★★★★*', dum.m82a1, '\t\t120000$(', a, ')')
            listb = listb + ['m82a1']
        if dum.aug > 0:
            a = a + 1
            print('  AUG★★★★★*', dum.aug, '\t\t95000$(', a, ')')
            listb = listb + ['aug']
        if dum.rpg > 0:
            a = a + 1
            print('  RPG★★★★★*', dum.rpg, '\t\t100000$(', a, ')')
            listb = listb + ['rpg']
        if dum.xlzz > 0:
            a = a + 1
            print('  凶霖之爪★★★★★*', dum.xlzz, '\t\t150000$(', a, ')')
            listb = listb + ['xlzz']
        if dum.swbj > 0:
            a = a + 1
            print('  死亡笔记★★★★★*', dum.swbj, '\t\t500000$(', a, ')')
            listb = listb + ['swbj']
        if dum.llj > 0:
            a = a + 1
            print('  龙鳞剑★★★★★*', dum.llj, '\t\t400000$(', a, ')')
            listb = listb + ['llj']
        if dum.szyj > 0:
            a = a + 1
            print('  神之YJ★★★★★*', dum.szyj, '\t\t1000000$(', a, ')')
            listb = listb + ['szyj']
        if dum.crsq > 0:
            a = a + 1
            print('  CR神器★★★★★*', dum.crsq, '\t\t1000000$(', a, ')')
            listb = listb + ['crsq']
        if dum.ygc > 0:
            a = a + 1
            print('  愚公铲★★★★★*', dum.ygc, '\t\t120000$(', a, ')')
            listb = listb + ['ygc']
        if dum.gylq > 0:
            a = a + 1
            print('  光焰龙枪★★★★★*', dum.gylq, '\t\t800000(', a, ')')
            listb = listb + ['gylq']
        if dum.mxj > 0:
            a = a + 1
            print('  木胸甲★*', dum.mxj, '\t\t60$(', a, ')')
            listb = listb + ['mxj']
        if dum.txj > 0:
            a = a + 1
            print('  铁胸甲★★*', dum.txj, '\t\t600$(', a, ')')
            listb = listb + ['txj']
        if dum.gxj > 0:
            a = a + 1
            print('  钢胸甲★★★*', dum.gxj, '\t\t6000$(', a, ')')
            listb = listb + ['gxj']
        if dum.qclsj > 0:
            a = a + 1
            print('  七彩神龙甲★★★★★*', dum.qclsj, '\t\t1000000$(', a, ')')
            listb = listb + ['qcslj']
        if dum.mtj > 0:
            a = a + 1
            print('  木腿甲★*', dum.mtj, '\t\t55$(', a, ')')
            listb = listb + ['mtj']
        if dum.ttj > 0:
            a = a + 1
            print('  铁腿甲★★*', dum.ttj, '\t\t550$(', a, ')')
            listb = listb + ['ttj']
        if dum.gtj > 0:
            a = a + 1
            print('  钢腿甲★★★*', dum.gtj, '\t\t5500$(', a, ')')
            listb = listb + ['gtj']
        listb = listb + self.listhh
        i = a
        print('背包魂环:')
        for i in self.listhh:
            a = a + 1
            print('  魂环', i, '年/t/t', i, '$(', a, ')')
        if a == 0:
            print('无')
        return listb, i

    # make
    def makewq(self):
        global dum
        print('背包武器：')
        listb = []
        a = 0
        if dum.s > 0:
            a = a + 1
            print('  屎★*', dum.s, '\t\t(', a, ')')
            listb = listb + ['s']
        if dum.tj > 0:
            a = a + 1
            print('  铁剑★*', dum.tj, '\t\t(', a, ')')
            listb = listb + ['tj']
        if dum.bs > 0:
            a = a + 1
            print('  匕首★*', dum.bs, '\t\t(', a, ')')
            listb = listb + ['bs']
        if dum.mg > 0:
            a = a + 1
            print('  木弓★*', dum.mg, '\t\t(', a, ')')
            listb = listb + ['mg']
        if dum.tm > 0:
            a = a + 1
            print('  铁矛★★*', dum.tm, '\t\t(', a, ')')
            listb = listb + ['tm']
        if dum.gj > 0:
            a = a + 1
            print('  钢剑★★*', dum.gj, '\t\t(', a, ')')
            listb = listb + ['gj']
        if dum.mdlg > 0:
            a = a + 1
            print('  蒙德拉贡★★*', dum.mdlg, '\t(', a, ')')
            listb = listb + ['mdlg']
        if dum.ak47 > 0:
            a = a + 1
            print('  AK-47★★★*', dum.ak47, '\t(', a, ')')
            listb = listb + ['ak47']
        if dum.uzi > 0:
            a = a + 1
            print('  UZI★★★*', dum.uzi, '\t(', a, ')')
            listb = listb + ['uzi']
        if dum.unp9 > 0:
            a = a + 1
            print('  UNP9★★★*', dum.unp9, '\t(', a, ')')
            listb = listb + ['unp9']
        if dum.szd > 0:
            a = a + 1
            print('  杀猪刀★★★*', dum.szd, '\t(', a, ')')
            listb = listb + ['szd']
        if dum.zd > 0:
            a = a + 1
            print('  爪刀★★★*', dum.zd, '\t\t(', a, ')')
            listb = listb + ['zd']
        if dum.tsbq > 0:
            a = a + 1
            print('  铁丝棒球棍★★★*', dum.tsbq, '\t(', a, ')')
            listb = listb + ['tsbq']
        if dum.wsd > 0:
            a = a + 1
            print('  武士刀★★★*', dum.wsd, '\t(', a, ')')
            listb = listb + ['wsd']
        if dum.mo > 0:
            a = a + 1
            print('  [无名刀]木偶★★★*', dum.mo, '\t(', a, ')')
            listb = listb + ['mo']
        if dum.tieg > 0:
            a += 1
            print('  铁弓★★★*', dum.tieg, '\t(', a, ')')
            listb += ['tieg']
        if dum.qlb > 0:
            a = a + 1
            print('  麒麟臂★★★★*', dum.qlb, '\t(', a, ')')
            listb = listb + ['qlb']
        if dum.ak74 > 0:
            a = a + 1
            print('  AK-74★★★★*', dum.ak74, '\t(', a, ')')
            listb = listb + ['ak74']
        if dum.m4 > 0:
            a = a + 1
            print('  M4★★★★*', dum.m4, '\t\t(', a, ')')
            listb = listb + ['m4']
        if dum.bsba > 0:
            a = a + 1
            print('  匕首(β-钛合金)★★★★*', dum.bsba, '\t\t(', a, ')')
            listb = listb + ['bsba']
        if dum.yj > 0:
            a = a + 1
            print('  YJ★★★★*', dum.yj, '\t\t(', a, ')')
            listb = listb + ['yj']
        if dum.fhg > 0:
            a += 1
            print('  复合弓★★★★*', dum.fhg, '\t(', a, ')')
            listb += ['fhg']
        if dum.kar98 > 0:
            a = a + 1
            print('  Kar98★★★★*', dum.kar98, '\t\t(', a, ')')
            listb = listb + ['kar98']
        if dum.my > 0:
            a = a + 1
            print('  [妖刀]芈月★★★★★*', dum.my, '\t\t(', a, ')')
            listb = listb + ['my']
        if dum.ak12 > 0:
            a = a + 1
            print('  AK-12★★★★★*', dum.ak12, '\t\t(', a, ')')
            listb = listb + ['ak12']
        if dum.m416 > 0:
            a = a + 1
            print('  M416★★★★★*', dum.m416, '\t\t(', a, ')')
            listb = listb + ['m416']
        if dum.m82a1 > 0:
            a = a + 1
            print('  M82A1★★★★★*', dum.m82a1, '\t\t(', a, ')')
            listb = listb + ['m82a1']
        if dum.aug > 0:
            a = a + 1
            print('  AUG★★★★★*', dum.aug, '\t\t(', a, ')')
            listb = listb + ['aug']
        if dum.rpg > 0:
            a = a + 1
            print('  RPG★★★★★*', dum.rpg, '\t\t(', a, ')')
            listb = listb + ['rpg']
        if dum.xlzz > 0:
            a = a + 1
            print('  凶霖之爪★★★★★*', dum.xlzz, '\t\t(', a, ')')
            listb = listb + ['xlzz']
        if dum.swbj > 0:
            a = a + 1
            print('  死亡笔记★★★★★*', dum.swbj, '\t\t(', a, ')')
            listb = listb + ['swbj']
        if dum.llj > 0:
            a = a + 1
            print('  龙鳞剑★★★★★*', dum.llj, '\t\t(', a, ')')
            listb = listb + ['llj']
        if dum.szyj > 0:
            a = a + 1
            print('  神之YJ★★★★★*', dum.szyj, '\t\t(', a, ')')
            listb = listb + ['szyj']
        if dum.crsq > 0:
            a = a + 1
            print('  CR神器★★★★★*', dum.crsq, '\t\t(', a, ')')
            listb = listb + ['crsq']
        if dum.ygc > 0:
            a = a + 1
            print('  愚公铲★★★★★*', dum.ygc, '\t\t(', a, ')')
            listb = listb + ['ygc']
        if dum.gylq > 0:
            a = a + 1
            print('  光焰龙枪★★★★★*', dum.gylq, '\t\t(', a, ')')
            listb = listb + ['gylq']
        if a == 0:
            print('无')
        return listb

    def making(self, name, xs):
        exec('self.' + str(name) + '=' + 'self.' + str(name) + '-' + str(xs))
        dum.new_time(0, 0, 0, 1)
        if name == 'clmg':
            self.shz = self.shz + (xs * 2)
        elif name == 'gm':
            self.xm = self.xm + (xs * 4)
        elif name == 'mt':
            self.xm = self.xm + (xs * 2)
        elif name == 'gk':
            self.mt = self.mt + (xs * 1)
            self.gm = self.gm + (xs * 2)
            self.cltk = self.cltk + (2 * xs)
        elif name == 'ls':
            self.cltk = self.cltk + (xs * 1)
            self.pg = self.pg + (xs * 1)
            self.xm = self.xm + (xs * 2)
        elif name == 'tm':
            self.cltk += xs * 1
            self.clmg += xs * 2
        elif name == 'gj':
            self.gk += xs * 1
        elif name == 'tj' or name == 'bs':
            self.cltk += xs * 1
        elif name == 'mg':
            self.gm += xs * 2
            self.xian += xs * 2
        elif name == 'szd':
            self.clmg = self.clmg + (xs * 2)
            self.gk = self.gk + (xs * 2)
        elif name == 'mdlg':
            self.xm = self.xm + (xs * 4)
            self.cltk = self.cltk + (xs * 2)
            self.pg = self.pg + (xs * 1)
        elif name == 'ak47':
            self.gm = self.gm + (xs * 3)
            self.gk = self.gk + (xs * 2)
            self.ls = self.ls + (xs * 2)
        elif name == 'uzi':
            self.gk = self.gk + (xs * 2)
            self.ls = self.ls + (xs * 3)
        elif name == 'unp9':
            self.gk = self.gk + (xs * 3)
            self.ls = self.ls + (xs * 2)
        elif name == 'taom':
            self.gm = self.gm + (xs * 4)
        elif name == 'zd':
            self.gk = self.gk + (xs * 3)
        elif name == 'tsbq':
            self.taom = self.taom + (xs * 3)
            self.gk = self.gk + (xs * 1)
        elif name == 'wsd':
            self.taom = self.taom + (xs * 2)
            self.gk = self.gk + (xs * 3)
        elif name == 'mo':
            self.taom = self.taom + (xs * 3)
            self.gm = self.gm + (xs * 3)
            self.xm = self.xm + (xs * 3)
        elif name == 'tieg':
            self.cltk += xs * 2
            self.pg += xs * 1
            self.xian += xs * 3
        elif name == 'fhg':
            self.lhj += xs * 3
            self.szh += xs * 2
            self.nrb += xs * 1
            self.xian += xs * 5
        elif name == 'nrb':
            self.pg = self.pg + (xs * 4)
        elif name == 'bm':
            self.taom = self.taom + (xs * 4)
        elif name == 'szh':
            self.taom = self.taom + (xs * 2)
        elif name == 'lhj':
            self.gk = self.gk + (xs * 3)
            self.bm = self.bm + (xs * 2)
        elif name == 'qlb':
            self.nrb = self.nrb + (xs * 1)
            self.lhj = self.lhj + (xs * 2)
        elif name == 'ak74':
            self.lhj = self.lhj + (xs * 2)
            self.bm = self.bm + (xs * 2)
            self.ls = self.ls + (xs * 4)
        elif name == 'm4':
            self.lhj = self.lhj + (xs * 4)
            self.szh = self.szh + (xs * 2)
            self.ls = self.ls + (xs * 2)
        elif name == 'kar98':
            self.bm = self.bm + (xs * 3)
            self.lhj = self.lhj + (xs * 2)
            self.ls = self.ls + (xs * 4)
            self.szh = self.szh + (xs * 1)
        elif name == 'nam':
            self.bm = self.bm + (xs * 4)
        elif name == 'thj':
            self.lhj = self.lhj + (xs * 3)
            self.gk = self.gk + (xs * 2)
            self.nm = self.nam + (xs * 2)
        elif name == 'wfb':
            self.nrb = self.nrb + (xs * 3)
            self.szh = self.szh + (xs * 2)
        elif name == 'gfz':
            self.wfb = self.wfb + (xs * 2)
            self.thj = self.thj + (xs * 2)
            self.lhj = self.lhj + (xs * 4)
            self.szh = self.szh + (xs * 4)
        elif name == 'gcsl':
            self.gfz = self.gfz + (xs * 1)
            self.szh = self.szh + (xs * 6)
        elif name == 'ak12':
            self.thj = self.thj + (xs * 2)
            self.gfz = self.gfz + (xs * 1)
            self.nm = self.nam + (xs * 3)
        elif name == 'm416':
            self.thj = self.thj + (xs * 3)
            self.gfz = self.gfz + (xs * 2)
            self.lhj = self.lhj + (xs * 4)
        elif name == 'm82a1':
            self.thj = self.thj + (xs * 4)
            self.gfz = self.gfz + (xs * 3)
            self.gcsl = self.gcsl + (xs * 2)
        elif name == 'aug':
            self.thj = self.thj + (xs * 4)
            self.gcsl = self.gcsl + (xs * 4)
        elif name == 'rpg':
            self.thj = self.thj + (xs * 8)
            self.gfz = self.gfz + (xs * 3)
            self.gcsl = self.gcsl + (xs * 4)
        else:
            return False

    def part(self):
        print('-------------------------分解-------------------------')
        run = True
        while run == True:
            listh = self.makewq()
            print('批量分解(P)')
            print('返回(0)')
            sr = input('')
            if sr == '0' or sr == '':
                run = False
            elif sr == 'P':
                su = input('分解物:')
                st = input('分解数:')
                try:
                    if eval('self.' + listh[int(su) - 1]) - int(st) >= 0:
                        a = 1
                        while a <= int(st):
                            a = a + 1
                            b = self.making(listh[int(su) - 1], 1)
                        if b == None:
                            print('分解成功!')
                            dum.new_time(0, 0, 0, 0, 30 * a)
                        else:
                            print('此物品不可分解!')
                except:
                    print('输入错误!')
            else:
                try:
                    b = self.making(listh[int(sr) - 1], 1)
                    if b == None:
                        print('分解成功!')
                    else:
                        print('此物品不可分解!')
                except:
                    print('输入错误!')
                input('')
                print('-----------------------------------------------------')

    def make(self):
        print('----------------------------合成----------------------------')
        run = True
        while run == True:
            listh = []
            i = 1
            self.bag_cl()
            print('------------------------可合成------------------------')
            if self.shz >= 2:
                print('木棍★\t\t\t树枝★*2(', i, ')')
                listh = listh + ['clmg']
                i = i + 1
            if self.xm >= 4:
                print('果木★★\t\t\t橡木★*4(', i, ')')
                listh = listh + ['gm']
                i = i + 1
            if self.xm >= 2:
                print('木炭★★\t\t\t橡木★*2(', i, ')')
                listh = listh + ['mt']
                i = i + 1
            if self.mt >= 1 and self.cltk >= 2 and self.gm >= 2:
                print('钢块★★★\t\t\t木炭★★*1|果木★★*2|铁块★★*2(', i, ')')
                listh = listh + ['gk']
                i = i + 1
            if self.cltk >= 1 and self.pg >= 1 and self.xm >= 2:
                print('螺钉★★\t\t\t铁块★★*1|皮革★★*1|橡木★*2(', i, ')')
                listh = listh + ['ls']
                i = i + 1
            if self.clmg >= 2 and self.gk >= 2:
                print('杀猪刀★★★\t\t木棍★*2|钢块★★★*2(', i, ')')
                listh = listh + ['szd']
                i = i + 1
            if self.xm >= 4 and self.cltk >= 2 and self.pg >= 1:
                print('蒙德拉贡★★\t\t橡木★*4|铁块★★*2|皮革★★*1(', i, ')')
                listh = listh + ['mdlg']
                i = i + 1
            if self.gm >= 3 and self.gk >= 2 and self.ls >= 2:
                print('AK-47★★★\t\t果木★★*3|钢块★★★*2|螺钉★★*2(', i, ')')
                listh = listh + ['ak47']
                i = i + 1
            if self.gk >= 2 and self.ls >= 3:
                print('UZI★★★\t\t钢块★★★*2|螺钉★★*3(', i, ')')
                listh = listh + ['uzi']
                i = i + 1
            if self.gk >= 3 and self.ls >= 2:
                print('UNP9★★★\t\t钢块★★★*3|螺钉★★*2(', i, ')')
                listh = listh + ['unp9']
                i = i + 1
            if self.gm >= 4:
                print('桃木★★★\t\t果木★★*4(', i, ')')
                listh = listh + ['taom']
                i = i + 1
            if self.gk >= 3:
                print('爪刀★★★\t\t钢块★★★*3(', i, ')')
                listh = listh + ['zd']
                i = i + 1
            if self.taom >= 3 and self.gk >= 1:
                print('铁丝棒球棍★★★\t\t桃木★★★*3|钢块★★★*1(', i, ')')
                listh = listh + ['tsbq']
                i = i + 1
            if self.taom >= 2 and self.gk >= 3:
                print('武士刀★★★\t\t桃木★★★*2|钢块★★★*3(', i, ')')
                listh = listh + ['wsd']
                i = i + 1
            if self.taom >= 3 and self.gm >= 3 and self.xm >= 3:
                print('[无名刀]木偶★★★\t桃木★★★*3|果木★★*3|橡木★*3(', i, ')')
                listh = listh + ['mo']
                i = i + 1
            if self.cltk >= 2 and self.pg >= 1 and self.xian >= 3:
                print('铁弓★★★\t\t铁块★★*2|皮革★★*1|线★*3(', i, ')')
                listh += ['tieg']
                i += 1
            if self.pg >= 4:
                print('呢绒布★★★\t\t皮革★★*4(', i, ')')
                listh = listh + ['nrb']
                i = i + 1
            if self.taom >= 2:
                print('树脂★★★\t\t桃木★★★*2(', i, ')')
                listh = listh + ['szh']
                i = i + 1
            if self.taom >= 4:
                print('柏木★★★★\t\t桃木★★★*4(', i, ')')
                listh = listh + ['bm']
                i = i + 1
            if self.gk >= 3 and self.bm >= 2:
                print('铝合金★★★★\t\t钢块★★★*3|柏木★★★★*2(', i, ')')
                listh = listh + ['lhj']
                i = i + 1
            if self.nrb >= 1 and self.lhj >= 2:
                print('麒麟臂★★★★\t\t呢绒布★★★*1|铝合金★★★★*2(', i, ')')
                listh = listh + ['qlb']
                i = i + 1
            if self.bm >= 2 and self.lhj >= 2 and self.ls >= 4:
                print('AK-74★★★★\t\t柏木★★★★*2|铝合金★★★★*2|螺钉★★*4')
                listh = listh + ['ak74']
                i = i + 1
            if self.lhj >= 4 and self.szh >= 2 and self.ls >= 2:
                print('M4★★★★\t\t铝合金★★★★*4|树脂★★★*2|螺钉★★*2(', i, ')')
                listh = listh + ['m4']
                i = i + 1
            if self.bm >= 3 and self.lhj >= 2 and self.ls >= 4 and self.szh >= 1:
                print('Kar98★★★★\t\t柏木★★★★*3|铝合金★★★★*2|螺钉★★*4|树脂★★★*1(', i, ')')
                listh = listh + ['kar98']
                i = i + 1
            if self.lhj >= 3 and self.szh >= 2 and self.nrb >= 1 and self.xian >= 5:
                print('复合弓★★★★\t\t铝合金★★★★*3|树脂★★★*2|呢绒布★★★*1|线★*5(', i, ')')
                listh += ['fhg']
                i += 1
            if self.bm >= 4:
                print('楠木★★★★★\t\t柏木★★★★*4(', i, ')')
                listh = listh + ['nam']
                i = i + 1
            if self.lhj >= 3 and self.gk >= 2 and self.nam >= 2:
                print('钛合金★★★★★\t\t铝合金★★★★*3|钢块★★★*2|楠木★★★★★*2(', i, ')')
                listh = listh + ['thj']
                i = i + 1
            if self.nrb >= 3 and self.szh >= 2:
                print('无纺布★★★★\t\t呢绒布★★★*3|树脂★★★*2(', i, ')')
                listh = listh + ['wfb']
                i = i + 1
            if self.wfb >= 2 and self.thj >= 2 and self.sxh >= 4 and self.lhj >= 4:
                print('高分子材料★★★★★\t\t无纺布★★★★*2|钛合金★★★★★*2|树脂★★★*4|铝合金★★★★*4(', i, ')')
                listh = listh + ['gfz']
                i = i + 1
            if self.gfz >= 1 and self.szh >= 6:
                print('工程塑料★★★★★\t\t高分子材料★★★★★*1|树脂★★★*6')
                listh = listh + ['gcsl']
                i = i + 1
            if self.thj >= 2 and self.gfz >= 1 and self.nam >= 3:
                print('AK-12★★★★★\t\t钛合金★★★★★*2|高分子材料★★★★★*1|楠木★★★★★*3(', i, ')')
                listh = listh + ['ak12']
                i = i + 1
            if self.thj >= 3 and self.gfz >= 2 and self.lhj >= 4:
                print('M416★★★★★\t\t钛合金★★★★★*3|高分子材料★★★★★*2|铝合金★★★★*4(', i, ')')
                listh = listh + ['m416']
                i = i + 1
            if self.thj >= 4 and self.gfz >= 3 and self.gcsl >= 2:
                print('M82A1★★★★★\t钛合金★★★★★*4|高分子材料★★★★★*3|工程塑料★★★★★*2(', i, ')')
                listh = listh + ['m82a1']
                i = i + 1
            if self.thj >= 4 and self.gcsl >= 4:
                print('AUG★★★★★\t\t钛合金★★★★★*4|工程塑料★★★★★*4(', i, ')')
                listh = listh + ['aug']
                i = i + 1
            if self.thj >= 8 and self.gfz >= 3 and self.gcsl >= 4:
                print('RPG★★★★★\t\t钛合金★★★★★*8|高分子材料★★★★★*3|工程塑料★★★★★*4(', i, ')')
                listh = listh + ['rpg']
                i = i + 1
            if i == 1:
                print('无可合成!')
            print('返回(0)')
            sr = input('')
            if sr == '0' or sr == '':
                run = False
            else:
                try:
                    b = self.making(listh[int(sr) - 1], -1)
                    print('合成成功!')
                except:
                    print('输入错误!')
                input('')
                print('-----------------------------------------------------')


def main():
    # 游戏本体:
    global dum
    global Debugmod
    global running
    global cv
    try:  # try
        dum.color()  # 设置颜色
        dum.djpd()  # 魂力判断
        dum.check_level()  # 等级判断
        dum.check_core()  # 魂核判断
        dum.zlsx()  # 战力刷新
        dum.slcspd()  # 比武场等级判断
        dum.jqzsset()  # 金钱钻石
        dum.wgmgset()  # 战斗力
        dum.jysxset()  # 经验
        dum.listhh = TabMake.px(dum.listhh, sx=False)  # 魂环排序
        t = '\t\t'
        if len(str(dum.zhzlshow)) >= 6 and ('万' not in str(dum.zhzlshow) or '亿' not in str(dum.zhzlshow)):
            t = '\t'
        elif ('万' in str(dum.zhzlshow) or '亿' in str(dum.zhzlshow)) and len(str(dum.zhzlshow)) >= 5:
            t = '\t'
        print('----------------------------系统----------------------------')
        print('时间：', dum.time_now())
        print('姓名：', dum.name, '\t\t 年龄:', int(round(dum.sm, 0)), '/', dum.cmsx)
        print('综合战力:', dum.zhzlshow, t, '魂力：', dum.djxr, '(', dum.dj, '/', (dum.dj // 10) * 10 + 10, ')')
        print('穿越后:', dum.timecy, '年\t\t 精神力:', dum.jslxr, '(', dum.jslshow, '/', dum.jslsx, ')')
        print('等级：', dum.levelshow, '(', dum.xpshow, '/', dum.levelsxshow, ')\t 魂核：', dum.soul_core_des, '(',
              dum.soul_coreshow, '/', dum.soul_coresxshow, ')')
        print('金钱($):', dum.jqshow, '\t\t 钻石(&):', dum.zsshow)
        print('历练(1) | 背包(2) | 信息(3) | 商店(4) | 宗门(5) | 修炼(6)')
        print('设置(7) | 锻造(8) | 装备(9) | 退出(0) |')
        bwe = input()
        clean_up()
        if bwe == '1':
            q = False
            while not q:
                clean_up()
                q = dum.fb()

        elif bwe == '2':
            print('----------------------------背包----------------------------')
            dum.new_time(0, 0, 0, 0, 10)
            dum.bag_zb()
            dum.bag_cl()
            dum.bag_hh()
            dum.bag_hg()
            input()

        elif bwe == '3':
            print('----------------------------信息----------------------------')
            dum.new_time(0, 0, 0, 0, 5)
            dum.information()
            input()

        elif bwe == '4':
            dum.new_time(0, 0, 0, 0, 15)
            bee = 0
            while bee != '8' and bee != '':
                print('----------------------------商店----------------------------')
                print('-欢迎！尊贵的', dum.name, '!')
                dum.jqzsset()
                print('金钱($)：', dum.jqshow)
                print('钻石(&)：', dum.zsshow)
                print('---------------------------金钱商店---------------------------')
                print('铁匠铺(1) | 震元堂(2) | 传灵塔(3) | 废品站(4) | 抽奖(5)')
                print('---------------------------钻石商店---------------------------')
                print('钻石换金钱:100→10000(6)')
                print('下五子棋（7）')
                print('返回(8)')
                bee = input()
                if bee == '1':
                    print('--------------------------铁匠铺--------------------------')
                    print('  武器:')
                    print('  杀猪刀★★★*1\t\t\t\t3000$(1)')
                    print('  AK-47★★★*1\t\t\t\t5000$(2)')
                    print('  UZI★★★*1\t\t\t\t4000$(3)')
                    print('  爪刀★★★*1\t\t\t\t4000$(4)')
                    print('  铁丝棒球棍★★★*1\t\t\t4000$(5)')
                    print('  武士刀★★★*1\t\t\t\t6000$(6)')
                    print('  [无名刀]木偶★★★*1\t\t\t6000$(7)')
                    print('---------------------------------------------------------')
                    print('  麒麟臂★★★★*1\t\t\t8000$(8)')
                    print('  AK-74★★★★*1\t\t\t10000$(9)')
                    print('  M4★★★★*1\t\t\t\t12000$(10)')
                    print('  YJ★★★★*1\t\t\t\t20000$(11)')
                    print('  Kar98★★★★*1\t\t\t30000$(12)')
                    print('---------------------------------------------------------')
                    print('  [妖刀]芈月★★★★★*1\t\t\t50000$(13)')
                    print('  RPG★★★★★*1\t\t\t120000$(14)')
                    print('---------------------------------------------------------')
                    print('  防具:')
                    print('  钢胸甲★★★*1\t\t\t\t8000$(15)')
                    print('  钢腿甲★★★*1\t\t\t\t7500$(16)')
                    print('---------------------------------------------------------')
                    sr = str(input('购买:'))
                    dum.shoppd_tjp(sr)
                    input()
                    print('')
                elif bee == '2':
                    print('--------------------------震元堂--------------------------')
                    print('  一阶灵药★★★*1\t\t\t1000$(1)')
                    print('  二阶灵药★★★*1\t\t\t5000$(2)')
                    print('  三阶灵药★★★*1\t\t\t10000$(3)')
                    print('  四阶灵药★★★★*1\t\t\t20000$(4)')
                    print('  五阶灵药★★★★*1\t\t\t40000$(5)')
                    print('  六阶灵药★★★★*1\t\t\t80000$(6)')
                    print('  七阶灵药★★★★★*1\t\t\t100000$(7)')
                    print('  八阶灵药★★★★★*1\t\t\t150000$(8)')
                    print('  九阶灵药★★★★★*1\t\t\t200000$(9)')
                    print('  长身不老药★★★★★*1\t\t\t10000000$(10)')
                    print('  返老还童药★★★★★*1\t\t\t10000000$(11)')
                    print('  神仙汤★★★★★★★*1\t\t\t1000000000$(12)')
                    print('---------------------------------------------------------')
                    sr = str(input('购买:'))
                    dum.shoppd_zyt(sr)
                    input()
                    print('')
                elif bee == '3':
                    print('--------------------------传灵塔--------------------------')
                    print('  十年魂环\t\t\t100$(1)')
                    print('  百年魂环\t\t\t1000$(2)')
                    print('  千年魂环\t\t\t10000$(3)')
                    print('  万年魂环(10000~50000)\t\t50000$(4)')
                    print('  万年魂环(50000~99999)\t\t100000$(5)')
                    print('---------------------------------------------------------')
                    sr = str(input('购买:'))
                    dum.shoppd_clt(sr)
                    input()
                    print('')
                elif bee == '4':
                    print('--------------------------废品站--------------------------')
                    listsb, a = dum.hs()
                    print('---------------------------------------------------------')
                    print('批量回收(0)')
                    sr = input('出售:')
                    if sr != '0':
                        try:
                            dum.shoppd_hsz(listsb[int(sr) - 1], int(sr))
                            print('出售成功!')
                        except:
                            print('出售失败!')
                        input()
                    else:
                        c = input('回收数量:')
                        sr = input('回收物:')
                        try:
                            if int(sr) < (a + 1):
                                i = 0
                                c = min(int(c), eval('dum.' + listsb[int(sr) - 1]))
                                while i < c:
                                    i = i + 1
                                    dum.shoppd_hsz(listsb[int(sr) - 1], int(sr))
                                print('出售成功!')
                            else:
                                print('输入错误!')
                        except:
                            print('输入错误!')
                        input()
                    print('')
                elif bee == '5':
                    wer = 0
                    while wer != '3':
                        print('抽奖:')
                        print('余额:', jq, sep='')
                        print(' 普通抽奖(1) |  高级抽奖(2) | 返回(3)')
                        wer = str(input(':'))
                        if wer == '1':
                            print('普通抽奖内容:')
                            print('  无(45%)')
                            print('  随机灵药(35%)')
                            print('  随机武器(20%)')
                            print('购买:5000$')
                            print('是(1) | 否(2)')
                            wcr = str(input(':'))
                            if wcr == '1' and jq - 5000 >= 0:
                                jq = jq - 5000
                                print('  抽奖中...')
                                dum.sunrise(mod=3)
                            else:
                                print('购买失败!')
                        else:
                            print('未开放!')
                            input('')
                        sr = 0
                    input('')
                elif bee == '6':
                    dum.shoppd_zs()
                elif bee == '7':
                    result = Go.main()
                    if result == 0:
                        dum.jq += 50
                elif bee == '8' or bee == '':
                    pass
                else:
                    print('未开放!')
                    sr = 0
                    input('')
                print('---------------------------------------------------------')
                clean_up()

        elif bwe == '5':
            dum.new_time(0, 0, 0, 0, 20)
            if dum.zm == '无':
                dum.choosezm()
            if dum.zm != '无':
                dum.defzm()

        elif bwe == '6':
            print('----------------------------修炼----------------------------')
            dum.new_time(0, 0, 0, 0, 5)
            dum.bj()

        elif bwe == '7':
            dum.zsgg()

        elif bwe == '8':
            run = True
            while run:
                print('----------------------------锻造----------------------------')
                print('合成(1) | 分解(2) | 返回(3)')
                sr = input('')
                if sr == '1':
                    dum.make()
                elif sr == '2':
                    dum.part()
                elif sr == '3' or sr == '':
                    run = False
                else:
                    print('未开放!')
                    input()
                clean_up()

        elif bwe == '9':
            dum.new_time(0, 0, 0, 0, 10)
            ert = True
            while ert:
                print('----------------------------装备----------------------------')
                ert = dum.zb()
                clean_up()

        elif bwe == '0':
            dum.save_save()
            if Debugmod:
                Debug(False)
            running = False

        else:
            print('未开放!')
            input()
        dum.smpd()
        dum.save_save()
        clean_up()
    except:
        print('游戏出现未知错误!')
        input()
        global var
        dum.var = var
        dum.save_save()
        if Debugmod:
            Debug(False)
        running = False


def return_new():
    # 恢复出厂设置
    global color
    global cv
    global listyy
    global save_number
    global loc
    print('确定恢复出厂设置?')
    print('是(1) | 否(2)')
    a = input()
    if a == '1':
        list_save = os.listdir(cv)
        for i in list_save:
            if '.json' in i:
                os.remove(cv + '\\' + i)
        loc = os.path.abspath('.')
        save_number = 1
        cv = loc + '\\存档'
        color = 'color F1'
        listyy = []
        save_data()


def save_data():
    global cv
    global save_number
    global color
    global listyy
    global loc
    with open(loc + '\\MUD_SAVE.json', 'w') as f_load:
        json.dump([cv, save_number, color, listyy], f_load)


# 主程序
check_system()

listyy = []
run = True
colormod = True
Debugmod = True
IfDebug = False
Debug_kind1 = 'color'
Debug_kind2 = 'color'
inal = '-' * 27
var = 'Test_1.0.6'
global list_xb
global list_leg
global list_r
global list_bb
list_xb = ['木胸甲★', '铁胸甲★★', '钢胸甲★★★', '七彩神龙甲★★★★★']
list_leg = ['木腿甲★', '铁腿甲★★', '钢腿甲★★★']
list_r = ['屎★', '铁剑★', '匕首★', '木弓★', '铁矛★★', '钢剑★★', '蒙德拉贡★★', 'AK-47★★★', 'UZI★★★', 'UNP9★★★',
          '杀猪刀★★★', '爪刀★★★', '铁丝棒球棍★★★', '武士刀★★★', '[无名刀]木偶★★★', '铁弓★★★', '麒麟臂★★★★', 'AK-74★★★★',
          'M4★★★★', '匕首(β-钛合金)★★★★', 'YJ★★★★', '复合弓★★★★', 'Kar98★★★★', '[妖刀]芈月★★★★★', 'AK-12★★★★★',
          'M416★★★★★', 'M81A2★★★★★', 'AUG★★★★★', 'RPG★★★★★', '凶霖之爪★★★★★', '死亡笔记★★★★★', '龙鳞剑★★★★★',
          '神之YJ★★★★★', 'CR神器★★★★★', '愚公铲★★★★★', '光焰龙枪★★★★★★★']
list_bb = list_xb + list_leg + list_r
# 获得当前目录
loc = os.path.abspath('.')
os.system('title 爽文修真')

# 导入储存变量
with open('MUD_SAVE.json', 'r') as f_load:
    list1 = json.load(f_load)
    cv = list1[0]
    save_number = list1[1]
    color = list1[2]
    listyy = list1[3]

while run:
    clean_up()
    if Debugmod:
        os.system(color)
    print(inal, '爽文修真', inal)
    print(' -' + inal, '正式', '-' + inal)
    print('')
    print('单人游戏(1) | 多人联机(2) | 墓地(3) | 设置(4) | 退出(5)')
    sd = input('')
    if sd == '1':

        try:
            r = True
            while r:
                clean_up()
                print('', '-' * 24, '单人游戏', '-' * 24)
                list_save = os.listdir(cv)
                a = 0
                list_save_new = []
                print('存档目录:')
                for i in list_save:
                    t = '\t\t'
                    if '.json' in i:
                        a = a + 1
                        b = i[0:-5]
                        c = MUD.is_Chinese(b)
                        if len(b) >= 16:
                            if not c:
                                b = b[0:11] + '...'
                            else:
                                b = b[0:6] + '...'
                        elif len(b) <= 5:
                            if not c:
                                t = '\t\t\t'
                            else:
                                if len(b) < 4:
                                    t = '\t\t\t'
                        print(b, t + '(', a, ')')
                        list_save_new = list_save_new + [i]
                if a == 0:
                    print('还没有存档呢,先去创建一个试试?')
                    r = False
                print('新建存档(0) | 返回(Enter)')
                ch = input()
                if ch == '0':
                    running = True
                    dum = MUD()
                    Debug(IfDebug, Debug_kind1)
                    p = True
                    while p:
                        print('请输入存档名称(回车默认):')
                        dum.save_name = input('')
                        if dum.save_name == '':
                            dum.save_name = '新建存档' + str(save_number)
                            save_number = save_number + 1
                        list2 = os.listdir(cv)
                        if dum.save_name + '.json' in list2:
                            save_number = save_number + 1
                            print('有存档名重复,若继续将会覆盖原有存档,是否继续?')
                            print('是(1) | 否(2)')
                            a = input('')
                            if a == '1':
                                p = False
                        else:
                            p = False
                    save_data()
                    dum.start()
                    while running:
                        main()
                elif ch == '':
                    r = False
                elif float(ch) % 2 == 0 or float(ch) % 2 == 1:
                    new_name = list_save_new[int(ch) - 1][0:-5]
                    while 1:
                        clean_up()
                        print('存档：', new_name)
                        print('加载存档(1) | 删除存档(2) | 重命名(3) | 备份(4) | 返回(5)')
                        name = input('')
                        if name == '2':
                            print('确认删除?')
                            print('是(1) | 否(2)')
                            er = input('')
                            if er == '1':
                                name = list_save_new[int(ch) - 1]
                                os.remove(cv + '\\' + name)
                                print('删除成功!')
                                input()
                                break
                        elif name == '' or name == '5':
                            break
                        elif name == '1':
                            name = list_save_new[int(ch) - 1]
                            with open(cv + '\\' + str(name), 'r') as new_save:
                                set1 = json.load(new_save)
                            dum = MUD()
                            i = 0
                            set2 = set1[1]
                            for a in set1[0]:
                                exec('dum.' + str(a) + '=' + 'set2[i]')
                                i = i + 1
                            if dum.var == var:
                                Debug(IfDebug, Debug_kind2)
                                print(inal, '爽文修真', inal)
                                print(' -' + inal, '正式', '-' + inal)
                                running = True
                                while running:
                                    main()
                            else:
                                try:
                                    Debug(IfDebug, Debug_kind2)
                                    print(inal, '爽文修真', inal)
                                    print(' -' + inal, '正式', '-' + inal)
                                    running = True
                                    while running:
                                        dum.var = var
                                        main()
                                except:
                                    print('游戏版本不同!请检查版本后再载入!')
                                    print('游戏版本:', var)
                                    print('存档版本:', dum.var)
                                    input()
                            r = False
                            break
                        elif name == '3':
                            new_name = input('请输入新名称(请勿与其他存档重复!):')
                            if new_name + '.json' in list_save_new:
                                print('新名称与其他存档重复!')
                                input()
                            else:
                                name = list_save_new[int(ch) - 1]
                                with open(cv + '\\' + name, 'r') as new_save:
                                    set1 = json.load(new_save)
                                dum = MUD()
                                i = 0
                                set2 = set1[1]
                                for a in set1[0]:
                                    exec('dum.' + str(a) + '=' + 'set2[i]')
                                    i = i + 1
                                dum.save_name = new_name
                                dum.save_save()
                                os.remove(cv + '\\' + name)
                                list_save = os.listdir(cv)
                                list_save_new = []
                                for i in list_save:
                                    if '.json' in i:
                                        list_save_new += [i]
                                print('重命名成功!')
                                input()
                        elif name == '4':
                            try:
                                name = list_save_new[int(ch) - 1]
                                with open(cv + '\\' + name, 'r') as new_save:
                                    set1 = json.load(new_save)
                                dum = MUD()
                                i = 0
                                set2 = set1[1]
                                for a in set1[0]:
                                    exec('dum.' + str(a) + '=' + 'set2[i]')
                                    i = i + 1
                                newn_name = 'False'
                                i = 0
                                while ((newn_name + '.json') in list_save_new) or newn_name == 'False':
                                    i += 1
                                    newn_name = new_name + '(' + str(i) + ')'
                                dum.save_name = newn_name
                                dum.save_save()
                                print('存档备份成功!')
                            except:
                                print('存档备份失败!')
                            input()
                        else:
                            print('未开放!')
                            input()
                else:
                    print('存档输入有误!')
                    input()

        except IndexError:
            print('找不到指定存档,请检查目录:')
            os.startfile(cv)
            input()
        except TypeError:
            print('输入有误!')
            input()
        except:
            print('存档路径有误,请确保路径正确!')
            input()

    elif sd == '3':
        a = 0
        for i in listyy:
            a = a + 1
            print(i)
        if a == 0:
            print('还没有死过人哪,哪来的遗言!')
        input('')

    elif sd == '4':
        u = True
        while u:
            clean_up()
            print('', '-' * 26, '设置', '-' * 26)
            print('存档设置(1) | 颜色设置(2) | 命令(3) | 关于(4) | 返回(5)')
            sb = input('')
            if sb == '1':
                print('设置存档储存位置:')
                print('返回(0) | 快捷路径(1) | 自动检测(2) | 打开文件夹(3)')
                print('(没事请不要乱动!)')
                print('当前位置:', cv)
                cr = input('')
                if cr != '0' and cr != '3' and cr != '':
                    if cr == '1':
                        print('快捷路径:')
                        print('桌面(1)')
                        print('默认(2)')
                        print('添加新路径(3)')
                        print('返回(0)')
                        srt = input('')
                        if srt == '1':
                            ca = os.path.join(os.path.expanduser('~'), 'Desktop')
                            print('当前路径:', cr)
                        elif srt == '2':
                            ca = loc + '\\存档'
                            print('当前路径:', cr)
                        elif srt == '3':
                            print('当前位置:', cv)
                            ca = input('请输入新路径:')
                            print('当前路径:', cr)
                        elif srt == '0' or srt == '':
                            pass
                        else:
                            print('输入错误!')
                            input()
                    elif cr == '2':
                        ca = loc + '\\存档'
                    cv = ca
                    print('当前位置:', cv)
                    input()
                elif cr == '3':
                    try:
                        os.startfile(cv)
                    except:
                        print('存档路径有误,请确保路径正确!')
                        input()
            elif sb == '2':
                print('', '-' * 26, '颜色', '-' * 26)
                print('默认模式(1) | 修仙模式(2) | 爽文模式(3) | 夜间模式(4)')
                sr2 = str(input(':'))
                if sr2 == '1':
                    color = 'color F1'
                    print('-默认模式已开启!')
                elif sr2 == '2':
                    color = 'color 1F'
                    print('-修仙模式已开启!')
                elif sr2 == '3':
                    color = 'color F0'
                    print('-爽文模式已开启!')
                elif sr2 == '4':
                    color = 'color 0F'
                    print('-夜间模式已开启!')
                if Debugmod:
                    os.system(color)
                input()
            elif sb == '3':
                print('', '-' * 26, '命令', '-' * 26)
                print('命令系统不完善,可能导致闪退或电脑坏掉(真的)请慎用!')
                print('       ^^^^^^        ^^^^  ^^^^^^^^^^^')
                print('注:无法更改"dum"中变量!')
                command = input('>>>')
                try:
                    if command == 'return_new()':
                        return_new()
                        print('已恢复默认设置!')
                    else:
                        exec(command)
                    print('执行成功!')
                except:
                    print('输入有误!')
                    input()
            elif sb == '4':
                print('', '-' * 26, '关于', '-' * 26)
                print('爽文修真正式版')
                print('游戏版本:', var)
                print('更新日期:23/7/13')
                input()
            elif sb == '5' or sb == '':
                u = False
            else:
                print('未开放!')
                input()
            save_data()

    elif sd == '5':
        run = False

    else:
        print('未开放!')
        input()

# 到底了!!!
