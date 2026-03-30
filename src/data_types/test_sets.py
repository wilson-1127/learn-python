"""Sets.
集合。

@see: https://www.w3schools.com/python/python_sets.asp
@see: https://docs.python.org/3.7/tutorial/datastructures.html#sets

A set is a collection which is unordered and unindexed.
In Python sets are written with curly brackets.

集合是一个无序且无索引的集合。
在 Python 中，集合用花括号编写。

Set objects also support mathematical operations like union, intersection, difference, and
symmetric difference.

集合对象还支持数学运算，如并集、交集、差集和对称差集。
"""


def test_sets():
    """Sets
    集合
    """
    fruits_set = {"apple", "banana", "cherry"}

    assert isinstance(fruits_set, set)

    # It is also possible to use the set() constructor to make a set.
    # Note the double round-brackets
    # 也可以使用 set() 构造函数来创建集合。
    # 注意双圆括号
    fruits_set_via_constructor = set(("apple", "banana", "cherry"))

    assert isinstance(fruits_set_via_constructor, set)


def test_set_methods():
    """Set methods
    集合方法
    """

    fruits_set = {"apple", "banana", "cherry"}

    # You may check if the item is in set by using "in" statement
    # 你可以使用 "in" 语句检查项目是否在集合中
    assert "apple" in fruits_set
    assert "pineapple" not in fruits_set

    # Use the len() method to return the number of items.
    # 使用 len() 方法返回项目数量。
    assert len(fruits_set) == 3

    # You can use the add() object method to add an item.
    # 你可以使用 add() 对象方法添加项目。
    fruits_set.add("pineapple")
    assert "pineapple" in fruits_set
    assert len(fruits_set) == 4

    # Use remove() method to remove an item.
    # 使用 remove() 方法删除项目。
    fruits_set.remove("pineapple")
    assert "pineapple" not in fruits_set
    assert len(fruits_set) == 3

    # Demonstrate set operations on unique letters from two word:
    # 演示两个单词中唯一字母的集合操作：
    first_char_set = set('abracadabra')
    second_char_set = set('alacazam')

    assert first_char_set == {'a', 'r', 'b', 'c', 'd'}  # unique letters in first word
    # 第一个单词中的唯一字母
    assert second_char_set == {'a', 'l', 'c', 'z', 'm'}  # unique letters in second word
    # 第二个单词中的唯一字母

    # Letters in first word but not in second.
    # 在第一个单词中但不在第二个单词中的字母。
    assert first_char_set - second_char_set == {'r', 'b', 'd'}

    # Letters in first word or second word or both.
    # 在第一个单词或第二个单词或两者中的字母。
    assert first_char_set | second_char_set == {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}

    # Common letters in both words.
    # 两个单词中的公共字母。
    assert first_char_set & second_char_set == {'a', 'c'}

    # Letters in first or second word but not both.
    # 在第一个或第二个单词中但不同时在两者中的字母。
    assert first_char_set ^ second_char_set == {'r', 'd', 'b', 'm', 'z', 'l'}

    # Similarly to list comprehensions, set comprehensions are also supported:
    # 与列表推导式类似，也支持集合推导式：
    word = {char for char in 'abracadabra' if char not in 'abc'}
    assert word == {'r', 'd'}
