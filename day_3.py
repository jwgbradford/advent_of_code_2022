
def read_file(file):
    input_file = open(file, 'r')
    input_data = input_file.read()
    input_file.closed
    return input_data

def get_data(file):
    file_data = read_file(file)
    #data_list = [[backpack[:len(backpack)//2], backpack[len(backpack)//2:]] for backpack in file_data.split("\n")]
    data_list = [backpack for backpack in file_data.split("\n")]
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

def find_badges(split_lists):
    grouped_list = []
    triples = []
    for i in range(0, len(split_lists), 3):
        temp = []
        for j in range(0, 3):
            temp.append(split_lists[i + j])
        grouped_list.append(temp)
    for triple in grouped_list:
        for item in triple[0]:
            if item in triple[1] and item in triple[2]:
                triples.append(item)
                break
    return calc_score(triples)

starting_list = get_data('day_3_sample.txt')
duplicates = find_duplicates(starting_list)
print(find_badges(starting_list))