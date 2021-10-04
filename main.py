#!/usr/bin/env python3

#Useful imports
from analyse import analyse
from result import result, printstatistics
from statistics_auto import statistics
import csv
#Constants
VERSION="1.0.5"
INPUT_CORRECT="input/correction.csv"
INPUT_USER="input/userinput.csv"
##########################
#Start of the main script
##########################
def main():
    try:
        with open(INPUT_CORRECT,mode = "r", encoding='utf-8-sig') as correction, open(INPUT_USER,mode = "r", encoding='utf-8-sig') as userInput:
            print("CSV auto-correction script version : ", VERSION)
            correctDict = csv.DictReader(correction)
            userDict = csv.DictReader(userInput)
            userlist = analyse(correctDict,userDict)
            result(userlist)
            stats = statistics(userlist)
            printstatistics(stats)
            print("Done!")
    except Exception as e:
        print(e)
##########################
##########################

main()

##########################
#######End of script######
##########################
