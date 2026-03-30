"""String Pattern Matching.
字符串模式匹配

@see: https://docs.python.org/3/tutorial/stdlib.html#string-pattern-matching

The re module provides regular expression tools for advanced string processing.
for complex matching and manipulation, regular expressions offer succinct, optimized solutions:
re 模块为高级字符串处理提供了正则表达式工具。
对于复杂的匹配和操作，正则表达式提供了简洁、优化的解决方案
"""

import re


def test_re():
    """String Pattern Matching
    字符串模式匹配
    """

    assert re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest') == [
        'foot',
        'fell',
        'fastest'
    ]
    # 在 'which foot or hand fell fastest' 中找到所有以 'f' 开头的单词
    # findall 查找所有匹配的字符串

    assert re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat') == 'cat in the hat'
    # 将 'cat in the the hat' 中的第一个以 'f' 开头的单词替换为 '\1'
    # sub 替换匹配的字符串

    # When only simple capabilities are needed, string methods are preferred because they are
    # easier to read and debug:
    # 当只需要简单功能时，字符串方法更受欢迎，因为它们更易于阅读和调试：
    assert 'tea for too'.replace('too', 'two') == 'tea for two'
    # 将 'tea for too' 中的 'too' 替换为 'two'
