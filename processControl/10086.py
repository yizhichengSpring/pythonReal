print('------------------10086查询功能-------------------')
print('输入1，查询当前余额')
print('输入2，查询当前剩余流量')
print('输入3，查询当前剩余通话')
print('输入0，退出自助查询系统')
while True:
    num = int(input())
    if num == 1:
        print('当前余额为:999元')
    elif num == 2:
        print('当前剩余流量为:5G')
    elif num == 3:
        print('当前剩余通话为:189分钟')
    else:
        print('退出自助查询系统')
        break

