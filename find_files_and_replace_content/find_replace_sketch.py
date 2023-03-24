import pathlib

def list_files(dirname):
    source_folder = pathlib.Path(dirname)
    all_files_listed = list(source_folder.rglob("*.txt"))
    return all_files_listed

def show_files_and_content(list_files):
    list_files_tmp = []
    # print(list_files)
    for files in list_files:
        # print(files)
        open_file = open(str(files))
        content = open_file.read()
        # print(open_file.read())
        if "I am Here" in content: # "1" = Content search
            # print("Found")
            # print(files)
            list_files_tmp.append(files)
            # print(list_files_tmp)
        #     print("Not Found")
        # print("proximo")
    # print(list_files_tmp)
    # print(list_files_tmp[1])
    return list_files_tmp

def change_content_file(show_files_and_content):
    # print(len(show_files_and_content))
    for change_content in show_files_and_content:
        file_to_execute_procedure = open(str(change_content), "rt")
        read_file_content = file_to_execute_procedure.read()
        replace_data_content = read_file_content.replace('I am Here','I am Here Again')
        file_to_execute_procedure.close()
        file_to_execute_procedure = open(str(change_content), "wt")
        file_to_execute_procedure.write(replace_data_content)
        file_to_execute_procedure.close()
    

start_list_files = list_files("test")
# print(start_list_files)
start_show_files_and_content = show_files_and_content(start_list_files)
start_change_content_file = change_content_file(start_show_files_and_content)



# source_folder = pathlib.Path("test")
# all_files_listed = list(source_folder.rglob("*.txt"))
# print(all_files_listed[2])