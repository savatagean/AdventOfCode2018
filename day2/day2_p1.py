import collections

inputfile = 'input.txt'

two_times_counter = 0
three_times_counter = 0
two_times_flag = False
three_times_flag = False

cheksum = 0

with open(inputfile) as fp:
    for line in fp:
        letters = collections.Counter(line)
        for letter in letters:
            if letters[letter] == 2:
                two_times_flag = True
            elif letters[letter] == 3:
                three_times_flag = True
        if two_times_flag:
            two_times_counter += 1
        if three_times_flag:
            three_times_counter += 1
        two_times_flag = False
        three_times_flag = False

cheksum = two_times_counter * three_times_counter

print cheksum