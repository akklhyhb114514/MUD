class Go():

    # 棋盘大小
    SIZE = 12

    # 是否停止落子
    OVER = True

    # 记录第几次落子，控制台打印第几手落子
    ICOUNT = 1

    # 游戏结果
    RESULT = 0

    # 棋盘数组
    board_list = []

    #初始化棋盘，默认二维数组元素值全是0
    def initBoard():
        for i in range(Go.SIZE):
            Go.board_list.append([i * 0 for i in range(Go.SIZE)])
        return Go.board_list

    # 打印棋盘，-1打印●  1打印○  0打印默认 +
    def printBoard():
        for i in Go.board_list:
            for j in i:
                print(" +" if j == 0 else "●" if j == -1 else "○", end="")
            print()

    # 用户输入时需要判断用户输入格式是否正确，
    def isCorrectInput(s) -> bool:
        res = False
        if "," in s and str(s).replace(",","").isnumeric():
            indexX, indexY = str(s).split(",")
            if int(indexX) >= 1 and int(indexX) <= Go.SIZE and int(indexY) >= 1 and int(indexY) <= Go.SIZE:
                res = True
        elif str(s) == '0':
            res = 0
        return res

    def get_RESULT():
        """判断游戏的结局。0为游戏进行中，1为玩家B获胜，-1为玩家A获胜，2为平局"""
        # 1. 判断是否纵向连续五子
        for x in range(Go.SIZE - 4):
            for y in range(Go.SIZE):
                if Go.board_list[x][y] == 1 and Go.board_list[x + 1][y] == 1 and Go.board_list[x + 2][y] == 1 and Go.board_list[x + 3][y] == 1 and Go.board_list[x + 4][y] == 1:
                    return 1
                if Go.board_list[x][y] == -1 and Go.board_list[x + 1][y] == -1 and Go.board_list[x + 2][y] == -1 and Go.board_list[x + 3][y] == -1 and Go.board_list[x + 4][y] == -1:
                    return -1

        # 2. 判断是否横向连续五子
        for x in range(Go.SIZE):
            for y in range(Go.SIZE - 4):
                if Go.board_list[x][y] == 1 and Go.board_list[x][y + 1] == 1 and Go.board_list[x][y + 2] == 1 and Go.board_list[x][y + 3] == 1 and Go.board_list[x][y + 4] == 1:
                    return 1
                if Go.board_list[x][y] == -1 and Go.board_list[x][y + 1] == -1 and Go.board_list[x][y + 2] == -1 and Go.board_list[x][y + 3] == -1 and Go.board_list[x][y + 4] == -1:
                    return -1

        # 3. 判断是否横向连续五子
        for x in range(Go.SIZE - 4):
            for y in range(Go.SIZE - 4):
                if Go.board_list[x][y] == 1 and Go.board_list[x + 1][y + 1] == 1 and Go.board_list[x + 2][y + 2] == 1 and Go.board_list[x + 3][y + 3] == 1 and Go.board_list[x + 4][y + 4] == 1:
                    return 1
                if Go.board_list[x][y] == -1 and Go.board_list[x + 1][y + 1] == -1 and Go.board_list[x + 2][y + 2] == -1 and Go.board_list[x + 3][y + 3] == -1 and Go.board_list[x + 4][y + 4] == -1:
                    return -1

        # 4. 判断是否横向连续五子
        for x in range(Go.SIZE - 4):
            for y in range(Go.SIZE - 4):
                if Go.board_list[x + 4][y] == 1 and Go.board_list[x + 3][y + 1] == 1 and Go.board_list[x + 2][y + 2] == 1 and Go.board_list[x + 1][y + 3] == 1 and Go.board_list[x][y + 4] == 1:
                    return 1
                if Go.board_list[x + 4][y] == -1 and Go.board_list[x + 3][y + 1] == -1 and Go.board_list[x + 2][y + 2] == -1 and Go.board_list[x + 1][y + 3] == -1 and Go.board_list[x][y + 4] == -1:
                    return -1

        # 5. 判断是否为平局
        for x in range(Go.SIZE):
            for y in range(Go.SIZE):
                if Go.board_list[x][y] == 0:  # 棋盘中还有剩余的格子，不能判断为平局
                    return 0

        # 6.平局
        return 2

    def putPiece(index):
        # 将全局变量引入到方法
        
        # 第一二手提醒玩家身份  棋手A或棋手B
        if Go.ICOUNT <= 2:
            print("记住你是棋手A" if Go.ICOUNT == 1 else "记住你是棋手B")

        # 判断玩家输入格式是否正确
        if Go.isCorrectInput(index):
            indexX ,indexY = index.split(",")
            # 判断是否该位置已经落过棋子
            if Go.board_list[int(indexX) - 1][int(indexY) - 1] == 0 :
                if Go.ICOUNT % 2 == 0:
                    print("第" + str(Go.ICOUNT) + "手落完,轮到棋手A落子")
                    #棋手B落子数组记录值为1
                    Go.board_list[int(indexX) - 1][int(indexY) - 1] = 1
                else:
                    print("现第"+str(Go.ICOUNT) + "手落完,轮到棋手B落子")
                    # 棋手B落子数组记录值为-1
                    Go.board_list[int(indexX) - 1][int(indexY) - 1] = -1
                # 此处待添加判断是否5子成线方法
            else:
                #当用户输入位置已经落子，当前步不算Go.ICOUNT需要减1
                Go.ICOUNT -= 1
                print("该位置已经落子,请重新落子")
            Go.printBoard()

            # 待添加判断是否5子成棋情况
            res = Go.get_RESULT()

            if res in [-1,1,2]:
                Go.OVER = False
                Go.RESULT = res
        elif Go.isCorrectInput(index) == 0:
            Go.OVER = 0
        else:
            # 当用户输入位置不正确，当前步不算Go.ICOUNT需要减1
            Go.ICOUNT -= 1
            print("输入的棋子位置不正确，请重新输入！")


    def main():
        print("欢迎来到五子棋游戏")
        Go.initBoard()
        Go.printBoard()
        while Go.OVER:
            index = input("请输入要下棋子位置，例如 1,2表示在第一行，第二列下一个棋子(0退出)：")
            Go.putPiece(index)
            Go.ICOUNT += 1
        if Go.OVER == 0:
            print('已退出!')
            return None
        player = "B" if Go.RESULT == 1 else "A"
        print("经过" + str(Go.ICOUNT)+ "手后，恭喜棋手"+ player +"获得胜利！！！" if Go.RESULT != 2 else "平局")
        if Go.RESULT ==1:
            return 0
        else:
            return 1


