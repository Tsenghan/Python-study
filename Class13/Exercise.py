#一个简单的查询，An very simple quest
name = input('Please input yuour name')
score = [['a',85],['b',80],['c',65],['d',95],['e',90]]

for each in score:
    if each[0] == name:
        print(name + '\'s score is:',each[1])
        break
if name not in each:
    print('don\'t exist!')