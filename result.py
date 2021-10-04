#!/usr/bin/env python3

#Constants:
OUTPUT_RES="output/results.txt"
OUTPUT_STAT="output/statistics.txt"

#Script starts here:
##########################
def result(userlist):
    '''This function prints the output result in a file
        result: list -> string
    '''
    try:
        with open(OUTPUT_RES, mode='w', encoding='utf-8-sig') as output:
            for item in userlist:
                output.write(str(item).translate(str.maketrans({'{': '', '}': '', '\'' : ''})) + "\n")
    except Exception as e:
        print(e)

def printstatistics(statlist):
    '''This function prints the statistics in a file
        printstatistics: list -> string
    '''
    try:
        with open(OUTPUT_STAT, mode ='w', encoding='utf-8-sig') as statistics:
            for item in statlist:
                statistics.write(str(item))
    except Exception as e:
        print(e)


 
##########################
##########################
##########################
