"""Variables

@see: https://docs.python.org/3/tutorial/introduction.html
@see: https://www.w3schools.com/python/python_variables.asp
@see: https://www.learnpython.org/en/Variables_and_Types

Python is completely object oriented, and not "statically typed".
You do not need to declare variables before using them, or declare
their type. Every variable in Python is an object.

Unlike other programming languages, Python has no command for
declaring a variable. A variable is created the moment you first assign
a value to it.

A variable can have a short name (like x and y) or a more descriptive name
(age, carname, total_volume).

Rules for Python variables:
- A variable name must start with a letter or the underscore character.
- A variable name cannot start with a number.
- A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ ).
- Variable names are case-sensitive (age, Age and AGE are three different variables).

变量

Python 是完全面向对象的，不是"静态类型"的。
你不需要在使用变量之前声明它们，也不需要声明
它们的类型。Python 中的每个变量都是一个对象。

与其他编程语言不同，Python 没有声明变量的命令。
变量在你第一次赋值时就被创建了。

变量可以有简短的名字（如 x 和 y）或更具描述性的名字
（age, carname, total_volume）。

Python 变量命名规则：
- 变量名必须以字母或下划线字符开头。
- 变量名不能以数字开头。
- 变量名只能包含字母数字字符和下划线（A-z, 0-9 和 _）。
- 变量名区分大小写（age, Age 和 AGE 是三个不同的变量）。
"""


def test_variables():


    integer_variable = 5
    string_variable = 'John'

    assert integer_variable == 5
    assert string_variable == 'John'

    variable_with_changed_type = 4  # x is of type int
    # x 是 int 类型
    variable_with_changed_type = 'Sally'  # x is now of type str
    # x 现在是 str 类型

    assert variable_with_changed_type == 'Sally'
