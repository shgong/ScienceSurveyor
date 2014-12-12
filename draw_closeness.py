
#! /usr/bin/env python

import sys, os
from pylab import *  # for plotting
from graph_tool.all import *


print "loading graph"
g = load_graph("data.dot","dot")
name = g.vertex_properties["name"]



print "calculate closeness"

c = closeness(g)


print "layout"

pos = sfdp_layout(g)



print "draw graph"

graph_draw(g, pos, vertex_fill_color=c,
vertex_size=prop_to_size(c, mi=5, ma=15),
vcmap=matplotlib.cm.gist_heat,
vorder=c, output="polblogs_closeness.pdf")