# 一个无视字符串的SUM实现过程
list1 = [1, 3.5, '2a', 'bb', 2]
list2 = []
for each in list1:
    if type(each) == int or type(each) == float:
        list2.append(each)
Summary = sum(list2)
print(Summary)
