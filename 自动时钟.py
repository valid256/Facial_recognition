import tkinter as tk
from time import strftime

# 创建一个窗口
window = tk.Tk()
window.title("自动时钟")

# 定义一个函数来获取当前时间并更新标签上的时间
def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

# 创建一个标签用于显示时间
label = tk.Label(window, font=('calibri', 40, 'bold'), background='purple', foreground='white')
label.pack(anchor='center')

# 调用time函数开始更新时间
time()

# 运行窗口主循环只是随随便便的我真的会谢
window.mainloop()
