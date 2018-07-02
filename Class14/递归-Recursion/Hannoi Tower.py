# 递归-汉诺塔解法实践
def hanoi(n,x,y,z):
    if n == 1:
        print (x, '-->',z)
    else:
        hanoi(n-1,x,z,y)# 将前n-1个从x移动到y
        print(x,'--->',z)# 将最底下的最后一个盘子从x移动到z
        hanoi(n-1,y,x,z)# 将y上的n-1个移动到z上
hanoi(8,'x','y','z')