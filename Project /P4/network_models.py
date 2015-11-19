#__author__ = 'yykishore'

import networkx as netx
import matplotlib.pylab as pylab
from collections import Counter
import math

def simulateRandomGraph(file_name):
    orig_g = netx.Graph()
    constructGraph(orig_g,file_name)
    largest_compnt = None
    size_largest_compnt = 0
    degreeList = []
    frequencyList = []

    num_edges = orig_g.number_of_edges()
    num_nodes = orig_g.number_of_nodes()

    print "num_nodes is " + str(num_nodes)
    print "num_edges is" + str(num_edges)

    graph_random = netx.gnm_random_graph(num_nodes,num_edges)

    connected_cmpnts = netx.connected_component_subgraphs(orig_g)

    for conn_cmpnt in connected_cmpnts:
        present_size = conn_cmpnt.size()
        if present_size > size_largest_compnt:
            largest_compnt = conn_cmpnt
            size_largest_compnt = present_size

    degree_collection = sorted(graph_random.degree().values(),reverse=True)
    dummy = Counter(degree_collection)

    for val in dummy:
         degreeList.append(val+1)
         frequencyList.append(dummy.get(val))

    print("RandomGraph: Average Path Length: " + str(netx.average_shortest_path_length(largest_compnt)))
    print("RandomGraph: Global Clustering Co-efficient: "+ str(netx.average_clustering(graph_random)))

    pylab.plot(degreeList,frequencyList,marker='.')
    pylab.xlabel("Degree")
    pylab.ylabel("Frequency")
    pylab.title("Degree Distribution-Random Graph")
    pylab.show()

def simulateSmallWorld(file_name):
    orig_g = netx.Graph()
    value = 0
    degreeList = []
    frequencyList = []
    constructGraph(orig_g,file_name)
    total_nodes = orig_g.number_of_nodes()
    degree_list = orig_g.degree().values()
    averageDegree = sum(degree_list)/total_nodes
    # print averageDegree
    #print type(orig_g.degree().values())

    print("total nodes is" + str(total_nodes))
    clusCoeff = (3*(averageDegree))/(4*(averageDegree-1))
    clusP = averageDegree/(total_nodes-1)

    if clusCoeff != 0:
         value = float(clusP)/clusCoeff

    temp = 1 - math.pow(value, 0.333)

    smallWorld = netx.watts_strogatz_graph(total_nodes, int(averageDegree), temp)
    degree_collection = sorted(smallWorld.degree().values(),reverse=True)

    dummy = Counter(degree_collection)
    for val in dummy:
         degreeList.append(val+1)
         frequencyList.append(dummy.get(val))

    print("SmallWorld: Average Path Length: " + str(netx.average_shortest_path_length(smallWorld)))
    print("SmallWorld: Global Clustering Coefficient: "+ str(netx.average_clustering(smallWorld)))

    pylab.plot(degreeList,frequencyList,marker='.')
    pylab.xlabel("Degree")
    pylab.ylabel("Frequency")
    pylab.title("Degree Distribution-Small World")
    pylab.show()

def simulatePreferentialModel(file_name):

    orig_g = netx.Graph()
    constructGraph(orig_g,file_name)
    total_nodes = orig_g.number_of_nodes()
    degreeList = []
    frequencyList = []

    print "total_nodes is " + str(total_nodes)

    prefModel = netx.barabasi_albert_graph(total_nodes,3)
    degree_collection = sorted(prefModel.degree().values(),reverse=True)

    dummy = Counter(degree_collection)
    for val in dummy:
         degreeList.append(val+1)
         frequencyList.append(dummy.get(val))

    print("PrefModel:Average Path Length: " + str(netx.average_shortest_path_length(prefModel)))
    print("PrefModel:Global Clustering Co-efficient: "+ str(netx.average_clustering(prefModel)))

    pylab.plot(degreeList,frequencyList,marker='.')
    pylab.xlabel("Degree")
    pylab.ylabel("Frequency")
    pylab.title("Degree Distribution-Preferential Attachment")
    pylab.show()

def constructGraph(G,file_name):
    fp_anon = open(file_name,'r')

    for line in fp_anon:
        stripped_line = line.strip()
        vertices = stripped_line.split(',')
        G.add_edge(int(vertices[0]), int(vertices[1]))
        #print vertices[0], vertices[1]

    fp_anon.close()

g = netx.Graph()
file_name = 'vertices_output.csv'

simulateRandomGraph(file_name)
simulateSmallWorld(file_name)
simulatePreferentialModel(file_name)