"""Class Definition Syntax.

类定义语法。

@see: https://docs.python.org/3/tutorial/classes.html

Python is an object oriented programming language.
Almost everything in Python is an object, with its properties and methods.
A Class is like an object constructor, or a "blueprint" for creating objects.

Python 是一种面向对象的编程语言。
Python 中几乎所有东西都是对象，具有属性和方法。
类就像是对象构造器，或者说是创建对象的"蓝图"。
"""


def test_class_definition():
    """Class definition.

    类定义。
    """

    # Class definitions, like function definitions (def statements) must be executed before they
    # have any effect. (You could conceivably place a class definition in a branch of an if
    # statement, or inside a function.)
    # 类定义和函数定义（def 语句）一样，必须先执行才能生效。（你可以将类定义放在 if 语句的
    # 分支中，或者放在函数内部。）

    class GreetingClass:
        """Example of the class definition

        类定义示例。

        This class contains two public methods and doesn't contain constructor.

        此类包含两个公共方法，不包含构造器。
        """
        name = 'user'

        def say_hello(self):
            """Class method.

            类方法。
            """
            # The self parameter is a reference to the class itself, and is used to access variables
            # that belongs to the class. It does not have to be named self , you can call it
            # whatever you like, but it has to be the first parameter of any function in the class.
            # self 参数是对类本身的引用，用于访问属于类的变量。它不必命名为 self，你可以随意
            # 命名，但它必须是类中任何函数的第一个参数。
            return 'Hello ' + self.name

        def say_goodbye(self):
            """Class method.

            类方法。
            """
            return 'Goodbye ' + self.name

    # When a class definition is entered, a new namespace is created, and used as the local scope —
    # thus, all assignments to local variables go into this new namespace. In particular, function
    # definitions bind the name of the new function here.
    # 当进入类定义时，会创建一个新的命名空间，并用作局部作用域——因此，所有对局部变量的
    # 赋值都进入这个新的命名空间。特别是，函数定义在这里绑定新函数的名称。

    # Class instantiation uses function notation. Just pretend that the class object is a
    # parameterless function that returns a new instance of the class. For example the following
    # code will creates a new instance of the class and assigns this object to the local variable.
    # 类实例化使用函数表示法。只需将类对象视为一个无参函数，返回类的新实例。例如，以下
    # 代码将创建类的新实例，并将此对象赋值给局部变量。
    greeter = GreetingClass()

    assert greeter.say_hello() == 'Hello user'
    assert greeter.say_goodbye() == 'Goodbye user'
