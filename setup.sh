#!/bin/bash
# 安装脚本 - 为 OrangePi RK3566 配置环境

echo "正在安装系统依赖..."
sudo apt update
sudo apt install -y python3-tk

echo ""
echo "创建虚拟环境..."
if ! python3 -m venv venv; then
    echo ""
    echo "✗ 虚拟环境创建失败！"
    echo ""
    PYTHON_VERSION=$(python3 --version 2>&1 | grep -oP '\d+\.\d+')
    echo "请先安装 python3-venv 包："
    echo "  sudo apt install python3-venv"
    if [ ! -z "$PYTHON_VERSION" ]; then
        echo "或者针对当前 Python $PYTHON_VERSION："
        echo "  sudo apt install python${PYTHON_VERSION}-venv"
    fi
    echo ""
    exit 1
fi

echo ""
echo "✓ 环境配置完成！"
echo "现在可以运行: ./run.sh"
