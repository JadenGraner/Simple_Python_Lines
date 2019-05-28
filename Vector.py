import numpy as np
import math

# Widdth and height of display in pixels; and the formation of the display (output)
x,y = 10,10
Screen = np.zeros((x,y),dtype=int)
# Aspect Ratio of pixels (As in if the pixels are rectangular or you wish to manipulate the image)
Pixelx,Pixely = 1,1
# The vertical and horizontal distance to the border between pixels, used for detecting wither an object falls within the area
Pixelxrad,Pixelyrad = Pixelx/2,Pixely/2
# The number of locations on an edge that are checked for visability
Line_Cuts = 10

# The array containing the Verts
Dots = np.array([[0,0],[8,2],[5,8]],dtype=np.float32)
# Array containing the edges (connections between verts)
Lines = np.array([[0,1],[1,2]],dtype=np.int)
# Empty Array for selected segments(Verts Along Edges) to be drawn, Should be a 2D array but I'm stupid, See FIX_1
Render = []
# Get each edge in the image and break it up into pixel checking locations and put it in Render
for A,B in Lines:
	Length = (Dots[B] - Dots[A])/Line_Cuts
	for Seg in range(Line_Cuts+1):
		Next = (Dots[A] + (Length*Seg))
		Render = np.append(Render,Next,axis=0)

# Convert the list render into an array, see FIX_1, It shoudl already be a 2D array here
Render = np.asarray(Render)
# Needed for a for loop later, see FIX_1
Renlen = len(Render)//2
# Check Each Pixel and see if any of the points in Render fall within them
for i in range(x):
	for j in range(y):
		for k in range(Renlen): # These Three lines used to be a nice clean "for Rendx,Rendy in Render" but I can't, see FIX_1
			Rendy = Render[k*2] # FIX_1
			Rendx = Render[(k*2)+1] # FIX_1
			if (Rendx > i-Pixelxrad) and (Rendx <= i+Pixelxrad):
				if (Rendy > j-Pixelyrad) and (Rendy <= j+Pixelyrad):
					Screen[i,j] = 1
# Print result to Console
print(Screen)
