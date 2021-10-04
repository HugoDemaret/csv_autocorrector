#!/usr/bin/env python3

#imports:

#constants:
PRED_DICT = {"Très bien":14,"Bien":10.5,"Moyennement":7,"Difficilement":3.5,"Très difficilement":0}
#script starts here:


def prediction_check(result,prediction):
    correctness = result-PRED_DICT[prediction]
    return correctness