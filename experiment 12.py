​string​ ​=​'apple mango apple orange orange apple apple guava mango mango' 
 ​str_lst​=​string​.​split​() 
  
 ​WordCount​=​{} 
 ​count​=​0 
 ​for​ ​key​ ​in​ ​str_lst​: 
 ​    ​if​ ​key​ ​not​ ​in​ ​WordCount​.​keys​(): 
 ​        ​WordCount​[​key​]​=​1 
 ​    ​else​: 
 ​        ​WordCount​[​key​]​+=​1 
  
 ​maxx​=​0 
 ​max_key​=​'' 
 ​for​ ​element​ ​in​ ​WordCount​.​items​(): 
 ​    ​key​, ​value​ ​=​ ​element 
 ​    ​if​ ​value​>​maxx​: 
 ​        ​maxx​=​value 
 ​        ​max_key​=​key​       
  
 ​print​(​f"Word with maximum number of occurence is ​{​max_key​}​ with no of occurence = ​{​maxx​}​"​)
