''''编写一个程序，实现“全部替换”功能'''''

filename = input('请输入文件名：')
file_origin = open(filename,'r')
char_origin = input('请输入想要替换的字符：')
char_replace = input('请输入新的字符：')
length = len(file_origin.read())
file_origin.seek(0,0)
file_new = ''
#查找替换
dict = {}
for each in range(length):
    char = file_origin.read(1)
    if char == char_origin:
        dict[each]=char
        file_new += char_replace
    else:
        file_new += char
#print(dict)
#print(file_new)
#保存文件
file_replace = open(filename,'w')
file_replace.write(file_new)
file_replace.close()