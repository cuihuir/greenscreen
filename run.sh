#!/bin/bash
# 启动脚本 - 使用虚拟环境运行屏幕检测应用

# 激活虚拟环境
source venv/bin/activate

# 检查 tkinter 是否可用
python -c "import tkinter" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "错误: tkinter 未安装"
    echo "请运行: sudo apt install python3-tk"
    deactivate
    exit 1
fi

# 运行应用
python screen_test.py

# 退出后自动停用虚拟环境
deactivate
