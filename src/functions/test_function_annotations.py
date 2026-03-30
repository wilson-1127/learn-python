"""Function Annotations.

@see: https://docs.python.org/3/tutorial/controlflow.html#function-annotations

Function annotations are completely optional metadata information about the types used
by user-defined functions.

Annotations are stored in the __annotations__ attribute of the function as a dictionary and have no
effect on any other part of the function. Parameter annotations are defined by a colon after the
parameter name, followed by an expression evaluating to the value of the annotation. Return
annotations are defined by a literal ->, followed by an expression, between the parameter list and
the colon denoting the end of the def statement.

函数注解。

函数注解是关于用户定义函数所使用类型的完全可选的元数据信息。

注解以字典形式存储在函数的 __annotations__ 属性中，对函数的其他部分没有任何影响。
参数注解通过在参数名后加冒号和计算为注解值的表达式来定义。
返回注解通过在参数列表和表示 def 语句结束的冒号之间使用字面量 -> 和表达式来定义。
"""


def breakfast(ham: str, eggs: str = 'eggs') -> str:
    """Breakfast creator.

    This function has a positional argument, a keyword argument, and the return value annotated.

    早餐创建器。

    这个函数有一个位置参数、一个关键字参数和返回值注解。
    """
    return ham + ' and ' + eggs


def test_function_annotations():
    """Function Annotations.

    函数注解。
    """

    assert breakfast.__annotations__ == {'eggs': str, 'ham': str, 'return': str}
