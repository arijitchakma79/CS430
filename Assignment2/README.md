Assignment: Homework 2
Author: Arijit Chakma
Language: Python
Operating System: Linux (Tux server compatible)
Main file: CG_hw2.py
Executable script: CG_hw2
Due Date: 23 October 2025

Overview:
------------------------------------------------------------------------------
This program reads polygon definitions expressed in PostScript commands,
applies 2D geometric transformations (scaling, rotation, translation), 
clips the transformed polygon against a world window using the 
Sutherland–Hodgman polygon clipping algorithm, and
outputs a valid PostScript file for rendering.

The input and output formats follow the assignment specification.
Only commands between %%%BEGIN and %%%END are processed.

File Structure:
------------------------------------------------------------------------------
CG_hw2              (executable wrapper script, chmod +x required)
CG_hw2.py           (main driver program with main())
parse_args.py       (command-line argument parser)
parse_ps.py         (PostScript reader/writer)
transform.py        (matrix-based transformation logic)
algorithm.py        (Sutherland–Hodgman polygon clipping)
README.txt
Makefile            (builds the executable script CG_hw2)

How to build and run the program:
------------------------------------------------------------------------------
First give the wrapper script execute permission:

    chmod +x CG_hw2

Then run:

    ./CG_hw2 [options] > output.ps

Examples:
    ./CG_hw2 -f hw2_a.ps -s 1.5 > hw2_ex1.ps
    ./CG_hw2 -f hw2_a.ps -m -250 -n -200 > hw2_ex2.ps
    ./CG_hw2 -f hw2_b.ps -a 170 -b 100 -c 270 -d 400 > hw2_ex3.ps
    ./CG_hw2 -f hw2_c.ps -s 2 > hw2_ex4.ps
    ./CG_hw2 -f hw2_c.ps -a 200 -b 100 -c 375 -d 400 > hw2_ex5.ps

Clipping Implementation:
------------------------------------------------------------------------------
File: algorithm.py
Class: SutherlandHodgman
Methods: clip(), clip_edge(), inside(), intersect()

Implements the standard Sutherland–Hodgman polygon clipping algorithm.
The polygon is iteratively clipped against each boundary of the world
window (LEFT, RIGHT, BOTTOM, TOP). Intersection points are computed
as needed and added to the output vertex list.

Transformations:
------------------------------------------------------------------------------
File: transform.py
Class: Transform
Methods: scale(), rotate(), translate(), apply(), apply_to_vertices()

Applies 2D transformations using 3×3 homogeneous transformation matrices.
Supports composition of multiple transformations and batch-application
to all polygon vertices.

Compilation / Execution:
------------------------------------------------------------------------------
No compilation is required (Python interpreter used).

To build:
    make

This will create an executable script named `CG_hw2` (or refresh it if it already exists).

To run:
    ./CG_hw2 [options]

Dependencies:
------------------------------------------------------------------------------
Python 3.10 or later (installed on Tux)
Uses only standard modules: math, sys
No external libraries required.

