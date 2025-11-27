def count_words(text):
    word_count = 0
    split_text = text.split()
    for word in split_text:
        word_count += 1
    
    return word_count

def character_count(text):
    character_dict = {}
    for word in text.lower():
        if word not in character_dict:
            character_dict[word] = 1
        elif word in character_dict:
            character_dict[word] += 1

    return character_dict

def sort_on(items):
    return items['num']

def sorted_list(character_dict):

    character_list = []

    for ch, count in character_dict.items():
        character_list.append({"char":ch,"num":count})

    character_list.sort(reverse=True, key=sort_on)

    return character_list





