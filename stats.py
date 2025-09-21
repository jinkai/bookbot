
def count_words(book):
    words_list = book.split()
    return len(words_list)

def count_characters(book):
    char_set = {}
    for character in book:
        lower_char = character.lower()
        if lower_char in char_set:
            char_set[lower_char] += 1
        else:
            char_set[lower_char] = 1
    return char_set

def get_character_num(letter_dict):
    return letter_dict["num"]

def sort_characters(characters):
    # for each letter in the dict, create a new dict and add to a list
    dictionary_list = []
    for character in characters:
        if character.isalpha():
            letter_dict = {"char": character, "num": characters[character]}
            dictionary_list.append(letter_dict)
    
    
    dictionary_list.sort(reverse=True, key=get_character_num)
    #print(dictionary_list)
    return dictionary_list