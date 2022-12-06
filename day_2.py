# scoring rubric
MARKING = {
    1 : ['A', 'X'],
    2 : ['B', 'Y'],
    3 : ['C', 'Z']
}

def read_file(file):
    input_file = open(file, 'r')
    input_data = input_file.read()
    input_file.closed
    return input_data

def get_data(file):
    file_data = read_file(file)
    data_list = [item.split(" ") for item in file_data.split("\n")]
    return data_list

def score_round(round_choices):
    player_1 = round_choices[0]
    player_1_score = 0
    player_2 = round_choices[1]
    player_2_state = 0
    player_2_score = 0
    for score in MARKING:
        if player_1 in MARKING[score]:
            player_1_score = score
        if player_2 in MARKING[score]:
            player_2_state = score
    if player_2_state == 3:
        if player_1_score < 3:
            player_2_score += 6 + player_1_score + 1
        else:
            player_2_score += 7
    elif player_2_state == 2:
        player_2_score = 3 + player_1_score
    else:
        if player_1_score > 1:
            player_2_score = player_1_score - 1
        else:
            player_2_score = 3
    return player_2_score

def old_round_scoring(round_choices):
    player_1 = round_choices[0]
    player_1_score = 0
    player_2 = round_choices[1]
    player_2_score = 0
    for score in MARKING:
        if player_1 in MARKING[score]:
            player_1_score = score
        if player_2 in MARKING[score]:
            player_2_score = score
    if player_2_score == player_1_score + 1 or player_2_score == player_1_score - 2:
        player_2_score += 6
    elif player_2_score == player_1_score:
        player_2_score += 3
    return player_2_score

def calc_match_score(matches):
    my_score = 0
    for round in matches:
        my_score += old_round_scoring(round)
    return my_score

starting_list = get_data('day_2.txt')
#print(starting_list)
print(old_round_scoring(starting_list))
print(calc_match_score(starting_list))