
This is a experiment based on Science Surveyor Project, see more information at [this](http://science-surveyor.github.io/) site.


# Overview

Science Surveyor is a web-based application to find out where scientific finds stands in its research area. We proposed to make an analysis tool covering important academic databases. We will start with open access repositories like arXiv and PLoS One, but later we would broaden our sources using API access to databases like Thomson Reuters, JSTOR, and Elsevier. 

In this project, we plan to measure a published finding in four dimensions:

- citation

- funding

- idea 

- time

We could generate a 3-dimension vector for each period of time we analysis. If we compare the literature area or a specific finding during different time, we may apply machine learning and regression analysis to find out some interesting trends from existing literatures. It would be a powerful tool for science journalist to understand the status of a certain area or work.



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


