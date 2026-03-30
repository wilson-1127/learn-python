“””Packages.

@see: https://docs.python.org/3/tutorial/modules.html#packages

Packages are a way of structuring Python’s module namespace by using “dotted module names”. For
example, the module name A.B designates a submodule named B in a package named A. Just like the
use of modules saves the authors of different modules from having to worry about each other’s
global variable names, the use of dotted module names saves the authors of multi-module packages
like NumPy or Pillow from having to worry about each other’s module names.

The __init__.py files are required to make Python treat the directories as containing packages;
this is done to prevent directories with a common name, such as string, from unintentionally hiding
valid modules that occur later on the module search path. In the simplest case, __init__.py can
just be an empty file, but it can also execute initialization code for the package or set the
__all__ variable, described later.

When the interpreter executes the import statement, it searches for module in a list of
directories assembled from the following sources:

- The directory from which the input script was run or the current directory if the interpreter is
being run interactively
- The list of directories contained in the PYTHONPATH environment variable, if it is set. (The
format for PYTHONPATH is OS-dependent but should mimic the PATH environment variable.)
- An installation-dependent list of directories configured at the time Python is installed

The resulting search path is accessible in the Python variable sys.path, which is obtained from a
module named sys:

>>> import sys
>>> sys.path

@see: https://realpython.com/python-modules-packages/

包。

包是一种通过使用”点分模块名”来构建 Python 模块命名空间的方式。例如，模块名 A.B 表示在名为 A 的包中名为 B 的子模块。
就像使用模块可以让不同模块的作者不必担心彼此的全局变量名一样，使用点分模块名可以让 NumPy 或 Pillow 等多模块包的作者不必担心彼此的模块名。

__init__.py 文件是必需的，用于让 Python 将目录视为包含包；这样做是为了防止具有通用名称（如 string）的目录无意中隐藏在模块搜索路径后面出现的有效模块。
在最简单的情况下，__init__.py 可以只是一个空文件，但它也可以执行包的初始化代码或设置 __all__ 变量（稍后描述）。

当解释器执行 import 语句时，它会在由以下来源组装的目录列表中搜索模块：

- 运行输入脚本的目录，或者如果解释器以交互方式运行，则为当前目录
- PYTHONPATH 环境变量中包含的目录列表（如果已设置）。（PYTHONPATH 的格式取决于操作系统，但应模仿 PATH 环境变量。）
- 安装时配置的与安装相关的目录列表

生成的搜索路径可在 Python 变量 sys.path 中访问，该变量从名为 sys 的模块获取：

>>> import sys
>>> sys.path
“””

# Users of the package can import individual modules from the package, for example.
# 包的用户可以从包中导入单个模块，例如：
import sound_package.effects.echo

# An alternative way of importing the submodule is:
# 导入子模块的另一种方式是：

# pylint: disable=reimported
from sound_package.effects import echo

# Yet another variation is to import the desired function or variable directly:
# 还有一种变体是直接导入所需的函数或变量：
from sound_package.effects.echo import echo_function

# Note that when using from package import item, the item can be either a submodule (or subpackage)
# of the package, or some other name defined in the package, like a function, class or variable.
# The import statement first tests whether the item is defined in the package; if not, it assumes
# it is a module and attempts to load it. If it fails to find it, an ImportError exception is
# raised.
#
# 请注意，当使用 from package import item 时，item 可以是包的子模块（或子包），也可以是包中定义的其他名称，如函数、类或变量。
# import 语句首先测试该项是否在包中定义；如果没有，它假定它是一个模块并尝试加载它。如果找不到它，将引发 ImportError 异常。

# Contrarily, when using syntax like import item.subitem.subsubitem, each item except for the last
# must be a package; the last item can be a module or a package but can’t be a class or function or
# variable defined in the previous item.
#
# 相反，当使用 import item.subitem.subsubitem 这样的语法时，除了最后一项外，每一项都必须是包；最后一项可以是模块或包，但不能是前一项中定义的类、函数或变量。


def test_packages():
    """Packages.

    包
    """
    assert sound_package.effects.echo.echo_function() == 'Do echo effect'
    assert echo.echo_function() == 'Do echo effect'
    assert echo_function() == 'Do echo effect'
