from tkinter import *
longueur=500
largeur=500
couleur=["red","blue"]
lesPoints=[]
i=0
def ligne():
    x=longueur/20
    x1=0
    while(x1<=500):
        x1+=x
        canvas.create_line(x1,0,x1,largeur,width=1,fill='black')
    y1=0
    while(y1<=500):
        y1+=x
        canvas.create_line(0,y1,longueur,y1,width=1,fill='black')
def pointeur(event):
    global i
    q=int(event.x/25)
    r=event.x%25
    if(r<=12):
        positionX=q*25
    else:
        positionX=((q+1)*25)
    q=int(event.y/25)
    r=event.y%25
    if(r<=12):
        positionY=q*25
    else:
        positionY=((q+1)*25)
    j=0
    for point in lesPoints:
        if(point[:2]==[positionX,positionY]):
            j+=1
    if(j==0):
        lesPoints.append([positionX,positionY,couleur[i%2]])
        print(lesPoints)
        canvas.create_oval(positionX-5,positionY-5,positionX-5+10,positionY-5+10,width=2,fill=couleur[i%2])
        i+=1
        verification([positionX,positionY])
def verification(pointClick):
    print("")
fenetre=Tk()
canvas=Canvas(fenetre,bg='white',height=longueur,width=largeur)
canvas.bind("<Button-1>", pointeur)
ligne()
canvas.pack()
fenetre.mainloop()