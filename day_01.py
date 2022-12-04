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
            dictionary_data[index].append(item)
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

starting_list = get_data('day_1_sample.txt')
calorie_dictionary = list_to_dict(starting_list)
best_elf, most_calories = find_most_calories(calorie_dictionary)
print(best_elf, ' ', most_calories)