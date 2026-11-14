from copy import copy
import random
import BetterRandom as br
import datas as ds
import obj_datas as ods

RAMDOM_NAME_SIGN = 'sj'

class Player:
    def __init__(self):
        self.basic_attribute = {'hp': 100, 'atk_phy': 100, 'atk_mag': 10, 'def_phy': 10, 'def_mag': 10,
        'power': 1}
        self.attribute = {'hp': 100, 'atk_phy': 100, 'atk_mag': 10, 'def_phy': 10, 'def_mag': 10, 
        'power': 1, 'lvl': 0, 'exp': 1, 'age' : 18, 'realm': '炼气一层', 'breakthrough_failed' : 0}
        self.equipment = []
        self.consumption = [] # 消耗品
        self.all_things =[]

        self.init()

    def init(self):
        self.init_basic_attribte()
        self.update_attribute()
        self.get_initial_equipment()

    def get_random_name(self):
        sn = random.choices(list(ds.name_list1.keys()), weights=list(ds.name_list1.values()), k=1)[0]
        fn = ''
        for i in range(random.randint(1, 2)):
            fn += random.choices(list(ds.name_list2.keys()), weights=list(ds.name_list2.values()), k=1)[0]
        return sn+fn

    def set_name(self, name):
        if name == RAMDOM_NAME_SIGN:
            self.name = self.get_random_name()
        else:
            self.name = name

    def set_sex(self, sex):
        self.sex = sex

    def init_basic_attribte(self):
        for k, v in ds.basic_attribute.items():
            self.basic_attribute[k] = br.normal_random(*v)

    def update_attribute(self):
        for k, v in self.basic_attribute.items():
            self.attribute[k] = round(v, 2)

    def update_lvl(self):
        '''
        修仙等级划分如下：
        下境界：
        炼气（一共13层）、
        筑基（分初、中、后期和大圆满）、
        结丹（分初、中、后期和大圆满）、
        元婴（分初、中、后期和大圆满）、
        化神（分初、中、后期和大圆满）。
        中境界：
        炼虚（分初、中、后期和大圆满）、
        合体（分初、中、后期和大圆满）、
        大乘（分初、中、后期和大圆满）。
        上境界：
        真仙境（分初、中、后期和大圆满）、
        金仙境（分初、中、后期和大圆满）、
        太乙境（分初、中、后期和大圆满）、
        大罗境（分初、中、后期和大圆满）、
        道祖境（分初、中、后期和大圆满）。
        '''
        l0 = ds.level_config[self.attribute['lvl']]
        for l in ds.level_config[self.attribute['lvl']+1:]:
            if self.attribute['exp'] >= l['min_exp']:
                if l0['stage'] == '大圆满期':
                    r = self.handle_breakthrough(l0, l)
                else:
                    r = True
                if r:
                    self.attribute['lvl'] += 1
                    self.attribute['realm'] = l['realm'] + l['stage']
            else:
                break
        
    def handle_breakthrough(self, current_cfg, next_cfg) -> bool:
            """处理境界突破逻辑"""
            success_rate = 100 #for debug
            # 开始渡劫
            if random.randint(1, 100) <= success_rate:
                # 渡劫成功 
                self.attribute['realm'] = next_cfg['realm'] + next_cfg['stage'] # 进入下个境界初期
                return True  # 返回True表示渡劫成功，否则返回False表示渡劫失败，需要回退到上个境界
            # 渡劫失败惩罚
            self.attribute['exp'] = current_cfg['min_exp']
            self.attribute['breakthrough_failed'] += 1
            return False
    
    def get_next_level_exp(self) -> int:
        return ds.level_config[self.attribute['lvl']+1]['min_exp']

    def update_all_things(self):
        self.all_things = []
        for o in self.equipment.copy():
            if o.amount > 0:
                self.all_things.append(o)
            else:
                self.equipment.remove(o) # 移除空的物物
        for o in self.consumption.copy():
            if o.amount > 0:
                self.all_things.append(o)
            else:
                self.equipment.remove(o) # 移除空的物物

    def add_equipment(self, equipment):
        self.equipment.append(equipment)
        self.update_all_things()

    def get_initial_equipment(self):
        self.add_equipment(copy(ods.equipments['铁剑★']))

    def discard(self, obj, amount):
        if obj.amount > amount:
            obj.amount -= amount
        else:
            obj.amount = 0
        self.update_all_things()

    def rename_obj(self, obj, new_name):
        obj.name = new_name