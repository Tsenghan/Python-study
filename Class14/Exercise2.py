''''编写一个符合以下要求的函数：

    a) 计算打印所有参数的和乘以基数（base=3）的结果
    b) 如果参数中最后一个参数为（base=5），则设定基数为5，基数不参与求和计算。'''

def Customfunc(*inputs, base=3):
    if inputs[-1] == 5: #判断最后一个参数的值
        base = 5
    output = sum(inputs[0:-1]) * base   #切片求和
    return (output)

