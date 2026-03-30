"""Modules.

@see: https://docs.python.org/3/tutorial/modules.html

As your program gets longer, you may want to split it into several files for easier maintenance.
You may also want to use a handy function that you’ve written in several programs without copying
its definition into each program.

To support this, Python has a way to put definitions in a file and use them in a script or in an
interactive instance of the interpreter. Such a file is called a module; definitions from a module
can be imported into other modules or into the main module (the collection of variables that you
have access to in a script executed at the top level and in calculator mode).

A module is a file containing Python definitions and statements. The file name is the module name
with the suffix .py appended. Within a module, the module’s name (as a string) is available as the
value of the global variable __name__.

When the interpreter executes the import statement, it searches for module in a list of
directories assembled from the following sources:

- The directory from which the input script was run or the current directory if the interpreter is
being run interactively
- The list of directories contained in the PYTHONPATH environment variable, if it is set. (The
format for PYTHONPATH is OS-dependent but should mimic the PATH environment variable.)
- An installation-dependent list of directories configured at the time Python is installed

The resulting search path is accessible in the Python variable sys.path, which is obtained from a
module named sys:

>>> import sys
>>> sys.path

@see: https://realpython.com/python-modules-packages/

模块。

随着程序变长，你可能希望将其分成多个文件以便于维护。你可能还想在多个程序中使用你编写的便捷函数，而无需将其定义复制到每个程序中。

为了支持这一点，Python 提供了一种将定义放在文件中并在脚本或解释器的交互式实例中使用它们的方法。这样的文件称为模块；模块中的定义可以导入到其他模块或主模块中（主模块是你在顶层执行的脚本和计算器模式中可以访问的变量集合）。

模块是包含 Python 定义和语句的文件。文件名是模块名加上 .py 后缀。在模块内部，模块的名称（作为字符串）可作为全局变量 __name__ 的值使用。

当解释器执行 import 语句时，它会在由以下来源组装的目录列表中搜索模块：

- 运行输入脚本的目录，或者如果解释器以交互方式运行，则为当前目录
- PYTHONPATH 环境变量中包含的目录列表（如果已设置）。（PYTHONPATH 的格式取决于操作系统，但应模仿 PATH 环境变量。）
- 安装时配置的与安装相关的目录列表

生成的搜索路径可在 Python 变量 sys.path 中访问，该变量从名为 sys 的模块获取：

>>> import sys
>>> sys.path
"""

# This does not enter the names of the functions defined in fibonacci_module directly in the
# current symbol table; it only enters the module name fibonacci_module there.
#
# 这不会将 fibonacci_module 中定义的函数名称直接放入当前符号表中；它只在那里输入模块名 fibonacci_module。
import fibonacci_module

# There is a variant of the import statement that imports names from a module directly into the
# importing module’s symbol table. For example:
#
# import 语句有一种变体，可以将名称从模块直接导入到导入模块的符号表中。例如：

# pylint: disable=reimported
from fibonacci_module import fibonacci_at_position, fibonacci_smaller_than

# There is even a variant to import all names that a module defines. This imports all names except
# those beginning with an underscore (_). In most cases Python programmers do not use this facility
# since it introduces an unknown set of names into the interpreter, possibly hiding some things you
# have already defined.
# >>> from fibonacci_module import *
#
# 甚至还有一种变体可以导入模块定义的所有名称。这会导入所有名称，除了以下划线 (_) 开头的名称。
# 在大多数情况下，Python 程序员不使用这个功能，因为它会向解释器引入一组未知的名称，可能会隐藏你已经定义的一些东西。
# >>> from fibonacci_module import *

# If the module name is followed by as, then the name following as is bound directly to the
# imported module:
#
# 如果模块名后面跟着 as，那么 as 后面的名称将直接绑定到导入的模块：
import fibonacci_module as fibonacci_module_renamed

# It can also be used when utilising from with similar effects:
#
# 它也可以在使用 from 时使用，效果类似：
from fibonacci_module import fibonacci_at_position as fibonacci_at_position_renamed

# When a module named spam is imported, the interpreter first searches for a built-in module with
# that name. If not found, it then searches for a file named spam.py in a list of directories
# given by the variable sys.path. sys.path is initialized from these locations:
#
# - The directory containing the input script (or the current directory when no file is specified).
# - PYTHONPATH (a list of directory names, with the same syntax as the shell variable PATH).
# - The installation-dependent default.
#
# 当导入名为 spam 的模块时，解释器首先搜索具有该名称的内置模块。如果未找到，它将在变量 sys.path 给出的目录列表中搜索名为 spam.py 的文件。sys.path 从以下位置初始化：
#
# - 包含输入脚本的目录（或未指定文件时的当前目录）。
# - PYTHONPATH（目录名称列表，语法与 shell 变量 PATH 相同）。
# - 与安装相关的默认值。


def test_modules():
    """Modules

    模块
    """

    assert fibonacci_module.fibonacci_at_position(7) == 13
    assert fibonacci_at_position(7) == 13
    assert fibonacci_module_renamed.fibonacci_at_position(7) == 13
    assert fibonacci_at_position_renamed(7) == 13

    assert fibonacci_module.fibonacci_smaller_than(100) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    assert fibonacci_smaller_than(100) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    assert fibonacci_module_renamed.fibonacci_smaller_than(10) == [0, 1, 1, 2, 3, 5, 8]

    # If you intend to use a function often you can assign it to a local name.
    # 如果你打算经常使用某个函数，可以将其赋值给一个本地名称。
    fibonacci = fibonacci_module.fibonacci_smaller_than
    assert fibonacci(100) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

    # The built-in function dir() is used to find out which names a module defines. It returns a
    # sorted list of strings.
    # 内置函数 dir() 用于查找模块定义了哪些名称。它返回一个排序后的字符串列表。
    assert dir(fibonacci_module) == [
        '__builtins__',
        '__cached__',
        '__doc__',
        '__file__',
        '__loader__',
        '__name__',
        '__package__',
        '__spec__',
        'fibonacci_at_position',
        'fibonacci_smaller_than',
    ]
