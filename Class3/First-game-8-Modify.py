print('-------------郑晗的Python学习之路-----------')
temp = input("不妨猜一下现在我心里想的是那个数：")
guess = int(temp)
times = 0
if guess == 8:
    print("卧槽，你是我心里的蛔虫嘛？！")
    print("哼，猜中了也没有奖励！")
else:
    while times < 3:
        print('剩余次数：'+ str(3-times))
        temp = input("哎呀，猜错了，请重新输入：")
        guess = int(temp)
        if guess == 8:
            print("卧槽，你是我心里的蛔虫嘛？！")
            print("哼，猜中了也没有奖励！")
        else:
            if guess > 8:
                print("大了大了！")
                times += 1
            else:
                print("小了小了！")
                times += 1
    print("一点都不默契，不玩啦！")
