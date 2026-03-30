"""Identity operators

@see: https://www.w3schools.com/python/python_operators.asp

Identity operators are used to compare the objects, not if they are equal, but if they are actually
the same object, with the same memory location.
身份操作符用于比较对象，不是比较它们是否相等，而是比较它们是否实际上是同一个对象，具有相同的内存位置。
"""
import pprint


def test_identity_operators():
    """Identity operators 身份操作符"""

    # Let's illustrate identity operators based on the following lists.
    # 让我们根据以下列表来阐述身份运算符。
    first_fruits_list = ["apple", "banana"]
    second_fruits_list = ["apple", "banana"]
    third_fruits_list = first_fruits_list

    print("")
    print(first_fruits_list)
    print(second_fruits_list)
    # is
    # Returns true if both variables are the same object.
    # is 返回值表示两个变量是否为同一对象。

    # Example:
    # first_fruits_list and third_fruits_list are the same objects.
    assert first_fruits_list is third_fruits_list

    # is not
    # Returns true if both variables are not the same object.

    # Example:
    # first_fruits_list and second_fruits_list are not the same objects, even if they have
    # the same content
    assert first_fruits_list is not second_fruits_list

    # To demonstrate the difference between "is" and "==": this comparison returns True because
    # first_fruits_list is equal to second_fruits_list.
    # 为了演示"是"和"=="之间的区别：这个比较返回True，因为
    # first_fruits_list 等于 second_fruits_list。
    assert first_fruits_list == second_fruits_list
