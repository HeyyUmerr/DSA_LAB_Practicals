given_array​ ​=​ [​1​, ​2​, ​4​, ​12​, ​6​, ​11​, ​43​, ​8​, ​76​, ​44​] 
  
 ​max1​ ​=​ ​max2​ ​=​ ​given_array​[​0​] 
  
 ​for​ ​i​ ​in​ ​given_array​: 
 ​    ​if​ ​i​>​max1​: 
 ​        ​max1​=​i 
  
 ​for​ ​i​ ​in​ ​given_array​: 
 ​    ​if​ ​i​ ​!=​ ​max1​: 
 ​        ​if​ ​i​>​max2​: 
 ​            ​max2​=​i 
  
 ​print​(​f"max possible product is ​{​max1​*​max2​}​"​)     
