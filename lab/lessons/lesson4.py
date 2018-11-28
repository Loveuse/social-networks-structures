#!/usr/bin/python

# Computes the betweenness of the graph in input
def betweenness(graph):
  betweenness = dict()
  for i in graph.keys():
    betweenness[i] = 0
  
  for s in graph.keys():
    #Initialization for any root
    tree = []
    
    queue = [s]
    
    parents = dict()
    for i in graph.keys():
      parents[i] = []
    
    spnum = dict()
    for i in graph.keys():
      spnum[i] = 0
    spnum[s] = 1
    
    distance = dict()
    for i in graph.keys():
      distance[i] = -1
    distance[s] = 0
    
    flow = dict()
    for i in graph.keys():
      flow[i] = 0
      
    #BFS
    while queue != []:
      c = queue.pop(0)
      tree.append(c)
      for i in graph[c]:
        if distance[i] == -1:
          queue.append(i)
          distance[i] = distance[c] + 1
        if distance[i] == distance[c] + 1:
          spnum[i] += spnum[c]
          parents[i].append(c)
        
    #BOTTOM-UP PHASE
    while tree != []:
      c = tree.pop()
      for i in parents[c]:
        flow[i] += (float(spnum[i])/spnum[c])*(1 + flow[c])
      if c != s:
        betweenness[c] += flow[c]

  return betweenness

def top(graph,k):
  b = betweenness(graph)
  top = []
  top_values = []
  for i in b.keys():
    added = 0
    for j in range(min(len(top),int(k))):
      if b[top[j]] < b[i]:
        top.insert(j,i)
        added = 1
        break
    if added == 0:
      top.append(i)
    if len(top) > int(k):
      top.pop()
  for i in range(len(top)):
    top_values.append(b[top[i]])
  return top, top_values
