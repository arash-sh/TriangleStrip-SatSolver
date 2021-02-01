# TriangleStrip-SatSolver

This code find a triangle strip for a given triangle mesh, if such a strip exits. The strip specifies a sequence of all the triangles in the mesh, where every triangle appears exactly once. In other words, the entire mesh is covered, while no triangle is repeated. This problem is equivalent to finding a Hamiltonian path in the dual graph [[1]](#1). The code was created for the Theory of Computation (CS517) class to evaluate the computation time of SAT solvers as the problem size grows. 

The problem is converted to a satisfiability (SAT) problem by creating the conjunctive normal form (CNF) of the dual graph. An explanation of this process can be found in [[2]](#2). The SAT problem is then solved with an off-the-shelf SAT solver ( Glucose3).

The repository also includes a simple loader for Wavefront OBJ files. This is not a full-fledged implementation of an OBJ loader and has certain constraints. Specifically, only triangular meshes are accepted and the mesh needs to have both vertex normal and texture coordinates defined. 

Few sample models are available in the [ExampleObjects](ExampleObjects) folder. To run the code type: 
```
python TriStrip <path-to-obj-file>
```



## References
<a id="1">[1]</a> Diaz-Gutierrez, P., Bhushan, A., Gopi, M., and Pajarola, R. Single-strips for fast interactive rendering. *The Visual Computer* 22, 6 (June 2006), 372–386.

<a id="2">[2]</a> Lyuu, Y.-D. Theory of Computation Lecture Notes. https://www.csie.ntu.edu.tw/~lyuu/complexity/2011/20111018.pdf.
