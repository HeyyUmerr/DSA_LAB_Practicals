​Alpa​ ​=​ [​''​, ​'A'​, ​'B'​, ​'C'​, ​'D'​, ​'E'​, ​'F'​, ​'G'​, ​'H'​, ​'I'​, ​'J'​, ​'K'​, ​'L'​, ​'M'​, ​'N'​, ​'O'​, ​'P'​, ​'Q'​, ​'R'​, ​'S'​, ​'T'​, ​'U'​, ​'V'​, ​'W'​, ​'X'​, ​'Y'​, ​'Z'​] 
  
 ​Array​ ​=​ [​1​, ​2​, ​2​, ​1​] ​#  ABBA, NB 
 ​Pair​ ​=​ [] 
  
  
 ​for​ ​i​ ​in​ ​range​(​len​(​Array​)​-​1​): 
 ​    ​num​ ​=​ ​int​(​str​(​Array​[​i​])​+​str​(​Array​[​i​+​1​]))   
 ​    ​Combo​ ​=​ []   
 ​     
 ​    ​j​=​0 
 ​    ​while​ ​j​ ​<​ ​len​(​Array​): 
 ​        ​if​ ​j​ ​!=​ ​i​ ​and​ ​j​ ​!=​ ​i​+​1​: 
 ​            ​Combo​.​append​(​Array​[​j​])     
 ​            ​j​ ​+=​ ​1 
 ​        ​else​: 
 ​            ​Combo​.​append​(​num​) 
 ​            ​j​ ​+=​ ​2 
 ​        ​if​ ​Combo​ ​not​ ​in​ ​Pair​:    
 ​            ​print​(​Pair​)  
 ​            ​Pair​.​append​(​Combo​) 
  
 ​double​ ​=​ [] 
 ​i​=​0 
 ​while​ ​i​ ​<​ ​len​(​Array​)​-​1​: 
 ​    ​pairs​ ​=​ ​int​(​str​(​Array​[​i​])​+​str​(​Array​[​i​+​1​])) 
 ​    ​double​.​append​(​pairs​) 
 ​    ​i​ ​+=​ ​2​   
  
 ​def​ ​isValid​(​elem​): 
 ​    ​count​ ​=​ ​0 
 ​    ​for​ ​item​ ​in​ ​elem​: 
 ​        ​if​ ​item​<​26​: 
 ​            ​count​ ​+=​ ​1​  
 ​    ​if​ ​count​ ​==​ ​len​(​elem​): 
 ​        ​return​ ​1 
 ​    ​return​ ​0​     
  
 ​def​ ​result​(​item​): 
 ​    ​AlpaList​=​'' 
 ​    ​for​ ​index​ ​in​ ​item​: 
 ​        ​AlpaList​ ​+=​ ​str​(​Alpa​[​index​])  
 ​    ​print​(​AlpaList​)   
  
 ​#printing result 
 ​result​(​Array​) ​#Case:1 
  
 ​for​ ​item​ ​in​ ​Pair​: ​#Case:2 
 ​    ​if​ ​isValid​(​item​): 
 ​        ​result​(​item​) 
  
 ​if​ ​isValid​(​double​): ​#Case:3 
 ​    ​if​ ​len​(​double​)​>​1​: 
 ​        ​result​(​double​)
