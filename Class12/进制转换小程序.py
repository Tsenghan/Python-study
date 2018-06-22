while 1:
    number=input('请输入一个整数：')
    if number == 'Q':
        break
    else:
        numeric = int(number)
        #十六进制
        print('十进制-->十六进制:{0:}-->{1:#x}'.format(number,numeric))
        #八进制
        print('十进制-->八进制:{0:}-->{1:#o}'.format(number, numeric))
        #二进制
        print('十进制-->二进制:{0:}-->{1}'.format(number, bin(numeric)))

