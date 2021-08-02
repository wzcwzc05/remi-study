# -*- coding:utf-8 -*-
import remi.gui as gui
from remi import start, App
#引入remi库

class MyApp(App):#创建MyApp类
    def __init__(self, *args):#初始化
        super(MyApp, self).__init__(*args)

    def main(self):#主程序
        container = gui.VBox(width=120, height=100)#设置容器宽度为120，高度为100
        self.lbl = gui.Label('Hello world!')#创建标签“Hello World”
        self.bt = gui.Button('Press me!')#创建按钮“Press me!”

        # 为鼠标点击按钮创造一个监听事件
        self.bt.onclick.do(self.on_button_pressed)

        # 添加部件
        container.append(self.lbl)
        container.append(self.bt)

        # 返回到根部件
        return container

    # 鼠标点击按钮的事件
    def on_button_pressed(self, widget):
        self.lbl.set_text('Button pressed!')
        self.bt.set_text('Hi!')

#开启服务器
start(MyApp)