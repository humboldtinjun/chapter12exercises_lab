# make a trigram that takes 3 words instead of 2
import unicodedata

trigram_counter = {}
window = []

def count_trigram(trigram):
    key = tuple(trigram)
    if key not in trigram_counter:
        trigram_counter[key] = 1
    else:
        trigram_counter[key] += 1



def process_word_trigram(word):
    window.append(word)

    if len(window) == 3:
        count_trigram(window)
        window.pop(0)

def split_line(line):
    return line.replace('—', ' ').split()



# Build  string of punctuation chars from the book
punc_marks = {}
for line in open('drjeckll.txt'):
    for char in line:
        if unicodedata.category(char).startswith('P'):
            punc_marks[char] = 1

punctuation = ''.join(punc_marks)

# Define the function
def clean_word(word):
    return word.strip(punctuation).lower()

filename = 'drjeckll.txt'


for line in open(filename):
    for word in split_line(line):
        word = clean_word(word)
        process_word_trigram(word)

def second_element(t):
    return t[1]

def print_most_common(counter, num=5):
    items = sorted(counter.items(), key=second_element, reverse=True)
    for words, freq in items[:num]:
        print(freq, ' '.join(words))

print_most_common(trigram_counter)
