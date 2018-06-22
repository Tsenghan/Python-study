# 闰年判断程序
Year = input('请输入四位年数：')
year = int(Year)
if (year/4 == int(year/4)) and (int(year/100) != year/100):   # 如何得到整除的结果？
    print(True)
elif year/400 == int(year/400):
    print(True)
else:
    print(False)
