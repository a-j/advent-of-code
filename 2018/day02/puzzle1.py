def convert_to_dict(box_id):
    letters = dict()
    for letter in sorted(box_id):
        if letter in letters:
            letters[letter] += 1 
        else:
            letters[letter] = 1 
    return letters

def get_count_of_letters(box_id):
    letters = convert_to_dict(box_id)
    letters_appear_twice = 0
    letters_appear_thrice = 0
    for key, value in letters.items():
        if value == 2:
            letters_appear_twice = 1
        if value == 3:
            letters_appear_thrice = 1

    return letters_appear_twice, letters_appear_thrice

with open('input.txt') as file_handle:
    lines = file_handle.readlines()
    twice_count = 0
    thrice_count = 0
    for line in lines:
        letters_appear_twice, letters_appear_thrice = get_count_of_letters(line.rstrip())
        twice_count += letters_appear_twice
        thrice_count += letters_appear_thrice
    print(twice_count*thrice_count)
