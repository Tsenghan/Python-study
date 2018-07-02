#斐波那契数列的迭代实现
def phii(n):
    if n ==1 or n ==2:
        return 1
    else:
        start =[1,1]
        for i in range(2,n):
            start.append(start[i-1]+start[i-2])
        return(start[n-1])

#小甲鱼的迭代实现：
def fab(n):
    n1=1
    n2=1
    n3=1
    if n<1:
        print('error')
        return -1
    while(n-2)>0:
        n3 = n2+n1
        n1 = n2
        n2=n3
        n-=1
    return n3

#递归实现：
def phiina(n):
    if n ==1 or n ==2:
        return 1
    else:
        return phiina(n-1)+phiina(n-2)
