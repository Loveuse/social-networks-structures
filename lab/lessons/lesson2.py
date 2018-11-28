#!/usr/bin/python

import random
import math

# n is the number of nodes
# r is the radius of each node (a node u is connected with each other node at distance at most r) - strong ties
# k is the number of random edges for each node u - weak ties
def WSGridGraph(n, r, k):
  line = int(math.sqrt(n))
  graph = dict()
  #Initialization
  for i in range(line): #i represents the grid row
    for j in range(line): #j represents the grid coloumn
      graph[i*line+j] = set() #Each node is identified by a number in [0, n - 1]

  #For each node u, we add an edge to each node at distance at most r from u
  for i in range(line):
    for j in range(line):
      for x in range(r+1): # x is the horizontal offset
        for y in range(r+1-x): # y is the vertical offset. The sum of offsets must be at most r
          if x + y > 0: # The sum of offsets must be at least 1
            if i + x < line and j + y < line: 
              graph[i*line+j].add((i+x)*line+(j+y))
              graph[(i+x)*line+(j+y)].add(i*line+j)
            # We do not consider(i+x,j-y) (i-x,j+y) and (i-x,j-y) since the edge between these nodes and (i,j) has been already added at previous iterations

      #For each node u, we add a node to k randomly chosen nodes
      for h in range(k):
        s = random.randint(0,n-1)
        if s != i*line+j:
          graph[i*line+j].add(s)
          graph[s].add(i*line+j)
  return graph

# n is the number of nodes
# r is the radius
# k is the number of random edges
def WS2DGraph(n, r, k):
  line = int(math.sqrt(n))
  graph = dict()
  #Initialization
  for i in range(n):
    x = random.random()
    y = random.random()
    graph[i] = dict()
    graph[i]["x"] = x*line
    graph[i]["y"] = y*line
    graph[i]["list"] = set()

  #For each node u, we add an edge to each node at distance at most r from u
  for i in range(n):
    for j in range(i+1,n):
      dist=math.sqrt((graph[i]["x"]-graph[j]["x"])**2 + (graph[i]["y"]-graph[j]["y"])**2) # Eclidean distance between i and j
      if dist <= r:
        graph[i]["list"].add(j)
        graph[j]["list"].add(i)

      #For each node u, we add an edge to k randomly chosen nodes
    for h in range(k):
      s = random.randint(0,n-1)
      if s != i:
        graph[i]["list"].add(s)
        graph[s]["list"].add(i)
  return graph


" WS2D"
def WS2DDirectGraph(n, r, k, m):
  line = int(math.sqrt(n))
  graph = dict()
  graphToReturn = dict()
  #Initialization
  for i in range(n):
    x = random.random()
    y = random.random()
    graph[i] = dict()
    graphToReturn[i] = set()
    graph[i]["x"] = x*line
    graph[i]["y"] = y*line

  #For each node u, we add an edge to each node at distance at most r from u
  while m > 0:
      i = random.randint(0, n-1)
      for j in range(n):
        if i != j and j not in graphToReturn[i]:
          dist = math.sqrt((graph[i]["x"]-graph[j]["x"])**2 + (graph[i]["y"]-graph[j]["y"])**2) # Eclidean distance between i and j
          if dist <= r:
            graphToReturn[i].add(j)
            m -= 1
            if m == 0:
              return graphToReturn
      #For each node u, we add an edge to k randomly chosen nodes
      for h in range(random.choice(list(k))):
        # s = random.randint(0,n-1)
        while True:
          s = random.randint(0,n-1)
          if s not in graph[i] and s!=i:
            break
        graphToReturn[i].add(s)
        m -= 1
        if m == 0:
          return graphToReturn
  return graphToReturn

">>>>>>  generalizedWS <<<<<<<"
def generalizedWS(n, r, k, m, clustering_exp=2):
  line = int(math.sqrt(n))
  graph = dict()


  #Initialization
  for i in range(line): #i represents the grid row
    for j in range(line): #j represents the grid coloumn
      graph[i*line+j] = set() #Each node is identified by a number in [0, n - 1]

  #For each node u, we add an edge to each node at distance at most r from u
  while m > 0:
    i = random.randint(0, line-1)
    for j in range(line):
        for x in range(r+1): # x is the horizontal offset
          for y in range(r+1-x): # y is the vertical offset. The sum of offsets must be at most r
           if x+y > 0: # the sum of offsets must be at least 1
             if i+x < line: # check for not going out the grid
               if j+y < line and (i+x)*line+(j+y) not in graph[i*line+j]:
                 graph[i*line+j].add((i+x)*line+(j+y))
                 m -= 1
                 if m == 0:  
                   return graph
               if j-y >= 0 and (i+x)*line+(j-y)  not in graph[i*line+j]:
                 graph[i*line+j].add((i+x)*line+(j-y))
                 m -= 1
                 if m == 0:    
                   return graph  
             if i-x >= 0:
               if j+y < line and (i-x)*line+(j+y) not in graph[i*line+j]:
                 graph[i*line+j].add((i-x)*line+(j+y))
                 m -= 1
                 if m == 0:
                   return graph
               if j-y >= 0 and (i-x)*line+(j-y) not in graph[i*line+j]:
                 graph[i*line+j].add((i-x)*line+(j-y))
                 m -= 1
                 if m == 0:
                   return graph

        for h in range(random.choice(list(k))):
          # s = random.randint(0,n-1)
          while True:
            s = random.randint(0,n-1)
            if s in graph[i*line+j] or s==i*line+j:
            	continue
            x = s / line
            y = s % line
            dist = math.sqrt((x-i)**2 + (y-j)**2) # Eclidean distance
           
            num_rand = random.random()
 
            p = 1/math.pow(dist, clustering_exp)

            if num_rand <=p:
              break
   
          graph[i*line+j].add(s)
          m -= 1
          if m == 0:
            return graph

  return graph  


" WS2D double for"
# def WS2DDirectGraph(n, r, k, m):
#   line = int(math.sqrt(n))
#   graph = dict()
#   graphToReturn = dict()
#   edges = 0
#   #Initialization
#   for i in range(n):
#     x = random.random()
#     y = random.random()
#     graph[i] = dict()
#     graphToReturn[i] = set()
#     graph[i]["x"] = x*line
#     graph[i]["y"] = y*line
#   #For each node u, we add an edge to each node at distance at most r from u
#   for i in range(n):
#     for j in range(i+1,n):
#       dist=math.sqrt((graph[i]["x"]-graph[j]["x"])**2 + (graph[i]["y"]-graph[j]["y"])**2) # Eclidean distance between i and j
#       if dist <= r:
#         graphToReturn[i].add(j)
#         edges += 1
 
#       #For each node u, we add an edge to k randomly chosen nodes
#     for h in range(random.choice(k)):
#       s = random.randint(0,n-1)
#       if s not in graph[i] and s!=i:
#         graphToReturn[i].add(s)
#         edges += 1

#   if m[0] < edges < m[1]:
#     print "NUM: EDGES ", edges
#     return graphToReturn  
#   else:
#     print "Not a good graph - NUM: EDGES ", edges
#     WS2DDirectGraph(n, r, k, m)

">>>>>>  generalizedWS double for <<<<<<<"
# def generalizedWS(n, r, k, m, clustering_exp=2):
#   line = int(math.sqrt(n))
#   graph = dict()
#   edges = 0
#   #Initialization
#   for i in range(line): #i represents the grid row
#     for j in range(line): #j represents the grid coloumn
#       graph[i*line+j] = set() #Each node is identified by a number in [0, n - 1]

#   #For each node u, we add an edge to each node at distance at most r from u
#   for i in range(line):
#     for j in range(line):
#       for x in range(r+1): # x is the horizontal offset
#         for y in range(r+1-x): # y is the vertical offset. The sum of offsets must be at most r
#          if x+y > 0: # the sum of offsets must be at least 1
#            if i+x < line: # check for not going out the grid
#              if j+y < line and (i+x)*line+(j+y) not in graph[i*line+j]:
#                graph[i*line+j].add((i+x)*line+(j+y))
#                edges += 1
#              if j-y >= 0 and (i+x)*line+(j-y)  not in graph[i*line+j]:
#                graph[i*line+j].add((i+x)*line+(j-y))    
#                edges += 1
#            if i-x >= 0:
#              if j+y < line and (i-x)*line+(j+y) not in graph[i*line+j]:
#                graph[i*line+j].add((i-x)*line+(j+y))
#                edges += 1
#              if j-y >= 0 and (i-x)*line+(j-y) not in graph[i*line+j]:
#                graph[i*line+j].add((i-x)*line+(j-y))
#                edges += 1
#               # print "EDGES ",edges
#             # We do not consider(i+x,j-y) (i-x,j+y) and (i-x,j-y) since the edge between these nodes and (i,j) has been already added at previous iterations

#       # For each node u, we add a node to k randomly chosen nodes
#       for h in range(random.choice(k)):
#         s = random.randint(0,n-1)
#         # if i>80:
#         #   print "i: ", i, " s: ",s, " Edges: ",edges
#         if s not in graph[i*line+j] and s!=i*line+j:
#             # else:
#             # 	print "Blocked - EDGES: ", edges, " S ",s 
#           x = s / line
#           y = s % line
#           dist = math.sqrt((x-i)**2 + (y-j)**2) # Eclidean distance
           
#           num_rand = random.random()

#           p = 1/math.pow(dist, clustering_exp)
           
#           if num_rand <= p:          
#             graph[i*line+j].add(s)
#             edges += 1
#             # print "EDGES ",edges

#   if m[0] < edges < m[1]:
#     print "NUM: EDGES ", edges
#     return graph  
#   else:
#     print "Not a good graph - NUM: EDGES ", edges
#     generalizedWS(n, r, k, m)        


def countEdges(graph):
  edges=0
  for i in graph.keys():
    edges += len(graph[i])
  return int(edges/2)

def countEdgesDirect(graph):
  edges=0
  for i in graph.keys():
    edges += len(graph[i])
  return edges




# def generalizedWS(n, r, k, clustering_exp=2):
#   line = int(math.sqrt(n))
#   graph = dict()

#   #Initialization
#   for i in range(line): #i represents the grid row
#     for j in range(line): #j represents the grid coloumn
#       graph[i*line+j] = set() #Each node is identified by a number in [0, n - 1]

#   #For each node u, we add an edge to each node at distance at most r from u
#   for i in range(line):
#     for j in range(line):
#       for x in range(r+1): # x is the horizontal offset
#         for y in range(r+1-x): # y is the vertical offset. The sum of offsets must be at most r
#           if x + y > 0: # The sum of offsets must be at least 1
#             if i + x < line and j + y < line: 
#               graph[i*line+j].add((i+x)*line+(j+y))
#               #graph[(i+x)*line+(j+y)].add(i*line+j)
#             # We do not consider(i+x,j-y) (i-x,j+y) and (i-x,j-y) since the edge between these nodes and (i,j) has been already added at previous iterations

#       for h in range(k):
#       	# while True:
#        #  	s = random.randint(0,n-1)
#        #  	if s in graph[i*line+j]
#        #  		break
#         if s != i*line+j:
#           x = s / line
#           y = s % line
#           print "s: ",s," x: ",x," y: ",y
#           dist = math.sqrt((x-i)**2 + (y-j)**2) # Eclidean distance
#           num_rand = random.random()

#           p = 1/math.pow(dist, clustering_exp)
          
#           if num_rand <= p:
          	
#             print "Dist: ", dist ," Num rand: ",num_rand," p: ",p
#             graph[i*line+j].add(s)

#   return graph  





# def WS2DDirectGraph(n, r, k):
#   line = int(math.sqrt(n))
#   graph = dict()
#   #Initialization
#   for i in range(n):
#     x = random.random()
#     y = random.random()
#     graph[i] = dict()
#     graph[i]["x"] = x*line
#     graph[i]["y"] = y*line
#     graph[i]["list"] = set()

#   #For each node u, we add an edge to each node at distance at most r from u
#   for i in range(n):
#     for j in range(i+1,n):
#       dist=math.sqrt((graph[i]["x"]-graph[j]["x"])**2 + (graph[i]["y"]-graph[j]["y"])**2) # Eclidean distance between i and j
#       if dist <= r:
#         graph[i]["list"].add(j)
#         graph[j]["list"].add(i)

#       #For each node u, we add an edge to k randomly chosen nodes
#     for h in range(k):
#       s = random.randint(0,n-1)
#       if s != i:
#         graph[i]["list"].add(s)
#   return graph