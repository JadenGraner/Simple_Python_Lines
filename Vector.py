import numpy as np
import math

x,y = 10,10


Pixelx,Pixely = 1,1

Pixelxrad,Pixelyrad = Pixelx/2,Pixely/2

Screen = np.zeros((x,y),dtype=int)

Line_Cuts = 10

Dots = np.array([[0,0],[8,2],[5,8]],dtype=np.float32)
Lines = np.array([[0,1],[1,2]],dtype=np.int)

Render = []
for A,B in Lines:
	Length = (Dots[B] - Dots[A])/Line_Cuts
	for Seg in range(Line_Cuts+1):
		Next = (Dots[A] + (Length*Seg))
		Render = np.append(Render,Next,axis=0)

Render = np.asarray(Render)
Renlen = len(Render)//2

for i in range(x):
	for j in range(y):
		for k in range(Renlen):
			Rendy = Render[k*2]
			Rendx = Render[(k*2)+1]
			if (Rendx > i-Pixelxrad) and (Rendx <= i+Pixelxrad):
				if (Rendy > j-Pixelyrad) and (Rendy <= j+Pixelyrad):
					Screen[i,j] = 1

print(Screen)
