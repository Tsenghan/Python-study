# 如何使int()实现四舍五入？
Number = input('请输入：')
number = float(Number)
low = int(number)
high = int(number) + 1
if (high - number) > (number - low):
    print(low)
else:
    print(high)
