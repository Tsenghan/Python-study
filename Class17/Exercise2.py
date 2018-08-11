#编写一个程序，比较用户输入的两个文件，如果不同，显示出所有不同处的行号与第一个不同字符的位置
file1 = input('请输入需要比较的第一个文件名称：')
open_file1 = open(file1)
file2 = input('请输入需要比较的第二个文件名称：')
open_file2= open(file2)
#开始比较
differs = [] #存放不同的值
length = len(open_file1.read()) #判断两者的长度
open_file1.seek(0,0) #指针复位
for each in range(length):
    if open_file1.read(1) != open_file2.read(1):
        differs.append(open_file1.tell())
#print
print('两个文件共有',len(differs),'处不同：')
for each in differs:
    print('第',each,'个字符不一样')