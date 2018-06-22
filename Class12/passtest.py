''' 密码安全性检查代码

 低级密码要求：
   1. 密码由单纯的数字或字母组成
   2. 密码长度小于等于8位

 中级密码要求：
   1. 密码必须由数字、字母或特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）任意两种组合
   2. 密码长度不能低于8位

 高级密码要求：
   1. 密码必须由数字、字母及特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）三种组合
   2. 密码只能由字母开头
   3. 密码长度不能低于16位'''

sym1=r"~!@#$%^&*()_=-/,.?<>;:[]{}|\""#定义字符类型
loop = True#默认开启循环
middin = False#默认没有特殊字符
passwd = input('请设定密码：')
while loop:

    #位数测试
    changdu=len(passwd)
    #成分测试
    lowin=passwd.isalnum()#纯数字字母，为低等级
    for each in passwd:
        if each in sym1:
            middin=True
        break
    highin=passwd[0].isalpha()#首位为字母，为高等级

    #输出结果
    if changdu>16 and highin:
        print('您的密码评级为：高'
              '请继续保持！')
        loop= False
        break
    elif changdu >8 and middin is True:
        print('您的密码评级为：中'
              '请以一下方法提升您的密码等级：'
              '1. 密码必须含数字、字母及特殊字符'
              '2. 密码不低于16位'
              '3. 密码以字母开头')
    else:
        print('您的密码评级为：低'
              '请以一下方法提升您的密码等级：'
              '1. 密码必须含数字、字母及特殊字符'
              '2. 密码不低于16位'
              '3. 密码以字母开头'
              ' ')
    passwd = input('请重新设定密码：')

