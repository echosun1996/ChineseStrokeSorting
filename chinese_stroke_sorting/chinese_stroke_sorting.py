# 最终版笔划排序程序
# ###############################################################
# 从文件中读取姓名列表，注意，每行一个人名。
import os

__name_list = []


def read_name_list_from_file(file_name):
    with open(str(file_name), 'r', encoding='UTF-8') as f:
        for line in f:
            __name_list.append(line.split('\n')[0])
    return __name_list


# ###############################################################
# 从 bh.txt 中读取笔划数据，并保存到全局变量中。

__chinese_char_dict = dict()


def __read_bh__():
    global __chinese_char_dict
    current_package_path = os.path.dirname(os.path.abspath(__file__))
    with open("".join([current_package_path, '/bh.txt']), 'r', encoding='UTF-8') as f:
        while True:
            line = f.readline()
            if not line:
                break
            line_after_split = line.split('\t')
            __chinese_char_dict[line_after_split[0]] = line_after_split[1].split('\n')[0]


# ###############################################################
# 将名字中每个字的笔画数保存到列表，并与人名组成一个新的列表。


__name_stroke_count_list = []  # 根据姓名与每个字的笔画数列表组成的列表


def __init_name_stroke_count_list__():
    global __chinese_char_dict, __name_stroke_count_list, __name_list
    for name in __name_list:
        name_total_strokes_list = []  # 名字的总笔画数
        for name_char in name:
            name_total_strokes_list.append(__chinese_char_dict.get(name_char))
        __name_stroke_count_list.append([name, name_total_strokes_list])


# ###############################################################
# 根据姓名排序

__char_num_i = 0


def __sort__():
    global __char_num_i, __name_stroke_count_list
    for i in range(len(__name_stroke_count_list)):
        for j in range(len(__name_stroke_count_list) - i - 1):
            if __char_num_i == 0 and int(__name_stroke_count_list[j][1][__char_num_i]) > int(
                    __name_stroke_count_list[j + 1][1][__char_num_i]):
                __name_stroke_count_list[j], __name_stroke_count_list[j + 1] = __name_stroke_count_list[j + 1], \
                                                                               __name_stroke_count_list[j]
                continue
            if len(__name_stroke_count_list[j][1]) <= __char_num_i:
                __name_stroke_count_list[j][1].append('0')
            if len(__name_stroke_count_list[j + 1][1]) <= __char_num_i:
                __name_stroke_count_list[j + 1][1].append('0')
            if __char_num_i != 0 and int(__name_stroke_count_list[j][1][__char_num_i - 1]) == int(
                    __name_stroke_count_list[j + 1][1][__char_num_i - 1]):
                if int(__name_stroke_count_list[j][1][__char_num_i]) > int(
                        __name_stroke_count_list[j + 1][1][__char_num_i]):
                    __name_stroke_count_list[j], __name_stroke_count_list[j + 1] = __name_stroke_count_list[j + 1], \
                                                                                   __name_stroke_count_list[j]


# 查找 char_num_i 是否需要变动
def __find_char_num_i_change__():
    global __char_num_i, __name_stroke_count_list
    for i in range(1, len(__name_stroke_count_list)):
        if __name_stroke_count_list[i - 1][1][__char_num_i] == __name_stroke_count_list[i][1][__char_num_i] and \
                __name_stroke_count_list[i - 1][1][__char_num_i] != '0':
            __char_num_i += 1
            return True
    return False


# ###############################################################
# 在控制台输出排序后的结果。
__name_result_list = []  # 排序后的名字


# 从 name_stroke_count_list 中去除笔画数列表
def __remove_stroke_count__():
    global __name_result_list, __name_stroke_count_list
    for name in __name_stroke_count_list:
        __name_result_list.append(name[0])


# ###############################################################
# 将排好序的人名列表存放在 result.txt 中。
# 通过设定 split_char,可以以不同的分隔形式存放到文件中。
def write_sort_result_to_file(sort_result_list, result_file_name, split_char='\n'):
    with open(result_file_name, 'w', encoding='UTF-8') as f:
        f.write(split_char.join(str(i) for i in sort_result_list))


def sort_by_stroke(name_list_input):
    global __name_list
    __name_list = name_list_input
    __read_bh__()
    __init_name_stroke_count_list__()

    while True:
        __sort__()
        if not __find_char_num_i_change__():
            break

    __remove_stroke_count__()
    return __name_result_list


def write_sort_result_to_human(sort_result_list, split_char=' '):
    return str(split_char.join(str(i) for i in sort_result_list))