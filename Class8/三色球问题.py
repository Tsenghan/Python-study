#红黄蓝三色球12只，放在一个盒子里，从中间任意摸8个。算出各种球的搭配。
print('r|y|g')
for red in range(0,4):  #红球可能的数目：0-4
    for yellow in range(0,4):       #黄球可能的数目：0-4
        for green in range (2,7):   #绿球可能的数目：2-7
            if red + yellow +green ==8:
                print(red,'|',yellow,'|',green)