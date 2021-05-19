#导入库：解析utf-16le & plot库
from codecs import open
import pylab as pl 
from matplotlib.pyplot import MultipleLocator

#1. 核心函数：根据输入的时间范围数据并清洗读取，导出为x,y两个列表。x为时间，y为压力值。
def data_flush(raw_data,hours_last = 24):
    #判断文件总行数
    lines = len(raw_data)
    min_last = 60*hours_last
    #开始提取有效数据行
    x1,x2,y,z = [],[],[],[]
    line_count = int(min_last*2) #计算单变量总行数
    #print('共检索到',line_count,'条数据')
    if line_count >= lines:
        print('!!! 输入超出已有数据范围，系统将自动显示最近12h的数据')
        line_count = 1440
    for row in range(lines-line_count,lines):
        row_ts = float(raw_data[row][-20:-2]) #提取本行时间戳
        row_name = raw_data[row][4:6] #提取本行变量名
        #if row_ts  > ts_start: #数据范围核查
        if row_name != '18': #变量名筛选
            y.append(float(raw_data[row][31:36])) #提取压力值
            x1.append(raw_data[row][10:26]) #提取时间值
        else: 
            x2.append(raw_data[row][9:25]) #提取时间值
            z.append(float(raw_data[row][30:33])) #提取温度值
    return x1,x2,y,z,
#2. 绘图函数
def plot_pic(x,y,x_locator=180,y_locator = 0.5,*para):
    #建立图表区
    fig = pl.figure(figsize=(15,5))
    print('-------------------------------------------------')
    print('{}图正在绘制，请稍后。。。。'.format(para[4]))
    #定义刻度密度
    #根据图片大小自动计算坐标轴密度
    x_locator = int(len(x)/7)
    x_major_locator=MultipleLocator(x_locator) #把x轴的刻度间隔设置为默认180分钟，并存在变量里
    y_major_locator=MultipleLocator(y_locator) #把x轴的刻度间隔设置为0.5，并存在变量里
    ax = pl.gca()
    ax.xaxis.set_major_locator(x_major_locator) #把x轴的主刻度间隔设置为变量值
    ax.yaxis.set_major_locator(y_major_locator) #把y轴的主刻度间隔设置为变量值
    #坐标轴标题
    pl.xlabel(para[1])
    pl.ylabel(para[0])
    #坐标轴范围
    pl.ylim(para[2], para[3])
    pl.grid() #打开网格
    pl.plot(x, y,color='r',linestyle = '-')
    #输出
    pl.savefig('./作图/{2}变化_{1}至{0}.jpg'.format(x[-1],x[0],para[4]))
    #简单的交互
    print('完成！')
    print('以下是{0}到{1}时间范围内约{2}小时的{3}变化曲线：'.format(x[0],x[-1],round(len(x)/60),para[4]))
    pl.show()
#3. 输入判断器
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False   

#主程序开始
data= open('Data_log_10.txt',encoding="UTF-16-LE") #打开文件
#读取原始数据到列表
raw_data= data.readlines() 
#输入数据
hours_last_input = input('请输入小时数：')
hours_last = 24
if is_number(hours_last_input):
    hours_last = float(hours_last_input)
else:
    print('输入有误，系统自动显示最近24h的数据')

#调用函数方法
x1,x2,y,z= data_flush(raw_data,hours_last)
# 释放内存
data.close()
'''
绘图函数参数：
plot(x,y,x坐标密度,y坐标密度,*[y坐标轴标题, x坐标轴标题, y下限, y上限, y标签])
'''
plot_pic(x1,y,x_locator,0.5,*['Pressure /Mpa', 'Time /min',0,8,'压力'])
plot_pic(x2,z,x_locator,1,*['T /°C', 'Time / min',175,190,'温度'])
