"""
You finally have Ceaesar beat,
huzzah, hooray!
But another puzzle rises to meet,
and stands in your way.

This code comes from a 16th century Italian,
but named after one from France.
To win this prized medallion,
around Caesar you must dance.

The input for this one,
is your triumph over Caesar.
For you to be done,
You must solve this brain-teaser.

Patience is your first key,
Resolve is the next,
When you finally start to see,
you'll put your skills to the test.

Hacking is the third key,
Coding is the last.
If you want to be finished and free,
then finish this one fast.
"""

from itertools import cycle

message_start = "weetbksa"
keys = ["patience", "resolve", "hacking", "coding"]

def vigenere_transform(message, key):
    output = ""
    for c, k in zip(message, cycle(key)):
        output += chr(((ord(c)-97+ord(k)-97)%26)+97)
    return output

# for testing
#output = vigenere_transform("attackatdawn", "lemon")
#print(output)

output = message_start
for key in keys:
    output = vigenere_transform(output, key)

# solution: lwuhllgq
print(output)
