"""
You've completed that one too,
just one more to go!
This next cipher isn't new,
but wouldn't you like to know.

An American discovered this technique,
and it shares a name with a logic gate.
So don't be shy or meek,
finish this at your fastest rate.

A four letter key is hidden,
and you must find it first.
The message below is encrypted,
and ready to do it's worst.

This may seem like guessing or shifting,
but I assure you it doesn't have to be,
let computers do the heavy lifting,
And the prize will be given to thee.
"""
# Solution: hackkcah
# TODO: Research getting the solution via eigen values

from itertools import chain, cycle, product

ciphertext = [int(i) for i in "30 25 65 19 3 9 18 90 86 0 0 0 86 6 8 \
              21 16 31 19 17 86 24 4 6 19 94 65 29 86 \
              17 12 84 1 25 18 28 31 30 6 84 15 31 20 \
              84 23 80 7 21 24 4 0 7 2 25 2 84 30 17 \
              2 31 23 4 9 27 24 80 25 24 88 80 65 29 \
              86 7 8 7 30 80 8 84 21 31 20 24 18 80 9 \
              21 21 27 65 3 31 4 9 84 15 31 20 84 17 \
              5 24 7 86 17 6 21 31 30 79 84 86 18 20 \
              0 86 17 21 84 26 21 0 7 2 80 8 84 17 31 \
              21 84 2 31 65 25 23 27 4 84 23 80 17 1 \
              12 10 13 17 86 22 14 6 86 9 14 1 86 23 \
              20 13 5 94 65 84 86 25 65 28 25 0 4 84 \
              15 31 20 84 19 30 11 27 15 21 5 84 31 4 \
              65 21 24 20 65 19 25 31 5 84 26 5 2 31 \
              86 4 14 84 23 28 13 84 30 17 2 31 31 30 \
              6 84 6 17 19 0 31 19 8 4 23 30 21 7 88 \
              80 65 23 25 30 6 6 23 4 18 84 25 30 65 \
              18 31 30 8 7 30 25 15 19 86 4 9 29 5 94 \
              65 84 31 22 65 13 25 5 65 3 23 30 21 84 \
              2 31 65 19 25 80 21 27 86 4 9 17 86 28 \
              0 7 2 80 17 21 4 4 65 27 16 80 21 28 31 \
              3 65 4 3 10 27 24 19 80 24 27 3 2 65 18 \
              31 30 0 24 86 17 15 7 1 21 19 84 31 3 \
              65 28 23 19 10 31 21 17 9".split()]
key_len = 4
validchars = []
validchars += list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
validchars += list("abcdefghijklmnopqrstuvwxyz")
validchars += list("1234567890 !\"'(),.:;?@_")
validchars = [ord(c) for c in validchars]
#print([chr(c) for c in validchars])

def split_into_chunks(chunkee, size):
    for i in range(0, len(chunkee), size):
        yield chunkee[i:i+size]

def is_key_valid(chunks, key_index, key_candidate):
    for chunk in chunks:
        try:
            if chunk[key_index]^key_candidate not in validchars:
                return False
        except IndexError:
            pass
    return True

def get_possible_keys(chunks, key_len):
    possible_keys = [[], [], [], []]
    for key_index in range(key_len):
        for key_candidate in range(255):
            if is_key_valid(chunks, key_index, key_candidate):
                possible_keys[key_index].append(key_candidate)
    return possible_keys

def get_possible_messages(keys, ciphertext):
    messages = []
    for key_product in product(*keys):
        cipher_key = list(key_product)
        messages += [''.join(chr(int(c)^k) for c,k in zip(ciphertext, cycle(cipher_key)))]
    return messages

def main():
    # decode the message
    chunks = list(split_into_chunks(ciphertext, key_len))
    possible_keys = get_possible_keys(chunks, key_len)
    possible_messages = get_possible_messages(possible_keys, ciphertext)

    # print results
    print(possible_keys)
    for msg in possible_messages:
        print(msg)

if __name__ == '__main__':
    main()
