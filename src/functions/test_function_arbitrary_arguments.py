"""Arbitrary Argument Lists

@see: https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists

Function can be called with an arbitrary number of arguments. These arguments will be wrapped up in
a tuple. Before the variable number of arguments, zero or more normal arguments may occur.

任意参数列表

函数可以使用任意数量的参数调用。这些参数将被包装在一个元组中。
在可变数量的参数之前，可以出现零个或多个普通参数。
"""


def test_function_arbitrary_arguments():
    """Arbitrary Argument Lists

    任意参数列表
    """

    # When a final formal parameter of the form **name is present, it receives a dictionary
    # containing all keyword arguments except for those corresponding to a formal parameter.
    # This may be combined with a formal parameter of the form *name which receives a tuple
    # containing the positional arguments beyond the formal parameter list.
    # (*name must occur before **name.) For example, if we define a function like this:
    # 当存在形式为 **name 的最终形参时，它会接收一个字典，其中包含除对应于形参的关键字参数外的所有关键字参数。
    # 这可以与形式为 *name 的形参结合使用，后者接收一个元组，其中包含超出形参列表的位置参数。
    # (*name 必须出现在 **name 之前。) 例如，如果我们这样定义一个函数：
    def test_function(first_param, *arguments):
        """This function accepts its arguments through "arguments" tuple"""
        # 这个函数通过 "arguments" 元组接收其参数
        assert first_param == 'first param'
        assert arguments == ('second param', 'third param')

    test_function('first param', 'second param', 'third param')

    # Normally, these variadic arguments will be last in the list of formal parameters, because
    # they scoop up all remaining input arguments that are passed to the function. Any formal
    # parameters which occur after the *args parameter are ‘keyword-only’ arguments, meaning that
    # they can only be used as keywords rather than positional arguments.
    # 通常，这些可变参数将是形参列表中的最后一个，因为它们会收集传递给函数的所有剩余输入参数。
    # 出现在 *args 参数之后的任何形参都是"仅关键字"参数，这意味着它们只能用作关键字而不能用作位置参数。
    def concat(*args, sep='/'):
        return sep.join(args)

    assert concat('earth', 'mars', 'venus') == 'earth/mars/venus'
    assert concat('earth', 'mars', 'venus', sep='.') == 'earth.mars.venus'
