# CS430 Extra Credit - PostScript Graphics Pipeline

## Program Features

This program implements a complete 2D graphics pipeline with the following features:

1. **PostScript File Parsing**: Reads and parses PostScript files containing drawing commands (moveto, lineto, curveto, stroke, Line) within `%%%BEGIN` and `%%%END` blocks.

2. **Bezier Curve Conversion**: Converts cubic Bezier curves to polylines using de Casteljau's algorithm with configurable segment count.

3. **2D Geometric Transformations**: Applies affine transformations in sequence:
   - Scaling (uniform or non-uniform)
   - Rotation (in degrees)
   - Translation (in X and Y directions)

4. **Line Clipping**: Uses the Cohen-Sutherland algorithm to clip polylines to a rectangular world window, removing geometry outside the viewing bounds.

5. **Viewport Mapping**: Maps coordinates from world space to viewport space using linear interpolation, allowing flexible display regions.

6. **PostScript Output Generation**: Generates valid PostScript code that can be rendered by PostScript viewers or printers.

7. **Command-Line Interface**: Supports comprehensive command-line arguments for all transformation, clipping, and viewport parameters.

## Language and Operating System

- **Programming Language**: Python 3.x
- **Operating System**: Cross-platform (Windows, macOS, Linux)
- **Tested on**: Windows 10

## Compiler/Interpreter

- **Interpreter**: Python 3.x interpreter (CPython)
- **No compilation required**: Python is an interpreted language
- **No external dependencies**: Uses only Python standard library modules (sys, math)

## Main File

The main entry point of the program is:
- **File**: `CG_hwEC.py`
- **Function**: `main()` (called when script is executed)

## How to Compile/Link the Program

This is a Python program and does not require compilation or linking. To run the program:

### Prerequisites
- Python 3.x must be installed on your system
- Verify installation: `python --version` or `python3 --version`

### Running the Program

1. **Navigate to the project directory**:
   ```bash
   cd extra_credit
   ```

2. **Run the program with default settings**:
   ```bash
   python CG_hwEC.py
   ```
   or
   ```bash
   python3 CG_hwEC.py
   ```

3. **Run with command-line arguments**:
   ```bash
   python CG_hwEC.py -f input.ps -s 2.0 -r 45 -m 10 -n 20
   ```

4. **Save output to a file**:
   ```bash
   python CG_hwEC.py -f input.ps > output.ps
   ```

### Command-Line Arguments

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `-f` | string | `ExtraCredit.ps` | Input PostScript file path |
| `-s` | float | `1.0` | Scale factor |
| `-r` | int | `0` | Rotation angle in degrees |
| `-m` | int | `0` | Translation in X direction |
| `-n` | int | `0` | Translation in Y direction |
| `-a` | int | `0` | World window left boundary |
| `-b` | int | `0` | World window bottom boundary |
| `-c` | int | `250` | World window right boundary |
| `-d` | int | `250` | World window top boundary |
| `-j` | int | `0` | Viewport left boundary |
| `-k` | int | `0` | Viewport bottom boundary |
| `-o` | int | `200` | Viewport right boundary |
| `-p` | int | `200` | Viewport top boundary |
| `-N` | int | `20` | Number of segments for Bezier curve approximation |

### Constraints

- World window: `a < c` and `b < d`
- Viewport X: `0 ≤ j < o ≤ 500`
- Viewport Y: `0 ≤ k < p ≤ 500`
- Bezier segments: `N > 0`

### Example Usage

```bash
python CG_hwEC.py -f hwEC.ps -s 2.0 -r 45 -m 10 -n 20 -a 0 -b 0 -c 100 -d 100 -j 50 -k 50 -o 450 -p 450 -N 30
```

## Project Structure

```
extra_credit/
├── CG_hwEC.py           # Main entry point (contains main())
├── parse_args.py        # Command-line argument parsing
├── parse_ps.py          # PostScript file parsing and writing
├── BezierCurve.py       # Bezier curve to polyline conversion
├── transform.py         # 2D transformation matrix operations
├── cohen_sutherland.py  # Line clipping algorithm
├── clip_polyline.py     # Polyline clipping wrapper
├── viewportMap.py       # World-to-viewport coordinate mapping
├── hwEC.ps             # Sample input PostScript file
└── ExtraCredit.ps      # Default input PostScript file
```

## Implementation Details

### Processing Pipeline

1. **Parse PostScript input** - Extract drawing commands from input file
2. **Convert Bezier curves** - Transform curves to polylines using de Casteljau's algorithm
3. **Apply transformations** - Scale, rotate, and translate geometry
4. **Clip to world window** - Remove geometry outside viewing bounds
5. **Map to viewport** - Transform coordinates to viewport space
6. **Generate PostScript output** - Write processed geometry as PostScript commands

### Supported PostScript Commands

- `x y moveto` - Move to point (x, y)
- `x y lineto` - Draw line to point (x, y)
- `x1 y1 x2 y2 x3 y3 curveto` - Draw cubic Bezier curve
- `x1 y1 x2 y2 Line` - Draw line from (x1, y1) to (x2, y2)
- `stroke` - Render the current path

All commands must be within `%%%BEGIN` and `%%%END` blocks.

## Output

The program outputs PostScript code to stdout. The output can be:
- Displayed in the terminal
- Redirected to a file for viewing in a PostScript viewer
- Sent directly to a PostScript printer
