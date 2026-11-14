class Weapons:

    def __init__(self, name, wg, gj_mg, durability, price):
        self.type = 'Weapons'
        self.name = name
        self.wg = wg
        self.gj_mg = gj_mg
        self.durability = durability
        self.price = price


class Armors:

    def __init__(self, name, xl, wf, mf, durability, price):
        self.type = 'Armors'
        self.name = name
        self.xl = xl
        self.wf = wf
        self.mf = mf
        self.durability = durability
        self.price = price


class Material:

    def __init__(self, name, price):
        self.type = 'Material'
        self.name = name
        self.price = price





