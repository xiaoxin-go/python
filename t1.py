from tkinter import *
import random
fontsize = 30
colors = ['red','green','blue','yellow','orange','cyan','purple']

#打开一个窗口，取随机颜色，并更改label的前景色
def onSpam():
    popup = Toplevel()
    color = random.choice(colors)
    Label(popup, text='Popup', bg='black', fg=color).pack(fill=BOTH)
    mainLabel.config(fg=color)

#随机更改label的前景色，每隔250毫秒更改一次
def onFlip():
    mainLabel.config(fg=random.choice(colors))
    main.after(250,onFlip)

#加大label字体，每隔100秒触发一次
def onGrow():
    global fontsize
    fontsize += 5
    mainLabel.config(font=('arial', fontsize, 'italic'))
    main.after(100, onGrow)

main = Tk()                         #创建主窗口
mainLabel = Label(main, text='Fun Gui!', relief=RAISED)     #创建label
mainLabel.config(font=('arial', fontsize, 'italic'), fg='cyan', bg='navy')      #配置label字体背景颜色和前景颜色
mainLabel.pack(side=TOP,expand=YES,fill=BOTH)                #显示label
Button(main, text='spam', command=onSpam).pack(fill=X)      #创建按钮，触发onSpam
Button(main, text='flip', command=onFlip).pack(fill=X)      #触发onFlip
Button(main, text='grow', command=onGrow).pack(fill=X)      #触发onGrow
main.mainloop()                                              #启动主窗口