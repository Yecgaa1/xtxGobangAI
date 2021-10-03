import numpy as np

x = y = type1 = offset = 0 #xy轴棋盘坐标，正在切割字符串的切割方案，偏移率
isDirectOut = False#是否直接输出
Score = np.zeros((15, 15), dtype=np.float)#棋盘赋分矩阵

chessBoard = np.zeros((15, 15), dtype=np.int32)#棋盘矩阵

round=2#回合数
# def ReFlashChessBoard():
#     global chessBoard
#     chessBoard = np.zeros((15, 15), dtype=np.int32)
#     print("Fine?")
# 坐标处理
def CoordinatesProcessing(result):
    '''
    处理Ai计算过程中倾斜offset的坐标计算问题
    :param result: 获取的字符串find结果
    :return: 处理好的x,y轴棋盘坐标
    '''
    if (type1 == 1):  # 横
        return result, y
    if (type1 == 2):  # 竖
        return x, result
    if (type1 == 3):  # 左斜
        if offset > 0:
            return offset + result, result
        else:
            return result, -offset + result
    if (type1 == 4):  # 右斜
        if offset > 0:
            return 14 - (offset + result), result
        else:
            return 14 - result, -offset + result


def ChangeScoreValue(value, result):
    '''
    转换倾斜坐标并赋分给Score矩阵
    :param value: 赋分值
    :param result: 获取的字符串find结果
    :return: None
    '''
    x, y = CoordinatesProcessing(result)
    Score[y][x] += value


# 本AI主攻！！！！，详情见笔记本
# 本AI只下白棋

def FindChess(str1):
    '''
    从字符串中找到想要的役种（），赋分或者是直接输出
    :param str1: 输入字符串
    :return: 找到的Result值
    '''
    global isDirectOut
    isDirectOut=False
    # 活四和冲四
    # 攻
    if True:
        result = str1.find("02222")
        if (result != -1):
            isDirectOut = True
            return result
        result = str1.find("22220")
        if (result != -1):
            isDirectOut = True
            return result + 4
        result = str1.find("20222")
        if (result != -1):
            isDirectOut = True
            return result + 1
        result = str1.find("22022")
        if (result != -1):
            isDirectOut = True
            return result + 2
        result = str1.find("22202")
        if (result != -1):
            isDirectOut = True
            return result + 3

    # 守
    if True:
        result = str1.find("01111")
        if (result != -1):
            isDirectOut = True
            return result
        result = str1.find("11110")
        if (result != -1):
            isDirectOut = True
            return result + 4
        result = str1.find("10111")
        if (result != -1):
            isDirectOut = True
            return result + 1
        result = str1.find("11011")
        if (result != -1):
            isDirectOut = True
            return result + 2
        result = str1.find("11101")
        if (result != -1):
            isDirectOut = True
            return result + 3

    # 活三
    # 攻
    if True:
        result = str1.find("2220")
        if result != -1:
            result = str1.find("02220")
            if result != -1:
                result = str1.find("0022200")
                if result != -1:
                    isDirectOut = True
                    return result + 1
                result = str1.find("1022201")
                if result != -1:
                    ChangeScoreValue(150, result + 1)
                    ChangeScoreValue(150, result + 5)
                result = str1.find("1022200")
                if result != -1:
                    isDirectOut = True
                    return result + 5
                result = str1.find("0022201")
                if result != -1:
                    isDirectOut = True
                    return result + 1
            result = str1.find("12220")
            if result != -1:
                result = str1.find("122200")
                if result != -1:
                    ChangeScoreValue(150, result + 4)
                    ChangeScoreValue(50, result + 5)
        else:
            result = str1.find("0222")
            if result != -1:
                result = str1.find("002221")
                if result != -1:
                    ChangeScoreValue(50, result)
                    ChangeScoreValue(150, result + 1)
        result = str1.find("2022")
        if result != -1:
            result = str1.find("020220")
            if result != -1:
                isDirectOut = True
                return result + 2
            result = str1.find("020221")
            if result != -1:
                ChangeScoreValue(150, result)
                ChangeScoreValue(150, result + 2)
            result = str1.find("120220")
            if result != -1:
                ChangeScoreValue(150, result + 2)
                ChangeScoreValue(150, result + 5)
        result = str1.find("2202")
        if result != -1:
            result = str1.find("022020")
            if result != -1:
                isDirectOut = True
                return result + 3
            result = str1.find("022021")
            if result != -1:
                ChangeScoreValue(150, result)
                ChangeScoreValue(150, result + 3)
            result = str1.find("122020")
            if result != -1:
                ChangeScoreValue(150, result + 3)
                ChangeScoreValue(150, result + 5)

    # 守
    if True:
        result = str1.find("1110")
        if (result != -1):
            result = str1.find("01110")
            if (result != -1):
                result = str1.find("0011100")
                if (result != -1):
                    isDirectOut = True
                    return result + 1
                result = str1.find("2011100")
                if (result != -1):
                    ChangeScoreValue(50, result + 1)
                    ChangeScoreValue(100, result + 5)
                    ChangeScoreValue(100, result + 6)
                result = str1.find("0011102")
                if (result != -1):
                    ChangeScoreValue(100, result)
                    ChangeScoreValue(100, result + 1)
                    ChangeScoreValue(20, result + 5)
            result = str1.find("211100")
            if (result != -1):
                ChangeScoreValue(100, result + 4)
                ChangeScoreValue(100, result + 5)
        result = str1.find("001112")
        if (result != -1):
            ChangeScoreValue(100, result)
            ChangeScoreValue(100, result + 1)
        result = str1.find("1011")
        if (result != -1):
            result = str1.find("010110")
            if (result != -1):
                ChangeScoreValue(50, result)
                ChangeScoreValue(100, result + 2)
                ChangeScoreValue(50, result + 5)
            result = str1.find("010112")
            if (result != -1):
                ChangeScoreValue(100, result)
                ChangeScoreValue(100, result + 2)
            result = str1.find("210110")
            if (result != -1):
                ChangeScoreValue(100, result + 5)
                ChangeScoreValue(100, result + 2)
        result = str1.find("1101")
        if (result != -1):
            result = str1.find("011010")
            if (result != -1):
                ChangeScoreValue(50, result)
                ChangeScoreValue(100, result + 3)
                ChangeScoreValue(50, result + 5)
            result = str1.find("011012")
            if (result != -1):
                ChangeScoreValue(100, result)
                ChangeScoreValue(100, result + 3)
            result = str1.find("211010")
            if (result != -1):
                ChangeScoreValue(100, result + 3)
                ChangeScoreValue(100, result + 5)

    # 活二，眠二
    if True:
        # 攻
        result = str1.find("220")
        if (result != -1):
            result = str1.find("0220")
            if (result != -1):
                ChangeScoreValue(50, result)
                ChangeScoreValue(50, result + 3)
            else:
                ChangeScoreValue(25, result + 3)
        else:
            result = str1.find("022")
            if (result != -1):
                ChangeScoreValue(25, result)

        # 守
        result = str1.find("110")
        if (result != -1):
            result = str1.find("0110")
            if (result != -1):
                ChangeScoreValue(25, result)
                ChangeScoreValue(25, result + 3)
            else:
                ChangeScoreValue(12.5, result + 3)
        else:
            result = str1.find("011")
            if (result != -1):
                ChangeScoreValue(12.5, result)

    # 单子基础赋分
    if True:
        # 攻
        result = str1.find("20")
        if (result != -1):
            result = str1.find("020")
            if (result != -1):
                result = str1.find("00200")
                if (result != -1):
                    ChangeScoreValue(12.5, result)
                    ChangeScoreValue(25, result + 1)
                    ChangeScoreValue(25, result + 3)
                    ChangeScoreValue(12.5, result + 4)
                else:
                    result = str1.find("0200")
                    if (result != -1):
                        ChangeScoreValue(12.5, result)
                        ChangeScoreValue(12.5, result + 2)
                        ChangeScoreValue(6.25, result + 3)
                    else:
                        result = str1.find("0020")
                        if (result != -1):
                            ChangeScoreValue(12.5, result+1)
                            ChangeScoreValue(12.5, result + 3)
                            ChangeScoreValue(6.25, result)
                        else:#x020x
                            result = str1.find("020")
                            ChangeScoreValue(6.25, result + 2)
                            ChangeScoreValue(6.25, result)
            else:
                result = str1.find("200")
                if (result != -1):
                    ChangeScoreValue(12.5, result + 2)
                    ChangeScoreValue(6.25, result)
                else:#x20x
                    result = str1.find("20")
                    ChangeScoreValue(6.25/2, result+1)
        else:
            result = str1.find("02")
            if (result != -1):
                result = str1.find("002")
                if (result != -1):
                    ChangeScoreValue(12.5, result + 1)
                    ChangeScoreValue(6.25, result)
                else:  # x02x
                    result = str1.find("02")
                    ChangeScoreValue(6.25/2, result)


        # 守
        result = str1.find("10")
        if (result != -1):
            result = str1.find("010")
            if (result != -1):
                result = str1.find("00100")
                if (result != -1):
                    ChangeScoreValue(6.25, result)
                    ChangeScoreValue(12.5, result + 1)
                    ChangeScoreValue(12.5, result + 3)
                    ChangeScoreValue(6.25, result + 4)
                else:
                    result = str1.find("0100")
                    if (result != -1):
                        ChangeScoreValue(6.25, result)
                        ChangeScoreValue(6.25, result + 2)
                        ChangeScoreValue(6.25/2, result + 3)
                    else:
                        result = str1.find("0010")
                        if (result != -1):
                            ChangeScoreValue(6.25, result + 1)
                            ChangeScoreValue(6.25, result + 3)
                            ChangeScoreValue(6.25/2, result)
                        else:  # x020x
                            result = str1.find("010")
                            ChangeScoreValue(6.25/2, result + 2)
                            ChangeScoreValue(6.25/2, result)
            else:
                result = str1.find("100")
                if (result != -1):
                    ChangeScoreValue(6.25, result + 2)
                    ChangeScoreValue(6.25/2, result)
                else:  # x20x
                    result = str1.find("10")
                    ChangeScoreValue(6.25 / 4, result + 1)
        else:
            result = str1.find("01")
            if (result != -1):
                result = str1.find("001")
                if (result != -1):
                    ChangeScoreValue(6.25, result + 1)
                    ChangeScoreValue(6.25/2, result)
                else:  # x02x
                    result = str1.find("01")
                    ChangeScoreValue(6.25 / 4, result)


def AiRun():
    global round
    '''
    Ai调用函数，分割棋盘为字符串并送去检测赋分
    :return: Ai建议的x,y轴坐标
    '''
    global x, y, isDirectOut, type1, offset, Score
    Score = np.zeros((15, 15), dtype=np.float)
    x = y = 0
    isDirectOut = False

    # 分数加权AI

    # 先分别做片段剪出
    # 横
    type1 = 1
    for y in range(0, 15):
        str1 = ""
        for i in range(0, 15):
            str1 += str(chessBoard[y][i])

        # 送去检测
        result = FindChess(str1)
        if isDirectOut:
            return result, y
    x = y = 0

    # 竖
    type1 = 2
    for x in range(0, 15):
        str1 = ""
        for i in range(0, 15):
            str1 += str(chessBoard[i][x])

        # 送去检测
        result = FindChess(str1)
        if isDirectOut:
            return x, result

    x = y = 0
    # 左斜
    type1 = 3
    for offset in range(-14, 14):
        str1 = ""
        arr = np.diagonal(chessBoard, offset=offset)
        for i in arr:
            str1 += str(i)

        # 送去检测
        result = FindChess(str1)
        # 倾斜确认坐标的方案
        # 对正的offset  x=offset+result,y=result
        # 对负的offset  x=result,y=-offset+result
        if isDirectOut:
            return CoordinatesProcessing(result)

    x = y = 0
    # 右斜
    type1 = 4
    for offset in range(-14, 14):
        str1 = ""
        arr = np.fliplr(chessBoard)
        arr = np.diagonal(arr, offset=offset)
        for i in arr:
            str1 += str(i)

        # 送去检测
        result = FindChess(str1)
        # 倾斜确认坐标的方案
        # 对正的offset  x=14-offset-result,y=result
        # 对负的offset  x=14-result,y=-offset+result
        if isDirectOut:
            return CoordinatesProcessing(result)

    print("Ai Run Finish!Round is"+str(round))
    np.savetxt('Score/'+str(round)+'.csv', Score, delimiter=',')
    y, x = (np.where(Score == np.max(Score)))
    round+=2

    return x[0], y[0]
