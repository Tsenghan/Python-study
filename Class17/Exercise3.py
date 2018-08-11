#编写一个程序，当用户输入文件名和行数（N）后，将该文件的前N行内容打印到屏幕上
filename = input('请输入要打开的文件：')
file = open('filename')
lines = int(input('请输入要显示前几行：'))
for each in range(lines):
    print(file.readline())
file.seek(0,0)
#用户可以随意输入需要显示的行数
linerange =input('请输入行数范围：')
line_start =int(linerange.split(':')[0])
line_end =int(linerange.split(':')[1])
for each in range(line_end):
    if each >= line_start-1:
        print(file.readline())
    else:
        file.readline()

