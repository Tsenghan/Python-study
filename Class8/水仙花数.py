#求100-999之间的所有水仙花数

for i in range(100,999):
    temp = i
    a=temp%10 #个位数
    b=(temp//10)%10 #十位数
    c=temp//100
    sum = a**3+b**3+c**3
    if temp == sum:
        print(temp)
