Not CLI anymore

Reverted back to normal py file.


Usage:


This Python script generates fractals using a configurable set of parameters. The fractals can be saved as images or displayed dynamically. Below is a guide to using the script.

## Requirements
- Python 3.x
- Required libraries: `matplotlib`, `numpy`

Install the required libraries using:pip install matplotlib numpy


## Configuration
The script can be configured by modifying the following variables at the top of the file:

- **USE_RANDOM**: Set to `True` for random fractal generation, or `False` for manual configuration.
- **VERTICES**: Number of vertices for the fractal (used only if `USE_RANDOM` is `False`).
- **POINTS**: Number of points to generate (used only if `USE_RANDOM` is `False`).
- **JUMP_FRACTION**: Fraction of the distance to jump towards a vertex (used only if `USE_RANDOM` is `False`).
- **SEED**: Seed for dynamic jump fraction calculation (used only if `USE_RANDOM` is `False`).
- **USE_DYNAMIC**: Enable dynamic jump fraction calculation (`True` or `False`).
- **COLORMAP**: Name of the Matplotlib colormap to use for coloring the fractal.
- **OUTPUT_PATH**: File path to save the generated fractal image.

## Running the Script
### Random Mode
Set `USE_RANDOM = True` to generate a fractal with random parameters. Run the script using:


### Manual Mode
Set `USE_RANDOM = False` and configure the parameters manually. Run the script using the py file.

### Output
- The fractal image will be saved to the file specified in `OUTPUT_PATH`.
- If `USE_RANDOM` is enabled, the script will print the random parameters used for generation.

## Example
To generate a fractal with 5 vertices, 500,000 points, and a jump fraction of 0.5:
```python
USE_RANDOM = False
VERTICES = 5
POINTS = 500000
JUMP_FRACTION = 0.5
USE_DYNAMIC = False
COLORMAP = "plasma"
OUTPUT_PATH = "fractal_plot.png"


Enjoy creating beautiful fractals!