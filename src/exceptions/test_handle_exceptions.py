"""Errors and Exceptions.

@see: https://docs.python.org/3/tutorial/errors.html#errors-and-exceptions

Even if a statement or expression is syntactically correct, it may cause an error when an attempt
is made to execute it. Errors detected during execution are called exceptions and are not
unconditionally fatal.

It is possible to write programs that handle selected exceptions.

错误和异常。

即使语句或表达式在语法上是正确的，在执行时也可能导致错误。执行期间检测到的错误称为异常，它们并非无条件致命。

可以编写程序来处理选定的异常。
"""


def test_handle_exceptions():
    """Handling of exceptions

    The try statement works as follows.

    - First, the try clause (the statement(s) between the try and except keywords) is executed.

    - If no exception occurs, the except clause is skipped and execution of the try statement
    is finished.

    - If an exception occurs during execution of the try clause, the rest of the clause is skipped.
    Then if its type matches the exception named after the except keyword, the except clause is
    executed, and then execution continues after the try statement.

    - If an exception occurs which does not match the exception named in the except clause, it is
    passed on to outer try statements; if no handler is found, it is an unhandled exception and
    execution stops with a message.

    异常处理

    try 语句的工作原理如下：

    - 首先，执行 try 子句（try 和 except 关键字之间的语句）。

    - 如果没有发生异常，则跳过 except 子句，try 语句的执行结束。

    - 如果在执行 try 子句期间发生异常，则跳过该子句的其余部分。然后，如果其类型与 except 关键字后面的异常名称匹配，则执行 except 子句，然后继续执行 try 语句之后的代码。

    - 如果发生的异常与 except 子句中命名的异常不匹配，则将其传递给外部的 try 语句；如果未找到处理程序，则它是一个未处理的异常，执行将停止并显示一条消息。
    """

    # Let's simulate division by zero exception.
    # 让我们模拟除以零的异常。
    exception_has_been_handled = False
    try:
        result = 10 * (1 / 0)  # division by zero
        # We should not get here at all.
        assert result
    except ZeroDivisionError:
        # We should get here because of division by zero.
        exception_has_been_handled = True

    assert exception_has_been_handled

    # Let's simulate undefined variable access exception.
    # 让我们模拟未定义变量访问异常。
    exception_has_been_handled = False
    try:
        # pylint: disable=undefined-variable
        result = 4 + spam * 3  # name 'spam' is not defined
        # 名称 'spam' 未定义
        # We should not get here at all.
        # 我们根本不应该到达这里。
        assert result
    except NameError:
        # We should get here because of division by zero.
        exception_has_been_handled = True

    assert exception_has_been_handled

    # A try statement may have more than one except clause, to specify handlers for different
    # exceptions. At most one handler will be executed. Handlers only handle exceptions that occur
    # in the corresponding try clause, not in other handlers of the same try statement. An except
    # clause may name multiple exceptions as a parenthesized tuple, for example:
    # try 语句可以有多个 except 子句，用于为不同的异常指定处理程序。最多只会执行一个处理程序。
    # 处理程序只处理相应 try 子句中发生的异常，而不处理同一 try 语句的其他处理程序中的异常。
    # except 子句可以将多个异常命名为带括号的元组，例如：

    exception_has_been_handled = False
    try:
        result = 10 * (1 / 0)  # division by zero
        # We should not get here at all.
        assert result
    except (ZeroDivisionError, NameError):
        # We should get here because of division by zero.
        # 由于除以零，我们应该到达这里。
        exception_has_been_handled = True

    assert exception_has_been_handled

    # Exception handlers may be chained.
    # 异常处理程序可以链式连接。
    exception_has_been_handled = False
    try:
        result = 10 * (1 / 0)  # division by zero
        # We should not get here at all.
        assert result
    except NameError:
        # We should get here because of division by zero.
        exception_has_been_handled = True
    except ZeroDivisionError:
        # We should get here because of division by zero.
        exception_has_been_handled = True

    assert exception_has_been_handled

    # The try … except statement has an optional else clause, which, when present, must follow all
    # except clauses. It is useful for code that must be executed if the try clause does not raise
    # an exception. For example:
    # try … except 语句有一个可选的 else 子句，如果存在，则必须位于所有 except 子句之后。
    # 它适用于当 try 子句没有引发异常时必须执行的代码。例如：

    exception_has_been_handled = False
    no_exceptions_has_been_fired = False

    try:
        result = 10
        # We should not get here at all.
        # 我们根本不应该到达这里。
        assert result
    except NameError:
        # We should get here because of division by zero.
        exception_has_been_handled = True
    else:
        no_exceptions_has_been_fired = True

    assert not exception_has_been_handled
    assert no_exceptions_has_been_fired
