#coding=utf-8
import random


jSingles = {0: '零', 1: '一', 2: '二', 3: '三', 4: '四', 5: 'ご', 6: '六', 7: '七', 8: '八', 9: '九'}
jTens = ['', '十', '百', '千', '万']


def parsetoJNumeric(euroNum):
    jNum = ''
    i = 0;
    num = int(euroNum)
    while (num != 0):
        digit = num % 10
        num = num / 10
        if digit != 0:
            jNum = jSingles[digit] + jTens[i] + jNum
        i += 1
    return jNum

def genRandomJNums(r):
    total = r.split(" ")
    rangeMin = int(total[1])
    rangeMax = int(total[2])
    i = int(total[3])
    while i > 0:
        print parsetoJNumeric(random.randint(rangeMin, rangeMax))
        i -= 1

r = raw_input("Number: ")
if r.find(",") == -1:
    if r.find("rand") > -1:
        genRandomJNums(r)
    else:
        print parsetoJNumeric(r)

else:
    euroNumList = r.split(",")
    for num in euroNumList:
        print num + ': ' + parsetoJNumeric(num)

