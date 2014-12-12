
# Science Surveyor

## Introduction

It is very important to make the public better understand scientific research. Science journalists is the bridge between the two groups, but there is a problem in contextualization of journal articles in time. Science journalists have limitations that it is nearly impossible to achieve both the thorough understanding of field and the timeliness of the news report, as there are so much to read and research, including the past researches, whether a certain finding is significant and how a finding stands in the fields’ consensus.

Such limitations would lead to dreadful consequences. The public might have a bad understanding of science nature and researchers if the journalist could not present the progress and findings of scientific research clearly.


## Goal

We propose designing the Science Surveyor system, a tool to help science journalists contextualize the scientific literatures in a timely manner. This tool would allow journalists to submit a scientific study that they want to cover.

 It would generate a map with three central dimensions, or layers: a consensus layer that would show whether the new finding is consistent with scientific consensus, a temporal layer that would show the pattern of publishing on this topic across time, a funding layer that would characterize the funding in that field. There might also be a general popularity calculated from the weighted average of the results in all three layers.


# Method

## Approach Overview

Science Surveyor is a web-based application to find out where scientific finds stands in its research area. We proposed to make an analysis tool covering important academic databases. We will start with open access repositories like arXiv and PLoS One, but later we would broaden our sources using API access to databases like Thomson Reuters, JSTOR, and Elsevier. 

In this project, we plan to measure a published finding in four dimensions:

- The first and most important metric would be the centrality and connectivity in a citation network which is a strong indicator of the impact. Such analysis would be a great tool to find out central studies with reliable sources and reputation in similar researches. 

- Another source would be information about funding. The private corporate funding could indicate biased results about the popularity of a research. 

- The third source is the idea network. It would use n-gram algorithm or bag of words model to address the topic similarity and relationship. 

- The last dimension is how it changes over time. Using the history information of citation and funding network by years or decades, we might find some patterns about popular areas.

We could generate a 3-dimension vector for each period of time we analysis. If we compare the literature area or a specific finding during different time, we may apply machine learning and regression analysis to find out some interesting trends from existing literatures. It would be a powerful tool for science journalist to understand the status of a certain area or work.


## previous research

There are many kinds of citation relationship analysis we knew in the previous work. In the project, as we should try to keep it clear enough for journalist to understand, we decide to choose  a non-direction citation relationship.

On account of the similar reason, we analyzed different centrality measures including current flow and load model, but only use metrics with pure topology relationship and score assigning, which is easier to understand, instead of some physics models.

The major advantage of our approach is the high dimension level of information. Unlike traditional research doing co-citation clustering and observe how groups evolve by time, we are observing a three-dimension vectors covered all three parts of a literature including citation, funding and ideas.

In order to keep such complexity easier enough for science journalist to understand, we are also developing language generation system transforming the network and machine learning data to daily language.



#Evaluation Method

The performance of such system includes several aspects. Generally whether it is user-friendly and the quality of results define wether this project would success. Traditional research about citation clustering would focus on a certain database like PubMed and compare the cluster view and time zone view of the result. However such result is a quite subjective evaluation which need human testers and evaluators.

There is also automatic measurement for efficiency and accuracy. First, the run time is a vital evaluation parameter which would define the working efficiency towards journalists. It is necessary to test how it works with different scales of the database. Secondly, the prediction accuracy about where a certain finding stands and how it might develop in the future also deserves carefully scrutinization. Basically we could use cross-validation when building a model while learning the research trends. We could also get some labeled finding/region match-ups, and try to do a validation in the research classification.


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