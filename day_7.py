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

raw_disc_data = get_data('day_7_sample.txt')
print(raw_disc_data)


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
print(d.getval(["/", "size"]))
# Set some new values
d.setval(["/", "dirs", "a", "files", "e.log"], 222)

print(d.data)