# coding:utf-8
# 适用口袋机型号 JC-STC

from time import sleep
from mcu import Jkmcu

#Windows -> port='COMX', X is 0,1,2,3... as your computer
#Linux -> port='/dev/xxx.xxxusbserialxxx'

demo = Jkmcu(port = "/dev/cu.wchusbserial1410")


#LED灯,LD0-LD3 number:0-3, status:0灭，1亮
#led(number, statuse)
for i in range(4):
	demo.led(i,0)
	sleep(0.5)
	demo.led(i,1)


#hc595流水灯,L0-L7
#hc595(0-255) 发送数据给hc595
a = 1
i = 0
while 1:
	demo.hc595(a << i)
	sleep(0.5)
	i += 1
	if i == 8:
		break

#OLED显示初始位置 （X,Y）显示字符串s
#oled(x,y,s)
for i in range(7):
	demo.oled(9*i,i,"Python")
	sleep(0.5)

demo.oled(10,4,"K0-3->LD0-3")

#按键,K0 K1 K2 K3 -> LD0 LD1 LD2 LD3
#key(0-6) 返回按键状态
while(1):
	for i in range(4):
		if demo.key(i):
			demo.led(i,0)
		else:
			demo.led(i,1)
