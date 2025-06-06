#!/usr/bin/env python3
import sys
import math
import time
from PIL import Image

def separable_sobel(data, width, height):
    w, h = width, height
    size = w * h
    Gx1 = [0] * size
    Gy1 = [0] * size

    # First pass: horizontal (Gx1) and vertical (Gy1) derivatives
    for y in range(1, h - 1):
        row = y * w
        up  = row - w
        down = row + w
        for x in range(1, w - 1):
            idx = row + x
            Gx1[idx] = data[idx - 1] - data[idx + 1]
            Gy1[idx] = data[up + x] - data[down + x]

    # Second pass: smoothing to get final Gx, Gy
    Gx = [0] * size
    Gy = [0] * size
    for y in range(1, h - 1):
        row = y * w
        up  = row - w
        down = row + w
        # Vertical smoothing for Gx
        for x in range(w):
            i = row + x
            Gx[i] = Gx1[up + x] + 2 * Gx1[i] + Gx1[down + x]
        # Horizontal smoothing for Gy
        for x in range(1, w - 1):
            i = row + x
            Gy[i] = Gy1[i - 1] + 2 * Gy1[i] + Gy1[i + 1]

    return Gx, Gy


def sobel_edge_detection(input_path, output_path, threshold=None):
    # Load and gray-convert
    img = Image.open(input_path).convert('L')
    width, height = img.size
    data = list(img.getdata())

    # --- Start timing core algorithm ---
    t0 = time.perf_counter()
    Gx, Gy = separable_sobel(data, width, height)

    size = width * height
    mag2 = [0] * size
    max_mag2 = 0.0
    # Gradient magnitude squared + find max
    for i in range(size):
        m = Gx[i] * Gx[i] + Gy[i] * Gy[i]
        mag2[i] = m
        if m > max_mag2:
            max_mag2 = m

    max_mag = math.sqrt(max_mag2) if max_mag2 > 0 else 1.0
    scale = 255.0 / max_mag

    edge = [0] * size
    if threshold is not None:
        for i, m in enumerate(mag2):
            v = int(math.sqrt(m) * scale)
            edge[i] = 255 if v >= threshold else 0
    else:
        for i, m in enumerate(mag2):
            edge[i] = int(math.sqrt(m) * scale)

    t1 = time.perf_counter()
    print(f"Edge detection processing time: {t1 - t0:.3f} seconds")  # Core processing time

    # Save output
    out_img = Image.new('L', (width, height))
    out_img.putdata(edge)
    out_img.save(output_path)
    print(f"Sobel edge map saved to {output_path}")


def print_usage():
    print("Usage: python optimized_sobel.py <input_image> <output_image> [threshold]")
    print("  threshold: optional integer 0–255 to binarize edges")


if __name__ == '__main__':
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print_usage()
        sys.exit(1)

    inp = sys.argv[1]
    out = sys.argv[2]
    thr = int(sys.argv[3]) if len(sys.argv) == 4 else None
    sobel_edge_detection(inp, out, thr)
