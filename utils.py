import pandas as pd
df=pd.read_csv('data/titanic.csv')
df=df[df['Sex']=='female']
print(df)
