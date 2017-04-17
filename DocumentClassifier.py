from Rules import Rule
class DocumentClassifier: 
    def ops(self,wordList):
        #create dict for rules 
        rule= Rule()
        Rulesdict={}
        Rulesdict= rule.createAdjList()
        #for item in (Rulesdict.keys()):
            #print (item,len(Rulesdict.get(item)))        
        # create Rules lookup
        RulesLookup={}
        for item in (Rulesdict.keys()):
            for itemValue in Rulesdict.get(item):
                if itemValue in RulesLookup:
                    tempcategorySet=RulesLookup.get(itemValue) 
                    tempcategorySet.add(item)
                    RulesLookup[itemValue] = tempcategorySet   
                else: 
                    categorySet= set()
                    categorySet.add(item)
                    RulesLookup.update({itemValue:categorySet})
                    
        #print "Rules lookup"        
        #for item1 in (RulesLookup.keys()):
        #   print (item1,RulesLookup.get(item1))
        #print "Rules lookup end"       
        
        # maintain the dictionary for storing the category and its confidence
        priorityQueue = {}
        for word in wordList:
            if word in RulesLookup:
                categoryList=[]
                categoryList=list(RulesLookup.get(word))
                
                for category in categoryList:
                    if category in priorityQueue:
                        tempVal=priorityQueue.get(category)
                        priorityQueue[category]=tempVal+1   
                    else:
                        priorityQueue.update({category:1})
                        
        #get the highest confidence category for a input document
        maxval=-1
        typeOfDoc=""                
        for item in (priorityQueue.keys()):
            categoryCount=len(Rulesdict.get(item))
            percentage= priorityQueue.get(item)*100 
            percentage=percentage/categoryCount
            print 'Confidence score for %s is %s' %(item,str(percentage)+"%" )
            if(maxval<percentage):
                maxval=percentage
                typeOfDoc=item       
        return typeOfDoc
        
        

