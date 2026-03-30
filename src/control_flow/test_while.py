"""WHILE statement
WHILE 语句

@see: https://docs.python.org/3/tutorial/controlflow.html
@see: https://docs.python.org/3/reference/compound_stmts.html#the-while-statement

The while loop executes as long as the condition remains true. In Python, like in C, any
non-zero integer value is true; zero is false. The condition may also be a string or list
value, in fact any sequence; anything with a non-zero length is true, empty sequences are
false.

while 循环只要条件保持为真就会执行。在 Python 中，像在 C 中一样，任何非零整数值都为真；
零为假。条件也可以是字符串或列表值，实际上任何序列都可以；任何具有非零长度的内容都为真，
空序列为假。

The test used in the example is a simple comparison. The standard comparison operators are
written the same as in C: < (less than), > (greater than), == (equal to), <= (less than or
equal to), >= (greater than or equal to) and != (not equal to).

示例中使用的测试是简单的比较。标准比较运算符的写法与 C 相同：<（小于）、>（大于）、
==（等于）、<=（小于或等于）、>=（大于或等于）和 !=（不等于）。
"""


def test_while_statement():
    """WHILE statement
    WHILE 语句
    """

    # Let's raise the number to certain power using while loop.
    # 让我们使用 while 循环将数字提升到某个幂。
    number = 2
    power = 5

    result = 1

    while power > 0:
        result *= number
        power -= 1

    # 2^5 = 32
    assert result == 32
