import os
import unittest

from .chinese_stroke_sorting import sort_by_stroke, write_sort_result_to_human, write_sort_result_to_file, \
    read_name_list_from_file


class SortByNameTest(unittest.TestCase):
    def read_name_list_from_file_test(self, input_test):
        right_result = ['张三', '李四', '王五', '赵六', '王一', '王一二']
        self.assertEqual(input_test, right_result)

    def sort_by_stroke_test(self, input_test):
        right_result = ['王一', '王一二', '王五', '李四', '张三', '赵六']
        self.assertEqual(input_test, right_result)

    def write_sort_result_to_human_test(self, input_test):
        right_result = '王一|王一二|王五|李四|张三|赵六'
        self.assertEqual(input_test, right_result)

    def testDefaultStopwords(self):
        current_package_path = os.path.dirname(os.path.abspath(__file__))
        name_list_file_path = str("".join([current_package_path, '/test_name_list.txt']))
        name_list = read_name_list_from_file(name_list_file_path)  # 从文件中读取
        print(name_list)
        self.read_name_list_from_file_test(name_list)

        sort_result = sort_by_stroke(name_list)  # 按笔画数排序
        print(sort_result)
        self.sort_by_stroke_test(sort_result)

        result_for_human = write_sort_result_to_human(sort_result, split_char='|')  # 获取以指定分隔符分割的可读文本
        print(result_for_human)
        self.write_sort_result_to_human_test(result_for_human)

        output_file = 'result.txt'
        write_sort_result_to_file(sort_result, output_file, split_char='\n')  # 将排序结果写入到文件

# if __name__ == "__main__":
#     unittest.main()
