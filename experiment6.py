nodesArray​ ​=​ [ 
 ​                [​0​,         ​3​,          ​float​(​'inf'​),   ​7​],  
 ​                [​8​,         ​0​,          ​2​,              ​float​(​'inf'​)],  
 ​                [​5​,    ​float​(​'inf'​),    ​0​,              ​1​],  
 ​                [​2​,    ​float​(​'inf'​),    ​float​(​'inf'​),   ​0​], 
 ​            ]  
  
 ​# print(nodesArray) 
  
 ​for​ ​k​ ​in​ ​range​(​len​(​nodesArray​)): 
 ​    ​for​ ​i​ ​in​ ​range​(​len​(​nodesArray​)): 
 ​        ​for​ ​j​ ​in​ ​range​(​len​(​nodesArray​)): 
 ​            ​nodesArray​[​i​][​j​] ​=​ ​min​(​nodesArray​[​i​][​j​], ​nodesArray​[​i​][​k​]​+​nodesArray​[​k​][​j​]) 
  
 ​for​ ​row​ ​in​ ​nodesArray​: 
 ​    ​for​ ​element​ ​in​ ​row​: 
 ​        ​print​(​element​, ​end​=​" "​) 
 ​    ​print​(​""​)     
  
 ​# print(nodesArray)
