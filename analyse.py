#!/usr/bin/env python3

import m_analyse as ma
import c_analyse as ca
import irma

#Constant definition:

CODE = "abcd"
MULTIPLE = ["Qu'est ce qu'un logiciel libre","Quels systèmes d'exploitation descendent d'Unix","Sélectionnez le nom de protocols graphique sous Linux"]
CUSTOM = ["A quoi sert le répertoire /lib"]

##########################
#Start of the script
##########################


def analyse(correctDict, userDict):
    '''This function analyses and compares user inputs with correction
        analyse: dict x dict -> list
    '''
    try:
        userlist = []
        correctDict = list(correctDict)
        cdict = correctDict[0]
        for subdict in userDict:
            if subdict["Code secret:"] == CODE:
                points = 0
                key = subdict["Email"]
                if subdict["Pensez-vous avoir réussi ce test ?"] == '':
                    predict = "Bien"
                else:
                    predict = subdict["Pensez-vous avoir réussi ce test ?"]
                for item in cdict:
                    if item in MULTIPLE:
                        points += ma.analyse_multiple(subdict[item],cdict[item])
                    elif item in CUSTOM:
                        points += ca.custom(subdict[item],item)
                    else:
                        if cdict[item] == subdict[item]:
                            points += 1
                        else:
                            continue
                person = {key : points,"Prediction ": subdict["Pensez-vous avoir réussi ce test ?"], "Irma": irma.prediction_check(points,predict)}
                print(person)
                userlist.append(person)
                print(userlist)
            else:
                continue
        return userlist
    except Exception as e:
        print(e)

##########################
##########################
##########################
