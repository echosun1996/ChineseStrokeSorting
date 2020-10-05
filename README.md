# 中文笔划排序程序

![Python package](https://github.com/naivenlp/naive-stopwords/workflows/Python%20package/badge.svg)
[![Python](https://img.shields.io/pypi/pyversions/naive-stopwords.svg?style=plastic)](https://badge.fury.io/py/naive-stopwords)

## 说明
本模块用于将中文名按笔划排序。

项目托管于PyPI：[单击访问](https://test.pypi.org/project/chinese-stroke-sorting/)。

相关问题欢迎反馈。

## 安装

```bash
pip install -i https://test.pypi.org/simple/ chinese-stroke-sorting
```

## 使用

```bash
>>> from chinese_stroke_sorting import sort_by_stroke
>>> name_list = ['张三','张二','张一一', '李四', '王五']
>>> print(sort_by_stroke(name_list)) 
['王五', '李四', '张一一', '张二', '张三']
``` 