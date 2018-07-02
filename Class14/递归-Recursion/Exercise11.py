#写一个函数get_digits(n)，将参数n分解出每个位的数字并按顺序存放到列表中。
# 举例：get_digits(12345) ==> [1, 2, 3, 4, 5]
def get_digits(num):
    list = []
    for i in range(len(str(num))):
        list.append(int(str(num)[i]))
    return list

#小甲鱼的递归
list = []
def get_digits2(num):
    if num>0:
        list.append(num % 10)
        get_digits(num // 10)
    return list
print(get_digits(445412135))