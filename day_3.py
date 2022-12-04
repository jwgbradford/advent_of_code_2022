
def read_file(file):
    input_file = open(file, 'r')
    input_data = input_file.read()
    input_file.closed
    return input_data

def get_data(file):
    file_data = read_file(file)
    data_list = [[backpack[:len(backpack)//2], backpack[len(backpack)//2:]] for backpack in file_data.split("\n")]
    return data_list

def find_duplicates(split_lists):
    duplicates = []
    for splits in split_lists:
        for item in splits[0]:
            if item in splits[1]:
                duplicates.append(item)
                break
    return duplicates

def calc_score(duplicate_list):
    score = 0
    for item in duplicate_list:
        if ord(item) - 96 > 0:
            score += ord(item) - 96
        else:
            score += ord(item) - 38
    return score

starting_list = get_data('day_3_sample.txt')
duplicates = find_duplicates(starting_list)
print(calc_score(duplicates))