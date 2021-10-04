#!/usr/bin/env python3

#Useful imports:
#Constant definition:

#Script starts here:

def analyse_multiple(userAnswer,correctAnswer):
    userAnswer.strip(" ")
    userAnswer = list(userAnswer.split(";"))
    correctAnswer.strip(" ")
    correctAnswer = list(correctAnswer.split(";"))
    points = 0
    for i in correctAnswer:
        if i in userAnswer:
            points += 1/len(correctAnswer)
        else:
            points -= 1/len(correctAnswer)
    if points < 0:
        return 0
    else:
        return points
    