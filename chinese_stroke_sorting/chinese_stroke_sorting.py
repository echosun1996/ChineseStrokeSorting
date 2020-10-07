# 最终版笔划排序程序
# ###############################################################
# 从文件中读取姓名列表，注意，每行一个人名。
import os

__char_num_i = 0


def read_name_list_from_file(input_file):
    name_list = []
    with open(str(input_file), 'r', encoding='UTF-8') as f:
        for line in f:
            name_list.append(line.split('\n')[0])
    return name_list


# ###############################################################
# 从 bh.txt 中读取笔划数据，并保存到全局变量中。


def __read_bh__():
    chinese_char_dict = dict()
    current_package_path = os.path.dirname(os.path.abspath(__file__))
    with open("".join([current_package_path, '/bh.txt']), 'r', encoding='UTF-8') as f:
        while True:
            line = f.readline()
            if not line:
                break
            line_after_split = line.split('\t')
            chinese_char_dict[line_after_split[0]] = line_after_split[1].split('\n')[0]
    return chinese_char_dict


# ###############################################################
# 将名字中每个字的笔画数保存到列表，并与人名组成一个新的列表。


def __init_name_stroke_count_list__(name_list, chinese_char_dict):
    name_stroke_count_list = []  # 根据姓名与每个字的笔画数列表组成的列表
    for name in name_list:
        name_total_strokes_list = []  # 名字的总笔画数
        for name_char in name:
            name_total_strokes_list.append(chinese_char_dict.get(name_char))
        name_stroke_count_list.append([name, name_total_strokes_list])
    return name_stroke_count_list


# ###############################################################
# 根据姓名排序


def __sort__(name_stroke_count_list):
    global __char_num_i
    for i in range(len(name_stroke_count_list)):
        for j in range(len(name_stroke_count_list) - i - 1):
            if __char_num_i == 0 and int(name_stroke_count_list[j][1][__char_num_i]) > int(
                    name_stroke_count_list[j + 1][1][__char_num_i]):
                name_stroke_count_list[j], name_stroke_count_list[j + 1] = name_stroke_count_list[j + 1], \
                                                                           name_stroke_count_list[j]
                continue
            if len(name_stroke_count_list[j][1]) <= __char_num_i:
                name_stroke_count_list[j][1].append('0')
            if len(name_stroke_count_list[j + 1][1]) <= __char_num_i:
                name_stroke_count_list[j + 1][1].append('0')
            if __char_num_i != 0 and int(name_stroke_count_list[j][1][__char_num_i - 1]) == int(
                    name_stroke_count_list[j + 1][1][__char_num_i - 1]):
                if int(name_stroke_count_list[j][1][__char_num_i]) > int(
                        name_stroke_count_list[j + 1][1][__char_num_i]):
                    name_stroke_count_list[j], name_stroke_count_list[j + 1] = name_stroke_count_list[j + 1], \
                                                                               name_stroke_count_list[j]
    return name_stroke_count_list


# 查找 char_num_i 是否需要变动
def __find_char_num_i_change__(name_stroke_count_list):
    global __char_num_i
    for i in range(1, len(name_stroke_count_list)):
        if name_stroke_count_list[i - 1][1][__char_num_i] == name_stroke_count_list[i][1][__char_num_i] and \
                name_stroke_count_list[i - 1][1][__char_num_i] != '0':
            __char_num_i += 1
            return True
    return False


# ###############################################################
# 在控制台输出排序后的结果。


# 从 name_stroke_count_list 中去除笔画数列表
def __remove_stroke_count__(name_stroke_count_list):
    name_result_list = []  # 排序后的名字
    for name in name_stroke_count_list:
        name_result_list.append(name[0])
    return name_result_list


# ###############################################################
# 将排好序的人名列表存放在 result.txt 中。
# 通过设定 split_char,可以以不同的分隔形式存放到文件中。
def write_sort_result_to_file(sort_result_list, output_file, split_char='\n'):
    with open(str(output_file), 'w', encoding='UTF-8') as f:
        f.write(split_char.join(str(i) for i in sort_result_list))


def sort_by_stroke(name_list_input):
    global __char_num_i
    __char_num_i = 0
    name_stroke_count_list = __init_name_stroke_count_list__(name_list_input, __read_bh__())

    while True:
        name_stroke_count_list = __sort__(name_stroke_count_list)
        if not __find_char_num_i_change__(name_stroke_count_list):
            break

    name_result_list = __remove_stroke_count__(name_stroke_count_list)
    return name_result_list


def write_sort_result_to_human(sort_result_list, split_char=' '):
    return str(split_char.join(str(i) for i in sort_result_list))
