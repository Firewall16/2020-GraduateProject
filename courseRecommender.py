#import needed modules
import numpy as np
import pandas as pd

def recommend (scores): 
    #import user scores
    user_scores = pd.read_csv(scores)
    user_scores.groupby('Title')['Score'].mean().sort_values(ascending=True)
    user_score_data = user_scores.pivot_table(index='UserID', columns='Title', values='Score')
    linux_score = user_score_data['Linux for Beginners']
    linuxBasics_corr = user_score_data.corrwith(linux_score)

    corr_linuxBasics = pd.DataFrame(linuxBasics_corr, columns=['Correlation'])
    corr_linuxBasics.dropna(inplace=True)
    corr_linuxBasics.sort_values('Correlation', ascending=False).head(10)

