
This is a experiment based on Science Surveyor Project, see more information at [this](http://science-surveyor.github.io/) site.


# Approach Overview
Science Surveyor is a web-based application to find out where scientific finds stands in its research area. We proposed to make an analysis tool covering important academic databases. We will start with open access repositories like arXiv and PLoS One, but later we would broaden our sources using API access to databases like Thomson Reuters, JSTOR, and Elsevier. 

In this project, we plan to measure a published finding in four dimensions:

- The first and most important metric would be the centrality and connectivity in a citation network which is a strong indicator of the impact. Such analysis would be a great tool to find out central studies with reliable sources and reputation in similar researches. 

- Another source would be information about funding. The private corporate funding could indicate biased results about the popularity of a research. 

- The third source is the idea network. It would use n-gram algorithm or bag of words model to address the topic similarity and relationship. 

- The last dimension is how it changes over time. Using the history information of citation and funding network by years or decades, we might find some patterns about popular areas.

We could generate a 3-dimension vector for each period of time we analysis. If we compare the literature area or a specific finding during different time, we may apply machine learning and regression analysis to find out some interesting trends from existing literatures. It would be a powerful tool for science journalist to understand the status of a certain area or work.



# Experiment

## Data
We use the ACL Anthology Network dataset from the University of Michigan's CLAIR Group. It has literature data from 2008 to 2013. In this experiment we mainly use the non-self author citation network data to generate the author centrality which contributes to the overall centrality evaluation of a finding.

## Library
We use python as our project language. We compared between a few python tool-kit for network analysis including snap.py, graph-tool, NetworkX and igraph.  According to the performance result, the python-core library like NetworkX and snap.py is 10 times slower than the C++ core library like igraph and graph-tool. As graph-tool works better at centrality measures like page rank and graph works better at degeneracy methods like k-core, considering that our core function is based on centrality measurements, we decided to choose graph-tool over igraph library.

## Centrality Measures
There are a great variety of centrality measures we could choose from. There are some basic centrality measures. Degree centrality simply count the links. Closeness shows the distance to other nodes, making it a good measurement while the research are close. Betweenness measures the  role a node plays as a bridge, which seems to be a good metric for connectivity. Eigenvector centrality like page rank would might be effective in the evaluation.

There are also some new approaches. Some researchers tried to avoid simply using shortest paths like betweenness centrality. Percolation centrality assumes there is a infection source, which is great in some social network analysis. Total communicability centrality describes the row sum of adjacency matrix, is great to describe the overall connectivity.

Considering the model compatibility to our database, with the general graph in Figure 1, degree centrality would be too simple to use. Closeness centrality would probably suffer while there are many cluster centers, so it is less efficient to calculate all the distance.  The shortest path betweenness would already work and percolation is not necessary as it is not  a transmission network. Total communicability might require too much math background for science journalists

In account of the accessibility to science reporters and the efficiency to work with other vector layers, we decided to choose betweenness and page rank as our experiment measurements.






# Set up Graph-tool

1.download release data from github

	svn checkout https://github.com/shgong/prototype/trunk/01_Data/aan/release

2.install macports

3.use macport install graph-tool

	sudo port install py27-graph-tool

	sudo port install py27-matplotlib

4.follow the instructions to setup macport python

	port notes py-graph-tool



# Python Code Example

1. change the name of author citation network in `map_generate.py`

2. run it to get centrality measures and save network to file ( it might take 20 minutes )

3. run `map_load_draw.py` file to generate the network graph

PS: `find_popular_authors.py` is simply counting the degrees





# Case Analysis


![alt text](https://raw.githubusercontent.com/shgong/ScienceSurveyor/master/table.png "Logo Title Text 1")

We applied both measurements to our network to see how it works with different types of nodes. For example, we choose one of the most cited author, Michael John Collins in AAN to see how the measure works. Both his betweenness centrality and page rank stayed in the first year, but dropped in the second year. We tried to compare it with a less famous author Susan E. Brennan, and find some interesting phenomenon which would help us improve the citation centrality measurement.

- Betweenness centrality have much higher value than page rank centrality in the central nodes, but they are at the similar magnitude in the outer nodes. Betweenness have more significant changes for outer nodes, shall we give it more weights?

- The influence of Collins is 80 times larger than Brennan in Betweenness criterion, while it is only around 10 times in PageRank. Which is more reasonable? 

To answer this questions and find the better criterion to describe the influence, we would consult some professors in this area to improve our system. We analyzing the distrution of both centralities may also help.


