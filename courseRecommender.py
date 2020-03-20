#import needed modules
import numpy as np
import pandas as pd

def recommend (scores, base): 
    results = " "
    #import user scores
    user_scores = pd.read_csv(scores)
    # sort the scores in accending order
    user_scores.groupby('Title')['Score'].mean().sort_values(ascending=True)

    # create a matrix of courses and score
    score_matrix = user_scores.pivot_table(index='UserID', columns='Title', values='Score')

    # grab score for baseline resource
    base_score = score_matrix[base]
    # find resourses that correlate
    base_corr = score_matrix.corrwith(base_score)

    # put results into data frame
    bCorr = pd.DataFrame(base_corr, columns=['Correlation'])
    bCorr.dropna(inplace=True)
    bCorr.sort_values('Correlation', ascending=False)

