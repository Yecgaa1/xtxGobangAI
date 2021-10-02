import numpy as np

x = y = type1 = offset = 0
isDirectOut = False
Score = np.zeros((15, 15), dtype=np.float)

chessBoard = np.zeros((15, 15), dtype=np.int32)


def ReFlashChessBoard():
    global chessBoard
    chessBoard = np.zeros((15, 15), dtype=np.int32)
    print("Fine?")
# 坐标处理
def CoordinatesProcessing(result):
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
    x, y = CoordinatesProcessing(result)
    Score[y][x] += value


# 本AI主攻！！！！，详情见笔记本
# 本AI只下白棋

def FindChess(str1):
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
        result = str1.find("0220")
        if (result != -1):
            ChangeScoreValue(100, result)
            ChangeScoreValue(100, result + 3)
        result = str1.find("0221")
        if (result != -1):
            ChangeScoreValue(50, result)
        result = str1.find("1220")
        if (result != -1):
            ChangeScoreValue(50, result + 3)

        # 守
        result = str1.find("0110")
        if (result != -1):
            ChangeScoreValue(50, result)
            ChangeScoreValue(50, result + 3)
        result = str1.find("0112")
        if (result != -1):
            ChangeScoreValue(25, result)
        result = str1.find("2110")
        if (result != -1):
            ChangeScoreValue(25, result + 3)

    # 单子基础赋分
    if True:
        # 攻
        result = str1.find("020")
        if (result != -1):
            ChangeScoreValue(25, result)
            ChangeScoreValue(25, result + 2)
        result = str1.find("021")
        if (result != -1):
            ChangeScoreValue(12.5, result)
        result = str1.find("120")
        if (result != -1):
            ChangeScoreValue(12.5, result + 2)

        # 守
        result = str1.find("010")
        if (result != -1):
            ChangeScoreValue(12.5, result)
            ChangeScoreValue(12.5, result + 2)
        result = str1.find("012")
        if (result != -1):
            ChangeScoreValue(6.25, result)
        result = str1.find("210")
        if (result != -1):
            ChangeScoreValue(6.25, result + 2)


def AiRun():
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

    print("Ai Run Finish!")
    y, x = (np.where(Score == np.max(Score)))

    return x[0], y[0]
