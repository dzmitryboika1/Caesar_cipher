abc_low = 'abcdefghijklmnopqrstuvwxyz'
abc_up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

phrase = input()
phrase_lst = phrase.split()
cypher_phrase_lst = []


def define_shift_len(abc_low, abc_up, word):
    counter = 0
    for c in word:
        if c in abc_low or c in abc_up:
            counter += 1
    return counter


def shift_word(word, abc_up, abc_low, shift):
    cypher_word = ''
    for i in range(len(word)):
        if word[i] in abc_up:
            cypher_word += abc_up[(abc_up.index(word[i]) + shift) % 26]
        elif word[i] in abc_low:
            cypher_word += abc_low[(abc_low.index(word[i]) + shift) % 26]
        else:
            cypher_word += word[i]
    return cypher_word


for el in phrase_lst:
    cypher_phrase_lst.append(shift_word(el, abc_up, abc_low, define_shift_len(abc_low, abc_up, el)))
phrase = ' '.join(cypher_phrase_lst)
print(phrase)
