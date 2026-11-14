import os
import ctypes
import ctypes.wintypes

def set_root_dir():
    # 设置根目录为当前目录
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

def set_color(text, background):
    # 设置颜色
    os.system(f'color {background}{text}')

def set_title(title):
    # 设置标题
    os.system(f'title {title}')

def set_console_properties(cols:int, lines:int):
    """设置控制台窗口属性"""
    # 设置屏幕缓冲区大小和窗口尺寸
    STD_OUTPUT_HANDLE = -11
    handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    
    # 设置屏幕缓冲区大小
    ctypes.windll.kernel32.SetConsoleScreenBufferSize(handle, ctypes.wintypes._COORD(cols, lines))
    
    # 设置窗口尺寸（参数为左、上、右、下坐标）
    rect = ctypes.wintypes.SMALL_RECT(0, 0, cols - 1, lines - 1)
    ctypes.windll.kernel32.SetConsoleWindowInfo(handle, True, ctypes.byref(rect))

    # 禁用窗口缩放
    GWL_STYLE = -16
    WS_THICKFRAME = 0x00040000
    WS_MAXIMIZEBOX = 0x00010000
    hwnd = ctypes.windll.kernel32.GetConsoleWindow()
    
    # 使用c_long处理指针类型
    style = ctypes.c_long(ctypes.windll.user32.GetWindowLongPtrW(hwnd, GWL_STYLE))
    new_style = style.value & ~WS_THICKFRAME & ~WS_MAXIMIZEBOX
    
    # 更新窗口样式并刷新
    ctypes.windll.user32.SetWindowLongPtrW(hwnd, GWL_STYLE, new_style)
    ctypes.windll.user32.SetWindowPos(hwnd, 0, 0, 0, 0, 0, 0x0001 | 0x0002 | 0x0020)

def clear_screen():
    # 清空屏幕
    os.system('cls')
