#尝试利用字典的特性编写一个通讯录程序吧，功能如图
print('----欢迎进入通讯录程序----')
print('----1、查询联系人资料-----')
print('----2、添加新的联系人-----')
print('----3、删除已有联系人-----')
print('----4、退出程序-----------')
card = {'小甲鱼':'020-8897425'}
while 1:
    sub = input('\n请输入相关指令代码：')
    if sub == '1':
        name = input('\n请输入联系人姓名：')
        if name in card:
            print(name,':',card[name])
        else:
            print('查无此人！')

    elif sub == '2':
        name = input('\n请输入联系人姓名：')
        if name in card:
            print('您输入的姓名已存在--->',name,':',card[name])
            ischange = input('是否修改用户资料？（yes/no）')
            if  ischange == 'yes':
                card[name]=input('请输入用户联系电话：')
            print(name, ':', card[name], '已更新')
        else:
            card[name]=input('请输入电话号码')

    elif sub == '3':
        name = input('\n请输入联系人姓名：')
        if name in card:
            value = card.pop(name)
            print(name,':',value,'已删除')
        else:
            print('查无此人！')

    elif sub == '4':
        print('|---感谢您使用通讯录程序---|')
        break
    else:
        print('输入有误，请重新输入。')
