# Utility functions used in other scripts 
import math 
import random 
from timeit import default_timer as timer

# outputs binary matrix m with m(i,j)=1 when face i includes vertex j
def face2vertexMatrix(v,f):
	mat = []
	for i in range (int(len(f)/3)):
		row = [0 for x in range(len(v))]
		row[f[i*3]] = 1
		row[f[i*3+1]] = 1
		row[f[i*3+2]] = 1
		
		mat.append(row)

	return mat
	
# Creates the dual graph* of the original graph
# * The dual graph is describe in: "Single-strips for fast interactive rendering," Diaz-Gutierrez et al.
def dualGraph(v,f):
	nRow = int(len(f)/3)
	nCol = int(len(v))
	vfMat = face2vertexMatrix(v,f)
	
	mat = [[0 for x in range(nRow)] for x in range(nRow)]

	for i in range(nRow):
		for j in range(i+1,nRow):
			sum = 0
			for k in range(nCol):
				sum += vfMat[i][k]*vfMat[j][k]
			if sum == 2:
				mat[i][j]= mat[j][i]= 1	
	return mat


# Create the Conjunctive normal form (CNF) of the graph
# The formation of clauses are based on: https://www.csie.ntu.edu.tw/~lyuu/complexity/2011/20111018.pdf
def graph2CNF(g):
	c = [] # clauses
	n = len(g)
	
	for j in range(n):
		c.append([indx(i,j,n) for i in range(n)])
	
	for j in range(n):
		for i in range(n):
			for k in range(i+1,n):
					c.append([-indx(i,j,n), -indx(k,j,n)])
					
	for i in range(n):
		c.append([indx(i,j,n) for j in range(n)])
	
	for i in range(n):
		for j in range(n):
			for k in range(j+1,n):
				c.append([-indx(i,j,n), -indx(i,k,n)])
	
	for i in range(n):
		for j in range(i+1,n):
			if (g[i][j])==0:
				for k in range(n-1):
					c.append([-indx(k,i,n), -indx(k+1,j,n)])
					c.append([-indx(k,j,n), -indx(k+1,i,n)])
	return c

# Convert the solution of the SAT problem to a path that covers all triangles 
def getPath(satSol,g):
	p = []
	n = len(g)
	for x in satSol:
		if x > 0:
			i,j = unIndx(x,n)
			p.insert(i,j)
			
	return p

# Define the vertex list that corresponds to the given triangle path 
def getStrip(path, v, f):
	vList = []
	n = int(len(f)/3)
	
	first = [f[path[0]*3], f[path[0]*3+1], f[path[0]*3+2]]	
	next = [f[path[1]*3], f[path[1]*3+1], f[path[1]*3+2]] 
	common = []
	for i in range(3):
		if next[i] in first:
			first.remove(next[i])
			common.append(next[i])
	vList = [v[first[0]]] + [v[common[0]]] + [v[common[1]]]
	print([first[0], common[0], common[1]])
	for i in range(1, len(path)):
		previous = [f[path[i-1]*3], f[path[i-1]*3+1], f[path[i-1]*3+2]]	
		current = [f[path[i]*3], f[path[i]*3+1], f[path[i]*3+2]]	
		for i in range(3):
			if previous[i] in current:
				current.remove(previous[i])
		if not len(current)== 1:
			print("ERROR")
		vList.append(v[current[0]])
		print(current[0])
		
	return vList

# Conver the matrix indices to the sequential index
def indx(i,j,n):
	return i*n+j+1

# Conver the sequential index to matrix indices
def unIndx(x,n):
	i = math.floor((x-1)/n)
	j = x-1-i*n
	return i,j

# Time keeping utility	
def keepTime(vec):
	if len(vec) == 0:
		vec.append(timer())
#		raise IndexError("\nTime record vector is empty")
	else:
		vec.append(timer()-vec[-1])
	return vec

