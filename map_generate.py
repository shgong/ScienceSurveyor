

#! /usr/bin/env python

import sys, os
from pylab import *  # for plotting
from graph_tool.all import *


g = Graph()
g.set_directed(False)
v_name = g.new_vertex_property("string")



N = 10000  # generate map with first N line data
count = 0
d = {}  # dictionary storing name and nodes
fname = "author2009.txt" #filename


# open file
with open(fname) as f:
    content = f.readlines()

N0=len(content)
print "Total Citations:", N0
print "Creating vertexes and edges"
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
		v = g.add_vertex()
		v_name[v] = a
		d[a] = v
		# print repr(a)," added"

	if b not in d:
		v = g.add_vertex()
		v_name[v] = b
		d[b] = v
		# print repr(b)," added"

	e = g.add_edge(d[a], d[b])

	# print repr(a),"->",repr(b)," added"
	N = N - 1



# ----------------------------------------------------------------------

print "save network file"

g.vertex_properties["name"] = v_name
g.save("data.dot","dot")

# I use dot file here as there is loading error in xml file
# and all elements are strings



# ----------------------------------------------------------------------


print "calculate pagerank"

c = pagerank(g)
fsave=open("centrality_pagerank_result.txt",'w')
for i in d:
	fsave.write(i+" ==> "+str(c[d[i]])+"\n")
fsave.close()

# ----------------------------------------------------------------------


print "calculate betweenness"

c,e = betweenness(g)
fsave=open("centrality_betweenness_result.txt",'w')
for i in d:
	fsave.write(i+" ==> "+str(c[d[i]])+"\n")
fsave.close()


# ----------------------------------------------------------------------

