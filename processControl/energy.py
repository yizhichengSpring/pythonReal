# coding: utf-8
flag = True
while flag:
    print('查询能力请输入能量来源！退出程序请输入0')
    print('能量来源入下:\n生活缴费、行走捐、共享单车、线下支付、网络购票')
    type = input()
    if type!='0':
        print('200g')
    else:
        flag = False
        print('已退出')

