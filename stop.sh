#!/bin/bash
# 停止脚本 - 强制关闭正在运行的屏幕检测应用

echo "正在终止 screen_test.py 进程..."

pkill -9 -f screen_test.py

sleep 0.5

# 验证
if pgrep -f "screen_test.py" > /dev/null; then
    echo "✗ 进程仍在运行，请手动执行: pkill -9 -f screen_test.py"
    exit 1
else
    echo "✓ 进程已终止"
    exit 0
fi
