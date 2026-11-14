from queue import Queue
from pynput import keyboard
import msvcrt 

# 在全局作用域添加
event_queue = Queue()
exit_flag = False

ALL_BUTTONS = 'all_buttons'

def get_pressed(key):
    try:
        # 转换按键为可读字符串
        key_str = key.char
    except AttributeError:
        # 处理特殊按键（如方向键）
        key_str = str(key).split('.')[-1]
    event_queue.put(('press', key_str))

def on_pressed(key) -> bool:
    try:
        if not event_queue.empty():  # 当按下key键时触发退出
            if key == event_queue.get()[1]:  # 检查队列中的按键是否与key相同
                return True
        print(1)
        return False
    except AttributeError:
        return False

def start_listener():
    # 启动监听器
    listener = keyboard.Listener(on_press=get_pressed)
    listener.daemon = True  # 设置为守护线程
    listener.start()
    return listener

def listening():
    try:
        return event_queue.get_nowait()  # (event_type, key_str)
    except:
        return None
            
def wait_for_key(keys) -> str:
    # 等待指定按键被按下
    while True:
        k = listening()
        if k != None and (ALL_BUTTONS in keys or k[1] in keys):
            return k[1]

def clear_input_buffer():
    while msvcrt.kbhit():
        msvcrt.getch()