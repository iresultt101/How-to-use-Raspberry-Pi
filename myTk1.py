import random
from tkinter import *
# import hashlib
# import time
import serial

ser = serial.Serial("/dev/ttyAMA0", 115200)

list_data = ['', '', '']


#
def get_data():
    """

    :return: 一次输出一个字符串（格式："A111111D"）
    """
    return random.sample(list_data, 1)[0]


class MY_GUI():
    def __init__(self, window):
        self.window = window
        self.var_label_A = StringVar()
        self.var_label_A.set("A000000D")
        self.var_label_B = StringVar()
        self.var_label_B.set("B000000D")
        self.var_label_C = StringVar()
        self.var_label_C.set("C000000D")

        self.set_init_window()
        self.window.mainloop()  # 父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示

    # 设置窗口
    def set_init_window(self):
        self.window.title("文本处理工具_v1.2")  # 窗口名
        # self.init_window_name.geometry('320x160+10+10')                         #290 160为窗口大小，+10 +10 定义窗口弹出时的默认展示位置
        self.window.geometry('1068x681+10+10')
        # self.init_window_name["bg"] = "pink"                                    #窗口背景色，其他背景色见：blog.csdn.net/chl0000/article/details/7657887
        # self.init_window_name.attributes("-alpha",0.9)                          #虚化，值越小虚化程度越高

        # 标签
        self.label_A = Label(self.window, textvariable=self.var_label_A)
        # self.label_A.grid(row=0, column=0)
        self.label_A.pack()

        self.label_B = Label(self.window, textvariable=self.var_label_B)
        # self.label_B.grid(row=1, column=0)
        self.label_B.pack()

        self.label_C = Label(self.window, textvariable=self.var_label_C)
        # self.label_C.grid(row=2, column=0)
        self.label_C.pack()

        self.window.after(100, self.update)

    # 功能函数
    def update(self):
        data = get_data()
        if len(data) == 11:
            if data[0] == "A" and data[-1] == "D":
                self.var_label_A.set(data)
            elif data[0] == "B" and data[-1] == "D":
                self.var_label_B.set(data)
            elif data[0] == "C" and data[-1] == "D":
                self.var_label_C.set(data)

        self.window.after(100, self.update)


if __name__ == '__main__':

    try:
        print("等待接收数据")
        while True:
            size = ser.inWaiting()               # 获得缓冲区字符
            if size != 0:
                response = ser.read(size)        # 读取内容并显示
                data=str(response)
                data=data[2:10]
                print(data)
                if len(data) == 8 :
                    if data[0] == "A":
                        list_data[0] = data
                        break
                    elif data[0] == "B":
                        list_data[1] = data
                        break
                    elif data[0] == "C":
                        list_data[2] = data
                        break
        print(list_data)
            #if list_data[0] is not '' and list_data[1] is not '' and list_data[2] is not '':
                #break


    except Exception as exc:
        print("读取异常", exc)

    init_window = Tk()  # 实例化出一个父窗口
    my_gui = MY_GUI(init_window)

