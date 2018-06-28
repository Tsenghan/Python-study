def newfunction(para):
    'There is the Function documents'
    #上一行是函数文档
    print('函数中，'+para+'才是具体的参数值！')
#关键字参数
def Saysome(name,words):
    print(name + '->'+ words)
#默认参数
def Saysome(name='default1',words='default2'):
    print(name + '->'+ words)
#收集参数
def test(*params):
    print('参数的长度是：',len(params))
    print('第二个参数是：',params[1])

def test(*params,para1='default1',para='default2'):
    print('参数的长度是：',len(params))
    print('第二个参数是：',params[1])