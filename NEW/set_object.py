import pygame

class set_object():

    '''
    Type:["wq","food","material","medicine"]
    Leval:[1,2,3,4,5,6,7]
    '''

    def __init__(self,name,emc,pic,type,level,time=0,tag=[],n=0):
        
        self.name = name
        self.n = n
        self.emc = emc
        self.pic = pygame.image.load(pic).convert_alpha()
        self.type = type
        self.level = level
        self.time = time
        self.tag = tag

    def set_shop(self,money_buy,money_sell):
        self.money_sell = money_sell
        self.money_buy = money_buy

    def set_gj(self,wg=0,mg=0,wf=0,mf=0,xl=0):
        self.gj_wg = wg
        self.gj_mg = mg
        self.gj_wf = wf
        self.gj_mf = mf
        self.gj_xl = xl

    def set_made(self,list_name,list_n):
        self.list_made_name = list_name
        self.list_made_n = list_n

    def set_apart(self,list_name,list_n):
        self.list_apart_name = list_name
        self.list_apart_n = list_name

    def set_food(self,hunger):
        self.food_hunger = hunger

    def set_medicine(self,health,time):
        self.medicine_health = health
        self.medicine_time = time

