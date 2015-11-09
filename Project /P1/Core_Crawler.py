#__author__ = 'yykishore'

#__author__ = 'yykishore'

import requests
import time

root_id = 5064613
def_page_start_number = 1
global_count = 0 #total no. of nodes visited
max_limit = 1004
#max_limit = 1010
#maximum no. of nodes to be visited

#initializing with the root node
global_node_array = [] #contains names
global_url_array = []
global_nodeId_array = []
global_vertices_array = []

#SudheerVazrapu
#26363285

global_node_array.append('YoganandaKishore')
global_nodeId_array.append(5064613)

global_url_ids = []
max_local_count = 15
nodes_left = True
url_first_part = 'https://independent.academia.edu/v0/profiles/user_relation?subdomain_param=api&id='
url_middle_part = '&type=followers&page='
present_id = root_id
present_node = 0
present_count = 1
max_each_node_count = 60

file_out = open('names_output.csv','w')
file2_out = open('vertices_output.csv','w')
file3_out = open('names_nums.csv','w')

while(global_count < max_limit):
    nodes_left = True
    def_page_start_number = 1
    present_id = global_nodeId_array[global_count]
    each_node_count = 0

    while(nodes_left):
        try:
            response = requests.get(url_first_part + str(present_id) + url_middle_part + str(def_page_start_number))
        except:
            time.sleep(3)
            continue

        json_data = response.json()

        if(len(json_data) < max_local_count):
            nodes_left = False

        each_node_count += len(json_data)

        if each_node_count > max_each_node_count:
            break

        for i in range(0,len(json_data)):

            name_display = json_data[i]['page_name']
            node_id = json_data[i]['id']
            formatted_name = name_display.encode('ascii','ignore')

            if node_id not in global_nodeId_array:
                global_node_array.append(formatted_name)
                global_nodeId_array.append(node_id)

                #file1_out.write(str(node_id) + "," + str(global_nodeId_array[global_count]) + "\n")
                print node_id,global_nodeId_array[global_count]

                present_count += 1
                present_node = present_count
            else:
                #get index of the repeated element
                repeated_node_index = global_nodeId_array.index(node_id)
                present_node = repeated_node_index + 1

            file2_out.write(str(present_node) + "," + str(global_count+1)+ "\n")
            print present_node,global_count+1

            file_out.write(str(formatted_name) + "," + str(global_node_array[global_count]) + "\n")
            print str(formatted_name),str(global_node_array[global_count])


        def_page_start_number += 1

    global_count += 1

file_out.close()
file2_out.close()

for i in range(0,present_node):
    print global_node_array[i],i+1
    file3_out.write(str(global_node_array[i]) + "," + str(i+1) + "\n")

print len(global_node_array)
file3_out.close()



