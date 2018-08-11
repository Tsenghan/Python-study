#打开并打印文件到屏幕

f = open('Openme.mp3')
for each_line in f:
    print(each_line)

#另存文件
f.seek(0,0)
new = open('OpenMe.txt','w')
for each in f:
    new.write(each)
    new.close()
#或者
new.write(f.read())