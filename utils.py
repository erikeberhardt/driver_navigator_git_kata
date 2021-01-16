import pandas as pd
def titanicfemale():
    df=pd.read_csv('data/titanic.csv')
    df=df[df['Sex']=='female']
    return df
