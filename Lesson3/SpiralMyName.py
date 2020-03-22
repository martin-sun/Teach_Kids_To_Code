# SpiralMyName.py - 打印一百个彩色名字
#导入turtle模块
import turtle          
# 打开一个画图板
t = turtle.Pen()  
# 改变背景颜色
turtle.bgcolor("black") 
# 画笔的颜色有四种，红、黄、蓝、绿
colors = ["red", "yellow", "blue", "green"]
# 打开文本输入框，询问你的名字 
your_name = turtle.textinput("输入你的名字", "你叫什么名字？")
# 画一百个不同颜色的你的名字
for x in range(100):    
    t.pencolor(colors[x%4]) # 每移动一次就换一次颜色    
    t.penup()               # 把笔抬起来，不要画     
    t.forward(x*4)          # 让笔在屏幕上方移动     
    t.pendown()             # 落笔，准备写下你的名字
    t.write(your_name, font = ("Arial", int( (x + 4) / 4), "bold") )    # 写下你的名字
    t.left(92)              # 向左转92°