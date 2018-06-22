#列表表达式
list0= []
for x in range (10):
    for y in range(10):
        if x%2 ==0:
            list0.append(x)
            if y%2 !=0:
                list0.append(y)
                print(list0)
            list0.clear()

#或者
list1= []
for x in range(10):
    for y in range(10):
        if x%2 == 0:
            if y%2 != 0:
                list1.append((x, y))
print(list1)

#或者
>>> list1 = [(x, y) for x in range(10) for y in range(10) if x%2==0 if y%2!=0]