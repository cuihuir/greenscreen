#!/usr/bin/env python3
"""
简单的全屏颜色显示工具，用于显示器坏点检测
按空格键或鼠标左键切换颜色，按 'q' 键退出
"""

import tkinter as tk


class ScreenTest:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Screen Test")

        # 全屏设置
        self.root.attributes('-fullscreen', True)
        self.root.configure(cursor='none')  # 隐藏鼠标指针

        # 颜色列表
        self.colors = [
            '#FF0000',  # 红色
            '#00FF00',  # 绿色
            '#0000FF',  # 蓝色
            '#FFFFFF',  # 白色
            '#000000',  # 黑色
            '#FFFF00',  # 黄色
            '#00FFFF',  # 青色
            '#FF00FF',  # 洋红
        ]
        self.current_color_index = 0

        # 创建画布
        self.canvas = tk.Canvas(
            self.root,
            highlightthickness=0,
            bg=self.colors[self.current_color_index]
        )
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # 绑定事件
        self.root.bind('q', self.quit_app)
        self.root.bind('Q', self.quit_app)
        self.root.bind('<Escape>', self.quit_app)
        self.root.bind('<space>', self.next_color)
        self.canvas.bind('<Button-1>', self.next_color)

    def next_color(self, event=None):
        """切换到下一个颜色"""
        self.current_color_index = (self.current_color_index + 1) % len(self.colors)
        self.canvas.configure(bg=self.colors[self.current_color_index])

    def quit_app(self, event=None):
        """退出应用"""
        self.root.destroy()

    def run(self):
        """运行应用"""
        self.root.mainloop()


if __name__ == '__main__':
    app = ScreenTest()
    app.run()
