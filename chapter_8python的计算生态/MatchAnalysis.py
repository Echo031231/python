# 体育竞技分析-实例
from random import random


# 输出一些介绍信息
def printIntro():
    print("这个程序模拟两个选手A和B的某种竞技比赛")
    print("程序运行时需要A和B的能力值(以0-1之间的小数表示)")


# 获得用户输入
def getInputs():
    a = eval(input("请输入选手A的能力值(0-1):"))
    b = eval(input("请输入选手B的能力值(0-1):"))
    n = eval(input("模拟比赛的场次:"))
    return a, b, n


# 需要使用probA和probB模拟n场比赛
def simNGames(n, probA, probB): 
    winsA, winsB = 0, 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA += 1
        else:
            winsB += 1
    return winsA, winsB

# 一场比赛模拟函数
def simOneGame(probA, probB):
    scoreA, scoreB = 0, 0
    serving = "A"
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA / (probA + probB):
                scoreA += 1
            else:
                serving = "B"
        else:
            if random() < probB / (probA + probB):
                scoreB += 1
            else:
                serving = "A"
    return scoreA, scoreB


# 比赛结束条件函数
def gameOver(a, b):
    return a == 15 or b == 15


def printSummary(winsA, winsB):
    n = winsA + winsB
    # 在格式化输出时，{:0.1%} 是用来将小数转化为百分比格式并保留一位小数
    print("竞技分析开始,共模拟{}场比赛".format(n)) 
    print("选手A获胜{}场比赛,占比{:0.1%}".format(winsA, winsA/n))
    print("选手B获胜{}场比赛,占比{:0.1%}".format(winsB, winsB/n))


def main():
    # 输出一些介绍信息
    printIntro()
    # 获得用户输入
    probA, probB, n = getInputs()
    # 需要使用probA和probB模拟n场比赛
    winsA, winsB = simNGames(n, probA, probB)
    # 输出结果
    printSummary(winsA, winsB)
    
main()







