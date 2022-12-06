def read_file(file):
    input_file = open(file, 'r')
    input_data = input_file.read()
    input_file.closed
    return input_data

def get_data(file):
    file_data = read_file(file)
    data_list = file_data.split("\n")
    return data_list

def non_sequential_find(data_string, chars):
    for index in range(len(data_string) - chars):
        unique = True
        sample = data_string[index : index + chars]
        for char in range(chars):
            for comp in range(char + 1, chars):
                if sample[char] == sample[comp]:
                    unique = False
        if unique:
            return index + chars
    return 0

data_packets = get_data('day_6.txt')
for packet in data_packets:
    print(non_sequential_find(packet, 14))