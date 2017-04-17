from tika import parser
import os.path
import shutil
import re
from Rules import Rule

r= Rule()
print r.createAdjList()


fileSourcePath= 'D:/Study/File Routing - Python Project/SourceDocs/ssn.pdf'
text = parser.from_file(fileSourcePath)
print text
sourceData=str(text).lower()
## for bank statements 
if re.search("(monthly).*?(bank).*?(statement)",sourceData):
    print "bank statements "
## for Mortgage statements
elif re.search("(mortgage).*?(statement)",sourceData):
    print "Mortgage statements "
## for ssn 
elif re.search("[0-9]{3}[-][0-9]{2}[-][0-9]{4}",sourceData):
    print "SSN Card "
## for W2  
elif re.search("[0-9]{2}[-][0-9]{7}",sourceData):
    print "w2 doc beacause it ein no"
    
#shutil.move(fileSourcePath, "D:/Study/File Routing - Python Project/DestinationFiles/bankstmt.xlsx")

