#!/usr/bin/env python
# coding: utf-8

# In[1]:



File = open("HarryPotterAndTheSorcerersStone.txt",encoding= 'UTF-8') 


# In[2]:


DictionaryOfWords = {}         #Dictionary mapping every word to a list (of indices of the words' occurences)
Novel = []                     #List of all words in the order, in which they appear!



i = 0                   #Counter Variable to keep track of index of words

for line in File.readlines():     #Iterate over all lines present in the text
 
   line = line.replace(".","").replace(",","").replace('?','').replace('!','').replace('[','').replace(']','')    .replace('(','').replace(')','').replace('%','').replace('/','')
   for word in line.split(' '):
    
     if word in DictionaryOfWords.keys():
            DictionaryOfWords[word].append(i)
    
     else:
            DictionaryOfWords[word]=[i]
            
            
     Novel.append(word) 
     i+=1
    


# In[3]:


def GetQuery():
   
    word = input("Enter word:")      #Get Input from the user regarding what word s/he wants to query for

    Number = input("no. of results:")      #Get Input from the user regarding how many results the user wants to see

    return (word,Number)                 #Return as output a tuple of the word and the Number of results


# 

# In[4]:


def PrintContext(index):
    
    global Novel                          #Declares the list Novel as a Global Variable
    
    #COMPLETE THE CODE FROM HERE:
    
    for i in range( index-5, index+6 ) :           #Define the range so that the task above is fulfilled
        
        print(Novel[i], end = ' ')          #Print the word (using List Indexing) with a space after that
        
    print('\n')


# In[5]:



def PrintResult(word, NumQuery):
  
    global DictionaryOfWords                #Allows us to use the Dictionary as a global variable
    
    #COMPLETE THE CODE FROM HERE:
    
    L = DictionaryOfWords[word] 
    
    for i in range(0,min(len(L),NumQuery)):
        
        PrintContext(L[i])  
PrintResult('Harry',6)        


# In[9]:


while 1>0 :   
    
    Choice = input('Press Y in order to Continue with the next query or N to end .Please press Enter after entering your choice!')
    
    #COMPLETE THE CODE FROM HERE:
    
    if Choice== 'Y':                     # If the user wants to query 
        
        a,b = GetQuery() #Use some of the past defined function to do so
        
        PrintResult(a, int(b))
        
    else:
        
        break    

