import json
import constant as ct

keys = tuple(ct.KEYS.keys())
BASIC_SIGN = {'pos' : '◆', '#' : '█', '0': '┼'}
SIGN_0 = {
    'top_left': '┌', 'top_right': '┐', 'bottom_left': '└', 'bottom_right': '┘', 'top': '┬', 
    'bottom': '┴', 'left': '├', 'right': '┤', 'middle': '┼'
    }
#0为空位 中间用┼ 边界用┌ ┬ ┐├ ┤└ ┴ ┘

def load_map(path):
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

class Map:
    def __init__(self, data, pos):
        self.map = data['map']
        self.sign = data['sign']
        self.map_rows = len(self.map)
        self.map_cols = len(self.map[0]) if self.map_rows > 0 else 0
        self.pos = list(pos)

    def get_map(self) -> str:
        """以pos为中心,打印范围为PRINT_RANGE的地图
        Example
        -------
        ┌┬┬┬┬┬┬┬┬┬┐
        ├┼┼◆┼┼┼┼┼■┤
        └┴┴┴┴┴┴┴┴┴┘
        """
        text = ''
        x_min = max(0, self.pos[0] - ct.PRINT_RANGE[0])
        x_max = min(self.map_cols, self.pos[0] + ct.PRINT_RANGE[0] + 1)
        y_min = max(0, self.pos[1] - ct.PRINT_RANGE[1])
        y_max = min(self.map_rows, self.pos[1] + ct.PRINT_RANGE[1] + 1)

        s_l = (x_min - self.pos[0] + ct.PRINT_RANGE[0]) * ' '
        s_r = (self.pos[0] + ct.PRINT_RANGE[1] - x_max) * ' ' + '\n'
        s_t = (y_min - self.pos[1] + ct.PRINT_RANGE[1]) * (' ' * ct.PRINT_RANGE[0] * 2 + ' \n')
        s_b = (self.pos[1] + ct.PRINT_RANGE[1] - y_max) * (' ' * ct.PRINT_RANGE[0] * 2 + ' \n')
        text += s_t

        for y in range(y_min, y_max):
            text += s_l
            for x in range(x_min, x_max):
                if self.map[y][x] == '0':
                    if x == self.pos[0] and y == self.pos[1]:
                        text += BASIC_SIGN['pos']
                    elif x == x_min and y == y_min:
                        text += SIGN_0['top_left']
                    elif x == x_max - 1 and y == y_min:
                        text += SIGN_0['top_right']
                    elif x == x_min and y == y_max - 1:
                        text += SIGN_0['bottom_left']
                    elif x == x_max - 1 and y == y_max - 1:
                        text += SIGN_0['bottom_right']
                    elif x == x_min:
                        text += SIGN_0['left']
                    elif x == x_max - 1:
                        text += SIGN_0['right']
                    elif y == y_min:
                        text += SIGN_0['top']
                    elif y == y_max - 1:
                        text += SIGN_0['bottom']
                    else:
                        text += SIGN_0['middle']
                elif self.map[y][x] == '#':
                    text += BASIC_SIGN['#']
                elif self.map[y][x] in self.sign.keys():
                    pass
            text += s_r
        text += s_b
        return text

    def get_map_with_menu(self) -> str:
        global keys
        s = self.get_map()
        s = s.split('\n')
        for i in range(1, len(keys) + 1):
            s[i] += f'    {keys[i - 1]}({ct.KEYS[keys[i - 1]]})'
        return '\n'.join(s)

    def print_map(self) -> None:
        print(self.get_map_with_menu(), end='')

    def update_move(self, key) -> bool:
        '''
        移动并返回是否移动成功
        '''
        if key == ct.KEYS['向上']:
            if self.pos[1] - 1 < 0 or self.map[self.pos[1] - 1][self.pos[0]] == '#': 
                return False
            self.pos[1] -= 1
        elif key == ct.KEYS['向下']:
            if self.pos[1] + 1 >= self.map_rows or self.map[self.pos[1] + 1][self.pos[0]] == '#':
                return False
            self.pos[1] += 1
        elif key == ct.KEYS['向左']:
            if self.pos[0] - 1 < 0 or self.map[self.pos[1]][self.pos[0] - 1] == '#':
                return False
            self.pos[0] -= 1
        elif key == ct.KEYS['向右']:
            if self.pos[0] + 1 >= self.map_cols or self.map[self.pos[1]][self.pos[0] + 1] == '#':
                return False
            self.pos[0] += 1
        return True
