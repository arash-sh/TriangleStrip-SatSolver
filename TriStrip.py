#!/usr/bin/python

import sys
from ObjLoader import LoadVerticesAndFaces
from Utils import *
from pysat.solvers import Glucose3
from timeit import default_timer as timer

if len(sys.argv) != 2 or not sys.argv[1].endswith(".obj"):
	raise TypeError("\nThe name of the .obj file should be provided as an argument, e.g.:\n\t python Tritrip.py sphere5.obj")

timeStamps = keepTime([])	

print("------- Loading Model -------", end = " ")
v, f = LoadVerticesAndFaces(sys.argv[1]) # Read the triangle mesh
timeStamps = keepTime(timeStamps)	
print("time: %f"% timeStamps[-1])

print("------- Creating Dual Graph -------", end = " ")
graph = dualGraph(v,f) # Convert the triangle mesh to its dual graph
timeStamps = keepTime(timeStamps)	
print("time: %f"% timeStamps[-1])

print("------- Generating Clauses -------", end = " ")
clauses = graph2CNF(graph) # Create the Conjunctive normal form of the dual graph
timeStamps = keepTime(timeStamps)	
print("time: %f"% timeStamps[-1])


print("------- Adding Clauses -------", end = " ")
g = Glucose3() # Instanciate the SAT solver and add the CNF clauses
for c in clauses:
	g.add_clause(c)
timeStamps = keepTime(timeStamps)	
print("time: %f"% timeStamps[-1])

print("------- Solving SAT -------", end = " ")
if g.solve(): # if the problem is solvable, convert the solution to the path that covers all triangles
	sol = g.get_model()
	path = getPath(sol,graph)
else:
	path = []

timeStamps = keepTime(timeStamps)	
print("time: %f"% timeStamps[-1])

print('\n%s: %d triangles  \t  %d vertices  \t  %d clauses\n' % (sys.argv[1],len(f)/3, len(v), len(clauses)))


if path ==[]:
	print("No strip exists")
else:
	print("Strip: %s" % path)
	

#print("Time stamps: %s" % timeStamps)

