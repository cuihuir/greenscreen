# GreenScreen

简单的全屏颜色显示工具，用于显示器坏点检测。

## 快速开始

```bash
# 首次运行：安装依赖
./setup.sh

# 启动应用
./run.sh

# 停止应用（SSH 模式下）
./stop.sh
```

## 使用方法

### 默认模式 - 显示所有颜色
```bash
./run.sh
```
按空格键或鼠标左键切换颜色（红、绿、蓝、白、黑、黄、青、洋红）

### 指定颜色
```bash
./run.sh --color green              # 只显示绿色
./run.sh -c red blue                # 红蓝两色切换
./run.sh -c '#00FF00'               # 使用十六进制颜色值
```

### 操作按键
- **切换颜色**: 空格 / 鼠标左键
- **退出**: `q` / `Esc`

## 环境要求

- Python 3.x
- tkinter (`sudo apt install python3-tk`)
- 适用于 OrangePi RK3566 及类似 Linux 设备

## License

MIT
