from typing import List

# random code from stackoverflow
# https://stackoverflow.com/questions/39818669/dynamically-accessing-nested-dictionary-keys
class DynamicAccessNestedDict:
    def __init__(self, data: dict):
        self.data = data

    def getval(self, keys: List):
        data = self.data
        for k in keys:
            data = data[k]
        return data

    def setval(self, keys: List, val) -> None:
        data = self.data
        lastkey = keys[-1]
        for k in keys[:-1]:  # when assigning drill down to *second* last key
            data = data[k]
        data[lastkey] = val

def read_file(file):
    input_file = open(file, 'r')
    input_data = input_file.read()
    input_file.closed
    return input_data

def get_data(file):
    file_data = read_file(file)
    data_list = file_data.split("\n")
    return data_list

def cd(pointer, dir, current_disc):
    if dir == '/':
        pointer = ['/']
    elif dir == '..':
        del pointer[-2:]
    else:
        pointer.append('dirs')
        dirs = current_disc.getval(pointer)
        if dir in dirs.keys():
            pointer.append(dir)
        else:
            pointer.append(dir)
            current_disc.setval(pointer, {
                'size' : 0,
                'dirs': {},
                'files' : {}
            }
            )
    return pointer, current_disc

def ls(temp_pointer, current_disc, data):
    list_entry = data.split(" ")
    if list_entry[0] == 'dir':
        temp_pointer.append('dirs')
        temp_pointer.append(list_entry[1])
        current_disc.setval(temp_pointer, {
                'size' : 0,
                'dirs': {},
                'files' : {}
            }
            )
        del temp_pointer[-1]
        del temp_pointer[-1]
    else:
        temp_pointer.append('files')
        temp_pointer.append(list_entry[1])
        current_disc.setval(temp_pointer, int(list_entry[0]))
        del temp_pointer[-1]
        del temp_pointer[-1]
        temp_pointer.append('size')
        dir_size = current_disc.getval(temp_pointer)
        dir_size += int(list_entry[0])
        current_disc.setval(temp_pointer, dir_size)
        del temp_pointer[-1]
    return current_disc

blank_disc = {
    '/' : {
        'size' : 0,
        'dirs': {},
        'files' : {}
    }
}
my_disc = DynamicAccessNestedDict(blank_disc)
raw_disc_data = get_data('day_7_sample.txt')
pointer = ['/']
for entry in raw_disc_data:
    if entry[0] == '$': # cmd
        cmd = entry[2:].split(" ")
    if cmd[0] == 'cd':
        pointer, my_disc = cd(pointer, cmd[1], my_disc)
    elif cmd[0] == 'ls' and entry != '$ ls':
        my_disc = ls(pointer, my_disc, entry)

print(my_disc.data)
# random code from stackoverflow
dct = {
    '/' : {
        'size' : 120,
        'dirs': {
            'a': {
                'size' : 0,
                'dirs' : {},
                'files' :{}
            },
            'd': {
                'size' : 0,
                'dirs' : {},
                'files' :{}
            },
        },
        'files' : {
            'b.txt' : 14848514,
            'c.dat' : 8504156
        }
    }
}

d = DynamicAccessNestedDict(dct)
#assert d.getval(["label"]) == "A"
assert d.getval(["/", "size"]) == 120
# Set some new values
d.setval(["/", "dirs", "a", "files", "e.log"], 222)