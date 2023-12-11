import os 
import pandas
def lire():
    data=pandas.read_csv("xxx.csv",sep=";")
    print(data)
def ecrire():
    df=pandas.dataFrames(columns=['nom','age'])
    list_row=['koto',100]
    df.loc[len(df)]=list_row
    os.makedins('folder/subfolder',exist_ok=True)
    df.to_csv('folder/subfolder/out.csv',sep=';',index=False)