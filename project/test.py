import sys, random, json
import cPickle as pickle
from lesson1 import randomDirectGraphWithAVGClust, randomBalancedGraphWithCheckAvg, getAvgcFromDirectGraph
from lesson2 import WS2DDirectGraph, generalizedWS
from lesson3 import readDirectGraph
from lesson4 import betweenness
from lesson5 import top
from voterModel import voterModel
from extractData import extract


def findBestSeed(graph, k, centrality, confidence, steps, filepointer, verbose = False, wiki=False, seed=None):
	if not wiki:
		seed, topValues = top(graph, k, centrality, confidence)
	influenced = voterModel(graph, seed, steps, filepointer, verbose) 

	while True:
		s = "Influenced: "+str(len(influenced))+" k: "+str(k)+"\n"
		filepointer.write(s)

		print "Influenced: ",len(influenced)," k: ",k
		k -= 5

		seed = seed[:k]
		tmpInfluenced = voterModel(graph, seed, steps, filepointer, verbose) 

		if len(tmpInfluenced) < len(influenced):
			k += 5
			break
		influenced = list(tmpInfluenced)

	return influenced


n = 7115
p = 0.4
k = 100
radius = 2

lowM = 75000
uppM = 125000

avgc = (0.1, 0.2)
confidence = 1.0e-3
steps = 100000

# load randomGraphs
# for i in xrange(100)
#  	with open('/randomGraphs/randGraph%d.json' %i, 'wb') as fp:
# 		graph = pickle.load(fp)


# graph = dict()
# for i in range(10):
# 	graph[i] = set()
# for i in range(9):
# 	graph[i].add(i+1)

# print graph
# print "      "

# print getAvgcFromDirectGraph(graph)

" >>>>> Wiki graph <<<<<< "

# wikiGraph, m = readDirectGraph(sys.argv[1])

# avgcWikiGraph = getAvgcFromDirectGraph(wikiGraph)

# print "Wiki bet..."
# beetSeed, _ = top(wikiGraph, k, 'b', confidence)

# print "Wiki eig..."
# eigSeed, _ = top(wikiGraph, k, 'e', confidence)
# print "Wiki pag..."
# pageSeed, _ = top(wikiGraph, k, 'p', confidence)

# with open("outWiki", "w") as text_file:
# 	for i in xrange(100):
		
# 		print "----- Wiki graph - n: ",n," m: ",m," avgc: ", avgcWikiGraph		
# 		s = "----- Wiki graph - n: "+str(n)+" m: "+str(m)+" avgc: "+ str(avgcWikiGraph)+"\n"
# 		text_file.write(s) 

# 		print "##### Betweenness + Voter on wiki-Vote num ",i," #####"  
# 		s = "##### Betweenness + Voter on wiki-Vote num "+str(i)+" #####\n"  
# 		text_file.write(s)		
# 		findBestSeed(wikiGraph, k, 'b', confidence, steps, text_file, False, True, beetSeed)

# 		print "##### Eigenvector + Voter on wiki-Vote num ",i," #####" 
# 		s = "##### Eigenvector + Voter on wiki-Vote num "+str(i)+" #####\n" 
# 		text_file.write(s)
# 		findBestSeed(wikiGraph, k, 'e', confidence, steps, text_file, False, True, eigSeed)

# 		print "##### PageRank + Voter on wiki-Vote num ",i," #####" 
# 		s = "##### PageRank + Voter on wiki-Vote num "+str(i)+" #####\n" 
# 		text_file.write(s)
# 		findBestSeed(wikiGraph, k, 'p', confidence, steps, text_file, False, True, pageSeed)

# 	text_file.write("----- ")

# print "Extract wiki......"
# extract("Wiki", "outWiki")


" >>>>> 100 Random Direct Balanced Graphs <<<<<< "

# with open("outRandom", "w") as text_file:
# 	for i in xrange(100):
# 		m = random.randint(lowM, uppM)
		
# 		randomBalancedGraph = randomBalancedGraphWithCheckAvg(n, p, m)
		
# 		avgcRandGraph = getAvgcFromDirectGraph(randomBalancedGraph)

# 		print "----- Random graph num ",i," - n: ",n," m: ",m," avgc: ", avgcRandGraph
# 		s = "----- Random graph num "+str(i)+" - n: "+str(n)+" m: "+str(m)+" avgc: "+str(avgcRandGraph)+"\n"
# 		text_file.write(s)

# 		print "##### Betweenness + Voter on randomBalancedGraph num ",i," #####"
# 		s = "##### Betweenness + Voter on randomBalancedGraph num "+str(i)+" #####\n"
# 		text_file.write(s)
# 		findBestSeed(randomBalancedGraph, k, 'b', confidence, steps, text_file, True)

# 		print "##### Eigenvector + Voter on randomBalancedGraph num ",i," #####"
# 		s = "##### Eigenvector + Voter on randomBalancedGraph num "+str(i)+" #####\n"
# 		text_file.write(s)
# 		findBestSeed(randomBalancedGraph, k, 'e', confidence, steps, text_file, True)

# 		print "##### PageRank + Voter on randomBalancedGraph num ",i," #####"
# 		s = "##### PageRank + Voter on randomBalancedGraph num "+str(i)+" #####\n"
# 		text_file.write(s)
# 		findBestSeed(randomBalancedGraph, k, 'p', confidence, steps, text_file, True)

# 	text_file.write("----- ")

# print "Extract random graph......"
# extract("Random", "outRandom", True)


" >>>>> 100 WS 2D <<<<<< "

# weakTies = [0, 5, 10]

# with open("outWS2D", "w") as text_file:

# 	for i in xrange(100):

# 		m = random.randint(lowM, uppM)

# 		WSGraph2D = WS2DDirectGraph(n, radius, weakTies, m)

# 		avgcWS2D = getAvgcFromDirectGraph(WSGraph2D)

# 		print "----- WS2D graph num ",i," - n: ",n," m: ",m," avgc: ", avgcWS2D
# 		s =  "----- WS2D graph num "+str(i)+" - n: "+str(n)+" m: "+str(m)+" avgc: "+str(avgcWS2D)+"\n"
# 		text_file.write(s) 

# 		print "##### Betweenness + Voter on WSGraph2D num ",i," #####"
# 		s = "##### Betweenness + Voter on WSGraph2D num "+str(i)+" #####\n"
# 		text_file.write(s) 
# 		findBestSeed(WSGraph2D, k, 'b', confidence, steps, text_file, False)


# 		print "##### Eigenvector + Voter on WSGraph2D num ",i," #####"
# 		s = "##### Eigenvector + Voter on WSGraph2D num "+str(i)+" #####\n"
# 		text_file.write(s) 
# 		findBestSeed(WSGraph2D, k, 'e', confidence, steps, text_file, False)


# 		print "##### PageRank + Voter on WSGraph2D num ",i," #####"
# 		s = "##### PageRank + Voter on WSGraph2D num "+str(i)+" #####\n"
# 		text_file.write(s)
# 		findBestSeed(WSGraph2D, k, 'p', confidence, steps, text_file, False)

# 	text_file.write("----- ")

# print "Extract WS2D......"
# extract("WS2D", "outWS2D")


" >>>>> 100 Generalized WS <<<<<< "

# weakTies = [0, 5, 10]

# with open("outGenWS", "w") as text_file:

# 	for i in xrange(100):

# 		m = random.randint(lowM, uppM)

# 		nodes = 84*84
# 		generalizedWSGraph = generalizedWS(nodes, radius, weakTies, m)

# 		avgcGenWS = getAvgcFromDirectGraph(generalizedWSGraph)

# 		print "----- Generalized WS graph num ",i," - n: ",nodes," m: ",m,"  avgc: ", avgcGenWS
# 		s = "----- Generalized WS graph num "+str(i)+" - n: "+str(nodes)+" m: "+str(m)+"  avgc: "+str(avgcGenWS)+"\n"
# 		text_file.write(s)

# 		print "##### Betweenness + Voter on Generalized WS graph num ",i," #####"
# 		s = "##### Betweenness + Voter on Generalized WS graph num "+str(i)+" #####\n"
# 		text_file.write(s)
# 		findBestSeed(generalizedWSGraph, k, 'b', confidence, steps, text_file, False)

# 		print "##### Eigenvector + Voter on Generalized WS graph num ",i," #####"
# 		s = "##### Eigenvector + Voter on Generalized WS graph num "+str(i)+" #####\n"
# 		text_file.write(s)
# 		findBestSeed(generalizedWSGraph, k, 'e', confidence, steps, text_file, False)

# 		print "##### PageRank + Voter on Generalized WS graph num ",i," #####"
# 		s = "##### PageRank + Voter on Generalized WS graph num "+str(i)+" #####\n"
# 		text_file.write(s)
# 		findBestSeed(generalizedWSGraph, k, 'p', confidence, steps, text_file, False)

# 	text_file.write("----- ")

# print "Extract GenWS......"
# extract("Generalized", "outGenWS")













" >>>>> 100 Random Direct Graphs with given avg <<<<<< "

# for i in xrange(100):
# 	randomGraph = randomDirectGraphWithAVGClust(n, p, avgc[0], avgc[1])

#  	with open('/randomGraphs/randGraph%d.json' %i, 'wb') as fp:
#  		pickle.dump(randomGraph, fp)

# 	print "##### Betweenness + Voter on RandomGraph %d #####" %i
# 	# findBestSeed(randomGraph, k, 'b', confidence, steps, True)

# 	print "##### Eigenvector + Voter on RandomGraph %d #####" %i
# 	# findBestSeed(randomGraph, k, 'e', confidence, steps, True)

# 	print "##### PageRank + Voter on RandomGraph %d #####" %i
# 	# findBestSeed(randomGraph, k, 'p', confidence, steps, True)