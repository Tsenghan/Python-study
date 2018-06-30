#内嵌函数
def fun1():
    print('fun1()is using....')
    def fun2():
        print('fun2 is using....')
    fun2()

#闭包
def funX(x):
    def funY(y):
       return x*y
    return funY()

def Fun1():
    x = 5
    def Fun2():
        x*=x
        return x
    return Fun2()
#这样会报错，可以使用容器类型改造：
def Fun1():
    x = [5]
    def Fun2():
        x[0]*=x[0]
        return x[0]
    return Fun2()
#在Python3中，有了新的方法：nonlocal
def Fun1():
    x = 5
    def Fun2():
        nonlocal x
        x*=x
        return x
    return Fun2()