print('Day 78: Eliminating repeated lines from a file\n')

outputfile = open('outputfile.txt', 'w')

inputfile = open('inputfile.txt', 'r')

lines_seen = set()

for line in inputfile:
    if line not in lines_seen:
        outputfile.write(line)
        lines_seen.add(line)

inputfile.close()
outputfile.close()