#!/usr/bin/env python3
"""
简单的全屏颜色显示工具，用于显示器坏点检测
按空格键或鼠标左键切换颜色，按 'q' 键退出
"""

import argparse
import tkinter as tk


class ScreenTest:
    # 预定义的颜色映射
    COLOR_MAP = {
        'green': '#00FF00',
        'red': '#FF0000',
        'blue': '#0000FF',
        'white': '#FFFFFF',
        'black': '#000000',
        'yellow': '#FFFF00',
        'cyan': '#00FFFF',
        'magenta': '#FF00FF',
    }

    # 默认颜色列表
    DEFAULT_COLORS = [
        
        '#00FF00',  # 绿色
        '#FF0000',  # 红色
        '#0000FF',  # 蓝色
        '#FFFFFF',  # 白色
        '#000000',  # 黑色
        '#FFFF00',  # 黄色
        '#00FFFF',  # 青色
        '#FF00FF',  # 洋红
    ]

    def __init__(self, colors=None):
        self.root = tk.Tk()

        # 设置颜色列表
        self.colors = colors if colors else self.DEFAULT_COLORS
        self.current_color_index = 0

        # 先隐藏窗口，避免显示中间状态
        self.root.withdraw()

        # 全屏设置
        self.root.attributes('-fullscreen', True)
        self.root.attributes('-topmost', True)
        self.root.configure(cursor='none')  # 隐藏鼠标指针

        # 获取屏幕尺寸并设置窗口
        self.root.update_idletasks()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f'{screen_width}x{screen_height}+0+0')

        # 创建画布
        self.canvas = tk.Canvas(
            self.root,
            highlightthickness=0,
            bg=self.colors[self.current_color_index]
        )
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # 所有设置完成后再显示窗口
        self.root.deiconify()
        self.root.focus_force()

        # 绑定事件
        self.root.bind('q', self.quit_app)
        self.root.bind('Q', self.quit_app)
        self.root.bind('<Escape>', self.quit_app)
        self.root.bind('<Control-c>', self.quit_app)  # Ctrl+C
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


def parse_args():
    """解析命令行参数"""
    parser = argparse.ArgumentParser(
        description='全屏颜色显示工具，用于显示器坏点检测',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  %(prog)s                    # 显示所有颜色（可切换）
  %(prog)s --color green      # 只显示绿色
  %(prog)s --color red blue   # 只显示红色和蓝色
  %(prog)s --color '#00FF00'  # 使用十六进制颜色值
        """
    )

    parser.add_argument(
        '-c', '--color',
        nargs='+',
        metavar='COLOR',
        help='指定要显示的颜色（可选: red, green, blue, white, black, yellow, cyan, magenta 或十六进制颜色值如 #00FF00）'
    )

    return parser.parse_args()


def main():
    """主函数"""
    args = parse_args()

    # 处理颜色参数
    colors = None
    if args.color:
        colors = []
        for color in args.color:
            # 检查是否是预定义颜色名称
            if color.lower() in ScreenTest.COLOR_MAP:
                colors.append(ScreenTest.COLOR_MAP[color.lower()])
            # 检查是否是十六进制颜色值
            elif color.startswith('#') and len(color) == 7:
                colors.append(color.upper())
            else:
                print(f"警告: 未知颜色 '{color}'，已忽略")

        if not colors:
            print("错误: 没有有效的颜色参数")
            return

    app = ScreenTest(colors=colors)
    app.run()


if __name__ == '__main__':
    main()
