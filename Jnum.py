#coding=utf-8
import string



#romanNumList = raw_input("Numbers: ").split(',')
r = raw_input("Number: ")

jSingles = {0: '零', 1: '一', 2: '二', 3: '三', 4: '四', 5: 'ご', 6: '六', 7: '七', 8: '八', 9: '九'}
jTens = ['', '十', '百', '千', '万']


def ParsetoJNumeric(romanNum):
    jNum = ''
    i = 0;
    num = int(romanNum)
    while (num != 0):
        digit = num % 10
        num = num / 10
        if digit != 0:
            jNum = jSingles[digit] + jTens[i] + jNum
        i += 1

    return jNum

print ParsetoJNumeric(r)