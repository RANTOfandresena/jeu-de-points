import pandas as pd
from math import *
#import matplotlib.pyplot as plt
def read_csv(filepath):
    data = pd.read_csv(filepath, sep=';')
    pd.set_option('display.max_columns', None)
    return data

def write_csv(filepath,data):
    data.to_csv(filepath,sep=";",index=False)
def calcul_distance(data_s, data_c):
    distance = pd.DataFrame(columns = ['PointA','PointB','x_A','y_A','x_B','y_B','Distance'])
    for i in range(0, len(data_s)):
        si = data_s.iloc[i,0]
        xi = data_s.iloc[i,1]
        yi = data_s.iloc[i,2]
        for j in range(0, len(data_c)):
            cj = data_c.iloc[j, 0]
            xj = data_c.iloc[j, 1]
            yj = data_c.iloc[j, 2]
            d = sqrt((xi-xj)**2 + (yi-yj)**2)
            list_row = [si,cj,xi,yi,xj,yj,d]
            distance.loc[len(distance)] = list_row
    return distance
def tracer_point(data_s, data_c):
    cl_sx=data_s.get('X')
    col_sy=data_s.get(('Y'))
    col_s=data_s.get('ID')
    plt.plot(col_sy,col_sy,'bo',label='source')
    plt.scatter(col_sx, col_sy)
    for i, txt in enumerate(col_s):
        plt.annotate(txt, (col_sx[i], col_sy[i]))
    col_cx = data_c.get('X')
    col_cy = data_c.get(',Y')
    col_c = data_c.get('ID')
    plt.plot(col_cx,col_cy,'ro',label='charge')
    plt.scatter(col_cx,col_cy)
    for i, txt in enumerate(col_c):
        plt.annotate(txt, (col_cx[i], col_cy[i]))
    
    plt.xlabel('x')
    ptl.ylabel('y')
    plt.title('source et charge')
    ptl.grid(True)
    plt.legend()
    plt.show()
    