from FileOperations import Fileop
from DocumentClassifier import DocumentClassifier
import shutil


filenames=[]
fileSourcePath="D:/Study/File Routing - Python Project/SourceDocs/testing/"
fileDestinationPath="D:/Study/File Routing - Python Project/DestinationFiles/"
fileStopWord="D:/Study/File Routing - Python Project/stopWords.txt"
fileop= Fileop(fileStopWord)
filenames= fileop.readDirectory(fileSourcePath)

# iterate for each file in filenames list
# read the data from file and send that data for calculating the confidence score
# Depending upon the confidence route the document to respective location

for filename in filenames:
    print 'File Name: %s' %filename
    wordList=[]
    wordList=fileop.readFile(fileSourcePath+filename) 
    documentClassifier= DocumentClassifier()
    if wordList is not "":
        typeOfDoc=documentClassifier.ops(wordList)
        print 'Type of Document : %s ' %typeOfDoc +"\n"
        ## route the document
        path=fileDestinationPath +typeOfDoc +"/"+filename
        shutil.copy(fileSourcePath+filename, path)
