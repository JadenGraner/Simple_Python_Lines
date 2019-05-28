import numpy as np
import math

x = 10
y = 10

Pixelx = 1
Pixely = 1

Pixelxrad = Pixelx/2
Pixelyrad = Pixely/2

Screen = np.zeros((x,y),dtype=int)
TxtScreen = np.chararray((x,y))

Vector_Cuts = 10

Dots = np.array([[0,0],[8,2],[5,8]],dtype=np.float32)
Lines = np.array([[0,1],[1,2]],dtype=np.int)

Render = []

# print('Dots',Dots[1]) #DEBUG

for A,B in Lines:
	# print('A,B',A,B) #DEBUG
	Length = (Dots[B] - Dots[A])/Vector_Cuts
	# print('Length',Length) #DEBUG
	for Seg in range(Vector_Cuts+1):
		Next = (Dots[A] + (Length*Seg))
		# print('Next',Next) #DEBUG
		# print('Render',Render) #DEBUG
		# print('NextSize',Next.size) #DEBUG
		# print('RenderSize',Render.size) #DEBUG
		Render = np.append(Render,Next,axis=0)

# print('Render',Render) #DEBUG

Render = np.asarray(Render)

Renlen = len(Render)//2

# print('Len Render',len(Render)) #DEBUG

for i in range(x):
	for j in range(y):
		# for k in range(len(Render)):
		# 	Rendx,Rendy = Render[k]
		# for Rendx,Rendy in Render:
		for k in range(Renlen):
			# print('Len Render',len(Render))
			Rendy = Render[k*2]
			Rendx = Render[(k*2)+1]
			if (Rendx > i-Pixelxrad) and (Rendx <= i+Pixelxrad):
				if (Rendy > j-Pixelyrad) and (Rendy <= j+Pixelyrad):
					Screen[i,j] = 1
		# if Screen[i,j] == 1:
		# 	BBox = "█".encode(encoding='UTF-8')
		# 	TxtScreen[i,j] = '',BBox
		# else:
		# 	TxtScreen[i,j] = " "
print(Screen)
