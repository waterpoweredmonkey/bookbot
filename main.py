def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)

    # print(word_count)
    
    character_occurrances = get_character_occurance(text)
    sorted_occurrances = sorted_char_list(character_occurrances)
    # print(sorted_occurrances)
    print_report(word_count,sorted_occurrances)

def print_report(word_count, list):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n\n")

    for item in list:
        char = item["char"]
        if char >= 'a' and char <= 'z':
            print(f"The '{char}' character was found {item["count"]} times")
    
    print("--- End report ---")
    

def sorted_char_list(dict):
    unsorted_occurrances = []
    for k,v in dict.items():
        unsorted_occurrances.append( {"char": k, "count": v } )
    unsorted_occurrances.sort(reverse=True, key=occurrances_sort)
    return unsorted_occurrances

def occurrances_sort(dict):
    return dict["count"]

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_word_count(text):
    words = text.split()
    return len(words)

def get_character_occurance(text):
    lower = text.lower()
    occurances = {}
    for i in range(0, len(lower)):
        char = lower[i]
        if char in occurances:
            occurances[char] += 1
        else:
            occurances[char] = 1
    return occurances

main()