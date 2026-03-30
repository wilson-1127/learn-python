"""FOR statement

@see: https://docs.python.org/3/tutorial/controlflow.html

The for statement in Python differs a bit from what you may be used to in C or Pascal.
Rather than always iterating over an arithmetic progression of numbers (like in Pascal), or
giving the user the ability to define both the iteration step and halting condition (as C),
Python’s for statement iterates over the items of any sequence (a list or a string), in the
order that they appear in the sequence. For example (no pun intended):

Python 中的 for 语句与你在 C 或 Pascal 中习惯的略有不同。
它不是总是遍历数字的等差数列（如 Pascal 中），也不是让用户能够定义迭代步长和停止条件（如 C 中），
Python 的 for 语句按序列中项目出现的顺序，遍历任何序列（列表或字符串）中的项目。
例如（没有双关的意思）：
"""


# pylint: disable=too-many-locals
def test_for_statement():
    """FOR statement

    FOR 语句
    """

    # Measure some strings:
    # 测量一些字符串的长度：
    words = ['cat', 'window', 'defenestrate']
    words_length = 0

    for word in words:
        words_length += len(word)

    # "cat" length is 3
    # "cat" 的长度是 3
    # "window" length is 6
    # "window" 的长度是 6
    # "defenestrate" length is 12
    # "defenestrate" 的长度是 12
    assert words_length == (3 + 6 + 12)

    # If you need to modify the sequence you are iterating over while inside the loop
    # (for example to duplicate selected items), it is recommended that you first make a copy.
    # Iterating over a sequence does not implicitly make a copy. The slice notation makes this
    # especially convenient:
    # 如果你需要在循环内部修改正在遍历的序列
    #（例如复制选定的项目），建议你先制作一个副本。
    # 遍历序列不会隐式地创建副本。切片表示法使这特别方便：
    for word in words[:]:  # Loop over a slice copy of the entire list.
                           # 遍历整个列表的切片副本。
        if len(word) > 6:
            words.insert(0, word)

    # Otherwise with for w in words:, the example would attempt to create an infinite list,
    # inserting defenestrate over and over again.
    # 否则，如果使用 for w in words:，这个例子会尝试创建一个无限列表，
    # 反复插入 defenestrate。

    assert words == ['defenestrate', 'cat', 'window', 'defenestrate']

    # If you do need to iterate over a sequence of numbers, the built-in function range() comes in
    # handy. It generates arithmetic progressions:
    # 如果你确实需要遍历一个数字序列，内置函数 range() 会很方便。
    # 它生成等差数列：
    iterated_numbers = []

    for number in range(5):
        iterated_numbers.append(number)

    assert iterated_numbers == [0, 1, 2, 3, 4]

    # To iterate over the indices of a sequence, you can combine range() and len() as follows:
    # 要遍历序列的索引，你可以按如下方式组合 range() 和 len()：
    words = ['Mary', 'had', 'a', 'little', 'lamb']
    concatenated_string = ''

    # pylint: disable=consider-using-enumerate
    for word_index in range(len(words)):
        concatenated_string += words[word_index] + ' '

    assert concatenated_string == 'Mary had a little lamb '

    # Or simply use enumerate().
    # 或者简单地使用 enumerate()。
    concatenated_string = ''

    for word_index, word in enumerate(words):
        concatenated_string += word + ' '

    assert concatenated_string == 'Mary had a little lamb '

    # When looping through dictionaries, the key and corresponding value can be retrieved at the
    # same time using the items() method.
    # 遍历字典时，可以使用 items() 方法同时获取键和对应的值。
    knights_names = []
    knights_properties = []

    knights = {'gallahad': 'the pure', 'robin': 'the brave'}
    for key, value in knights.items():
        knights_names.append(key)
        knights_properties.append(value)

    assert knights_names == ['gallahad', 'robin']
    assert knights_properties == ['the pure', 'the brave']

    # When looping through a sequence, the position index and corresponding value can be retrieved
    # at the same time using the enumerate() function
    # 遍历序列时，可以使用 enumerate() 函数同时获取位置索引和对应的值。
    indices = []
    values = []
    for index, value in enumerate(['tic', 'tac', 'toe']):
        indices.append(index)
        values.append(value)

    assert indices == [0, 1, 2]
    assert values == ['tic', 'tac', 'toe']

    # To loop over two or more sequences at the same time, the entries can be paired with
    # the zip() function.
    # 要同时遍历两个或多个序列，可以使用 zip() 函数将条目配对。
    questions = ['name', 'quest', 'favorite color']
    answers = ['lancelot', 'the holy grail', 'blue']
    combinations = []

    for question, answer in zip(questions, answers):
        combinations.append('What is your {0}?  It is {1}.'.format(question, answer))

    assert combinations == [
        'What is your name?  It is lancelot.',
        'What is your quest?  It is the holy grail.',
        'What is your favorite color?  It is blue.',
    ]


def test_range_function():
    """Range function

    Range 函数

    If you do need to iterate over a sequence of numbers, the built-in function range() comes in
    handy. It generates arithmetic progressions.

    如果你确实需要遍历一个数字序列，内置函数 range() 会很方便。
    它生成等差数列。

    In many ways the object returned by range() behaves as if it is a list, but in fact it isn’t.
    It is an object which returns the successive items of the desired sequence when you iterate
    over it, but it doesn’t really make the list, thus saving space.

    在许多方面，range() 返回的对象表现得像是一个列表，但实际上它不是。
    它是一个对象，当你遍历它时返回所需序列的连续项目，但它并不真正创建列表，从而节省空间。

    We say such an object is iterable, that is, suitable as a target for functions and constructs
    that expect something from which they can obtain successive items until the supply is exhausted.
    We have seen that the for statement is such an iterator. The function list() is another; it
    creates lists from iterables:

    我们说这样的对象是可迭代的，也就是说，适合作为期望从中获取连续项目直到供应耗尽的函数和结构的
    目标。我们已经看到 for 语句就是这样的迭代器。list() 函数是另一个；它从可迭代对象创建列表：
    """

    assert list(range(5)) == [0, 1, 2, 3, 4]

    # The given end point is never part of the generated sequence; range(10) generates 10 values,
    # the legal indices for items of a sequence of length 10. It is possible to let the range start
    # at another number, or to specify a different increment (even negative; sometimes this is
    # called the ‘step’):
    # 给定的终点永远不会是生成序列的一部分；range(10) 生成 10 个值，
    # 即长度为 10 的序列的合法索引。可以让范围从另一个数字开始，或指定不同的增量
    #（甚至是负数；有时这被称为’步长’）：

    assert list(range(5, 10)) == [5, 6, 7, 8, 9]
    assert list(range(0, 10, 3)) == [0, 3, 6, 9]
    assert list(range(-10, -100, -30)) == [-10, -40, -70]
