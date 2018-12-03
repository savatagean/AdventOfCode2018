import re

inputfile = 'input.txt'

fwidth, fheight = 1000, 1000
fabric = [['' for x in range(fwidth)] for y in range(fheight)]

counter = 0

with open(inputfile) as fp:
    for line in fp:
        leftindex = re.findall(r'@ (\d+)', line)
        left = int(leftindex[0])
        topindex = re.findall(r',(\d+)', line)
        top = int(topindex[0])
        widthindex = re.findall(r': (\d+)', line)
        width = int(widthindex[0]) 
        heightindex = re.findall(r'x(\d+)', line)
        height = (int(heightindex[0]))
        for w in range(left, left+width):
            for h in range(top, top+height):
                if fabric[w][h] == '':
                    fabric[w][h] = '*'
                elif fabric[w][h] == '*':
                    fabric[w][h] = 'x'

with open(inputfile) as fp:
    for line in fp:
        leftindex = re.findall(r'@ (\d+)', line)
        left = int(leftindex[0])
        topindex = re.findall(r',(\d+)', line)
        top = int(topindex[0])
        widthindex = re.findall(r': (\d+)', line)
        width = int(widthindex[0]) 
        heightindex = re.findall(r'x(\d+)', line)
        height = (int(heightindex[0]))
        idindex = re.findall(r'#(\d+)', line)
        id = int(idindex[0])
        for w in range(left, left+width):
            for h in range(top, top+height):
                if fabric[w][h] == '*':
                    counter += 1
        if counter == width*height:
            print(id)
        counter = 0
