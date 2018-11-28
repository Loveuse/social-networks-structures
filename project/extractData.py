from __future__ import division
import sys
import csv


def extract(keyword, path, randomG):

	PATHNAME = path

	filename = open(PATHNAME, 'r')

	lines = filename.readlines()

	k = -1
	graphInfo = dict()
	
	with open("out/"+keyword+'.csv', 'wb') as csvfile:

		writer = csv.writer(csvfile, delimiter=',')
		if randomG:
			writer.writerow(["Avgc", "", "Betweenness", "", "", "", "", "", "Eigenvector", "", "", "", "", "", "PageRank", "", "", "", ""])
			writer.writerow([ "", "", "Seed", "25%", "50%", "75%", "100%", "", "Seed", "25%", "50%", "75%", "100%" ,"", "Seed", "25%", "50%", "75%", "100%" ])
		else:
			writer.writerow(["Avgc", "", "Betweenness", "", "", "Eigenvector", "", "", "PageRank",""])
			writer.writerow(["", "", "Seed", "Influenced", "", "Seed", "Influenced", "", "Seed", "Influenced"])
		i = 0
		while i < len(lines):
			if lines[i].startswith("----- "):
				k += 1
				if k!=0:
					if not randomG:
						writer.writerow([
							graphInfo[k-1]['avgc'], 
							"", 
							graphInfo[k-1]["Betweenness"]["seed"], 
							graphInfo[k-1]["Betweenness"]["Influenced"],  						
							"", 
							graphInfo[k-1]["Eigenvector"]["seed"], 
							graphInfo[k-1]["Eigenvector"]["Influenced"], 
							"", 
							graphInfo[k-1]["PageRank"]["seed"], 
							graphInfo[k-1]["PageRank"]["Influenced"] 
						])
					else:
						writer.writerow([
							graphInfo[k-1]['avgc'], 
							"", 
							graphInfo[k-1]["Betweenness"]["seed"], 
							graphInfo[k-1]["Betweenness"]["25"],
							graphInfo[k-1]["Betweenness"]["50"],
							graphInfo[k-1]["Betweenness"]["75"],
							graphInfo[k-1]["Betweenness"]["100"] if "100" in graphInfo[k-1]["Betweenness"] else "",  						
							"", 
							graphInfo[k-1]["Eigenvector"]["seed"], 
							graphInfo[k-1]["Eigenvector"]["25"],
							graphInfo[k-1]["Eigenvector"]["50"],
							graphInfo[k-1]["Eigenvector"]["75"],
							graphInfo[k-1]["Eigenvector"]["100"] if "100" in graphInfo[k-1]["Eigenvector"] else "",
							"", 
							graphInfo[k-1]["PageRank"]["seed"], 
							graphInfo[k-1]["PageRank"]["25"],
							graphInfo[k-1]["PageRank"]["50"],
							graphInfo[k-1]["PageRank"]["75"],
							graphInfo[k-1]["PageRank"]["100"] if "100" in graphInfo[k-1]["PageRank"] else ""
						])
				if i == len(lines)-1:
					break
				graphInfo[k] = dict()
				graphInfo[k]['m'] = lines[i].split("m: ")[1].split(" ")[0]
				graphInfo[k]['avgc'] = lines[i].split("avgc: ")[1].split(" ")[0]
				i += 1
			elif lines[i].startswith("####"):
				centrality = lines[i].split("##### ")[1].split(" ")[0]
				graphInfo[k][centrality] = dict()
				i += 1
				if randomG:
					while not (lines[i].startswith("###") or lines[i].startswith("-----")):
						i += 1
					while not lines[i].startswith("Influenced"):
						i -= 1
					graphInfo[k][centrality]["seed"] = int(lines[i].split("k: ")[1].split(" ")[0])
					i -= 1
					while lines[i].startswith("- "):
						perc = lines[i].split("- ")[1].split("%")[0]

						graphInfo[k][centrality][""+perc+""] = int(lines[i].split(": ")[1]) 
						i -= 1
					i += 1
					while not (lines[i].startswith("###") or lines[i].startswith("-----")):
						i += 1
				else:
					while lines[i].startswith("Influenced"):
						i += 1
					graphInfo[k][centrality]["Influenced"] = lines[i-1].split("Influenced: ")[1].split(" ")[0]
					graphInfo[k][centrality]["seed"] = int(lines[i-1].split("k: ")[1].split(" ")[0])
	
			else:
				break
			

	csvfile.close()

	return graphInfo




def getMeans(graphInfo, centrality):
	keys = graphInfo.keys()

	meanInfluenced = sum([ v[centrality][Influenced] for _,v in graphInfo.items()]) / len(keys)
	meanAvgc = 	sum([ v["avgc"] for _,v in graphInfo.items()])/len(keys)

	tops = dict()
	for _,v in graphInfo.items():
		for k in v[centrality]:
			if k["seed"] not in tops:
				tops[k["seed"]] = []
			tops[k[seed]].append(k["Influenced"])

	for k,v in tops.items():
		tops[k] = sum([ j in v ]) / len(keys)
	return meanInfluenced, tops, meanAvgc
	# meansM = sum([ v["m"] for _,v in graphInfo.items()])/len(keys)

# inFile = sys.argv[1]
# keyword = sys.argv[2]
# outFile = sys.argv[3] # da vedere come generare grafici
# extract(keyword, inFile, True)

