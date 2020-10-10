##################################################
##  Does not work with multi-word hangman games
##  Does not work with pop culture words
##################################################
import re
from collections import defaultdict

def find_best_letter(word_length: int, expression: str, invalids: set, letters_so_far: set) -> list:
    counts = defaultdict(int)
    for line in open('words_alpha.txt'):
        
        if len(line.strip()) == word_length   and \
           re.match(expression, line.strip()) and \
           all([letter not in line.strip() for letter in invalids]):
            
            [inc_dic_value(counts, l) for l in line.strip().replace('\w', '') if l not in letters_so_far]

    return sorted(counts.items(), key=lambda x:-x[1])

def inc_dic_value(dic: dict, key: str) -> None:
    dic[key] += 1
    return

if __name__ == '__main__':

    num_chars_in_word = int(input("Enter in num chars in word: "))
    invalids = set([])
    word_so_far = input("Enter in word so far, with unknown letters as underscores: ")
    
    while True:        
        expression = ''.join([char.lower() if char != '_' else '\w' for char in word_so_far])
        letters_so_far = set([x for x in word_so_far if x != '_'])
        english_words = find_best_letter(num_chars_in_word, expression, invalids, letters_so_far)
        for w in english_words:
            print(w)

        letter = input("Enter in the letter you guessed: ").lower()
        success = True if input("Was your guess successful? (y/n): ") == 'y' else False
        if success:
            word_so_far = input("Enter in the word so far, with unknown letters as underscores: ")
        else:
            invalids.add(letter)
