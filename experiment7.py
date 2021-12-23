# A class to represent the adjacency list of the node 
 ​class​ ​AdjNode​: 
 ​        ​def​ ​_init_​(​self​, ​data​): 
 ​                ​self​.​vertex​ ​=​ ​data 
 ​                ​self​.​next​ ​=​ ​None 
  
  
 ​# A class to represent a graph. A graph 
 ​# is the list of the adjacency lists. 
 ​# Size of the array will be the no. of the 
 ​# vertices "V" 
 ​class​ ​Graph​: 
 ​        ​def​ ​_init_​(​self​, ​vertices​): 
 ​                ​self​.​V​ ​=​ ​vertices 
 ​                ​self​.​graph​ ​=​ [​None​] ​*​ ​self​.​V 
  
 ​        ​# Function to add an edge in an undirected graph 
 ​        ​def​ ​add_edge​(​self​, ​src​, ​dest​):​#0 1 
 ​                ​# Adding the node to the source node 
 ​                ​node​ ​=​ ​AdjNode​(​dest​) ​# node = 1 
 ​                ​node​.​next​ ​=​ ​self​.​graph​[​src​]  
 ​                ​self​.​graph​[​src​] ​=​ ​node 
 ​     
 ​                ​# Adding the source node to the destination as 
 ​                ​# it is the undirected graph 
 ​                ​node​ ​=​ ​AdjNode​(​src​) 
 ​                ​node​.​next​ ​=​ ​self​.​graph​[​dest​] 
 ​                ​self​.​graph​[​dest​] ​=​ ​node 
 ​     
 ​        ​# Function to print the graph 
 ​        ​def​ ​print_graph​(​self​): 
 ​                ​for​ ​i​ ​in​ ​range​(​self​.​V​): 
 ​                        ​print​(​"Adjacency list of vertex {}​\n​ head"​.​format​(​i​), ​end​=​""​) 
 ​                        ​temp​ ​=​ ​self​.​graph​[​i​] 
 ​                        ​while​ ​temp​: 
 ​                                ​print​(​" -> {}"​.​format​(​temp​.​vertex​), ​end​=​""​) 
 ​                                ​temp​ ​=​ ​temp​.​next 
 ​                        ​print​(​" ​\n​"​) 
  
 ​def​ ​is_strongly_connected​(​adjacency_list​, ​no_of_nodes​): 
 ​    ​first​ ​=​ ​adjacency_list​[​0​] 
 ​    ​temp​ ​=​ ​first 
 ​    ​count​ ​=​ ​no_of_nodes 
 ​     
 ​    ​while​ ​temp​: 
 ​        ​count​ ​=​ ​count​-​1 
 ​        ​temp​ ​=​ ​temp​.​next 
 ​     
 ​    ​if​ ​count​!=​0​: 
 ​        ​return​ ​False 
  
 ​    ​for​ ​index​ ​in​ ​range​(​1​, ​no_of_nodes​+​1​): 
 ​        ​temp​=​adjacency_list​[​index​]  
 ​        ​count​ ​=​ ​no_of_nodes 
  
 ​        ​while​ ​temp​: 
 ​            ​temp​ ​=​ ​temp​.​next 
 ​            ​count​ ​-=​ ​1 
 ​         
 ​        ​if​ ​count​>​0​: 
 ​            ​return​ ​False 
  
 ​    ​return​ ​True 
  
 ​V​ ​=​ ​5 
 ​grh​ ​=​ ​Graph​(​V​) 
 ​grh​.​add_edge​(​0​, ​1​) 
 ​grh​.​add_edge​(​0​, ​4​) 
 ​grh​.​add_edge​(​1​, ​2​) 
 ​grh​.​add_edge​(​1​, ​3​) 
 ​grh​.​add_edge​(​1​, ​4​) 
 ​grh​.​add_edge​(​2​, ​3​) 
 ​grh​.​add_edge​(​3​, ​4​) 
 ​# grh.add_edge(0, 1) 
 ​# grh.add_edge(0, 2) 
 ​# grh.add_edge(1, 2) 
 ​# grh.add_edge(2, 1) 
  
  
  
  
 ​print​(​is_strongly_connected​(​grh​.​graph​, ​V​-​1​))
