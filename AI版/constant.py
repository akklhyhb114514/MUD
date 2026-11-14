import GetPressed as gp
import SysOpe as so

so.set_root_dir()
TITLE = '爽文修真'
VERSION = '25.0.1'
WINDOW_SIZE = (64, 25)

CHINESE_COL_WIDTH = 16

LINSENER = gp.start_listener()

ANSI_COLORS = {
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'orange': '\033[38;5;208m', 
    'purple': '\033[38;5;129m', 
    'white': '\033[97m',
    'black': '\033[30m',
    'gray': '\033[90m',
    'bold': '\033[1m',
    'reset': '\033[0m'
}

TITLE_UNIT = '─'

# Map config
PRINT_RANGE = (10, 4)
KEYS = {'向上': 'w', '向下': 's', '向左': 'a', '向右': 'd'}
