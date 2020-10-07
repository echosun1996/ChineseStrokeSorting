# 中文笔划排序程序

![Python package](https://github.com/echosun1996/ChineseStrokeSorting/workflows/Python%20package/badge.svg)
![PyPI version](https://badge.fury.io/py/chinese-stroke-sorting.svg)
![Python](https://img.shields.io/pypi/pyversions/chinese-stroke-sorting.svg?style=plastic)

## 特点
- 支持对名单列表进行按笔划排序
- 支持从文件中读取名单列表
- 支持以便于阅读的方式输出排序后的结果
- 支持将排序后的名单列表写入文件

## 安装

```bash
pip install chinese-stroke-sorting
```

## 更新

```bash
pip install --upgrade chinese-stroke-sorting
```

## 使用说明

```bash
>>> # 导入包
>>> from chinese_stroke_sorting import sort_by_stroke, write_sort_result_to_human, \
    write_sort_result_to_file, read_name_list_from_file

>>> # 直接对名单列表排序
>>> name_list = ['张三','张二','张一一', '李四', '王五']
>>> print(sort_by_stroke(name_list)) 
['王五', '李四', '张一一', '张二', '张三']

>>> # 从文件中读取名单列表
>>> name_list_file_path = 'test_name_list.txt'
>>> name_list = read_name_list_from_file(name_list_file_path)
>>> print(name_list)
['张三', '李四', '王五', '赵六', '王一', '王一二']

>>> # 以便于阅读的方式显示排序结果
>>> sort_result = sort_by_stroke(name_list)
>>> result_for_human = write_sort_result_to_human(sort_result, split_char='|')
>>> print(result_for_human)
王一|王一二|王五|李四|张三|赵六

>>> # 将排序结果写入文件
>>> output_file = 'result.txt'
>>> write_sort_result_to_file(sort_result, output_file, split_char='\n')

``` 

## 说明

项目发布于PyPI：[单击访问](https://pypi.org/project/chinese-stroke-sorting/) 

本模块尚不完善，有任何相关问题或建议，欢迎在本项目的github页面中提交issue: [单击访问](https://github.com/echosun1996/ChineseStrokeSorting)

# License
GNU General Public License v3.0