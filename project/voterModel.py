import random

def voterModel(graph, seed, steps, filepointer, verbose=False):
	nodes = len(graph.keys())
	percentages = [nodes * x/100.0 for x in range(25, 125, 25)]
	influenced = list(seed)
	percInfl = 0
	for i in range(steps):
		if len(influenced) == len(graph):
			if verbose:
				if len(percentages) != 0:
					percInfl += 25
					s = "- "+str(percInfl)+"% nodes influenced in step: "+str(i)+"\n"
					filepointer.write(s)
					print "- ",percInfl,"% nodes influenced in step: ",i
				return influenced

		while True:
			u = random.choice(list(graph.keys()))
			if u not in seed:
				break
		if u not in influenced and len(graph[u]) != 0:
			v = random.choice(list(graph[u]))
			if v in influenced:
				influenced.append(u)
				if verbose:
					if len(influenced) >= percentages[0]:
						percentages.pop(0)
						percInfl += 25
						s = "- "+str(percInfl)+"% nodes influenced in step: "+str(i)+"\n"
						filepointer.write(s)
						print "- ",percInfl,"% nodes influenced in step: ",i
	return influenced

