import pathlib

def list_files(dirname):
    source_folder = pathlib.Path(dirname)
    all_files_listed = list(source_folder.rglob("*.txt"))
    return all_files_listed

def show_files_and_content(list_files):
    list_files_tmp = []
    for files in list_files:
        open_file = open(str(files))
        content = open_file.read()
        if "I am Here" in content: # "1" = Content search
            list_files_tmp.append(files)
    return list_files_tmp

def change_content_file(show_files_and_content):
    for change_content in show_files_and_content:
        file_to_execute_procedure = open(str(change_content), "rt")
        read_file_content = file_to_execute_procedure.read()
        replace_data_content = read_file_content.replace('I am Here','I am Here Again')
        file_to_execute_procedure.close()
        file_to_execute_procedure = open(str(change_content), "wt")
        file_to_execute_procedure.write(replace_data_content)
        file_to_execute_procedure.close()
    
start_list_files = list_files("test")
start_show_files_and_content = show_files_and_content(start_list_files)
start_change_content_file = change_content_file(start_show_files_and_content)
