import random

from MUD import *

class hunshou:
    list_kind = ['龙神', '冰噬龙', '金眼黑龙王', '阴阳混沌鸟', '深渊魔龙', '光明圣龙', '暗黑魔龙', '雷电霸王龙',
                 '荆棘龙', '白虎',
                 '暗黑魔虎', '紫雷熊', '金刚狒狒', '风狼', '闪豹', '凤凰', '曼陀罗花', '树妖', '穿山甲', '蓝银皇',
                 '蓝银草',
                 '大地魔犀', '金丝魔猿', '树蛇', '史莱姆王', '史莱姆', '独角兽', '死亡蠕虫', '深海魔鲸王', '僵尸',
                 '骷髅', '蜂后',
                 '豪烈刚猪', '雷光鼠'
                 ]

    def __init__(self, dum):
        self.year = random.randint(dum.jy * 0.5, dum.jy * 1.2)
        self.wg = random.randint(9, 17)
        self.mg = random.randint(2, 9)
        self.wf = random.randint(8, 20)
        self.mf = random.randint(3, 10)
        self.xl = random.randint(90, 160)
        r = random.randint((100-dum.dj)**2, 10000)
        if r == 1:
            self.kind = 2
            self.name = hunshou.list_kind[self.kind]
            self.wg = self.wg*2
            self.mg = self.mg*3
            self.wf = self.wf*2
            self.mf = self.mf*2
            self.xl = self.xl*4
            self.wgxs = 10
            self.mgxs = 12
            self.wfxs = 10
            self.mfxs = 10
            self.xlxs = 20



    def djpd(self):
        self.dj = int(round((self.year ** (1 / 3)), 0)) + 1
        self.sx = int(round((self.dj + 1) ** 3, 0))
        self.zhzl = self.zhzl + self.dj * 10
        while self.dj >= self.djjs:
            self.sxxs = self.sxxs + ((self.djjs ** 2) / 100000)
            self.djjs = self.djjs + 1

        self.wgxs = self.wgxs*self.sxxs
        self.mgxs = self.mgxs*self.sxxs
        self.wfxs = self.wfxs*self.sxxs
        self.mfxs = self.mfxs*self.sxxs
        self.xlxs = self.xlxs*self.sxxs

        self.zhzl()

    def zhzl(self):
        self.zhzl = int(round((self.xl * self.xlxs + self.wg * self.wgxs + self.mg * self.mgxs + self.wf * self.wfxs +
                               self.mf * self.mfxs) * 6 * self.sxxs,0))

    def information(self):
        print(self.name+'('+str(self.year)+'年'+')')
        print('综合战力:', self.zhzl, t, '血量：', int(round(self.xl * self.xlxs * self.sxxs, 0)))
        print('物攻：', int(round(self.wg * self.wgxs * self.sxxs, 0)), '\t\t 魔攻：',
              int(round(self.gj_mg * self.gj_mgxs * self.sxxs, 0)))
        print('物防：', int(round(self.wf * self.wfxs * self.sxxs, 0)), '\t\t 魔防：',
              int(round(self.mf * self.mfxs * self.sxxs, 0)))

    def hlgz(self, dum):
        ai = hunshou(dum)
        ai.hsdjpd()
        ai.hsinformation()
        jg = ai.fight()
        q = random.randint(int(round(year ** 0.5, 0)) - 1, int(round(year ** 0.5)) + 9)
        i = 0
        if jg == 1:
            while i <= q:
                i = i + 1
                a = random.randint(0, year)
                if 0 <= a < 60:
                    jy = random.randint(year // 10, year // 10 + 20)
                    print('获得经验 +', jy)
                    self.jy = self.jy + jy
                elif 60 <= a < 80:
                    jq = random.randint(year // 10, year // 10 + 20)
                    print('获得金钱 +', jq)
                    self.jq = self.jq + jq
                elif 80 <= a < 200:
                    print('获得魂环(', year, ')')
                    self.listhh = self.listhh + [year]
                elif 200 <= a < 300:
                    jq = random.randint(year // 10, year // 10 + 20)
                    print('获得金钱 +', jq)
                    self.jq = self.jq + jq
                elif 300 <= a < 700:
                    jy = random.randint(year // 10, year // 10 + 20)
                    print('获得经验 +', jy)
                    self.jy = self.jy + jy
                elif 700 <= a < 900:
                    if year <= 70000:
                        self.sunrise(int(year // 20000))
                elif 900 <= a < 1200:
                    print('获得魂环(', year, ')')
                    self.listhh = self.listhh + [year]

        else:
            self.living = False
        input('')
