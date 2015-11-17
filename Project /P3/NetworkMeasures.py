#__author__ = 'yykishore'

import networkx as netx
import operator
import scipy.stats as spy

def localClusteringCoefficient(file_name):
    graph = netx.Graph()
    constructGraph(graph,file_name)
    print("local clustering coefficient is" + str(netx.clustering(graph)))

def globalClusteringCoefficient(file_name):
    graph = netx.Graph()
    constructGraph(graph,file_name)
    print("global clustering coefficient is " + str(netx.average_clustering(graph)))

def eigenVectorCentrality(file_name):
    G = netx.DiGraph()
    constructGraph(G,file_name)

    EigenVectorCentrality = netx.eigenvector_centrality(G)
    #print EigenVectorCentrality

    #sorting by values of the dictionary and storing
    sorted_EigenVectorCentrality = sorted(EigenVectorCentrality.items(), key=operator.itemgetter(1),reverse=True)
    #print sorted_EigenVectorCentrality

    print("EigenVectorCentrality values are")
    top_ten_limit = 10
    for top_count in range(0,top_ten_limit):
        print sorted_EigenVectorCentrality[top_count]
        top_ten_eigen.append(sorted_EigenVectorCentrality[top_count][1])

def pageRankCentrality(file_name):
    G = netx.DiGraph()
    constructGraph(G,file_name)

    PageRankCentrality = netx.pagerank(G)
    sorted_PageRankCentrality = sorted(PageRankCentrality.items(), key=operator.itemgetter(1),reverse=True)

    print("pageRankCentrality values are")
    top_ten_limit = 10
    for top_count in range(0,top_ten_limit):
        print sorted_PageRankCentrality[top_count]
        top_ten_page.append(sorted_PageRankCentrality[top_count][1])

def degreeCentrality(file_name):
    G = netx.DiGraph()
    constructGraph(G,file_name)

    degreeCentrality = netx.degree_centrality(G)
    sorted_degreeCentrality = sorted(degreeCentrality.items(),key=operator.itemgetter(1),reverse=True)

    print("Centrality values are")
    top_ten_limit = 10
    for top_count in range(0,top_ten_limit):
        print sorted_degreeCentrality[top_count]
        top_ten_centrality.append(sorted_degreeCentrality[top_count][1])


def rankCorrelation():

    EigenPageCorr = spy.pearsonr(top_ten_eigen,top_ten_page)
    print("Eigen Page Rank Correlation:: " + str(EigenPageCorr[0]))

    EigenDegreeCorr = spy.pearsonr(top_ten_eigen,top_ten_centrality)
    print("Eigen Degree Correlation:: " + str(EigenDegreeCorr[0]))

    DegreePageCorr = spy.pearsonr(top_ten_centrality,top_ten_page)
    print("Degree PageRank Correlation:: " + str(DegreePageCorr[0]))

def jaccardSimilarity(file_name):
    G = netx.Graph()
    constructGraph(G,file_name)

    jaccard_values = netx.jaccard_coefficient(G)
    print type(jaccard_values)

    maxOne = 0
    maxTwo = 0
    total_count = 0

    for val in jaccard_values:

            if (maxOne < val[2]):
                maxTwo = maxOne
                maxOne = val[2]
            elif (maxTwo < val[2]):
                maxTwo = val[2]

            if maxOne == 1:
                break

    print maxOne,maxTwo

    #for i in jaccard_values:
     #   print i
    #print(jaccard_values)

def constructGraph(G,file_name):
    fp_anon = open(file_name,'r')

    for line in fp_anon:
        stripped_line = line.strip()
        vertices = stripped_line.split(',')
        G.add_edge(int(vertices[0]), int(vertices[1]))
        #print vertices[0], vertices[1]

    fp_anon.close()


g = netx.Graph()
#file_name = 'anonymized_vertices_big.csv'
file_name = 'vertices_output.csv'
#file_name = 'names_output.csv'
top_ten_eigen = []
top_ten_page = []
top_ten_centrality = []

localClusteringCoefficient(file_name)
globalClusteringCoefficient(file_name)
eigenVectorCentrality(file_name)
pageRankCentrality(file_name)
degreeCentrality(file_name)
rankCorrelation()
jaccardSimilarity(file_name)

#jaccard 1.0 0.5 max min


#print top_ten_eigen
#print top_ten_page
#print top_ten_centrality
