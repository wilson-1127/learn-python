# Python 学习与速查手册



> 这是一组按[主题](#目录)分类的 Python 脚本，包含带有解释的代码示例、不同的用例以及进一步阅读的链接。

> _其他语言版本：_ [_Português_](README.pt-BR.md), [_Español_](README.es-ES.md), [_繁體中文_](README.zh-TW.md)。

它是一个**学习乐园**，因为你可以更改或添加代码来观察其工作原理，并使用断言进行[测试](#测试代码)。它还允许你对编写的代码进行[代码检查](#代码检查)，并检查其是否符合 Python 代码风格指南。总的来说，这可以让你的学习过程更具互动性，并帮助你在起步阶段就保持相当高的代码质量。

它是一个**速查手册**，因为你可以在想要回顾[标准 Python 语句和结构](#目录)的语法时随时回到这些代码示例。此外，由于代码中充满了断言，你能够直接看到预期函数/语句的输出，而无需运行它们。

> _你可能还会对 🤖 [交互式机器学习实验](https://github.com/trekhleb/machine-learning-experiments) 感兴趣_

## 如何使用本仓库

本仓库中的每个 Python 脚本都具有以下结构：

```python
"""列表  <--- 此处为主题名称

# @see: https://www.learnpython.org/en/Lists  <-- 此处为延伸阅读链接

这里可能会有关于当前主题的更详细解释（即关于列表的一般信息）。
"""


def test_list_type():
    """此处为子主题的解释。

    每个文件都包含测试函数，用于说明子主题（例如列表类型、列表方法）。
    """

    # 这里是构建列表的示例。  <-- 注释用于解释操作
    squares = [1, 4, 9, 16, 25]

    # 列表可以被索引和切片。
    # 索引返回该项。
    assert squares[0] == 1  # <-- 断言用于说明结果。
    # 切片返回一个新列表。
    assert squares[-3:] == [9, 16, 25]  # <-- 断言用于说明结果。
```

通常情况下，你可能想执行以下操作：

- [找到](#目录)你想学习或回顾的主题。
- 阅读每个脚本文档字符串中链接的注释和/或文档（如上例所示）。
- 查看代码示例和断言，以了解用法示例和预期输出。
- 更改代码或添加新的断言来观察工作原理。
- [运行测试](#测试代码)并对代码进行[代码检查](#代码检查)，以查看其是否有效且编写正确。

## 目录

1. **入门**
    - [什么是 Python](src/getting_started/what_is_python.md)
    - [Python 语法](src/getting_started/python_syntax.md)
    - [变量](src/getting_started/test_variables.py)
2. **运算符**
    - [算术运算符](src/operators/test_arithmetic.py)（`+`、`-`、`*`、`/`、`//`、`%`**）
    - [位运算符](src/operators/test_bitwise.py)（`&`、`|`、`^`、`>>`、`<<`、`~`）
    - [赋值运算符](src/operators/test_assigment.py)（`=`、`+=`、`-=`、`/=`、`//=` 等）
    - [比较运算符](src/operators/test_comparison.py)（`==`、`!=`、`>`、`<`、`>=`、`<=`）
    - [逻辑运算符](src/operators/test_logical.py)（`and`、`or`、`not`）
    - [身份运算符](src/operators/test_identity.py)（`is`、`is not`）
    - [成员运算符](src/operators/test_membership.py)（`in`、`not in`）
3. **数据类型**
    - [数字](src/data_types/test_numbers.py)（包括布尔值）
    - [字符串](src/data_types/test_strings.py) 及其方法
    - [列表](src/data_types/test_lists.py) 及其方法（包括列表推导式）
    - [元组](src/data_types/test_tuples.py)
    - [集合](src/data_types/test_sets.py) 及其方法
    - [字典](src/data_types/test_dictionaries.py)
    - [类型转换](src/data_types/test_type_casting.py)
4. **控制流**
    - [`if` 语句](src/control_flow/test_if.py)
    - [`for` 语句](src/control_flow/test_for.py)（以及 `range()` 函数）
    - [`while` 语句](src/control_flow/test_while.py)
    - [`try` 语句](src/control_flow/test_try.py)
    - [`break` 语句](src/control_flow/test_break.py)
    - [`continue` 语句](src/control_flow/test_continue.py)
5. **函数**
    - [函数定义](src/functions/test_function_definition.py)（`def` 和 `return` 语句）
    - [函数内变量的作用域](src/functions/test_function_scopes.py)（`global` 和 `nonlocal` 语句）
    - [默认参数值](src/functions/test_function_default_arguments.py)
    - [关键字参数](src/functions/test_function_keyword_arguments.py)
    - [任意参数列表](src/functions/test_function_arbitrary_arguments.py)
    - [解包参数列表](src/functions/test_function_unpacking_arguments.py)（`*` 和 `**` 语句）
    - [Lambda 表达式](src/functions/test_lambda_expressions.py)（`lambda` 语句）
    - [文档字符串](src/functions/test_function_documentation_string.py)
    - [函数注解](src/functions/test_function_annotations.py)
    - [函数装饰器](src/functions/test_function_decorators.py)
6. **类**
    - [类定义](src/classes/test_class_definition.py)（`class` 语句）
    - [类对象](src/classes/test_class_objects.py)
    - [实例对象](src/classes/test_instance_objects.py)
    - [方法对象](src/classes/test_method_objects.py)
    - [类变量和实例变量](src/classes/test_class_and_instance_variables.py)
    - [继承](src/classes/test_inheritance.py)
    - [多重继承](src/classes/test_multiple_inheritance.py)
7. **模块**
    - [模块](src/modules/test_modules.py)（`import` 语句）
    - [包](src/modules/test_packages.py)
8. **错误和异常**
    - [异常处理](src/exceptions/test_handle_exceptions.py)（`try` 语句）
    - [抛出异常](src/exceptions/test_raise_exceptions.py)（`raise` 语句）
9. **文件**
    - [读写文件](src/files/test_file_reading.py)（`with` 语句）
    - [文件对象的方法](src/files/test_file_methods.py)
10. **补充内容**
    - [`pass` 语句](src/additions/test_pass.py)
    - [生成器](src/additions/test_generators.py)（`yield` 语句）
11. **标准库简介**
    - [序列化](src/standard_libraries/test_json.py)（`json` 库）
    - [文件通配符](src/standard_libraries/test_glob.py)（`glob` 库）
    - [字符串模式匹配](src/standard_libraries/test_re.py)（`re` 库）
    - [数学](src/standard_libraries/test_math.py)（`math`、`random`、`statistics` 库）
    - [日期和时间](src/standard_libraries/test_datetime.py)（`datetime` 库）
    - [数据压缩](src/standard_libraries/test_zlib.py)（`zlib` 库）
12. **用户输入**
    - [终端输入](src/user_input/test_input.py)（`input` 语句）

## 前提条件

**安装 Python**

确保你的机器上已安装 [Python3](https://realpython.com/installing-python/)。

你可能希望使用 Python 标准库 [venv](https://docs.python.org/3/library/venv.html) 来创建虚拟环境，并将 Python、pip 和所有依赖包安装到本地项目目录中，以避免与系统范围的包及其版本发生冲突。

根据你的安装情况，你可以通过运行 `python` 或 `python3` 来访问 Python3 解释器。同理，pip 包管理器可能可以通过运行 `pip` 或 `pip3` 来访问。

你可以通过运行以下命令检查 Python 版本：

```bash
python --version
```

请注意，在本仓库中，每当你看到 `python` 时，默认它指的是 Python **3**。

**安装依赖**

通过运行以下命令安装项目所需的所有依赖：

```bash
pip install -r requirements.txt
```

## 测试代码

测试使用 [pytest](https://docs.pytest.org/en/latest/) 框架编写。

你可以通过添加带有 `test_` 前缀的文件和函数来为自己添加新的测试（例如 `test_topic.py` 文件中包含 `def test_sub_topic()` 函数）。

要从项目根目录运行所有测试，请执行以下命令：

```bash
pytest
```

要运行特定的测试，请执行：

```bash
pytest ./path/to/the/test_file.py
```

## 代码检查

代码检查使用 [pylint](http://pylint.pycqa.org/) 和 [flake8](http://flake8.pycqa.org/en/latest/) 库完成。

### PyLint

要检查代码是否遵循 [PEP 8](https://www.python.org/dev/peps/pep-0008/) 风格指南，请运行：

```bash
pylint ./src/
```

如果检测器发现错误（例如 `missing-docstring`），你可以通过运行以下命令阅读有关特定错误的更多信息：

```bash
pylint --help-msg=missing-docstring
```

[更多关于 PyLint 的信息](http://pylint.pycqa.org/)

### Flake8

要检查代码是否遵循 [PEP 8](https://www.python.org/dev/peps/pep-0008/) 风格指南，请运行：

```bash
flake8 ./src
```

或者，如果你想要更详细的输出，可以运行：

```bash
flake8 ./src --statistics --show-source --count
```

[更多关于 Flake8 的信息](http://flake8.pycqa.org/en/latest/)

## 作者

- [@trekhleb](https://trekhleb.dev)
