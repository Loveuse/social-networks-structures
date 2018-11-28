#!/usr/bin/python

import random
import math

# nomefile is the name of the file to read
def readGraph(nomefile):
  infile = open(nomefile,"r")
  graph = dict()
  for line in infile:
    if "#" not in line:
      u,v = line.split()
      if u not in graph:
        graph[u] = set()
      graph[u].add(v)
      if v not in graph:
        graph[v] = set()
      graph[v].add(u)
  return graph

# nomefile is the name of the file to read
def readDirectGraph(nomefile):
  m = 0
  infile = open(nomefile,"r")
  graph = dict()
  for line in infile:
    if "#" not in line:
      u,v = line.split()
      if u not in graph:
        graph[u] = set()
      graph[u].add(v)
      m += 1
      if v not in graph:
      	graph[v] = set()
  return graph, m

# Return the largest shortest path and the number of nodes and edges of the largest component
def diameter(graph):
  n = len(graph)
  nodes = 0
  edges = 0
  diameter = 0
  for i in graph.keys():
    visited = []
    max_distance = 0
    tmp_edge = 0
    queue = [i]
    distance = dict()
    for j in graph.keys():
      distance[j] = -1
    distance[i] = 0
    while queue != []:
      s = queue.pop(0)
      visited.append(s)
      tmp_edge += len(graph[s])
      for j in graph[s]:
        if distance[j] < 0:
          queue.append(j)
          distance[j] = distance[s] + 1
          if distance[j] > max_distance:
            max_distance = distance[j]
    if len(visited) > nodes:
      nodes = len(visited)
      edges = tmp_edge/2
    if max_distance > diameter:
      diameter = max_distance
  return nodes,edges,diameter

# A unique function for counting edges, triangles, length-2 paths and measuring the average clustering
def CounterUtility(graph):
  n = len(graph)
  edges=0
  triangles = 0
  paths = 0
  total=0
  for i in graph.keys():
    edges += len(graph[i])
    neigh_pairs = (len(graph[i])*(len(graph[i])-1))/2
    closed_pairs = 0
    for j in graph[i]:
      for k in graph[j]:
        if k != i:
          paths += 1
        if k in graph[i]:
          closed_pairs += 1
    triangles += closed_pairs
    if neigh_pairs > 0:
      total += float(closed_pairs)/(2*neigh_pairs)
  return int(edges/2), int(triangles/6), int(paths/2), float(total)/n