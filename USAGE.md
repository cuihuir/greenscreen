# 使用指南

## 基本用法

### 1. 显示所有颜色（默认模式）
```bash
./run.sh
```
按空格键或鼠标左键可以在 8 种颜色之间切换。

### 2. 只显示单个颜色
```bash
./run.sh --color green       # 只显示绿色
./run.sh -c red              # 只显示红色（短选项）
./run.sh -c '#00FF00'        # 使用十六进制颜色值
```

### 3. 显示多个指定颜色
```bash
./run.sh --color red green blue    # 在红、绿、蓝之间切换
./run.sh -c white black            # 在白、黑之间切换
```

## 可用颜色名称

- `green` - 绿色
- `red` - 红色
- `blue` - 蓝色
- `white` - 白色
- `black` - 黑色
- `yellow` - 黄色
- `cyan` - 青色
- `magenta` - 洋红

## 操作说明

- **切换颜色**: 空格键 或 鼠标左键
- **退出程序**: `q` 键 或 `Esc` 键

## 查看帮助

```bash
./run.sh --help
```
