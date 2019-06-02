import os
import numpy as np
import math
from PIL import Image
import imageio
# Jaden M Graner 2019

Res = 5 # Simple resolution multiplier, increases scale of screen and scales everything

x,y = 14*Res,10*Res # Widdth and height of display in pixels

Pixel_x,Pixel_y = 1,1 # Aspect Ratio of pixels (As in if the pixels are rectangular or you wish to manipulate the image)
Pixel_x_radi,Pixel_y_radi = Pixel_x/2,Pixel_y/2 # The vertical and horizontal distance to the border between pixels, used for detecting wither an object falls within the area
Line_Cuts = 10*Res # The number of locations on an edge that are checked for visability

Dot_Ani =  [True,True,True] # Determines the initial movements of the verts


Dots = np.array([[5,0],[5,5],[5,9]],dtype=np.int) # The array containing the Verts

Lines = np.array([[0,1],[1,2]],dtype=np.int) # Array containing the edges (connections between verts)

for i in range(Dots.shape[0]): # Applies Resolution Multiplication to Verts
	for j in range(Dots.shape[1]):
		Dots[i,j] *= Res


def Animation(Dots): # Moves verts left to right
	Ani_Top = 13*Res # Max and min values of the vert movement
	Ani_Bot = 1*Res
	for m,Dot in enumerate(Dot_Ani,0): # Loops through each dot and its animation value
		if Dot == True:
			Dots[m,0] += 1+m
		else:
			Dots[m,0] -= 1+m
		if (Dots[m,0] > Ani_Top) or (Dots[m,0] < Ani_Bot): # Keep Animated verts within limits, if above/below flip T/F
			Dot_Ani[m] = not Dot
	return(Dots)



Local = os.path.dirname(os.path.realpath(__file__)) # location for new file, here it'll be in the same directory as the py file

Frames = 60 # how many frames to render

Frame_Path = [] # Makes a list of the name of each frame so it can reconstruct them in order later

for l in range(Frames): # self explanitory

	Screen = np.zeros((y,x,3),dtype=np.uint8) # The formation of the display (output), As well as 3Z layrs for future RGB support # wiped every new frame

   # ANIMATION SEQUENCES GO HERE:
	Dots = Animation(Dots)

	Render = [] # Empty Array for selected segments(Verts Along Edges) to be drawn, Should be a 2D array but I'm stupid, See FIX_1

	for A,B in Lines: # Get each edge in the image and break it up into pixel checking locations and put it in Render
		Length = (Dots[B] - Dots[A])/Line_Cuts
		for Seg in range(Line_Cuts+1):
			Next = (Dots[A] + (Length*Seg))
			Render = np.append(Render,Next,axis=0)

	Render = np.asarray(Render) # Convert the list render into an array, see FIX_1, It shoudl already be a 2D array here
	Ren_Len = len(Render)//2 # Needed for a for loop later, see FIX_1

	for i in range(y): # Check Each Pixel and see if any of the points in Render fall within them
		for j in range(x):
			for k in range(Ren_Len): # These Three lines used to be a nice clean "for Rendx,Rendy in Render" but I can't, see FIX_1
				Rendy = Render[k*2] # FIX_1
				Rendx = Render[(k*2)+1] # FIX_1
				if (Rendx > i-Pixel_x_radi) and (Rendx <= i+Pixel_x_radi):
					if (Rendy > j-Pixel_y_radi) and (Rendy <= j+Pixel_y_radi):
						Screen[i,j] = [255,255,255] # RGB value to insert

	Img = Image.fromarray(Screen,mode='RGB') # Simply convert the output array to an image
	Num = str(l) # Convert int to string for file name
	Frame_Path.append(Local+'/list/'+'output_'+Num+'.png')
	Img.save(Local+'/list/'+'output_'+Num+'.png') # Location to put the new image N0TE It Didn't like L+'/my.tiff'

Frame_List = [] # A list of images to be combined

for Frame in Frame_Path: # Grabs paths from list, then collects the images, and brings them together to make a gif
	if Frame.endswith('png'):
		Frame_List.append(imageio.imread(Frame))
imageio.mimsave(Local+'/'+'movie.gif',Frame_List) # Gif will be made in folder with python file
