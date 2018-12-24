import sys
import time
sys.path.insert(0,'modules/') #loads the module directory.
import templateSearching as ts
import basicPrint as bp #basic print module
import mapper as mp #displays the tweet data on a map file
import JSONSearcher as search
import regexSearcher as regs

if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")

def choices():
    choice = input("Enter your choice: ")
    #print(choice)
    if choice == "1":
        bp.basicPrint()
    elif choice == "2":
        mp.Mapper()
    elif choice == "3":
        ts.templateSearcher()
    elif choice == "4":
        search.jsonSearcher()
    elif choice == "5":
        regs.regexSearcher()
    else:
        print("You didn't select a valid option, please select a valid option.")
        choices()

print("The Forensic JSON Parser")
print("========================")
print("Please select a option from below")
print("1: Basic JSON parse + Dump")
print("2: Mapper - Place tweet locations on a map")
print("3: Template searcher")
print("4: Text Searcher")
print("5: Regex Searcher")
choices()
