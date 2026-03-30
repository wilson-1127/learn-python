"""Fibonacci numbers module.

@see: https://docs.python.org/3/tutorial/modules.html

A module is a file containing Python definitions and statements. The file name is the module name
with the suffix .py appended. Within a module, the module’s name (as a string) is available as the
value of the global variable __name__.

斐波那契数模块。

模块是包含 Python 定义和语句的文件。文件名是模块名加上 .py 后缀。
在模块内部，模块的名称（作为字符串）可作为全局变量 __name__ 的值使用。
"""


def fibonacci_at_position(position):
    """Return Fibonacci number at specified position

    返回指定位置的斐波那契数
    """
    current_position = 0
    previous_number, current_number = 0, 1
    while current_position < position:
        current_position += 1
        previous_number, current_number = current_number, previous_number + current_number
    return previous_number


def fibonacci_smaller_than(limit):
    """Return Fibonacci series up to limit

    返回小于指定上限的斐波那契数列
    """
    result = []
    previous_number, current_number = 0, 1
    while previous_number < limit:
        result.append(previous_number)
        previous_number, current_number = current_number, previous_number + current_number
    return result


# When you run a Python module with:
#
# >>> python fibonacci.py <arguments>
#
# the code in the module will be executed, just as if you imported it, but with
# the __name__ set to “__main__”. That means that by adding this code at the end of your module
# you can make the file usable as a script as well as an importable module, because the code that
# parses the command line only runs if the module is executed as the “main” file:
#
# >>> python fibonacci.py 50
#
# 当你运行 Python 模块时：
#
# >>> python fibonacci.py <参数>
#
# 模块中的代码将被执行，就像你导入它一样，但 __name__ 被设置为 “__main__”。
# 这意味着通过在模块末尾添加这段代码，你可以使文件既可作为脚本使用，也可作为可导入的模块使用，
# 因为解析命令行的代码只有在模块作为”主”文件执行时才会运行：
#
# >>> python fibonacci.py 50
if __name__ == '__main__':
    import sys
    print(fibonacci_smaller_than(int(sys.argv[1])))
