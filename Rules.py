class Rule:
    #create the adjacency list for category and their wordlist using training data  
    def createAdjList(self):     
        # empty dictionary
        adjLists_dict = {}
        
        # insert (Category, wordlist) pairs into dictionary
        adjLists_dict["bank statement"] = ["bank","statement","amount","monthly","yearly","deposits","withdrawals","balance","checkbook","summary","checking","saving"]
        adjLists_dict["w2"] = ["ssn","tax","w2","ein","employer","wages","box","medicare","amount","withheld","irs","contributions","compensation","benefits","taxes","federal","state","dependent","nontaxable","returns","exempt","liability","investment","employee","income"]
        adjLists_dict["1099"] = ["ssn","tax","1099","medicare","contributions","taxes","box","ein","income","state","tax","irs","misc","withheld","amount","returns","filing","foreign","federal","nonemployee","compensation","royalties","revenue","direct","corp","contract","hire","withhold","tin","partnerships","itin","issuer"]
        adjLists_dict["1098T"] = ["ssn","tax","1098t","ein","form","irs","tuition","amount","expenses","education","credit","student","grants","scholarships","institution","educational","claim","adjustments","graduate","taxpayer","revenue","refund","tin","reimbursements","academic","federal","school","penalty","liability"]
        adjLists_dict["UniTrans"] = ["amount","statement","university","tuition","fee","student","semester","rates","due","balance","undergraduate","graduate","charges","account","id","edu","aid","scholarships"]
        adjLists_dict["Mortgage"] = ["mortgage","due","payment","principal","amount","interest","statement","taxes","apr","late","fee","statement"]

        
        #print("\nPrint all adjacency lists")
        #for item in (adjLists_dict.keys()):
            #   print (item,adjLists_dict.get(item))
        return adjLists_dict


        
        


   
  