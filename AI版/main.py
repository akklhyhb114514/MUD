# 安装依赖：python -m pip install <package>
# 打包.exe：pyinstaller -F AI版\main.py
#实现主界面
import constant as ct
import json
import SysOpe as so
import GetPressed as gp
import datas as ds
import game

#Initialization
def load_config() -> dict:
    with open('config.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def init():
    config = load_config()
    so.set_color(config['text_color'], config['background_color'])
    so.set_title(ct.TITLE)
    so.set_console_properties(*ct.WINDOW_SIZE)

def exit_main():
    exit(0)
#Operation
def print_head():
    #      ────────────────────────────────────────────────────────────── 参考线
    # 总长度64字符（参考线长度）
    print(ds.MAIN_TITLE)

def print_main_menu():
    print_head()
    print('单人游戏(1) | 人物墓地(2) | 游戏设置(3) | 退出游戏(4)')
    
def main():
    #在此位置监听输入
    while True:
        so.clear_screen()
        print_main_menu()
        k = gp.wait_for_key(('1', '2', '3', '4'))
        if k == '1': #单人游戏
            game.main() #进入游戏主界面
        elif k == '4': #退出游戏
            exit_main()


if __name__ == '__main__':
    main()