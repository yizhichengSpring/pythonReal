# coding:utf-8
print("------------------跳一跳----------------")
print('欢迎回来，请开始游戏.......')
print('请输入(中心、音乐块、微信支付块)')
while True:
    wechat = str(input('请输入'))
    if wechat == '音乐块':
        print('您的分数为',30)
    elif wechat == '中心':
        print('您的分数为',32)
    elif wechat == '微信支付块':
        print('您的分数为',42)
