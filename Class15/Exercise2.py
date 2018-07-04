#尝试编写一个用户登录程序（这次尝试将功能封装成函数），程序实现如图：
print('|---新建用户N/n---|')
print('|---登陆账号E/e---|')
print('|---退出程序Q/q---|')
sql = {}
def add(name):
    '注册方法'
    while name in sql:
        name = input('此用户名已经被使用，请重新输入：')
    passwd = input('请输入密码：')
    passtest(passwd)
    sql[name] = passwd
    return print('注册成功！,赶紧登陆试试吧！')

def login(name,passwd):
    '登陆方法'
    while name not in sql:
        name = input('用户名不存在！请重新输入：')
    if sql[name]!=passwd:
        return print('密码错误！')
    else:
        return print('登陆成功！')

def passtest(passwd):
    '密码可用性评估'
    sym1 = r"~!@#$%^&*()_=-/,.?<>;:[]{}|\""  # 定义字符类型
    loop = True  # 默认开启循环
    middin = False  # 默认没有特殊字符
    while loop:
        # 位数测试
        changdu = len(passwd)
        # 成分测试
        lowin = passwd.isalnum()  # 纯数字字母，为低等级
        for each in passwd:
            if each in sym1:
                middin = True
            break
        highin = passwd[0].isalpha()  # 首位为字母，为高等级

        # 输出结果
        if changdu > 16 and highin:
            print('您的密码评级为：高'
                  '请继续保持！')
            loop = False
            break
        elif changdu > 8 and middin is True:
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

while 1:
    sub = input('---请输入指令代码：')
    if sub == 'n' or sub=='N':
       name = input('请输入新用户名：')
       add(name)
    elif sub == 'e'or sub=='E':
        name = input('请输入您的用户名：')
        passwd = input('请输入密码：')
        login(name,passwd)
    elif sub == 'Q'or sub=='q':
        print('谢谢使用！')
        break
    else:
        print('输入有误,请重试！')