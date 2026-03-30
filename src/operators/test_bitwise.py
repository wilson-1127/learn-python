"""Bitwise operators

@see: https://www.w3schools.com/python/python_operators.asp

Bitwise operators manipulate numbers on bit level.

位运算符在二进制位级别上操作数字。
"""


def test_bitwise_operators():
    """Bitwise operators

    位运算符
    """

    # AND
    # Sets each bit to 1 if both bits are 1.
    # 按位与（AND）
    # 如果两个位都为 1，则将每个位设置为 1。
    #
    # Example:
    # 示例：
    # 5 = 0b0101
    # 3 = 0b0011
    assert 5 & 3 == 1  # 0b0001

    # OR
    # Sets each bit to 1 if one of two bits is 1.
    # 按位或（OR）
    # 如果两个位中有一个为 1，则将每个位设置为 1。
    #
    # Example:
    # 示例：
    # 5 = 0b0101
    # 3 = 0b0011
    assert 5 | 3 == 7  # 0b0111

    # NOT
    # Inverts all the bits.
    # 按位非（NOT）
    # 反转所有的位。
    assert ~5 == -6

    # XOR
    # Sets each bit to 1 if only one of two bits is 1.
    # 按位异或（XOR）
    # 如果两个位中只有一个为 1，则将每个位设置为 1。
    #
    # Example:
    # 示例：
    # 5 = 0b0101
    # 3 = 0b0011
    number = 5  # 0b0101
    number ^= 3  # 0b0011
    assert 5 ^ 3 == 6  # 0b0110

    # Signed right shift
    # Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost
    # bits fall off.
    # 有符号右移
    # 通过从左侧推入最左边位的副本向右移位，并让最右边的位脱落。
    #
    # Example:
    # 示例：
    # 5 = 0b0101
    assert 5 >> 1 == 2  # 0b0010
    assert 5 >> 2 == 1  # 0b0001

    # Zero fill left shift
    # Shift left by pushing zeros in from the right and let the leftmost bits fall off.
    # 零填充左移
    # 通过从右侧推入零向左移位，并让最左边的位脱落。
    #
    # Example:
    # 示例：
    # 5 = 0b0101
    assert 5 << 1 == 10  # 0b1010
    assert 5 << 2 == 20  # 0b10100
