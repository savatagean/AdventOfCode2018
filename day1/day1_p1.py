inputfile = 'input.txt'

with open(inputfile) as fp:
    frequency = sum([int(x) for x in fp])

print frequency