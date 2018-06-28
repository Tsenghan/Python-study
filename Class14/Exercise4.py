''''编写一个函数 findstr()，该函数统计一个长度为 2 的子字符串在另一个字符串中出现的次数。
例如：假定输入的字符串为
“You cannot improve your past, but you can improve your future. Once time is wasted, life is wasted.”，
子字符串为“im”，函数执行后打印“子字母串在目标字符串中共出现 3 次”。'''

#次数统计
def findstr(str1='test',str2='te'):
    'str1 is the target and str2 is the bullet'
    findcount=str1.count(str2)
    return(findcount)
#调用函数
target = input('请输入目标字符串：')
bullet = input('请输入子字符串（两个字符）：')
print('子字符串在目标中共出现了'+str(findstr(target,bullet))+'次')