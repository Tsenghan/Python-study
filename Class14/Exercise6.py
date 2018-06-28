'''编写一个函数，分别统计出传入字符串参数（可能不只一个参数）的英文字母、空格、数字和其它字符的个数。'''
def charcount(*str1):
    for chars in str1:  #按顺序取用收集参数，赋值给chars
        digit = 0   #数字，初始化
        letter = 0  #字母，初始化
        space = 0   #空格，初始化
        others = 0  #其他，初始化
        #使用循环体判断并统计子字符串chars中各种类字符的个数
        for each in chars:
            if each.isdigit():
                digit+=1
            elif each.isalpha():
                letter+=1
            elif each.isspace():
                space+=1
            else:
                others+=1
        #格式化输出打印字符。
        print('第{0}个字符串中有:{1}个数字,{2}个字母，{3}个空格,{4}个其他字符'.format(str1.index(chars)+1, digit, letter, space,others))
