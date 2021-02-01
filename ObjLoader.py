## A simple script to read an Wavefront .obj file.
## The obj file has to consist of only triangles (no quads or other polygons) and needs to have both normal and UV information available
## 
import os
import sys
import re
import random


def LoadVerticesAndFaces(filename):
	v, vn, vt, f, norms, texts =[], [], [], [], [], []
	iv, ivn, ivt=0, 0, 0


	InputFile = open(filename,'r')

	if InputFile.mode == 'r':

		ls = InputFile.readlines()
		for l in ls:
			tokens = re.split(' +',l.strip());
			
			if tokens[0]=='v': # vertex
				if len(tokens)==4: # requires 3 vertex coordinates (x,y,z)
					v.append([float(tokens[1]), float(tokens[2]), float(tokens[3])])
					iv=iv+1
				else:
					print('ERROR: The Wrong size of vertex vector: ' + str(len(tokens)-1))
			elif tokens[0]=='vn': # Vertex normal           
				if len(tokens)==4: # requires 3 normal coordinates (nx,ny,nz)
					vn.append([float(tokens[1]), float(tokens[2]), float(tokens[3])])
					ivn=ivn+1
				else:
					print('ERROR: The Wrong size of normal vector: ' + str(len(tokens)-1))
			elif tokens[0]=='vt': # Vertex UV coordinates
				if len(tokens)==3 or len(tokens)==4: # Accepts only 2D UV coordinates. If there are 3 coordinates, ignores the last one
					vt.append([float(tokens[1]), float(tokens[2])])
					# print vt[ivt]
					ivt=ivt+1
				else:
					print('ERROR: The Wrong size of texture vector: ' + str(len(tokens)-1))
			elif tokens[0]=='f':  # Face (triangle)         
				if len(tokens)==4: # Accepts only triangles (3 vertices)
					for i in range(1,4):
						temp = re.split('/',tokens[i])
						f.append(int(temp[0])-1);  
						texts.append(int(temp[1])-1);
						norms.append(int(temp[2])-1);  
				else:
					print('ERROR: The Wrong size of vertices for triangle: ' + str(len(tokens)-1))

	else:
		print("File not found")
		
	InputFile.close() 

	return v, f
