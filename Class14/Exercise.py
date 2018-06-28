#编写一个函数power()模拟内建函数pow()，即power(x, y)为计算并返回x的y次幂的值。
def power(x,y):
    return(x**y)

#编写一个函数，利用欧几里得算法（脑补链接）求最大公约数，例如gcd(x, y)返回值为参数x和参数y的最大公约数。
def gcd(x,y):
    while x != 0:
        x, y = y % x, x
    return y

#编写一个将十进制转换为二进制的函数，要求采用“除2取余”（脑补链接）的方式，结果与调用bin()一样返回字符串形式。
def tobin(x):
    temp = x #保存原始的数字
    if type(x) != int:  #判断输入合法性
        return(print('input error! Only int can be accepted.'))

    elif x ==0:
        return('0b0')
    else:
        if x < 0:
            x = -x  #转换为正数计算
        char1 = ''  #建立一个空的字符串
        while x != 0:   #被除数不为零，则开始循环
            rest = x%2  #计算被除数除以二的余数
            char1 += str(rest)  #把余数写入
            x //=2  #除以2的商，重新作为被除数
        char2 = 'ob'+ char1[::-1]   #反转字符串，加入前缀
        #输出：
        if temp <0:
            return '-' + char2
        else:
            return char2
