"""Strings.
字符串。

@see: https://docs.python.org/3/tutorial/introduction.html
@see: https://www.w3schools.com/python/python_strings.asp
@see: https://www.w3schools.com/python/python_ref_string.asp

Besides numbers, Python can also manipulate strings, which can be
expressed in several ways. They can be enclosed in single quotes ('...')
or double quotes ("...") with the same result.

除了数字，Python 还可以操作字符串，可以用多种方式表示。它们可以用单引号 ('...')
或双引号 ("...") 括起来，结果相同。
"""

import pytest


def test_string_type():
    """String type
    字符串类型
    """

    # String with double quotes.
    # 双引号字符串。
    name_1 = "John"
    # String with single quotes.
    # 单引号字符串。
    name_2 = 'John'
    # Strings created with different kind of quotes are treated the same.
    # 使用不同类型引号创建的字符串被视为相同。
    assert name_1 == name_2
    assert isinstance(name_1, str)
    assert isinstance(name_2, str)

    # \ can be used to escape quotes.
    # use \' to escape the single quote or use double quotes instead.
    # \ 可用于转义引号。
    # 使用 \' 转义单引号，或使用双引号代替。
    single_quote_string = 'doesn\'t'
    double_quote_string = "doesn't"

    assert single_quote_string == double_quote_string

    # \n means newline.
    # \n 表示换行。
    multiline_string = 'First line.\nSecond line.'
    # Without print(), \n is included in the output.
    # But with print(), \n produces a new line.
    # 没有 print()，\n 包含在输出中。
    # 但使用 print()，\n 会产生新行。
    assert multiline_string == 'First line.\nSecond line.'

    # Strings can be indexed, with the first character having index 0.
    # There is no separate character type; a character is simply a string
    # of size one. Note that since -0 is the same as 0, negative indices
    # start from -1.
    # 字符串可以被索引，第一个字符的索引为 0。
    # 没有单独的字符类型；字符只是大小为 1 的字符串。
    # 注意由于 -0 与 0 相同，负索引从 -1 开始。
    word = 'Python'
    assert word[0] == 'P'  # First character.
    # 第一个字符。
    assert word[5] == 'n'  # Fifth character.
    # 第五个字符。
    assert word[-1] == 'n'  # Last character.
    # 最后一个字符。
    assert word[-2] == 'o'  # Second-last character.
    # 倒数第二个字符。
    assert word[-6] == 'P'  # Sixth from the end or zeroth from the beginning.
    # 倒数第六个字符或第一个字符。

    assert isinstance(word[0], str)

    # In addition to indexing, slicing is also supported. While indexing is
    # used to obtain individual characters, slicing allows you to obtain
    # substring:
    # 除了索引，还支持切片。索引用于获取单个字符，
    # 切片允许你获取子字符串：
    assert word[0:2] == 'Py'  # Characters from position 0 (included) to 2 (excluded).
    # 从位置 0（包含）到 2（不包含）的字符。
    assert word[2:5] == 'tho'  # Characters from position 2 (included) to 5 (excluded).
    # 从位置 2（包含）到 5（不包含）的字符。

    # Note how the start is always included, and the end always excluded.
    # This makes sure that s[:i] + s[i:] is always equal to s:
    # 注意开始总是包含的，结束总是排除的。
    # 这确保 s[:i] + s[i:] 总是等于 s：
    assert word[:2] + word[2:] == 'Python'
    assert word[:4] + word[4:] == 'Python'

    # Slice indices have useful defaults; an omitted first index defaults to
    # zero, an omitted second index defaults to the size of the string being
    # sliced.
    # 切片索引有有用的默认值；省略的第一个索引默认为零，
    # 省略的第二个索引默认为被切片字符串的大小。
    assert word[:2] == 'Py'  # Character from the beginning to position 2 (excluded).
    # 从开头到位置 2（不包含）的字符。
    assert word[4:] == 'on'  # Characters from position 4 (included) to the end.
    # 从位置 4（包含）到末尾的字符。
    assert word[-2:] == 'on'  # Characters from the second-last (included) to the end.
    # 从倒数第二个（包含）到末尾的字符。

    # One way to remember how slices work is to think of the indices as
    # pointing between characters, with the left edge of the first character
    # numbered 0. Then the right edge of the last character of a string of n
    # characters has index n, for example:
    # 记住切片如何工作的一种方法是将索引视为指向字符之间，
    # 第一个字符的左边缘编号为 0。那么 n 个字符的字符串的
    # 最后一个字符的右边缘索引为 n，例如：
    #
    # +---+---+---+---+---+---+
    #  | P | y | t | h | o | n |
    #  +---+---+---+---+---+---+
    #  0   1   2   3   4   5   6
    # -6  -5  -4  -3  -2  -1

    # Attempting to use an index that is too large will result in an error.
    # 尝试使用过大的索引将导致错误。
    with pytest.raises(Exception):
        not_existing_character = word[42]
        assert not not_existing_character

    # However, out of range slice indexes are handled gracefully when used
    # for slicing:
    # 但是，当用于切片时，超出范围的切片索引会被优雅地处理：
    assert word[4:42] == 'on'
    assert word[42:] == ''

    # Python strings cannot be changed — they are immutable. Therefore,
    # assigning to an indexed position in the string
    # results in an error:
    # Python 字符串不能被改变 —— 它们是不可变的。因此，
    # 给字符串中的索引位置赋值会导致错误：
    with pytest.raises(Exception):
        # pylint: disable=unsupported-assignment-operation
        word[0] = 'J'

    # If you need a different string, you should create a new one:
    # 如果你需要不同的字符串，你应该创建一个新的：
    assert 'J' + word[1:] == 'Jython'
    assert word[:2] + 'py' == 'Pypy'

    # The built-in function len() returns the length of a string:
    # 内置函数 len() 返回字符串的长度：
    characters = 'supercalifragilisticexpialidocious'
    assert len(characters) == 34

    # String literals can span multiple lines. One way is using triple-quotes: """..."""
    # or '''...'''. End of lines are automatically included in the string, but it's possible
    # to prevent this by adding a \ at the end of the line. The following example:
    # 字符串字面量可以跨越多行。一种方法是使用三引号："""...""" 或 '''...'''。
    # 行尾自动包含在字符串中，但可以通过在行尾添加 \ 来防止这种情况。
    # 以下示例：
    multi_line_string = '''\
        First line
        Second line
    '''

    assert multi_line_string == '''\
        First line
        Second line
    '''


def test_string_operators():
    """Basic operations
    基本操作

    Strings can be concatenated (glued together) with the + operator,
    and repeated with *: 3 times 'un', followed by 'ium'

    字符串可以使用 + 运算符连接（粘在一起），
    并使用 * 重复：3 次 'un'，然后是 'ium'
    """

    assert 3 * 'un' + 'ium' == 'unununium'

    # 'Py' 'thon'
    python = 'Py' 'thon'
    assert python == 'Python'

    # This feature is particularly useful when you want to break long strings:
    # 此功能在你想拆分长字符串时特别有用：
    text = (
        'Put several strings within parentheses '
        'to have them joined together.'
    )
    assert text == 'Put several strings within parentheses to have them joined together.'

    # If you want to concatenate variables or a variable and a literal, use +:
    # 如果你想连接变量或变量和字面量，请使用 +：
    prefix = 'Py'
    assert prefix + 'thon' == 'Python'


def test_string_methods():
    """String methods
    字符串方法
    """

    hello_world_string = "Hello, World!"

    # The strip() method removes any whitespace from the beginning or the end.
    # strip() 方法删除开头或结尾的任何空白。
    string_with_whitespaces = " Hello, World! "
    assert string_with_whitespaces.strip() == "Hello, World!"

    # The len() method returns the length of a string.
    # len() 方法返回字符串的长度。
    assert len(hello_world_string) == 13

    # The lower() method returns the string in lower case.
    # lower() 方法返回小写字符串。
    assert hello_world_string.lower() == 'hello, world!'

    # The upper() method returns the string in upper case.
    # upper() 方法返回大写字符串。
    assert hello_world_string.upper() == 'HELLO, WORLD!'

    # The replace() method replaces a string with another string.
    # replace() 方法用另一个字符串替换字符串。
    assert hello_world_string.replace('H', 'J') == 'Jello, World!'

    # The split() method splits the string into substrings if it finds instances of the separator.
    # split() 方法如果找到分隔符的实例，会将字符串拆分为子字符串。
    assert hello_world_string.split(',') == ['Hello', ' World!']

    # Converts the first character to upper case
    # 将第一个字符转换为大写
    assert 'low letter at the beginning'.capitalize() == 'Low letter at the beginning'

    # Returns the number of times a specified value occurs in a string.
    # 返回指定值在字符串中出现的次数。
    assert 'low letter at the beginning'.count('t') == 4

    # Searches the string for a specified value and returns the position of where it was found.
    # 在字符串中搜索指定值并返回找到它的位置。
    assert 'Hello, welcome to my world'.find('welcome') == 7

    # Converts the first character of each word to upper case
    # 将每个单词的第一个字符转换为大写
    assert 'Welcome to my world'.title() == 'Welcome To My World'

    # Returns a string where a specified value is replaced with a specified value.
    # 返回一个字符串，其中指定值被替换为指定值。
    assert 'I like bananas'.replace('bananas', 'apples') == 'I like apples'

    # Joins the elements of an iterable to the end of the string.
    # 将可迭代对象的元素连接到字符串的末尾。
    my_tuple = ('John', 'Peter', 'Vicky')
    assert ', '.join(my_tuple) == 'John, Peter, Vicky'

    # Returns True if all characters in the string are upper case.
    # 如果字符串中的所有字符都是大写，则返回 True。
    assert 'ABC'.isupper()
    assert not 'AbC'.isupper()

    # Check if all the characters in the text are letters.
    # 检查文本中的所有字符是否都是字母。
    assert 'CompanyX'.isalpha()
    assert not 'Company 23'.isalpha()

    # Returns True if all characters in the string are decimals.
    # 如果字符串中的所有字符都是十进制数字，则返回 True。
    assert '1234'.isdecimal()
    assert not 'a21453'.isdecimal()


def test_string_formatting():
    """String formatting.
    字符串格式化。

    Often you'll want more control over the formatting of your output than simply printing
    space-separated values. There are several ways to format output

    通常，你会希望对输出的格式有更多控制，而不仅仅是打印空格分隔的值。
    有几种格式化输出的方法
    """

    # To use formatted string literals, begin a string with f or F before the opening quotation
    # mark or triple quotation mark. Inside this string, you can write a Python expression
    # between { and } characters that can refer to variables or literal values.
    # 要使用格式化字符串字面量，在开始引号或三引号之前以 f 或 F 开始字符串。
    # 在此字符串中，你可以在 { 和 } 字符之间编写 Python 表达式，
    # 该表达式可以引用变量或字面值。
    year = 2018
    event = 'conference'

    assert f'Results of the {year} {event}' == 'Results of the 2018 conference'

    # The str.format() method of strings requires more manual effort. You'll still use { and } to
    # mark where a variable will be substituted and can provide detailed formatting directives,
    # but you'll also need to provide the information to be formatted.
    # 字符串的 str.format() 方法需要更多的手动工作。你仍然使用 { 和 } 来标记
    # 变量将被替换的位置，并可以提供详细的格式化指令，
    # 但你还需要提供要格式化的信息。
    yes_votes = 42_572_654  # equivalent of 42572654
    # 等同于 42572654
    no_votes = 43_132_495   # equivalent of 43132495
    # 等同于 43132495
    percentage = yes_votes / (yes_votes + no_votes)

    assert '{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage) == ' 42572654 YES votes  49.67%'

    # When you don’t need fancy output but just want a quick display of some variables for debugging
    # purposes, you can convert any value to a string with the repr() or str() functions. The str()
    # function is meant to return representations of values which are fairly human-readable, while
    # repr() is meant to generate representations which can be read by the interpreter (or will
    # force a SyntaxError if there is no equivalent syntax). For objects which don’t have a
    # particular representation for human consumption, str() will return the same value as repr().
    # Many values, such as numbers or structures like lists and dictionaries, have the same
    # representation using either function. Strings, in particular, have two distinct
    # representations.
    # 当你不需要花哨的输出，而只是想快速显示一些变量以进行调试时，
    # 你可以使用 repr() 或 str() 函数将任何值转换为字符串。str() 函数用于返回
    # 人类可读的值表示，而 repr() 用于生成解释器可读的表示（如果没有等效语法，
    # 则会强制引发 SyntaxError）。对于没有特定人类可读表示的对象，
    # str() 将返回与 repr() 相同的值。许多值，如数字或列表和字典等结构，
    # 使用任一函数都有相同的表示。特别是字符串，有两种不同的表示。

    greeting = 'Hello, world.'
    first_num = 10 * 3.25
    second_num = 200 * 200

    assert str(greeting) == 'Hello, world.'
    assert repr(greeting) == "'Hello, world.'"
    assert str(1/7) == '0.14285714285714285'

    # The argument to repr() may be any Python object:
    # repr() 的参数可以是任何 Python 对象：
    assert repr((first_num, second_num, ('spam', 'eggs'))) == "(32.5, 40000, ('spam', 'eggs'))"

    # Formatted String Literals
    # 格式化字符串字面量

    # Formatted string literals (also called f-strings for short) let you include the value of
    # Python expressions inside a string by prefixing the string with f or F and writing
    # expressions as {expression}.
    # 格式化字符串字面量（也称为 f-strings）让你通过在字符串前加 f 或 F 并将
    # 表达式写为 {expression} 来在字符串中包含 Python 表达式的值。

    # An optional format specifier can follow the expression. This allows greater control over how
    # the value is formatted. The following example rounds pi to three places after the decimal.
    # 可选的格式说明符可以跟在表达式后面。这允许更好地控制值的格式化方式。
    # 以下示例将 pi 四舍五入到小数点后三位。
    pi_value = 3.14159
    assert f'The value of pi is {pi_value:.3f}.' == 'The value of pi is 3.142.'

    # Passing an integer after the ':' will cause that field to be a minimum number of characters
    # wide. This is useful for making columns line up:
    # 在 ':' 后传递整数将使该字段成为最小字符宽度。
    # 这对于使列对齐很有用：
    table_data = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
    table_string = ''
    for name, phone in table_data.items():
        table_string += f'{name:7}==>{phone:7d}'

    assert table_string == ('Sjoerd ==>   4127'
                            'Jack   ==>   4098'
                            'Dcab   ==>   7678')

    # The String format() Method
    # 字符串 format() 方法

    # Basic usage of the str.format() method looks like this:
    # str.format() 方法的基本用法如下：
    assert 'We are {} who say "{}!"'.format('knights', 'Ni') == 'We are knights who say "Ni!"'

    # The brackets and characters within them (called format fields) are replaced with the objects
    # passed into the str.format() method. A number in the brackets can be used to refer to the
    # position of the object passed into the str.format() method
    # 括号及其中的字符（称为格式字段）被传递给 str.format() 方法的对象替换。
    # 括号中的数字可用于引用传递给 str.format() 方法的对象的位置
    assert '{0} and {1}'.format('spam', 'eggs') == 'spam and eggs'
    assert '{1} and {0}'.format('spam', 'eggs') == 'eggs and spam'

    # If keyword arguments are used in the str.format() method, their values are referred to by
    # using the name of the argument.
    # 如果在 str.format() 方法中使用关键字参数，则通过参数名称引用其值。
    formatted_string = 'This {food} is {adjective}.'.format(
        food='spam',
        adjective='absolutely horrible'
    )

    assert formatted_string == 'This spam is absolutely horrible.'

    # Positional and keyword arguments can be arbitrarily combined
    # 位置参数和关键字参数可以任意组合
    formatted_string = 'The story of {0}, {1}, and {other}.'.format(
        'Bill',
        'Manfred',
        other='Georg'
    )

    assert formatted_string == 'The story of Bill, Manfred, and Georg.'

    # If you have a really long format string that you don’t want to split up, it would be nice if
    # you could reference the variables to be formatted by name instead of by position. This can be
    # done by simply passing the dict and using square brackets '[]' to access the keys
    # 如果你有一个很长的格式字符串不想拆分，最好能通过名称而不是位置引用要格式化的变量。
    # 这可以通过简单地传递字典并使用方括号 '[]' 访问键来完成

    table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
    formatted_string = 'Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; Dcab: {0[Dcab]:d}'.format(table)

    assert formatted_string == 'Jack: 4098; Sjoerd: 4127; Dcab: 8637678'

    # This could also be done by passing the table as keyword arguments with the '**' notation.
    # 这也可以通过使用 '**' 符号将表作为关键字参数传递来完成。
    formatted_string = 'Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table)

    assert formatted_string == 'Jack: 4098; Sjoerd: 4127; Dcab: 8637678'
