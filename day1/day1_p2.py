inputfile = 'input.txt'

freq_array = []
freq_sum_array = []
frequency = 0
i = 0
the_number = 0

with open(inputfile) as fp:
    freq_array = [int(x) for x in fp]

while True:
    frequency = frequency + freq_array[i]
    if frequency in freq_sum_array:
        the_number = frequency
        break
    freq_sum_array.append(frequency)
    i=i+1
    if i == len(freq_array):
        i = 0

print the_number