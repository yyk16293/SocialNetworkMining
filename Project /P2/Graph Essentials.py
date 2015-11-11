#__author__ = 'yykishore'

#reference:
#https://networkx.github.io/documentation/latest/tutorial/tutorial.html
#power law graph out degree slope: -1.88556578332
#power law graph out degree intercept: 9.27420111098
#power law graph indegree slope: -0.614755050667
#power law graph indegree intercept: 3.96815578899

import networkx as netx
import random
import numpy
import matplotlib.pylab as pylab

def calc_diameter(G,file_name):
    G = netx.Graph()
    constructGraph(G,file_name)
    print("diameter is " + str(netx.diameter(G)))

def countCycles(G,file_name):
    G = netx.Graph()
    count_cycles = 0
    constructGraph(G,file_name)
    cycles_list = netx.cycle_basis(G)##returns of list of all cycles in the graph

    for verticecycle in cycles_list:
        if len(verticecycle) == 3:
            count_cycles += 1

    print("No. of 3-cycles is " + str(count_cycles))

def countBridges(G,file_name):
    G = netx.Graph()
    count_bridges = 0
    constructGraph(G,file_name)

    edgeList = G.edges()
    orig_connec_compnts = netx.number_connected_components(G)

    for edge in edgeList:
        G.remove_edge(edge[0],edge[1])
        present_connec_compnts = netx.number_connected_components(G)
        if present_connec_compnts == orig_connec_compnts+1:
            count_bridges = count_bridges +1
        G.add_edge(edge[0],edge[1])

    print("No. of bridges is" + str(count_bridges))

def powerLawDistOutDegree(G,file_name):

    fp_outdegree = open('power_outdegree.csv','w')
    dir_G = netx.DiGraph()
    constructGraph(dir_G,file_name)

    out_degree_dict = dir_G.out_degree()

    sorted_list = sorted(out_degree_dict.items(), key=lambda x: x[1],reverse=True)
    #print sorted_list
    interchanged_sorted_list = [(t[1], t[0]) for t in sorted_list]
    #print interchanged_sorted_list

    item_count_dict = {}
    for item in interchanged_sorted_list:
        if item[0] in item_count_dict:
            item_count_dict[item[0]] += 1
        else:
            item_count_dict[item[0]] = 1

    #print item_count_dict

    degree_list = []
    frequency_list = []

    for key in sorted(item_count_dict):
        degree_list.append(key)
        frequency_list.append(item_count_dict[key])

    degree_list[0] = degree_list[1]
    frequency_list[0] = frequency_list[1]


    for i in range(1,len(degree_list)):
        fp_outdegree.write(str(degree_list[i]) + "," + str(frequency_list[i]) + "\n")
    fp_outdegree.close()

    #print degree_list
    #print frequency_list

    power_graph = numpy.polyfit(numpy.log(degree_list),numpy.log(frequency_list),1)
    slope, intercept = power_graph
    print "power law graph out degree slope: "  + str(slope)
    print "power law graph out degree intercept: "  + str(intercept)


def powerLawDistInDegree(G,file_name):

    fp_indegree = open('power_indegree.csv','w')
    dir_G = netx.DiGraph()
    constructGraph(dir_G,file_name)

    out_degree_dict = dir_G.in_degree()

    sorted_list = sorted(out_degree_dict.items(), key=lambda x: x[1],reverse=True)
    #print sorted_list
    interchanged_sorted_list = [(t[1], t[0]) for t in sorted_list]
    #print interchanged_sorted_list

    item_count_dict = {}
    for item in interchanged_sorted_list:
        if item[0] in item_count_dict:
            item_count_dict[item[0]] += 1
        else:
            item_count_dict[item[0]] = 1

    #print item_count_dict

    degree_list = []
    frequency_list = []

    for key in sorted(item_count_dict):
        degree_list.append(key)
        frequency_list.append(item_count_dict[key])

    degree_list[0] = degree_list[1]
    frequency_list[0] = frequency_list[1]
    #degree_list.append(0.1)
    #frequency_list.append(0.1)


    frequency_list = frequency_list[::-1]
    #for i in range(1,len(degree_list)):
     #   degree_list[i] += 1

    for i in range(1,len(degree_list)):
        fp_indegree.write(str(degree_list[i]) + "," + str(frequency_list[i])+"\n")

    fp_indegree.close()
    #print degree_list
    #print frequency_list
    #print len(degree_list),len(frequency_list)

    power_law_graph = numpy.polyfit(numpy.log(degree_list),numpy.log(frequency_list),1)
    slope, intercept = power_law_graph
    print "power law graph indegree slope: "  + str(slope)
    print "power law graph indegree intercept: "  + str(intercept)

def constructGraph(G,file_name):
    fp_anon = open(file_name,'r')

    for line in fp_anon:
        stripped_line = line.strip()
        vertices = stripped_line.split(',')
        G.add_edge(int(vertices[0]), int(vertices[1]))
        #print vertices[0], vertices[1]

    fp_anon.close()

G = netx.Graph()
file_name = 'vertices_output.csv'

constructGraph(G,file_name)
calc_diameter(G,file_name)
countCycles(G,file_name)
countBridges(G,file_name)
powerLawDistOutDegree(G,file_name)
powerLawDistInDegree(G,file_name)

#Diameter is 6
#No. of 3-cycles is 9135
#No. of bridges is12234


