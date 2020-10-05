import unittest


from .main import sort_by_stroke


class SortByNameTest(unittest.TestCase):

    def testDefaultStopwords(self):
        name_list = ['张三', '张二', '张一一', '李四', '王五']
        print(sort_by_stroke(name_list))

if __name__ == "__main__":
    unittest.main()