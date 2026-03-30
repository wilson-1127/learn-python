"""Class and Instance Variables.

类变量和实例变量。

@see: https://docs.python.org/3/tutorial/classes.html#class-and-instance-variables

Generally speaking, instance variables are for data unique to each instance and class variables are
for attributes and methods shared by all instances of the class.

一般来说，实例变量用于每个实例独有的数据，类变量用于类的所有实例共享的属性和方法。
"""


def test_class_and_instance_variables():
    """Class and Instance Variables.

    类变量和实例变量。
    """

    # pylint: disable=too-few-public-methods
    class Dog:
        """Dog class example

        狗类示例。
        """
        kind = 'canine'  # Class variable shared by all instances.
        # 类变量，被所有实例共享。

        def __init__(self, name):
            self.name = name  # Instance variable unique to each instance.

    fido = Dog('Fido')
    buddy = Dog('Buddy')

    # Shared by all dogs.
    # 被所有狗共享。
    assert fido.kind == 'canine'
    assert buddy.kind == 'canine'

    # Unique to fido.
    # 仅属于 fido。
    assert fido.name == 'Fido'

    # Unique to buddy.
    # 仅属于 buddy。
    assert buddy.name == 'Buddy'

    # Shared data can have possibly surprising effects with involving mutable objects such as lists
    # and dictionaries. For example, the tricks list in the following code should not be used as a
    # class variable because just a single list would be shared by all Dog instances.
    # 共享数据在使用可变对象（如列表和字典）时可能会产生令人意外的效果。例如，以下代码中的
    # tricks 列表不应作为类变量使用，因为所有 Dog 实例将共享同一个列表。

    # pylint: disable=too-few-public-methods
    class DogWithSharedTricks:
        """Dog class example with wrong shared variable usage

        狗类示例，错误地使用了共享变量。
        """
        tricks = []  # Mistaken use of a class variable (see below) for mutable objects.
        # 错误地将类变量用于可变对象（见下文）。

        def __init__(self, name):
            self.name = name  # Instance variable unique to each instance.

        def add_trick(self, trick):
            """Add trick to the dog

            给狗添加技巧。

            This function illustrate mistaken use of mutable class variable tricks (see below).

            此函数演示了可变类变量 tricks 的错误用法（见下文）。
            """
            self.tricks.append(trick)

    fido = DogWithSharedTricks('Fido')
    buddy = DogWithSharedTricks('Buddy')

    fido.add_trick('roll over')
    buddy.add_trick('play dead')

    assert fido.tricks == ['roll over', 'play dead']  # unexpectedly shared by all dogs
    # 出乎意料地被所有狗共享。
    assert buddy.tricks == ['roll over', 'play dead']  # unexpectedly shared by all dogs
    # 出乎意料地被所有狗共享。

    # Correct design of the class should use an instance variable instead:
    # 类的正确设计应该使用实例变量：

    # pylint: disable=too-few-public-methods
    class DogWithTricks:
        """Dog class example

        狗类示例。
        """

        def __init__(self, name):
            self.name = name  # Instance variable unique to each instance.
            # 实例变量，每个实例独有。
            self.tricks = []  # creates a new empty list for each dog
            # 为每只狗创建一个空列表。

        def add_trick(self, trick):
            """Add trick to the dog

            给狗添加技巧。

            This function illustrate a correct use of mutable class variable tricks (see below).

            此函数演示了可变类变量 tricks 的正确用法（见下文）。
            """
            self.tricks.append(trick)

    fido = DogWithTricks('Fido')
    buddy = DogWithTricks('Buddy')

    fido.add_trick('roll over')
    buddy.add_trick('play dead')

    assert fido.tricks == ['roll over']
    assert buddy.tricks == ['play dead']
