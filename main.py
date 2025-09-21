import sys
from stats import count_characters, count_words, sort_characters


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    

    

def main():
    
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book = get_book_text(sys.argv[1])
    num_words = count_words(book)
    #print(f"{num_words} words found in the document")

    num_characters = count_characters(book)
    sorted_dict_list = sort_characters(num_characters)
    #print(num_characters)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for character in sorted_dict_list:
        print(f"{character["char"]}: {character["num"]}")
    print("============= END ===============")


main()