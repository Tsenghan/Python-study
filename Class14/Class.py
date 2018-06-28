#创建一个函数，名称为 Myfirstfunction
def Myfirstfunction():
    print('这是一个函数!第一个哦')
    print('我表示很激动！')
    print('再次我要感谢Python')
    print('人生苦短，我用PY')
Myfirstfunction()


#带参数的函数
def Mysecondfunction(name):
    print(name + ' i Love you!')

#带多个参数的函数
def add(num1,num2,num3):
    result = num1+num2+num3
    print(result)

#函数的返回值
def addrt(num1,num2,num3):
    result = num1+num2+num3
    return(result)