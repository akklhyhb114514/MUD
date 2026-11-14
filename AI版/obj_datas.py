import equipment as eqp


#descriptions:
DESCRIPTION0 = '粗制滥造的武器'
DESCRIPTION1 = '凡铁所铸的普通兵器'
DESCRIPTION2 = '经过灵气滋养的初级灵器'
DESCRIPTION3 = '炼器师精心打造的法宝'
DESCRIPTION4 = '地脉灵火淬炼的秘宝'
DESCRIPTION5 = '上古流传的仙器残片'
DESCRIPTION6 = '天地造化孕育的先天灵宝'
DESCRIPTION7 = '突破天道限制的混沌至宝'

# (name, level, atk_phy, atk_mag, def_phy, def_mag, hp, power, durability, description)
EQUIPMENT_DATA = (
    ('铁剑★', 2, 50, 0, 0, 0, 0, 0, 120, DESCRIPTION1),
    )

equipments = {}
for data in EQUIPMENT_DATA:
    equipments[data[0]] = eqp.Equipment(data)
