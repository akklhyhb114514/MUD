import BetterRandom as br
import BetterPrint as bp
import datas as ds

class Equipment:
    def __init__(self, args):
        self.type = type
        self.attribute = {'name': args[0]}
        self.name = args[0]
        self.level = args[1]
        self.used_durability = 0
        self.amount = 1
        self.type = 'equipment'

        self.init_level(self.level)
        self.init_attribute(args)

    def init_level(self, level):
        self.attribute['level_number'] = br.normal_random(101, 899, level * 80 + 100)
        self.attribute['level_description'] = ds.level_description[self.attribute['level_number'] // 100]
        self.attribute['level_coefficient'] = (self.attribute['level_number'] / 100 - level) / level + 1
    
    def init_attribute(self, args):
        self.attribute['atk_phy'] = args[2] * self.attribute['level_coefficient']
        self.attribute['atk_mag'] = args[3] * self.attribute['level_coefficient']
        self.attribute['def_phy'] = args[4] * self.attribute['level_coefficient']
        self.attribute['def_mag'] = args[5] * self.attribute['level_coefficient']
        self.attribute['hp'] = args[6] * self.attribute['level_coefficient']
        self.attribute['power'] = args[7] * self.attribute['level_coefficient']
        self.attribute['durability'] = round(args[8] * self.attribute['level_coefficient'])
        self.attribute['description'] = args[9]

    def print_information(self) -> str:
        s = ''
        s += f"名称：{self.name}\n"
        s += f"品质：{self.attribute['level_description']}({self.attribute['level_number']}/{ds.MAX_EQUIPMENT_LEVEL})\n"
        s += f"物理攻击：{bp.align(self.attribute['atk_phy'], 20)}物理防御：{bp.align(self.attribute['def_phy'], 20)}\n"
        s += f"魔法攻击：{bp.align(self.attribute['atk_mag'], 20)}魔法防御：{bp.align(self.attribute['def_mag'], 20)}\n"
        s += f"血量：{bp.align(self.attribute['hp'], 24)}力量：{bp.align(self.attribute['power'], 24)}\n"
        s += f"耐久度： {bp.align(self.attribute['durability'] - self.used_durability, 20)}\n"
        s += f"{self.attribute['description']}\n"
        s = bp.highlight_objs(s)
        return s

    def discard(self, n):
        if self.amount > n:
            self.amount -= n
            return True
        self.amount = 0
        return False