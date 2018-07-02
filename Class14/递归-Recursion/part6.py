''''写一个求阶乘的函数
---n！= n*(n-1)*(n-2)*....*2*1'''


#非递归版本：
def stage(x):
    out = 1
    for i in range(x):
        if x>1:
            out*=x
            x-=1
        else:
            return out
print(stage(5))

#递归版本：
def factorial(n):
    if n ==1:
        return 1
    else:
        return  n*factorial(n-1)
number = int(input('please input:'))
result = factorial(number)
print(number,'\'s factorial is:',result)