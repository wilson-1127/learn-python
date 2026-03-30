"""Serialization.

@see: https://www.learnpython.org/en/Serialization

Python provides built-in JSON libraries to encode and decode JSON.

序列化。

Python 提供了内置的 JSON 库来编码和解码 JSON。
"""

import json


def test_json():
    """JSON serialization.

    JSON 序列化
    """

    # There are two basic formats for JSON data. Either in a string or the object data-structure.
    # The object data-structure, in Python, consists of lists and dictionaries nested inside each
    # other. The object data-structure allows one to use python methods (for lists and dictionaries)
    # to add, list, search and remove elements from the data-structure. The String format is mainly
    # used to pass the data into another program or load into a data-structure.
    # JSON 数据有两种基本格式。要么是字符串，要么是对象数据结构。
    # 在 Python 中，对象数据结构由相互嵌套的列表和字典组成。
    # 对象数据结构允许使用 Python 方法（针对列表和字典）来添加、列出、搜索和删除数据结构中的元素。
    # 字符串格式主要用于将数据传递到另一个程序或加载到数据结构中。

    person_dictionary = {'first_name': 'John', 'last_name': 'Smith', 'age': 42}
    assert person_dictionary['first_name'] == 'John'
    assert person_dictionary['age'] == 42

    json_string = '{"first_name": "John", "last_name": "Smith", "age": 42}'

    # To load JSON back to a data structure, use the "loads" method. This method takes a string
    # and turns it back into the json object data-structure:
    # 要将 JSON 加载回数据结构，请使用 "loads" 方法。此方法接受一个字符串
    # 并将其转换回 json 对象数据结构：
    person_parsed_dictionary = json.loads(json_string)

    assert person_parsed_dictionary == person_dictionary
    assert person_parsed_dictionary['first_name'] == 'John'
    assert person_parsed_dictionary['age'] == 42

    # To encode a data structure to JSON, use the "dumps" method. This method takes an object and
    # returns a String:
    # 要将数据结构编码为 JSON，请使用 "dumps" 方法。此方法接受一个对象并
    # 返回一个字符串：
    encoded_person_string = json.dumps(person_dictionary)

    assert encoded_person_string == json_string
