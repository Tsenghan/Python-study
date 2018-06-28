'''寻找水仙花数：
题目要求：如果一个3位数等于其各位数字的立方和，则称这个数为水仙花数。
例如153 = 1^3+5^3+3^3，因此153是一个水仙花数。编写一个程序，找出所有的水仙花数。'''
start = 0
#判断水仙花数
def shuixianhua(num=0):
    number = str(num)
    numsum = 0
    for each in number:
        numsum += int(each)**3
    if numsum ==num:
        return(1)
    else:
        return(0)
#循环寻找所有水仙花数
for each in range(99,1000):
    if shuixianhua(each)==1:
        print(each)

