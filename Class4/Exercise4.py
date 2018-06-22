import random
num = random.randint(1,100) # 生成随机数
print('-------------郑晗的Python学习之路-----------')  # Title
print("不妨猜一下现在我心里想的是那个数：")  # 第一次询问,仅供屏显
times = 3   # 开始倒计数
guess = 0   # 引入guess变量
while times > 0 and guess != num:   # 进入循环条件：没猜对且次数有剩余（第一次默认没有猜对）
    print('Ps:(还有'+ str(times) + '次机会)')
    temp = input()  # 得到用户输入的字符串
    times -= 1  # 次数少一
    if times>0:
    # 进入判断程序
        if temp.isdigit():
            guess = int(temp)  # 转化为整型
            if guess == num:    # 正误判断句
                print("卧槽，你是我心里的蛔虫嘛？！")
                print("哼，猜中了也没有奖励！")
                break
            else:
                if guess > num: # 大小判断句
                    print("大了大了！")
                    print("哎呀，猜错了，请重新输入：")
                else:
                    print("小了小了！")
                    print("哎呀，猜错了，请重新输入：")
        else:
            print('输入有误！输入一个整数！：')
    else:
        print("一点都不默契，不玩啦！")





