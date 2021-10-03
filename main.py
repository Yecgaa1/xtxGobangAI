import numpy as np
import pygame
import sys
import os
import shutil
import ScoreAI
from ScoreAI import chessBoard
from ScoreAI import Score

Mode = 1  # 0为玩家间，1为与AI
size = width, height = 820, 720#界面大小
screen = pygame.display.set_mode(size, 0, 32)#screen控件初始化
BLACK = (0, 0, 0)#白子的RGB参数
WHITE = (255, 255, 255)#黑子的RGB参数
NowPlayer = 1  # 黑1白2,黑色先手


def DrawChess(x, y, who):
    '''
    棋子绘制函数
    :param x: 本次落子的x坐标
    :param y: 本次落子的y坐标
    :param who: 绘制哪一方的棋子
    :return: None
    '''
    if who == 1:
        pygame.draw.circle(screen, BLACK, (x * 50 + 10, y * 50 + 10), 20)
    else:
        pygame.draw.circle(screen, WHITE, (x * 50 + 10, y * 50 + 10), 20)


def WinCheck(x, y, NowPlayer):
    '''
    获胜判断函数
    :param x: 次落子的x坐标
    :param y: 本次落子的y坐标
    :param NowPlayer: 现在正在进行游戏的玩家
    :return: bool 是否存在获胜
    '''

    str1 = ""
    Flag = False

    # 先横

    # 旧方案：逻辑判别
    # #边界维护
    # if(x<5):i=0
    # else:i=x-4
    # step=0#计算连续数量
    # while(i<x+5 and i<15):
    #     if(step==5):
    #         Flag = True
    #         break
    #     if(chessBoard[y][i]!=NowPlayer):
    #         step=0
    #     else:
    #         step += 1
    #     i+=1

    # 新方案：字符串判别（我都有内存跑python了缺这点吗（））
    # 横
    for i in range(0, 15):
        str1 += str(chessBoard[y][i])
    if (NowPlayer == 1):
        result = str1.find("11111")
    else:
        result = str1.find("22222")

    if (result != -1):
        Flag = True

    # 竖
    str1 = ""
    for i in range(0, 15):
        str1 += str(chessBoard[i][x])
    if (NowPlayer == 1):
        result = str1.find("11111")
    else:
        result = str1.find("22222")

    if (result != -1):
        Flag = True

    # 左斜
    str1 = ""
    arr = np.diagonal(chessBoard, offset=x - y)

    for i in arr:
        str1 += str(i)
    if (NowPlayer == 1):
        result = str1.find("11111")
    else:
        result = str1.find("22222")

    if (result != -1):
        Flag = True

    # 右斜
    str1 = ""
    arr = np.fliplr(chessBoard)
    arr = np.diagonal(arr, offset=14 - x - y)

    for i in arr:
        str1 += str(i)
    if (NowPlayer == 1):
        result = str1.find("11111")
    else:
        result = str1.find("22222")

    if (result != -1):
        Flag = True

    print(Flag)

    return Flag


def DownChess(x, y):
    '''
    落子判断函数,给玩家和机器人使用
    :param x: 本次落子的x坐标
    :param y: 本次落子的y坐标
    :return: None
    '''
    global NowPlayer
    if (chessBoard[y][x] == 0):
        chessBoard[y][x] = NowPlayer
        DrawChess(x, y, NowPlayer)
        isWin = WinCheck(x, y, NowPlayer)
        if isWin:
            if NowPlayer==1:
                print("Player Win!")
                DrawText("Player Win!",750,360)
            else:
                print("PC Win!")
                DrawText("PC Win!", 750, 360)

        # 换人
        if (NowPlayer == 1):
            NowPlayer = 2
        else:
            NowPlayer = 1


def AngelProcess(x, y):
    '''
    转换鼠标的xy坐标为棋盘的xy坐标并附带坐标修正
    :param x: 获取的鼠标单击的x坐标
    :param y: 获取的鼠标单击的y坐标
    :return: None
    '''
    global NowPlayer
    if (x < 10):
        x = 0
    elif ((x - 10) % 50 < 25):
        x = (int)((x - 10) / 50)
    else:
        x = (int)((x - 10) / 50) + 1
    if (y < 10):
        y = 0
    elif ((y - 10) % 50 < 25):
        y = (int)((y - 10) / 50)
    else:
        y = (int)((y - 10) / 50) + 1
    DownChess(x, y)


def DrawText(str1, x, y):
    '''
    绘制字符到界面上
    :param str1: 要绘制的字符串
    :param x: 该字符的x轴中心坐标
    :param y: 该字符的y轴中心坐标
    :return: None
    '''
    fontObj = pygame.font.Font(None, 20)  # 通过字体文件获得字体对象
    textSurfaceObj = fontObj.render(str1, True, BLACK)  # 配置要显示的文字
    textRectObj = textSurfaceObj.get_rect()  # 获得要显示的对象的rect
    textRectObj.center = (x, y)  # 设置显示对象的坐标
    screen.blit(textSurfaceObj, textRectObj)  # 绘制字体


def DrawBoard():
    '''
    绘制棋盘函数
    :return: None
    '''
    screen.fill((249, 223, 127))
    step = 0

    for i in range(10, 711, 50):
        pygame.draw.line(screen, BLACK, (i, 10), (i, 710))
        DrawText(str(step), i, 5)
        pygame.draw.line(screen, BLACK, (10, i), (710, i))
        DrawText(str(step), 5, i)
        step += 1

    # DrawText("ReMake!", 770, 690)


if __name__ == '__main__':
    global chessBoard

    try:
        shutil.rmtree('Score')
        os.mkdir('Score')
    except:
        print("没有要清理的文件")
    pygame.init()
    img = pygame.image.load("counter_0.ico")
    pygame.display.set_icon(img)  # 可以填img
    pygame.display.set_caption("xtx的五子棋 v0.3a")
    clock = pygame.time.Clock()
    clock.tick(30)
    AIState = True  # 保证只执行一次
    # 绘制棋盘
    DrawBoard()
    while True:
        clock.tick(30)
        # 处理不同事件
        for event in pygame.event.get():
            # 检查是否关闭窗口
            if Mode == 1 and NowPlayer == 2 and AIState == True:
                AIState = False
                x, y = ScoreAI.AiRun()
                DownChess(x, y)
                if (x != -1):
                    print(x, y)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:  # 鼠标按下
                x, y = pygame.mouse.get_pos()  # 获取鼠标位置
                if(x>720 or y>720):
                    continue #防误触
                # 曾经的重开键
                # if (730 < x < 810 and 680 < y < 720):  # 重开
                #     NowPlayer = 1
                #     DrawBoard()
                #     ScoreAI.ReFlashChessBoard()
                #     chessBoard = np.zeros((15, 15), dtype=np.int32)
                #     continue
                AngelProcess(x, y)
                AIState = True

        # 刷新屏幕
        pygame.display.update()
