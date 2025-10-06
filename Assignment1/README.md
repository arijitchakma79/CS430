Assignment: Homework 1
Author: Arijit Chakma
Language: Python 3
Operating System: Linux (Tux server compatible)
Main file: CG_hw1.py
Executable script: CG_hw1
Due Date: 6 October 2025.

Overview:
------------------------------------------------------------------------------
This program implements a simplified PostScript line drawing processor.
It reads a simplified PostScript input file, applies 2D geometric
transformations (scaling, rotation, and translation), clips the transformed
lines to a defined world window using the Cohen–Sutherland algorithm, and
outputs a simplified PostScript file suitable for rendering with Ghostscript.

The input and output formats follow the specification provided in the
assignment. Only commands between %%%BEGIN and %%%END are processed.

File Structure:
------------------------------------------------------------------------------
CG_hw1              (executable script)
CG_hw1.py           (main program)
parse_args.py       (argument parser)
parse_ps.py         (PostScript reader/writer)
transform.py        (transformation logic)
cohen_sutherland.py (clipping algorithm)
README.txt

How to run the program:
------------------------------------------------------------------------------
First use the command chmod +x CG_hw1 to make the file executable.
Then use the command ./CG_hw1 [options] to run the program.

Examples:
    ./CG_hw1 -f hw1.ps > out.ps
    ./CG_hw1 -f hw1.ps -s 0.8 -r 10 -m 85 -n 25 > hw1_out.ps
    ./CG_hw1 -f hw1.ps -a -25 -b -50 -c 399 -d 399 > worldwindow.ps

View output using:
    gs hw1_out.ps  (if you have Ghostscript installed.)


Clipping Implementation:
------------------------------------------------------------------------------
File: cohen_sutherland.py
Function: clip_line(self, x1, y1, x2, y2)
Lines: 29–60

Implements the standard Cohen–Sutherland line clipping algorithm using
bitwise region codes to determine whether a line should be accepted,
rejected, or clipped against the world window.

When a line is completely outside the window, a debug message is printed:
    (x1, y1), (x2, y2) outside of window.


Compilation / Execution
------------------------------------------------------------------------------
No compilation is required (Python interpreter used).

To make the script executable:
    chmod +x CG_hw1

Then run:
    ./CG_hw1 [options]

Dependencies:
------------------------------------------------------------------------------
Python 3.10 or later (installed on Tux)
Uses only standard modules: math, sys
No external library used.

Notes
------------------------------------------------------------------------------
- Code runs correctly on Tux without any special libraries.
- Output verified using Ghostscript, installed locally.
- All debug output is written to stderr.

