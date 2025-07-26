import matplotlib.pyplot as plt
import random
import math
import numpy as np
import sys

# === CONFIGURATION ===
USE_RANDOM = True        # Set to True for random fractal, False for manual
VERTICES = 3              # Used only if USE_RANDOM is False
POINTS = 500000           # Used only if USE_RANDOM is False
JUMP_FRACTION = 1       # Used only if USE_RANDOM is False
SEED = 0                  # Used only if USE_RANDOM is False
USE_DYNAMIC = True       # Enable dynamic jump fraction
COLORMAP = "plasma"       # Matplotlib colormap name
OUTPUT_PATH = "fractal_plot.png"  # Output file name

def sigmoid(n):
    return 1 / (1 + math.exp(-n))

def generateJumpFraction(distance, f, sign, rng):
    if rng == 0:
        return abs(math.tanh(sigmoid(distance * sign))) + 1
    elif rng == 1:
        return abs(math.sqrt(abs(distance)) - 2)
    elif rng == 2:
        return math.tanh(distance) + 1
    elif rng == 3:
        return abs(f - 1)
    elif rng == 4:
        return math.sin(sigmoid(sign * distance))
    else:
        return math.log1p(math.sqrt(sigmoid(distance)))

def kodas(vertex_count=3, num_points=200000, jump_fraction=0.5, factorSeed=0, use_dynamic=True):
    vertices = [(math.cos(2 * math.pi * i / vertex_count), math.sin(2 * math.pi * i / vertex_count))
                for i in range(vertex_count)]

    x, y = 0.0, 0.0
    points = []
    original_jump_fraction = jump_fraction

    for _ in range(num_points):
        vx, vy = random.choice(vertices)

        if use_dynamic:
            distance = math.sqrt((vx - x)**2 + (vy - y)**2)
            sign = math.pow(-1, random.randint(0, 1))
            jump_fraction = generateJumpFraction(distance, original_jump_fraction, sign, factorSeed)

        x += (vx - x) * jump_fraction
        y += (vy - y) * jump_fraction

        if abs(x) > 1e308 or abs(y) > 1e308 or math.isnan(x) or math.isnan(y):
            print(f"Aborted at step {_}: overflow")
            break

        points.append((x, y))

    return points, vertices

def plotas(points, vertices, cmap_name="plasma", point_size=0.2, save_path="fractal_plot.png"):
    if not points:
        raise ValueError("No points generated")

    x_vals, y_vals = zip(*points)
    x_vals = np.clip(np.array(x_vals), -10, 10)
    y_vals = np.clip(np.array(y_vals), -10, 10)

    distances = np.sqrt(x_vals ** 2 + y_vals ** 2)
    distances = distances / distances.max() if distances.max() > 0 else np.zeros_like(distances)
    colors = plt.get_cmap(cmap_name)(distances)

    vx, vy = zip(*vertices)

    dpi = 400
    fig, ax = plt.subplots(figsize=(3840/dpi, 2160/dpi), facecolor="black", dpi=dpi)
    ax.set_facecolor("black")
    ax.scatter(x_vals, y_vals, s=point_size, c=colors, marker=".", linewidths=0)
    ax.scatter(vx, vy, color="white", marker="o", s=40, linewidths=0)
    ax.set_aspect('equal')
    ax.axis('off')
    plt.savefig(save_path, dpi=dpi, facecolor=fig.get_facecolor(), bbox_inches='tight')
    plt.close(fig)

def randomPlot():
    vertex_count = random.randint(3, 10)
    num_points = random.randint(100000, 1000000)
    jump_fraction = random.uniform(0.1, 2.0)
    factorSeed = random.randint(0, 5)
    cmap_name = random.choice(plt.colormaps())

    print(f"[Random] Vertices: {vertex_count}, Points: {num_points}, "
          f"Jump Fraction: {round(jump_fraction, 3)}, Seed: {factorSeed}, Colormap: {cmap_name}")

    points, vertices = kodas(
        vertex_count=vertex_count,
        num_points=num_points,
        jump_fraction=jump_fraction,
        factorSeed=factorSeed,
        use_dynamic=True
    )
    plotas(points, vertices, cmap_name=cmap_name)

if __name__ == "__main__":
    try:
        if USE_RANDOM:
            randomPlot()
        else:
            print(f"[Manual] Vertices: {VERTICES}, Points: {POINTS}, "
                  f"Jump Fraction: {JUMP_FRACTION}, Seed: {SEED}, "
                  f"Dynamic: {USE_DYNAMIC}, Colormap: {COLORMAP}")

            points, vertices = kodas(
                vertex_count=VERTICES,
                num_points=POINTS,
                jump_fraction=JUMP_FRACTION,
                factorSeed=SEED,
                use_dynamic=USE_DYNAMIC
            )

            plotas(points, vertices, cmap_name=COLORMAP, save_path=OUTPUT_PATH)
            print(f"Saved to {OUTPUT_PATH}")
    except Exception as e:
        print(f"ERROR: {e}")
        print("UNEXPECTED ERROR, MAYBE TRY OTHER PARAMETERS")
        sys.exit(1)
