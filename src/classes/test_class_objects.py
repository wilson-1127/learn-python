"""Class Definition Syntax.

@see: https://docs.python.org/3/tutorial/classes.html#class-objects

After defining the class attributes to a class, the class object can be created by assigning the
object to a variable. The created object would have instance attributes associated with it.
"""


def test_class_objects():
    """Class Objects.

    Class objects support two kinds of operations:
    - attribute references
    - instantiation.

    类对象。

    类对象支持两种操作：
    - 属性参考
    - 实例化。
    """

    # ATTRIBUTE REFERENCES use the standard syntax used for all attribute references in
    # Python: obj.name. Valid attribute names are all the names that were in the class’s namespace
    # when the class object was created. For class MyCounter the following references are valid
    # attribute references:

    #属性引用使用用于所有属性引用的标准语法
    # Python：obj.name。有效的属性名称是类命名空间中的所有名称
    # 创建类对象时。对于MyCounter类，以下参考资料是有效的
    # 评估项目参考：

    class ComplexNumber:
        """Example of the complex numbers class"""

        real = 0
        imaginary = 0

        def get_real(self):
            """Return real part of complex number."""
            return self.real

        def get_imaginary(self):
            """Return imaginary part of complex number."""
            return self.imaginary

    assert ComplexNumber.real == 0

    # __doc__ is also a valid attribute, returning the docstring belonging to the class
    assert ComplexNumber.__doc__ == 'Example of the complex numbers class'

    # Class attributes can also be assigned to, so you can change the value of
    # ComplexNumber.counter by assignment.
    # 类属性也可以被赋值，因此你可以通过赋值来改变ComplexNumber.counter的值。
    ComplexNumber.real = 10
    assert ComplexNumber.real == 10

    # CLASS INSTANTIATION uses function notation. Just pretend that the class object is a
    # parameterless function that returns a new instance of the class. For example
    # (assuming the above class):
    # 类实例化使用函数符号。就假装班级对象是一个
    # 返回类新实例的无参数函数。例如
    # （假设上述类）：
    complex_number = ComplexNumber()

    assert complex_number.real == 10
    assert complex_number.get_real() == 10

    # Let's change counter default value back.
    ComplexNumber.real = 10
    assert ComplexNumber.real == 10

    # The instantiation operation (“calling” a class object) creates an empty object. Many classes
    # like to create objects with instances customized to a specific initial state. Therefore a
    # class may define a special method named __init__(), like this:

    # 实例化操作（“调用”类对象）创建一个空对象。很多班级
    # 喜欢创建具有自定义到特定初始状态的实例的对象。因此，一个
    # 類可以定義一個名為__init__（）的特殊方法，如下如下：
    class ComplexNumberWithConstructor:
        """Example of the class with constructor"""
        def __init__(self, real_part, imaginary_part):
            self.real = real_part
            self.imaginary = imaginary_part

        def get_real(self):
            """Return real part of complex number."""
            return self.real

        def get_imaginary(self):
            """Return imaginary part of complex number."""
            return self.imaginary

    complex_number = ComplexNumberWithConstructor(3.0, -4.5)
    assert complex_number.real, complex_number.imaginary == (3.0, -4.5)
