​given_array​ ​=​ [​1​, ​2​, ​4​, ​12​, ​6​, ​11​, ​43​, ​8​, ​76​, ​44​] 
 ​required_sum​ ​=​ ​5 
  
 ​pairs​=​[] 
 ​for​ ​indexi​, ​elementi​ ​in​ ​enumerate​(​given_array​): 
 ​    ​for​ ​indexj​, ​elementj​ ​in​ ​enumerate​(​given_array​): 
 ​        ​summ​ ​=​ ​elementi​+​elementj 
 ​        ​if​ ​summ​ ​==​ ​required_sum​: 
 ​            ​pairs​.​append​((​indexi​, ​indexj​)) 
  
 ​print​(​pairs​) 
