import os
import numpy as np
import math
from PIL import Image
# Jaden M Graner 2019


x,y = 10,10 # Widdth and height of display in pixels
Screen = np.zeros((x,y,3),dtype=np.uint8) # The formation of the display (output), As well as 3Z layrs for future RGB support

Pixelx,Pixely = 1,1 # Aspect Ratio of pixels (As in if the pixels are rectangular or you wish to manipulate the image)
Pixelxrad,Pixelyrad = Pixelx/2,Pixely/2 # The vertical and horizontal distance to the border between pixels, used for detecting wither an object falls within the area
Line_Cuts = 10 # The number of locations on an edge that are checked for visability

Dots = np.array([[0,0],[8,2],[5,8]],dtype=np.int) # The array containing the Verts

Lines = np.array([[0,1],[1,2]],dtype=np.int) # Array containing the edges (connections between verts)

Render = [] # Empty Array for selected segments(Verts Along Edges) to be drawn, Should be a 2D array but I'm stupid, See FIX_1

for A,B in Lines: # Get each edge in the image and break it up into pixel checking locations and put it in Render
	Length = (Dots[B] - Dots[A])/Line_Cuts
	for Seg in range(Line_Cuts+1):
		Next = (Dots[A] + (Length*Seg))
		Render = np.append(Render,Next,axis=0)

Render = np.asarray(Render) # Convert the list render into an array, see FIX_1, It shoudl already be a 2D array here
Renlen = len(Render)//2 # Needed for a for loop later, see FIX_1

for i in range(x): # Check Each Pixel and see if any of the points in Render fall within them
	for j in range(y):
		for k in range(Renlen): # These Three lines used to be a nice clean "for Rendx,Rendy in Render" but I can't, see FIX_1
			Rendy = Render[k*2] # FIX_1
			Rendx = Render[(k*2)+1] # FIX_1
			if (Rendx > i-Pixelxrad) and (Rendx <= i+Pixelxrad):
				if (Rendy > j-Pixelyrad) and (Rendy <= j+Pixelyrad):
					Screen[i,j] = [255,255,255] #RGB

# print(Screen) # Print result to Console #REMOVED 5/30/19 REPLACED with image display

local = os.path.dirname(os.path.realpath(__file__)) # location for new file, here it'll be in the same directory as the py file

img = Image.fromarray(Screen,mode='RGB') # Simply convert the output array to an image
img.save(local+'/'+'output.tiff') # Location to put the new image # It Didn't like L+'/my.tiff', so I had to use local+'/'+'my.tiff'
img.show() # Show image when done
