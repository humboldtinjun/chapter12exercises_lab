# make a function uses first 2 words as keys and the third as value and store in dict.
import unicodedata


punc_marks = {}
for line in open("drjeckll.txt"):  # make sure filename is defined first
    for char in line:
        if unicodedata.category(char).startswith('P'):
            punc_marks[char] = 1

punctuation = ''.join(punc_marks)

def clean_word(word):
    return word.strip(punctuation).lower()



def split_line(line):
    return line.replace('—', ' ').split()

successor_map = {}
window = []

def add_trigram(trigram):
    key = tuple(trigram[:2])  # first two words as key
    successor = trigram[2]    # third word the successor

    if key not in successor_map:
        successor_map[key] = [successor]
    else:
        successor_map[key].append(successor)

def process_word_trigram(word):
    window.append(word)

    if len(window) == 3:
        add_trigram(window)
        window.pop(0)

for line in open("drjeckll.txt"):
    for word in split_line(line):
        word = clean_word(word)
        process_word_trigram(word)



