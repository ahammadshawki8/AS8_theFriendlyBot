def write_info(info):
    for item in info:
        write_item(item)
        return True

def read_info():
    with open("past_actions.txt", "r") as read_file:
        info_str = read_file.read()
        info_list = info_str.split("\n")[:-1]
        return info_list

def clear_info():
    deleted_info = read_info()
    with open("past_actions.txt", "w") as write_file:
        write_file.write("")
        return deleted_info

def write_item(item):
    with open("past_actions.txt", "a") as write_file:
        write_file.write(item + "\n")
        return True

def clear_item(item):
    deleted_info = clear_info()
    if item in deleted_info:
        deleted_info.remove(item)
    write_info(deleted_info)