"""Function Decorators.

@see: https://www.thecodeship.com/patterns/guide-to-python-function-decorators/

Function decorators are simply wrappers to existing functions. In the context of design patterns,
decorators dynamically alter the functionality of a function, method or class without having to
directly use subclasses. This is ideal when you need to extend the functionality of functions that
you don't want to modify. We can implement the decorator pattern anywhere, but Python facilitates
the implementation by providing much more expressive features and syntax for that.

函数装饰器。

函数装饰器本质上是对现有函数的包装器。在设计模式的上下文中，装饰器动态地改变函数、方法或类的功能，
而无需直接使用子类。当你需要扩展不想修改的函数的功能时，这是理想的选择。
我们可以在任何地方实现装饰器模式，但 Python 通过提供更具表现力的特性和语法来简化实现。
"""


def test_function_decorators():
    """Function Decorators.

    函数装饰器。
    """

    # Function decorators are simply wrappers to existing functions. Putting the ideas mentioned
    # above together, we can build a decorator. In this example let's consider a function that
    # wraps the string output of another function by p tags.
    # 函数装饰器本质上是对现有函数的包装器。将上面提到的想法结合起来，我们可以构建一个装饰器。
    # 在这个例子中，让我们考虑一个用 p 标签包装另一个函数字符串输出的函数。

    # This is the function that we want to decorate.
    # 这是我们想要装饰的函数。
    def greeting(name):
        return "Hello, {0}!".format(name)

    # This function decorates another functions output with <p> tag.
    # 这个函数用 <p> 标签装饰另一个函数的输出。
    def decorate_with_p(func):
        def function_wrapper(name):
            return "<p>{0}</p>".format(func(name))
        return function_wrapper

    # Now, let's call our decorator and pass the function we want decorate to it.
    # 现在，让我们调用我们的装饰器，并将我们想要装饰的函数传递给它。
    my_get_text = decorate_with_p(greeting)

    # Here we go, we've just decorated the function output without changing the function itself.
    # 好了，我们刚刚装饰了函数输出，而没有改变函数本身。
    assert my_get_text('John') == '<p>Hello, John!</p>'  # With decorator.
    assert greeting('John') == 'Hello, John!'  # Without decorator.

    # Now, Python makes creating and using decorators a bit cleaner and nicer for the programmer
    # through some syntactic sugar  There is a neat shortcut for that, which is to mention the
    # name of the decorating function before the function to be decorated. The name of the
    # decorator should be prepended with an @ symbol.
    # 现在，Python 通过一些语法糖使程序员创建和使用装饰器更加简洁和优雅。
    # 有一个简洁的快捷方式，即在要装饰的函数之前提到装饰函数的名称。
    # 装饰器的名称应该以 @ 符号开头。

    @decorate_with_p
    def greeting_with_p(name):
        return "Hello, {0}!".format(name)

    assert greeting_with_p('John') == '<p>Hello, John!</p>'

    # Now let's consider we wanted to decorate our greeting function by one more functions to wrap a
    # div the string output.
    # 现在让我们考虑我们想要再用一个函数来装饰我们的问候函数，以包装字符串输出的 div。

    # This will be our second decorator.
    # 这将是我们的第二个装饰器。
    def decorate_with_div(func):
        def function_wrapper(text):
            return "<div>{0}</div>".format(func(text))
        return function_wrapper

    # With the basic approach, decorating get_text would be along the lines of
    # greeting_with_div_p = decorate_with_div(decorate_with_p(greeting_with_p))
    # 使用基本方法，装饰 get_text 的方式类似于
    # greeting_with_div_p = decorate_with_div(decorate_with_p(greeting_with_p))

    # With Python's decorator syntax, same thing can be achieved with much more expressive power.
    # 使用 Python 的装饰器语法，同样的事情可以用更具表现力的方式实现。
    @decorate_with_div
    @decorate_with_p
    def greeting_with_div_p(name):
        return "Hello, {0}!".format(name)

    assert greeting_with_div_p('John') == '<div><p>Hello, John!</p></div>'

    # One important thing to notice here is that the order of setting our decorators matters.
    # If the order was different in the example above, the output would have been different.
    # 这里需要注意的一个重要点是设置装饰器的顺序很重要。
    # 如果上面的例子中顺序不同，输出也会不同。

    # Passing arguments to decorators.
    # 向装饰器传递参数。

    # Looking back at the example before, you can notice how redundant the decorators in the
    # example are. 2 decorators(decorate_with_div, decorate_with_p) each with the same
    # functionality but wrapping the string with different tags. We can definitely do much better
    # than that. Why not have a more general implementation for one that takes the tag to wrap
    # with as a string? Yes please!
    # 回顾前面的例子，你可以注意到例子中的装饰器是多么冗余。
    # 2 个装饰器（decorate_with_div、decorate_with_p）每个都有相同的功能，但用不同的标签包装字符串。
    # 我们肯定可以做得更好。为什么不有一个更通用的实现，接受要包装的标签作为字符串呢？太好了！

    def tags(tag_name):
        def tags_decorator(func):
            def func_wrapper(name):
                return "<{0}>{1}</{0}>".format(tag_name, func(name))
            return func_wrapper
        return tags_decorator

    @tags('div')
    @tags('p')
    def greeting_with_tags(name):
        return "Hello, {0}!".format(name)

    assert greeting_with_tags('John') == '<div><p>Hello, John!</p></div>'
