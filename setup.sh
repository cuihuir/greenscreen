#!/bin/bash
# 安装脚本 - 为 OrangePi RK3566 配置环境

echo "正在安装系统依赖..."
sudo apt update
sudo apt install -y python3-tk

echo ""
echo "环境配置完成！"
echo "现在可以运行: ./run.sh"
