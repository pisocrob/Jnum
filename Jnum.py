#coding=utf-8




#romanNumList = raw_input("Numbers: ").split(',')


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

r = raw_input("Number: ")

if r.find(",") == -1:
    print parsetoJNumeric(r)
else:
    euroNumList = r.split(",")
    for num in euroNumList:

        print num + ': ' + parsetoJNumeric(num)

