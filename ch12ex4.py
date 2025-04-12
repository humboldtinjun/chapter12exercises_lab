# use the successor map to generat a 50 word sentence
import unicodedata
import random

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



# start with a random key (bigram)
key = random.choice(list(successor_map.keys())) #picks a random key out of successor map
output = list(key)  # start output with the two words in the key

# generate 50 more words
for i in range(50):
    successors = successor_map.get(key) # using get prevents a key error if it there isnt a key
    if not successors:
        break  # no known next word, stop here
    next_word = random.choice(successors) # picks another word
    output.append(next_word) #adds word to end of the list

    # slide the key window forward
    key = (key[1], next_word)

# print results as a sentence
print(' '.join(output)) # puts it in a sentence instead of new lines thats default