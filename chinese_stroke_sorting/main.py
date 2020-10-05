# ###############################################################
# 最终版笔划排序程序

# ###############################################################
# 从 wait_for_sort.txt 文件中读取姓名列表，注意，每行一个人名。
import os

name_list = []

def read_from_file(file_name):
    global name_list
    with open(file_name, 'r', encoding='UTF-8') as f:
        for line in f:
            name_list.append(line.split('\n')[0])
# print('待排序的名单：')
# print(name_list)

# ###############################################################
# 从 bh.txt 中读取笔划数据，并保存到全局变量中。

# file_name = "bh.txt"  # 定义数据文件名
chinese_char_dict = dict()

def read_from_bh():
    global chinese_char_dict
    current_package_path = os.path.dirname(os.path.abspath(__file__))
    with open("".join([current_package_path,'/bh.txt']), 'r', encoding='UTF-8') as f:
        while True:
            line = f.readline()
            if not line:
                break
            line_after_split = line.split('\t')
            chinese_char_dict[line_after_split[0]] = line_after_split[1].split('\n')[0]




# ###############################################################
# 将名字中每个字的笔画数保存到列表，并与人名组成一个新的列表。


name_stroke_count_list = []  # 根据姓名与每个字的笔画数列表组成的列表


def init_name_stroke_count_list():
    global chinese_char_dict, name_stroke_count_list,name_list
    for name in name_list:
        name_total_strokes_list = []  # 名字的总笔画数
        for name_char in name:
            name_total_strokes_list.append(chinese_char_dict.get(name_char))
        name_stroke_count_list.append([name, name_total_strokes_list])



# print('姓名与笔画数列表：')
# print(name_stroke_count_list)

# ###############################################################
# 根据姓名排序

char_num_i = 0


def sort_by_name():
    global char_num_i,name_stroke_count_list
    for i in range(len(name_stroke_count_list)):
        for j in range(len(name_stroke_count_list) - i - 1):
            if char_num_i == 0 and int(name_stroke_count_list[j][1][char_num_i]) > int(
                    name_stroke_count_list[j + 1][1][char_num_i]):
                name_stroke_count_list[j], name_stroke_count_list[j + 1] = name_stroke_count_list[j + 1], \
                                                                           name_stroke_count_list[j]
                continue
            if len(name_stroke_count_list[j][1]) <= char_num_i:
                name_stroke_count_list[j][1].append('0')
            if len(name_stroke_count_list[j + 1][1]) <= char_num_i:
                name_stroke_count_list[j + 1][1].append('0')
            if char_num_i != 0 and int(name_stroke_count_list[j][1][char_num_i - 1]) == int(
                    name_stroke_count_list[j + 1][1][char_num_i - 1]):
                if int(name_stroke_count_list[j][1][char_num_i]) > int(name_stroke_count_list[j + 1][1][char_num_i]):
                    name_stroke_count_list[j], name_stroke_count_list[j + 1] = name_stroke_count_list[j + 1], \
                                                                               name_stroke_count_list[j]


# 查找 char_num_i 是否需要变动
def find_char_num_i_change():
    global char_num_i, name_stroke_count_list
    for i in range(1, len(name_stroke_count_list)):
        if name_stroke_count_list[i - 1][1][char_num_i] == name_stroke_count_list[i][1][char_num_i] and \
                name_stroke_count_list[i - 1][1][char_num_i] != '0':
            char_num_i += 1
            return True
    return False




# print(name_stroke_count_list)
# ###############################################################
# 在控制台输出排序后的结果。
name_result_list = []  # 排序后的名字


# 从 name_stroke_count_list 中去除笔画数列表
def remove_stroke_count():
    global name_result_list,name_stroke_count_list
    for name in name_stroke_count_list:
        name_result_list.append(name[0])

# ###############################################################
# 将排好序的人名列表存放在 result.txt 中。
# 通过设定 split_char,可以以不同的分隔形式存放到文件中。
def write_to_file(result_file_name,split_char):
    global name_result_list
    with open(result_file_name, 'w', encoding='UTF-8') as f:
        f.write(split_char.join(str(i) for i in name_result_list))


def sort_by_stroke(name_list_input):
    global name_result_list,name_list
    name_list = name_list_input
    # read_from_file()
    # name_list = ['张三', '李四', '王五']
    read_from_bh()
    init_name_stroke_count_list()

    while True:
        sort_by_name()
        if not find_char_num_i_change():
            break

    remove_stroke_count()
    return name_result_list
    # print('排序后的名单：')
    # print(" ".join(str(i) for i in name_result_list))

    # result_file_name = 'result.txt'
    # split_char = "\n"
    # write_to_file(result_file_name,split_char)