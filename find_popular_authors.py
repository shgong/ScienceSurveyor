

#! /usr/bin/env python

import sys, os


N = 10000  # generate map with first N line data
count = 0
d = {}  # dictionary storing name and nodes
fname = "author2008.txt" #filename


# open file
with open(fname) as f:
    content = f.readlines()

N0=len(content)
print "Total Citations:", N0
print "start counting"
N=N0

# ----------------------------------------------------------------------

for line in content:
	if N <= 0:
		break
	if N % 5000 == 0:
		print "{0:.2f}%".format( (1-N*1.0/N0) * 100)

	a,b = line.split(" ==> ")
	b=b[:-1]

	if a not in d:
		d[a] = 0
		# print repr(a)," added"

	if b not in d:
		d[b]=0
		# print repr(b)," added"

	d[a]+=1
	d[b]+=1

	# print repr(a),"->",repr(b)," added"
	N = N - 1


print "find the people with most paper"

authorm=""
authorc=0

for i in d:
	if d[i]>3000:
		print i
