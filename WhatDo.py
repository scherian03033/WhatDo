#!/usr/bin/python
import sys
from random import randint
import datetime

def monthDay2num(m,d):
    return m * 100 + d


## Evolve this to tag each item with a season bitmap (i.e numbers 1-15)
##  1 = Winter 12/21-3/19
##  2 = Spring 3/20-6/20
##  4 = Summer 6/21-9/21
##  8 = Fall 9/22-12/20
##  15 = year round

SeasonLookup = [[3,19,1],[6,20,2],[9,21,3],[12,20,4],[12,31,1]]
SeasonLookupLen = len(SeasonLookup)
SeasonNames = ["Winter", "Spring", "Summer", "Fall"]

if (len(sys.argv) == 1):
	filename = "whatdo.txt"
else:
	filename = sys.argv[1]

f = open(filename)
lines = f.readlines()

listLen = len(lines)

today = datetime.date.today()
# For Testing:
# today = datetime.date(2013,12,21)
# print "Today is",today

season = 15

for i in range(SeasonLookupLen):
    if (monthDay2num(today.month,today.day) <= monthDay2num(SeasonLookup[i][0],SeasonLookup[i][1])):
        season = SeasonLookup[i][2]
        break

print "Season is", SeasonNames[season-1]

done = False

while (done == False):
    idx = randint(0,listLen-1)
    parseLine = lines[idx].split(";")
    if (int(parseLine[0]) & season):
        idea = parseLine[1]
        done = True

print "\nYou might like to", idea[0:len(idea)-1]+"?\n"

