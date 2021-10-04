#!/usr/bin/env python3

#Useful imports
import math
import numpy as np

#constants:
IRMA = "\nPour la note Irma : \n Négative : sur-évaluation \n Positive : sous-évaluation \n Nulle : Bonne prédiction \n Globalement, si la note est positive et inférieure à 2, la prédiction est 'bonne'\n"

#Statistic script for csv form auto-correction
def statistics(userlist):
    assert type(userlist) is list, 'userlist is not list'
    raw_points = []
    irma_points = []
    for user in userlist:
        for key in user:
            if key not in ["Prediction : ","Irma"]:
                raw_points.append(user[key])
            elif key == "Irma":
                irma_points.append(user[key])
    note_stat = note_stats(raw_points)
    irma_stat = note_stats(irma_points)
    return "PURE STATISTICS : \n" + note_stat + "\n##################################\n" + "\nIRMA (PREDICTION) STATISTICS : \n" + irma_stat +  "\n##################################\n" + IRMA

def note_stats(raw_points):
    arr = np.array(raw_points,dtype = float)
    min = np.min(raw_points)
    max = np.max(raw_points)
    mean = np.mean(arr)
    med = np.median(arr)
    var = np.var(arr, ddof=1)
    std_dev = np.std(arr,ddof=1)
    return " Mean = "+ str(mean) + "\n Median = " + str(med) + "\n Variance = " + str(var) + "\n Standard deviation = " + str(std_dev) + "\n Minimal = " + str(min) + "\n Maximal = " + str(max)