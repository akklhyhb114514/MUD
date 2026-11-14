from wcwidth import wcswidth
import constant as ct
import datas as ds

NORMAL_CHARS = list('0123456789abcdefghijklmnopqrstuvwxyz') # 0-9 a-z

def align(text, width, fill=' ') -> str:
    padding = width - wcswidth(str(text))
    return f"{text}{fill * padding}"


def print_highlight(text, highlight_words, color='yellow') -> str:
    """
    高亮文本中的指定词汇
    :param text: 原始文本
    :param highlight_words: 需要高亮的词汇列表
    :param color: 颜色名称（red/green/yellow/blue/bold）
    """
    for word in highlight_words:
        text = text.replace(word, f"{ct.ANSI_COLORS[color]}{word}{ct.ANSI_COLORS['reset']}")
    return text


def highlight(text, color) -> str:
    return f"{ct.ANSI_COLORS[color]}{text}{ct.ANSI_COLORS['reset']}"


def get_title(title_str, color=None) -> str:
    # 总长度64字符（参考线长度）
    total_space = ct.WINDOW_SIZE[0] - wcswidth(title_str) - 2  # 减去标题和两个空格
    left = total_space // 2
    right = total_space - left
    if color:
        title_str = f"{ct.ANSI_COLORS[color]}{title_str}{ct.ANSI_COLORS['reset']}"
    # 使用format确保精确填充
    return "{0}{1}{2}".format(
        ct.TITLE_UNIT * left,
        f' {title_str} ',
        ct.TITLE_UNIT * right
    )


def highlight_objs(text) -> str:
    s = text.split('\n')
    s0 = ''
    for i in range(len(s)):
        t = s[i].split(' ')
        for j in range(len(t)):
            for y in range(len(ds.obj_levels)):
                if ds.obj_levels[y] in t[j]:
                    t[j] = f"{ct.ANSI_COLORS[ds.level_colors[y]]}{t[j]}{ct.ANSI_COLORS['reset']}"
                    break
            s0 += f"{t[j]} "
        s0 += '\n'
    for i in ds.obj_colors.keys():
        s0 = print_highlight(s0, ds.obj_colors[i], i)
    return s0
        

def print_center(text, length, fill=' ') -> str:
    text = str(text)
    text_width = wcswidth(text)
    left_padding = (length - text_width) // 2
    right_padding = length - text_width - left_padding
    # 处理边界情况（当总长度小于文本宽度时）
    left_padding = max(0, left_padding)
    right_padding = max(0, right_padding)
    return fill * left_padding + text + fill * right_padding