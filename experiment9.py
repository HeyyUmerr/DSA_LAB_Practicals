​arr​=​[​7​, ​6​, ​10​, ​5​, ​9​, ​2​, ​1​, ​15​, ​10​, ​25​, ​7​] 
  
 ​def​ ​MaxMin​(​Arr​, ​Lb​, ​Ub​, ​Max​, ​Min​): 
  
 ​    ​if​  ​Lb​ ​==​ (​Ub​-​1​): 
 ​        ​if​ ​Arr​[​Ub​]​>​Arr​[​Lb​] ​and​ ​Arr​[​Ub​]​>​Max​: ​# Ub bigger  
 ​            ​Max​=​Arr​[​Ub​] 
  
 ​            ​if​(​Arr​[​Lb​]​<​Min​): 
 ​                ​Min​=​Arr​[​Lb​] 
 ​            ​# print(Max, Min)     
 ​            ​return​ ​Max​, ​Min 
 ​        ​else​: 
 ​            ​if​ ​Arr​[​Lb​]​>​Max​: ​# Lb bigger 
 ​                ​Max​=​Arr​[​Lb​]  
 ​                ​if​(​Arr​[​Ub​]​<​Min​): 
 ​                    ​Min​=​Arr​[​Ub​]    
 ​            ​# print(Max, Min) 
 ​            ​return​ ​Max​, ​Min 
  
 ​    ​elif​ ​Ub​ ​==​ ​Lb​: 
 ​        ​if​ ​Arr​[​Ub​]​>​Max​: 
 ​            ​Max​=​Arr​[​Ub​] 
 ​        ​if​ ​Arr​[​Ub​]​<​Min​: 
 ​            ​Min​=​Arr​[​Ub​] 
 ​        ​return​ ​Max​, ​Min 
  
 ​    ​mid​ ​=​ (​Ub​+​Lb​)​//​2 
 ​    ​Max​, ​Min​ ​=​ ​MaxMin​(​Arr​, ​Lb​, ​mid​, ​Max​, ​Min​)     
 ​    ​Max​, ​Min​ ​=​MaxMin​(​Arr​, ​mid​+​1​, ​Ub​, ​Max​, ​Min​)     
 ​    ​return​ ​Max​, ​Min 
  
 ​Max​=​Min​=​arr​[​0​] 
  
 ​Max​, ​Min​ ​=​ ​MaxMin​(​arr​, ​0​, ​len​(​arr​)​-​1​, ​Max​, ​Min​) 
  
  
 ​print​(​Max​, ​Min​)
