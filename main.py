import os 
import pandas as pd
from tools import *
def lire():
    data=pd.read_csv("xxx.csv",sep=";")
    print(data)
def ecrire():
    df=pd.dataFrames(columns=['nom','age'])
    list_row=['koto',100]
    df.loc[len(df)]=list_row
    os.makedins('folder/subfolder',exist_ok=True)
    df.to_csv('folder/subfolder/out.csv',sep=';',index=False)
if __name__ == '__main__':
    data_c = read_csv("dataC.csv")
    data_s = read_csv("dataS.csv")
    distance_s_c = calcul_distance(data_s, data_c)
    print(distance_s_c)
    write_csv("distance_s_c.csv",distance_s_c)
    #tracer_point(data_s, data_c)