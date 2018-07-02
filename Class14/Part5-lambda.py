def ds(x):
    return 2*x +1

#等价于
ds=lambda x:2*x+1


#一个奇数过滤器
def add(x):
    return x%2
temp = range(10)
show = filter(add,temp)
list(show)
#lambda实现
list(filter(lambda x:x%2,range(10)))

#合并列表
list(map(lambda x,y:[x,y],[1,3,5,7,9],[2,4,6,8,10]))
#Out: [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]