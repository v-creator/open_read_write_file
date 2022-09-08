import os

dir = os.getcwd()
folder_name = 'sorted_file'
path = os.path.join(dir,folder_name)

def sorted_file(dir):
    list_file = os.listdir(dir)
    dict_file = {}
    for i in range(len(list_file)):
        with open(os.path.join(dir,list_file[i]), 'r', encoding='utf-8') as file:
            content = file.readlines()
            dict_file[list_file[i]] = content
    sort_dict = sorted(dict_file.items(), key=lambda x: x[1])
    with open('result_file.txt', 'a', encoding='utf-8') as file:
        for line in sort_dict:
            file.writelines([line[0],'\n'])
            file.writelines([str(len(line[1])),'\n'])
            file.writelines(line[1])
            file.writelines('\n')

sorted_file(path)