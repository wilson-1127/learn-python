# CLAUDE.md

本文档为 Claude Code (claude.ai/code) 提供在本仓库中工作的指导。

## 项目概述

这是一个用于教育目的的 Python 仓库（trekhleb/learn-python）。`src/` 目录下包含按主题分类的示例脚本，通过 `test_*` 函数和内联断言来演示 Python 概念。它不是一个生产包；这里的“测试”是可运行的示例，供学习阅读。

## 常用命令

- **安装依赖：**
  ```bash
  pip install -r requirements.txt
  ```

- **运行全部测试：**
  ```bash
  pytest
  ```

- **运行单个测试文件：**
  ```bash
  pytest ./src/data_types/test_lists.py
  ```

- **运行单个测试函数：**
  ```bash
  pytest ./src/data_types/test_lists.py::test_list_type
  ```

- **代码检查：**
  ```bash
  pylint ./src
  flake8 ./src --statistics --count
  ```

## 代码结构

- **`src/`** 按主题分为子目录：`getting_started`、`operators`、`data_types`、`control_flow`、`functions`、`classes`、`modules`、`exceptions`、`files`、`additions`、`standard_libraries`、`user_input`。
- 每个主题文件命名为 `test_<topic>.py`，包含一个或多个 `test_<subtopic>()` 函数，函数内使用内联 `assert` 语句来说明行为。
- 文件级别的文档字符串包含主题名称和外部文档链接；函数级别的文档字符串解释子主题。

## 特殊情况

- **`src/modules/`** 包含独立辅助模块（`fibonacci_module.py`）和一个包（`sound_package/`），用于在 `test_modules.py` 和 `test_packages.py` 中演示 Python 导入。
- **`pylintrc`** 通过 `init-hook` 配置 `sys.path.append('./src/modules')`，以便在代码检查期间解析模块的相对导入。
- **`.flake8`** 设置 `max-line-length = 100`。
