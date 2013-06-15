from random import randint

## Evolve this to tag each item with a season bitmap (i.e numbers 1-15)

filename = "whatdo.txt"

f = open(filename)
lines = f.readlines()

listLen = len(lines)

idx = randint(0,listLen-1)

print "\nWhy don't you", lines[idx]