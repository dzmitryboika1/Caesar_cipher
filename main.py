# the program ciphers whole inputted phrase preserving the original punctuation and letter case
# feature is a shift for cipher of each word is equal the length of the word

# the function counts length of each word to determine shift
def define_shift(word):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    counter = 0
    for letter in word:
        if letter.lower() in abc:
            counter += 1
    return counter


# func changes each letter to the letter in abc according to the passed shift value
def cipher_word(word, shift):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    cyphered_word = ''
    for i in range(len(word)):
        if word[i].lower() in abc:
            if word[i].islower():
                cyphered_word += abc[(abc.index(word[i]) + shift) % 26]
            elif word[i].isupper():
                cyphered_word += abc[(abc.index(word[i].lower()) + shift) % 26].upper()
        else:
            cyphered_word += word[i]
    return cyphered_word


phrase = input()
phrase_lst = phrase.split()
cypher_phrase_lst = []
for el in phrase_lst:
    cypher_phrase_lst.append(cipher_word(el, define_shift(el)))
phrase = ' '.join(cypher_phrase_lst)
print(phrase)
