#编写一个程序，接受用户的输入并保存为新的文件
filename = input('请输入文件名：')
newfile = open (filename+'.txt','w')
while 1:
    content = input('''请输入内容【单独输入':w'保存退出]:''')
    if content == ':w':
        newfile.close()
        break
    else:
        newfile.write(content)

