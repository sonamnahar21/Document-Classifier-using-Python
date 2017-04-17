import os
from tika import parser
import re

class Fileop: 
    
    def __init__(self,stopWordFilePath):
        self.stopWordFilePath=stopWordFilePath
        
    #read fileNames form Directory    
    def readDirectory(self,path):
        fileNames=[]
        fileNames=os.listdir(path)
        return fileNames
     
    #read the data from file and generate the list of unique words in that file   
    def readFile(self,filename):
        text = parser.from_file(filename)
        if text=={}:
            print "File is not legible  or it may be password protected \n"
            return ""
        else:
            sourceData=str(text).lower()
            sourceData= sourceData.replace('\\n'," ")
            sourceData= sourceData.replace('-'," ")
        
            #print sourceData
            
            ## for Unique words in file ##
            words = re.findall('\w+', sourceData)
            uniq_wordSet = set(words)
            wordList = list(uniq_wordSet)
            #print "\n unique words\n\n"
            #print wordList
            return self.readAndRemoveStopWords(wordList)
        
    # remove the stop words from unique word list      
    def readAndRemoveStopWords(self,inputWordList):
        stopText = parser.from_file(self.stopWordFilePath)
        sourceData=str(stopText).lower()
        stopList=list(sourceData)
        inputWordList = [i for j, i in enumerate(inputWordList) if j not in stopList]
        return inputWordList
