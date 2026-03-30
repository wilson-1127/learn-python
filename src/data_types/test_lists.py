"""Lists.

# @see: https://www.learnpython.org/en/Lists
# @see: https://docs.python.org/3/tutorial/introduction.html
# @ee: https://docs.python.org/3/tutorial/datastructures.html#more-on-lists

Python knows a number of compound data types, used to group together
other values. The most versatile is the list, which can be written as a
list of comma-separated values (items) between square brackets. Lists
might contain items of different types, but usually the items all have
the same type.

列表。

Python 有许多复合数据类型，用于将其他值组合在一起。最灵活的是列表，
它可以写成方括号之间逗号分隔的值（项目）列表。列表可能包含不同类型的项目，
但通常所有项目都具有相同的类型。
"""

import pytest


def test_list_type():
    """List type.

    列表类型。
    """

    # Lists are very similar to arrays. They can contain any type of variable, and they can contain
    # as many variables as you wish. Lists can also be iterated over in a very simple manner.
    # Here is an example of how to build a list.
    # 列表与数组非常相似。它们可以包含任何类型的变量，并且可以包含任意数量的变量。
    # 列表也可以以非常简单的方式进行迭代。以下是如何构建列表的示例。
    squares = [1, 4, 9, 16, 25]

    assert isinstance(squares, list)

    # Like strings (and all other built-in sequence type), lists can be
    # indexed and sliced:
    # 与字符串（以及所有其他内置序列类型）一样，列表可以被索引和切片：
    assert squares[0] == 1  # indexing returns the item
    # 索引返回项目
    assert squares[-1] == 25
    assert squares[-3:] == [9, 16, 25]  # slicing returns a new list
    # 切片返回一个新列表

    # All slice operations return a new list containing the requested elements.
    # This means that the following slice returns a new (shallow) copy of
    # the list:
    # 所有切片操作都返回一个包含所请求元素的新列表。
    # 这意味着以下切片返回列表的一个新（浅）副本：
    assert squares[:] == [1, 4, 9, 16, 25]

    # Lists also support operations like concatenation:
    # 列表还支持连接等操作：
    assert squares + [36, 49, 64, 81, 100] == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

    # Unlike strings, which are immutable, lists are a mutable type, i.e. it
    # is possible to change their content:
    # 与不可变的字符串不同，列表是可变类型，即可以更改其内容：
    cubes = [1, 8, 27, 65, 125]  # something's wrong here, the cube of 4 is 64!
    # 这里有问题，4的立方是64！
    cubes[3] = 64  # replace the wrong value
    # 替换错误的值
    assert cubes == [1, 8, 27, 64, 125]

    # You can also add new items at the end of the list, by using
    # the append() method
    # 你也可以使用 append() 方法在列表末尾添加新项目
    cubes.append(216)  # add the cube of 6
    # 添加6的立方
    cubes.append(7 ** 3)  # and the cube of 7
    # 以及7的立方
    assert cubes == [1, 8, 27, 64, 125, 216, 343]

    # Assignment to slices is also possible, and this can even change the size
    # of the list or clear it entirely:
    # 也可以对切片进行赋值，这甚至可以改变列表的大小或完全清空它：
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    letters[2:5] = ['C', 'D', 'E']  # replace some values
    # 替换一些值
    assert letters == ['a', 'b', 'C', 'D', 'E', 'f', 'g']
    letters[2:5] = []  # now remove them
    # 现在删除它们
    assert letters == ['a', 'b', 'f', 'g']
    # clear the list by replacing all the elements with an empty list
    # 通过用空列表替换所有元素来清空列表
    letters[:] = []
    assert letters == []

    # The built-in function len() also applies to lists
    # 内置函数 len() 也适用于列表
    letters = ['a', 'b', 'c', 'd']
    assert len(letters) == 4

    # It is possible to nest lists (create lists containing other lists),
    # for example:
    # 可以嵌套列表（创建包含其他列表的列表），例如：
    list_of_chars = ['a', 'b', 'c']
    list_of_numbers = [1, 2, 3]
    mixed_list = [list_of_chars, list_of_numbers]
    assert mixed_list == [['a', 'b', 'c'], [1, 2, 3]]
    assert mixed_list[0] == ['a', 'b', 'c']
    assert mixed_list[0][1] == 'b'


def test_list_methods():
    """Test list methods.

    测试列表方法。
    """

    fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

    # list.append(x)
    # Add an item to the end of the list.
    # Equivalent to a[len(a):] = [x].
    # 在列表末尾添加一个项目。等价于 a[len(a):] = [x]。
    fruits.append('grape')
    assert fruits == ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana', 'grape']

    # list.remove(x)
    # Remove the first item from the list whose value is equal to x.
    # It raises a ValueError if there is no such item.
    # 从列表中删除第一个值等于 x 的项目。如果没有这样的项目，则引发 ValueError。
    fruits.remove('grape')
    assert fruits == ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

    with pytest.raises(Exception):
        fruits.remove('not existing element')

    # list.insert(i, x)
    # Insert an item at a given position. The first argument is the index of the element
    # before which to insert, so a.insert(0, x) inserts at the front of the list,
    # and a.insert(len(a), x) is equivalent to a.append(x).
    # 在给定位置插入一个项目。第一个参数是要在其之前插入的元素的索引，
    # 因此 a.insert(0, x) 在列表开头插入，a.insert(len(a), x) 等价于 a.append(x)。
    fruits.insert(0, 'grape')
    assert fruits == ['grape', 'orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

    # list.index(x[, start[, end]])
    # Return zero-based index in the list of the first item whose value is equal to x.
    # Raises a ValueError if there is no such item.
    # The optional arguments start and end are interpreted as in the slice notation and are used
    # to limit the search to a particular subsequence of the list. The returned index is computed
    # relative to the beginning of the full sequence rather than the start argument.
    # 返回列表中第一个值等于 x 的项目的基于零的索引。如果没有这样的项目，则引发 ValueError。
    # 可选参数 start 和 end 按照切片符号解释，用于将搜索限制在列表的特定子序列。
    # 返回的索引是相对于完整序列的开头计算的，而不是 start 参数。
    assert fruits.index('grape') == 0
    assert fruits.index('orange') == 1
    assert fruits.index('banana') == 4
    assert fruits.index('banana', 5) == 7  # Find next banana starting a position 5
    # 从位置5开始查找下一个 banana

    with pytest.raises(Exception):
        fruits.index('not existing element')

    # list.count(x)
    # Return the number of times x appears in the list.
    # 返回 x 在列表中出现的次数。
    assert fruits.count('tangerine') == 0
    assert fruits.count('banana') == 2

    # list.copy()
    # Return a shallow copy of the list. Equivalent to a[:].
    # 返回列表的浅副本。等价于 a[:]。
    fruits_copy = fruits.copy()
    assert fruits_copy == ['grape', 'orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

    # list.reverse()
    # Reverse the elements of the list in place.
    # 就地反转列表的元素。
    fruits_copy.reverse()
    assert fruits_copy == [
        'banana',
        'apple',
        'kiwi',
        'banana',
        'pear',
        'apple',
        'orange',
        'grape',
    ]

    # list.sort(key=None, reverse=False)
    # Sort the items of the list in place (the arguments can be used for sort customization,
    # see sorted() for their explanation).
    # 就地排序列表的项目（参数可用于自定义排序，请参阅 sorted() 的说明）。
    fruits_copy.sort()
    assert fruits_copy == [
        'apple',
        'apple',
        'banana',
        'banana',
        'grape',
        'kiwi',
        'orange',
        'pear',
    ]

    # list.pop([i])
    # Remove the item at the given position in the list, and return it. If no index is specified,
    # a.pop() removes and returns the last item in the list. (The square brackets around the i in
    # the method signature denote that the parameter is optional, not that you should type square
    # brackets at that position.)
    # 删除列表中给定位置的项目并返回它。如果没有指定索引，a.pop() 删除并返回列表中的
    # 最后一个项目。（方法签名中 i 周围的方括号表示该参数是可选的，而不是说你应该在该
    # 位置输入方括号。）
    assert fruits == ['grape', 'orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
    assert fruits.pop() == 'banana'
    assert fruits == ['grape', 'orange', 'apple', 'pear', 'banana', 'kiwi', 'apple']

    # list.clear()
    # Remove all items from the list. Equivalent to del a[:].
    # 从列表中删除所有项目。等价于 del a[:]。
    fruits.clear()
    assert fruits == []


def test_del_statement():
    """The del statement

    There is a way to remove an item from a list given its index instead of its value: the del
    statement. This differs from the pop() method which returns a value. The del statement can also
    be used to remove slices from a list or clear the entire list (which we did earlier by
    assignment of an empty list to the slice).

    del 语句

    有一种方法可以根据索引而不是值从列表中删除项目：del 语句。这与返回值的 pop() 方法不同。
    del 语句也可用于从列表中删除切片或清空整个列表（我们之前通过将空列表赋值给切片来完成）。
    """

    numbers = [-1, 1, 66.25, 333, 333, 1234.5]

    del numbers[0]
    assert numbers == [1, 66.25, 333, 333, 1234.5]

    del numbers[2:4]
    assert numbers == [1, 66.25, 1234.5]

    del numbers[:]
    assert numbers == []

    # del can also be used to delete entire variables:
    # del 也可用于删除整个变量：
    del numbers
    with pytest.raises(Exception):
        # Referencing the name a hereafter is an error (at least until another
        # value is assigned to it).
        # 此后引用名称 a 是错误的（至少在另一个值被赋值给它之前）。
        assert numbers == []  # noqa: F821


def test_list_comprehensions():
    """List Comprehensions.

    List comprehensions provide a concise way to create lists. Common applications are to make new
    lists where each element is the result of some operations applied to each member of another
    sequence or iterable, or to create a subsequence of those elements that satisfy a certain
    condition.

    A list comprehension consists of brackets containing an expression followed by a for clause,
    then zero or more for or if clauses. The result will be a new list resulting from evaluating
    the expression in the context of the for and if clauses which follow it.

    列表推导式。

    列表推导式提供了一种创建列表的简洁方式。常见应用是创建新列表，其中每个元素是对另一个
    序列或可迭代对象的每个成员应用某些操作的结果，或者创建满足特定条件的那些元素的子序列。

    列表推导式由包含表达式的方括号组成，后跟 for 子句，然后是零个或多个 for 或 if 子句。
    结果将是一个新列表，该列表是通过在随后的 for 和 if 子句的上下文中评估表达式而产生的。
    """

    # For example, assume we want to create a list of squares, like:
    # 例如，假设我们想创建一个平方数列表，如下：
    squares = []
    for number in range(10):
        squares.append(number ** 2)

    assert squares == [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

    # Note that this creates (or overwrites) a variable named "number" that still exists after
    # the loop completes. We can calculate the list of squares without any side effects using:
    # 请注意，这会创建（或覆盖）一个名为 "number" 的变量，该变量在循环完成后仍然存在。
    # 我们可以使用以下方法计算平方数列表而没有任何副作用：
    squares = list(map(lambda x: x ** 2, range(10)))
    assert squares == [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

    # or, equivalently (which is more concise and readable):
    # 或者，等价地（更简洁且可读）：
    squares = [x ** 2 for x in range(10)]
    assert squares == [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

    # For example, this listcomp combines the elements of two lists if they are not equal.
    # 例如，这个列表推导式将两个列表的元素组合起来，如果它们不相等的话。
    combinations = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
    assert combinations == [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

    # and it’s equivalent to:
    # 它等价于：
    combinations = []
    for first_number in [1, 2, 3]:
        for second_number in [3, 1, 4]:
            if first_number != second_number:
                combinations.append((first_number, second_number))

    assert combinations == [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

    # Note how the order of the for and if statements is the same in both these snippets.
    # 请注意这两个片段中 for 和 if 语句的顺序是相同的。

    # If the expression is a tuple (e.g. the (x, y) in the previous example),
    # it must be parenthesized.
    # 如果表达式是元组（例如前一个例子中的 (x, y)），则必须用括号括起来。

    # Let's see some more examples:
    # 让我们看更多示例：

    vector = [-4, -2, 0, 2, 4]

    # Create a new list with the values doubled.
    # 创建一个值加倍的新列表。
    doubled_vector = [x * 2 for x in vector]
    assert doubled_vector == [-8, -4, 0, 4, 8]

    # Filter the list to exclude negative numbers.
    # 过滤列表以排除负数。
    positive_vector = [x for x in vector if x >= 0]
    assert positive_vector == [0, 2, 4]

    # Apply a function to all the elements.
    # 对所有元素应用一个函数。
    abs_vector = [abs(x) for x in vector]
    assert abs_vector == [4, 2, 0, 2, 4]

    # Call a method on each element.
    # 对每个元素调用一个方法。
    fresh_fruit = ['  banana', '  loganberry ', 'passion fruit  ']
    clean_fresh_fruit = [weapon.strip() for weapon in fresh_fruit]
    assert clean_fresh_fruit == ['banana', 'loganberry', 'passion fruit']

    # Create a list of 2-tuples like (number, square).
    # 创建一个形如 (数字, 平方) 的2元组列表。
    square_tuples = [(x, x ** 2) for x in range(6)]
    assert square_tuples == [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

    # Flatten a list using a listcomp with two 'for'.
    # 使用带有两个 'for' 的列表推导式来扁平化列表。
    vector = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flatten_vector = [num for elem in vector for num in elem]
    assert flatten_vector == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_nested_list_comprehensions():
    """Nested List Comprehensions

    The initial expression in a list comprehension can be any arbitrary expression, including
    another list comprehension.

    嵌套列表推导式

    列表推导式中的初始表达式可以是任意表达式，包括另一个列表推导式。
    """

    # Consider the following example of a 3x4 matrix implemented as a list of 3 lists of length 4:
    # 考虑以下示例，一个 3x4 矩阵实现为3个长度为4的列表的列表：
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]

    # The following list comprehension will transpose rows and columns:
    # 以下列表推导式将转置行和列：
    transposed_matrix = [[row[i] for row in matrix] for i in range(4)]
    assert transposed_matrix == [
        [1, 5, 9],
        [2, 6, 10],
        [3, 7, 11],
        [4, 8, 12],
    ]

    # As we saw in the previous section, the nested listcomp is evaluated in the context of the
    # for that follows it, so this example is equivalent to:
    # 正如我们在上一节中看到的，嵌套列表推导式在它后面的 for 的上下文中进行评估，
    # 因此这个例子等价于：
    transposed = []
    for i in range(4):
        transposed.append([row[i] for row in matrix])

    assert transposed == [
        [1, 5, 9],
        [2, 6, 10],
        [3, 7, 11],
        [4, 8, 12],
    ]

    # which, in turn, is the same as:
    # 这反过来又等同于：
    transposed = []
    for i in range(4):
        # the following 3 lines implement the nested listcomp
        # 以下3行实现了嵌套列表推导式
        transposed_row = []
        for row in matrix:
            transposed_row.append(row[i])
        transposed.append(transposed_row)

    assert transposed == [
        [1, 5, 9],
        [2, 6, 10],
        [3, 7, 11],
        [4, 8, 12],
    ]

    # In the real world, you should prefer built-in functions to complex flow statements.
    # The zip() function would do a great job for this use case:
    # 在现实世界中，你应该优先使用内置函数而不是复杂的流程语句。
    # zip() 函数在这种情况下会做得很好：
    assert list(zip(*matrix)) == [
        (1, 5, 9),
        (2, 6, 10),
        (3, 7, 11),
        (4, 8, 12),
    ]
