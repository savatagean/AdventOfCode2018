from operator import itemgetter

inputfile = 'input.txt'

words = []
wordsInverse = []
counter = 0
j= 0
match_counter = 0

with open(inputfile) as fp:
    for line in fp:
        words.append(line)

del words[249]

for i in reversed(words):
    wordsInverse.append(i)

del wordsInverse[0]

for a in words:
    for b in wordsInverse:
        for k in a:
            if k == itemgetter(j)(b):
                match_counter += 1
            j+=1
            if match_counter == 26 and a !=b:
                print b
                print a
        match_counter = 0
        j = 0
