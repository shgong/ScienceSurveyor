# Installation

1.download release data from github

	svn checkout https://github.com/shgong/prototype/trunk/01_Data/aan/release

2.install macports

3.use macport install graph-tool

	sudo port install py27-graph-tool

	sudo port install py27-matplotlib

4.follow the instructions to setup macport python

	port notes py-graph-tool




# Usage

1. change the name of author citation network in `map_generate.py`

2. run it to get centrality measures and save network to file ( it might take 20 minutes )

3. run `map_load_draw.py` file to generate the network graph

PS: `find_popular_authors.py` is simply counting the degrees