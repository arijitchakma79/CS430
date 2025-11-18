Assignment: Homework 3
Author: Arijit Chakma
Language: Python
Operating System: Linux (Tux server compatible)
Main file: CG_hw3.py
Executable script: CG_hw3
Due Date: [To be filled]

Overview:
------------------------------------------------------------------------------
This program reads polygon definitions expressed in PostScript commands,
applies 2D geometric transformations (scaling, rotation, translation),
clips the transformed polygon against a world window using the
Sutherland–Hodgman polygon clipping algorithm,
maps the clipped polygons from world coordinates to viewport coordinates,
fills the polygons using the scanline fill algorithm,
and outputs a PBM (Portable BitMap) raster image file.

The input format follows the assignment specification.
Only commands between %%%BEGIN and %%%END are processed.

File Structure:
------------------------------------------------------------------------------
CG_hw3              (executable wrapper script, chmod +x required)
CG_hw3.py           (main driver program with main())
parse_args.py       (command-line argument parser)
parse_ps.py         (PostScript reader)
transform.py        (matrix-based transformation logic)
sutherland_hodgman.py (Sutherland–Hodgman polygon clipping)
scanline.py         (scanline fill algorithm for polygon rasterization)
helper.py           (world-to-viewport mapping and PBM output)
README.md
Makefile            (builds the executable script CG_hw3)

How to build and run the program:
------------------------------------------------------------------------------
First give the wrapper script execute permission:

    chmod +x CG_hw3

Then run:

    ./CG_hw3 [options] > output.pbm

Examples:
    ./CG_hw3 -f hw3_a.ps -s 1.5 > hw3_ex1.pbm
    ./CG_hw3 -f hw3_a.ps -m -250 -n -200 > hw3_ex2.pbm
    ./CG_hw3 -f hw3_b.ps -a 170 -b 100 -c 270 -d 400 > hw3_ex3.pbm
    ./CG_hw3 -f hw3_c.ps -s 2 > hw3_ex4.pbm
    ./CG_hw3 -f hw3_c.ps -a 200 -b 100 -c 375 -d 400 -j 50 -k 50 -o 450 -p 450 > hw3_ex5.pbm

Command-Line Arguments:
------------------------------------------------------------------------------
-f <file>   Input PostScript file (default: hw3_split.ps)
-s <float>  Scale factor (default: 1.0)
-r <int>    Rotation angle in degrees (default: 0)
-m <int>    Translation in x direction (default: 0)
-n <int>    Translation in y direction (default: 0)
-a <int>    World window left boundary (default: 0)
-b <int>    World window bottom boundary (default: 0)
-c <int>    World window right boundary (default: 250)
-d <int>    World window top boundary (default: 250)
-j <int>    Viewport left boundary (default: 0)
-k <int>    Viewport bottom boundary (default: 0)
-o <int>    Viewport right boundary (default: 200)
-p <int>    Viewport top boundary (default: 200)

Clipping Implementation:
------------------------------------------------------------------------------
File: sutherland_hodgman.py
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
to all polygon vertices. Transformations are applied in the order:
scale, rotate, then translate.

Viewport Mapping:
------------------------------------------------------------------------------
File: helper.py
Function: world_to_viewport()

Maps points from world coordinate space (defined by window bounds a, b, c, d)
to viewport coordinate space (defined by viewport bounds j, k, o, p).
Uses linear scaling to maintain aspect ratio and relative positioning.

Scanline Fill Algorithm:
------------------------------------------------------------------------------
File: scanline.py
Function: scanline_fill()

Implements the scanline fill algorithm for polygon rasterization.
Uses an Edge Table (ET) and Active Edge Table (AET) to efficiently
fill polygon interiors. The algorithm:
1. Builds an Edge Table containing all polygon edges sorted by y-min
2. Processes scanlines from bottom to top
3. Maintains an Active Edge Table for edges intersecting current scanline
4. Fills pixel spans between edge pairs
5. Updates edge x-coordinates using inverse slopes

The frame buffer is a 501×501 array (indices 0-500) representing
the rasterized image, where 1 indicates a filled pixel and 0 indicates
an empty pixel.

Output Format:
------------------------------------------------------------------------------
File: helper.py
Function: write_pbm()

Outputs a PBM (Portable BitMap) image in ASCII format (P1).
The format consists of:
- Header: "P1"
- Dimensions: width height
- Pixel data: 0 (white/empty) or 1 (black/filled)
Pixel data is written row by row from top to bottom.

Compilation / Execution:
------------------------------------------------------------------------------
No compilation is required (Python interpreter used).

To build:
    make

This will create an executable script named `CG_hw3` (or refresh it if it already exists).

To run:
    ./CG_hw3 [options] > output.pbm

Dependencies:
------------------------------------------------------------------------------
Python 3.10 or later (installed on Tux)
Uses only standard modules: math, sys
No external libraries required.

