'''编写一个函数，判断传入的字符串参数是否为“回文联”（
回文联即用回文形式写成的对联，既可顺读，也可倒读。例如：上海自来水来自海上）'''
def panduanhuiwen(str1):
    str2 = str1[::-1]
    if str1 ==str2:
        return '是'
    else:
        return '不是'
str1=input('请输入一句话：')
print(panduanhuiwen(str1)+'回文联')