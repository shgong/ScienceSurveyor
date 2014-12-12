

#! /usr/bin/env python

import sys, os
from pylab import *  # for plotting
from graph_tool.all import *


g = load_graph("data.dot","dot")
name = g.vertex_properties["name"]


# draw map 
print "generating layout"

pos = sfdp_layout(g)

print "start drawing"
graph_draw(g, pos, output_size=(1000, 1000), vertex_color=[1,1,1,0],
           vertex_size=1, edge_pen_width=0.2, output="draw.png")
print "finished"