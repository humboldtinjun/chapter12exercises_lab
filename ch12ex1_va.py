# ask virtual assistant how to use setdefault with rewriting add_bigram

#original
def add_bigram(bigram):
    first, second = bigram

    if first not in successor_map:
        successor_map[first] = [second]
    else:
        successor_map[first].append(second)

""" set default returns the value for the key if it exists, if it doesnt it sets
dict[key] = default and returns that default, in one line it handles creating the list 
if missing or appending it to the list"""
def add_bigram(bigram):
    first, second = bigram
    successor_map.setdefault(first, []).append(second)

#What’s the difference between GPT-style large language models and Markov chain text analysis?
"""Markov chains are like “guessing the next word based on just a couple words before.” 
GPT-style models look at a much longer context, learn grammar and facts, and generate more fluent, 
context-aware responses."""