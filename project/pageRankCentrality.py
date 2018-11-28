from __future__ import division

def pageRankCentrality(graph, confidence, damping=1.0e-5):
	tmp = {}
	pageRank = {}
	# for every node contains the set of nodes that links to it
	incomings = {}

	done = False

	nodes = graph.keys()

	size = len(graph)
	for i in nodes:
		pageRank[i] = 1/size
		incomings[i] = set()


	for i in nodes:
		for j in graph[i]:
			incomings[j].add(i)

	#it = 1
	while not done:
		maxPageRank = 0.0
		for i in nodes:
			tmp[i] = pageRank[i]
			tmp[i] = (1-damping) * sum( [ pageRank[j]/len(graph[j]) + (damping/size) for j in incomings[i] ])
			if tmp[i] > maxPageRank:
				maxPageRank = tmp[i]
		
		#it += 1
		diff = 0
		for i in nodes:
			diff += abs(pageRank[i]-float(tmp[i])/maxPageRank) # Distance between old and new centrality vector
			pageRank[i] = tmp[i]/maxPageRank

		if diff < confidence:
			done = True

	return pageRank 

