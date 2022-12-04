from operator import itemgetter

def read_file(file):
    input_file = open(file, 'r')
    input_data = input_file.read()
    input_file.closed
    return input_data

def get_data(file):
    file_data = read_file(file)
    data_list = file_data.split("\n")
    return data_list

def list_to_dict(list_data):
    dictionary_data = {}
    index = 1
    dictionary_data[index] = []
    for item in list_data:
        if item == '':
            index += 1
            dictionary_data[index] = []
        else:
            dictionary_data[index].append(int(item))
    return dictionary_data

def find_most_calories(dict_list):
    most_calories, best_elf = 0, 0
    for elf in dict_list:
        elf_haul = 0
        for item in dict_list[elf]:
            elf_haul += int(item)
        if elf_haul > most_calories:
            most_calories = elf_haul
            best_elf = elf
    return best_elf, most_calories

def sort_by_calories(dict_list):
    temp_dict = {k:sum(dict_list[k]) for k in dict_list}
    sorted_dict = {k: v for k,v in sorted(temp_dict.items(), key=itemgetter(1))}
    return sorted_dict

def return_last_items(dict_list, number_of_items):
    dict_len = len(dict_list)
    key_elves = list(dict_list)[dict_len - number_of_items:]
    sub_dict = {elf : dict_list[elf] for elf in key_elves}
    return sub_dict

def sum_dict(dict_list):
    temp_sum = 0
    for elf in dict_list:
        temp_sum += dict_list[elf]
    return temp_sum

starting_list = get_data('day_1.txt')
calorie_dictionary = list_to_dict(starting_list)
best_elf, most_calories = find_most_calories(calorie_dictionary)
print(best_elf, ' ', most_calories)
sorted_elves = sort_by_calories(calorie_dictionary)
#print(sorted_elves)
most_elves = return_last_items(sorted_elves, 3)
group_calories = sum_dict(most_elves)
print(group_calories)