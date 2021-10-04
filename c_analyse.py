#!/usr/bin/env python3

#Useful imports:

import re 




#Constant definition:

stopWords = ["le","les","la","du","des","de","au","aux","avec","par"]
INPUT_DICT = {"A quoi sert le répertoire /lib":"input/libdirectory.txt"}




#Script starts here:
##opens the keyword, sanitizes strings/lists
def custom(userAnswer,key):
    with open(INPUT_DICT[key], mode='r', encoding='utf-8-sig') as wordlist:
        wordlist = [word.replace('\n','') for word in wordlist]
        userAnswer = cleaning(userAnswer)
        userlist = userAnswer.split(' ')
        userlist = remove_stop(userlist)
        result = check(userlist, wordlist)
        return result


###Cleans the string (removes accents, diacritics, special characters etc)
def cleaning(userAnswer):
    userAnswer = str(userAnswer.translate(str.maketrans({'(': ' ', ')': ' ', '.':' ', '\'':' ','\n':' ',',':' ',';':' ','/':' ','\\':' '})))
    userAnswer = userAnswer.replace(' +','')
    userAnswer = userAnswer.replace('  ',' ')
    userAnswer = userAnswer.lstrip(' ')
    userAnswer = userAnswer.lower()
    userAnswer = remove_accents(userAnswer)
    return userAnswer
    
###Checks if the user input words are in the keyword list
def check(userlist,wordlist):
    #add a sanitizing function to select only the radical of each word, wich might improve results and avoid typo related errors
    count = 0
    for uword in userlist:
        if uword in wordlist:
            count += 1
        else:
            continue 
    if count >= 3:
        return 1
    elif count > 2:
        return 0.5
    else:
        return 0

###Removes accents
def remove_accents(userAnswer):
    userAnswer = re.sub(u"[àáâãäå]", 'a', userAnswer)
    userAnswer = re.sub(u"[èéêë]", 'e', userAnswer)
    userAnswer = re.sub(u"[ìíîï]", 'i', userAnswer)
    userAnswer = re.sub(u"[òóôõö]", 'o', userAnswer)
    userAnswer = re.sub(u"[ùúûü]", 'u', userAnswer)
    userAnswer = re.sub(u"[ýÿ]", 'y', userAnswer)
    userAnswer = re.sub(u"[ß]", 'ss', userAnswer)
    userAnswer = re.sub(u"[ñ]", 'n', userAnswer)
    return userAnswer 

###Removes stopwords
def remove_stop(userAnswer):
    userAnswer = [word for word in userAnswer if word not in stopWords]
    return userAnswer