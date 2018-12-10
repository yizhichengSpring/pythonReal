#coding:utf-8
import random
print('------猜数字游戏------')
num = random.randint(0,10)
print(num)
while True:
    randomNum = input('请输入1-10之间的任何一个数')
    if num > int(randomNum):
        print('太小了')
    elif int(randomNum) > num:
        print('太大了')
    elif int(randomNum) == num:
        print('猜对了')
        break

