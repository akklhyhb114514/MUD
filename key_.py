import keyboard

def ifkey(key: list) -> str:
    up = True
    while up:
        for k in key:
            if keyboard.is_pressed(k):
                up = False
                break
    while keyboard.is_pressed(k):
        pass
    return k


def input_k(string: str) -> str:
    number_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    
