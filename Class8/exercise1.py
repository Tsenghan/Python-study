#可以试错的次数
times = 3

#正确的密码
password = 'zhenghan'

 #循环体开始
yourtime = 0
while yourtime<times:
    passa = input('Please input your password:')
    if '*' in passa:
        print('You cannot input * as password strings.'
              'you have ' + str(times-yourtime) + ' times to retry')
    elif passa == password:
        print('Correct!')

        break
    else:
        yourtime+=1
        print('please retry')
        print('you have ' + str(times-yourtime) + ' times to retry')

#后续语句
if passa == password:
    print('Welcome login.')
else:
    print('GAME OVER')