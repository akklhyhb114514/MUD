import constant as ct
import json
import player
import GetPressed as gp
import SysOpe as so
import BetterPrint as bp
import datas as ds

running = True

def load_save(path):
    pass

def save_game(path):
    pass

def exit_game():
    global running
    running = False

def choice_name() -> str:
    gp.clear_input_buffer()
    return input('请输入你的名字(sj随机)：')

def choice_sex() -> str:
    print('请选择你的性别(男(1) | 女(2))')
    r = gp.wait_for_key(('1', '2'))
    if r == '1': return '男'
    return '女'

def new_player():
    p = player.Player()
    p.set_name(choice_name())
    p.set_sex(choice_sex())
    return p

def print_bag(p:player.Player):
    p.update_all_things()
    total_page = len(p.all_things) // (ct.WINDOW_SIZE[1] - 2) + 1
    now_page = 0
    while True:
        #       ────────────────────────────────────────────────────────────── 参考线
        print('┌──────────────────────────── 背包 ────────────────────────────┐')  # 总长度64字符
        s = ''
        n = 0
        index0 = now_page * (len(bp.NORMAL_CHARS) - 1)
        for i in p.all_things[index0: index0 + len(bp.NORMAL_CHARS)]:
            if n == len(bp.NORMAL_CHARS) - 1: 
                break
            s += f'│ {bp.align(i.name, 20)} * {bp.align(i.amount, 6)} {bp.align(f'({bp.NORMAL_CHARS[n]})', 4)}\n'
            n += 1
        if n != 0:
            print(bp.highlight_objs(s), end='')
            print('└', bp.print_center(f' 第{now_page+1}页/共{total_page}页 ', len(bp.NORMAL_CHARS) - 1, '─'), '┘', sep='')  # 总长度64字符
        else:
            print('背包空空如也...')
        key = gp.wait_for_key(bp.NORMAL_CHARS + ['enter'])
        if key == 'enter':
            break
        a = bp.NORMAL_CHARS.index(key)
        o = p.all_things[a + now_page * (len(bp.NORMAL_CHARS) - 1)]
        while True:
            so.clear_screen()
            print(o.print_information(), end='')
            print('丢弃(1) | 重命名(2) | 返回(3)')
            key = gp.wait_for_key(['1', '2', '3'])
            gp.clear_input_buffer()
            if key == '1':
                print('确定丢弃吗(将会永远失去)?')
                print('是(1) | 否(2)')
                key = gp.wait_for_key(['1', '2'])
                if key == '1':
                    s = 1
                    if o.amount != 1:
                        gp.clear_input_buffer()
                        while True:
                            s = input('请输入丢弃数量：')
                            try:
                                s = int(s)
                                break
                            except:
                                print('输入错误，请重新输入')
                    p.discard(o, s)
                    print('丢弃成功!')
                    gp.wait_for_key((gp.ALL_BUTTONS,))
                    break
            elif key == '2':
                n = input('请输入新名字：')
                p.rename_obj(o, n)
                print('重命名成功!')
                gp.wait_for_key((gp.ALL_BUTTONS,))
            else:
                break

def print_info(p:player.Player):
    p.update_lvl()
    #      ────────────────────────────────────────────────────────────── 参考线
    print('┌───────────────────────── 个人信息 ─────────────────────────┐')  # 总长度64字符
    text = f"""│ 姓名：{bp.align(p.name, 18)}  性别：{bp.align(p.sex, 27)}│
│ 年龄：{bp.align(p.attribute['age'], 18)}  修为：{bp.align(f'{p.attribute['realm']}({p.attribute['exp']}/{p.get_next_level_exp()})', 27)}│
│ 血量：{bp.align(p.attribute['hp'], 18)}  力量：{bp.align(p.attribute['power'], 27)}│
│ 物攻：{bp.align(p.attribute['atk_phy'], 18)}  魔攻：{bp.align(p.attribute['atk_mag'], 27)}│
│ 物防：{bp.align(p.attribute['def_phy'], 18)}  魔防：{bp.align(p.attribute['def_mag'], 27)}│"""
    print(bp.print_highlight(text, ['姓名', '性别', '等级', '修为']))
    print('└────────────────────────────────────────────────────────────┘')  # 总长度64字符
    print('(按任意键返回)')
    input()
    gp.wait_for_key((gp.ALL_BUTTONS,))

def print_menu():
    #      ────────────────────────────────────────────────────────────── 参考线
    print('──────────────────────────────────────────────────────────────')
    print_map()
    print('信息(1) | 背包(2) | 退出(3)')

def print_map():
    ds.M0.print_map()

def main():
    global running
    p = new_player()

    while running:
        so.clear_screen()
        print_menu()
        while True:
            k = gp.wait_for_key(['1', '2', '3'] + list(ct.KEYS.values()))
            so.clear_screen()
            if k == '1': 
                print_info(p)
            elif k == '2': 
                print_bag(p)
            elif k == '3':
                exit_game()
            elif k in ct.KEYS.values():
                r = ds.M0.update_move(k)
            gp.clear_input_buffer()
            break

    running = True



