"""
Rules: Throughout this puzzle, you will get various answers. When you get an answer, put it in the URL after the slash. For instance, this page is hackathon.adtran.com:8080/start. If the first answer is finish (it's not), you would navigate to hackathon.adtran.com:8080/finish to get the next answer. Keep solving until you find the easter egg at the end. All answers, keys and inputs will be lower-case.

Greetings, all, and welcome to this riddle,
I hope you have some fun.
You'll probably have to futz and fiddle,
To finish and be done.

This challenge is all about cryptography,
So get to work a-cracking.
We'll also deal with geography,
And a little bit of hacking

Our first challenge takes place in ancient Rome,
from a leader fierce and wise.
He invented a quite early code
which hides today's wonderful prize

With cipher in hand you're ready to run,
you'll take one step, then two more.
You'll have to keep on stepping each time by one,
Until you've stepped by twenty four

goodluck
"""

# solution: weetbksa
message = "goodluck"
steps = 16

solution = ''
for c in message:
    newc = chr(ord(c) + steps)
    if (ord(c)+steps) >= (ord('a')+26):
        newc = chr(ord(newc)-26)

    solution += newc
print("solution: {}".format(solution))
