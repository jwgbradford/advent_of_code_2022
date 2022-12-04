def read_file(file):
    input_file = open(file, 'r')
    input_data = input_file.read()
    input_file.closed
    return input_data

def get_data(file):
    file_data = read_file(file)
    data_list = [data for data in file_data.split("\n")]
    return data_list

def nested_pairs(data_list):
    nesting = 0
    for pair_combo in data_list:
        pair_one, pair_two = pair_combo.split(",")
        one_pt1, one_pt2 = pair_one.split("-")
        two_pt1, two_pt2 = pair_two.split("-")
        if (
            int(one_pt1) <= int(two_pt1) and 
            int(one_pt2) >= int(two_pt2) or
            int(one_pt1) >= int(two_pt1) and 
            int(one_pt2) <= int(two_pt2)
        ):
            nesting += 1
    return nesting


list_of_data = get_data('day_4_sample.txt')
print(nested_pairs(list_of_data))