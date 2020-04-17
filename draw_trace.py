import tcp_Spectrum as instr
import re
from matplotlib import pyplot as plt 
import numpy as np


inst=instr.open('10.0.6.150',5025)
if inst==-1:
    connection_flag=False
else:
    connection_flag=True

name=instr.query(inst,'*IDN?')#获取频谱仪名称
freq_start=float(instr.query(inst,'FREQ:STAR?'))#获取频谱仪开始频率
freq_stop=float(instr.query(inst,'FREQ:STOP?'))#获取频谱仪截至频率
ref_pow=float(instr.query(inst,'DISP:WIND:TRAC:Y:RLEV?'))#获取频谱仪参考电平
div=float(instr.query(inst,'DISP:WIND:TRAC:Y:PDIV?'))#获取频谱仪每格多少dB


if connection_flag:    
    plt.ion() #开启一个画面
    while True: #轮询读取频谱仪TRACE
        #获取迹线
        trace=instr.query(inst,'TRAC? TRACE1')
        str_lst= re.split(r',',trace)
        #效验数据长度
        data_len= len(str_lst)

        #绘制频谱初始化
        plt.clf()  
        plt.grid()        
        plt.suptitle(name,fontsize=15)
        plt.xlim(freq_start,freq_stop)
        plt.ylim(ref_pow-div*10,ref_pow)    

        if data_len==1001 or data_len==401:#数据长度为1001或401时继续处理数据，否则数据包不完整
            #数据处理
            y=np.asarray(str_lst,dtype='float64')
            x=np.linspace(freq_start,freq_stop,len(y))
            #绘制频谱                      
            plt.plot(x,y)
            plt.pause(0.1)
            plt.ioff()
        else:            
            plt.pause(0.1)
            plt.ioff()
        
instr.close(inst)