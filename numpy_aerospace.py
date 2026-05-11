import numpy as np

v = np.linspace(0,300,50)

D = 0.5 * 1.225 * v**2 * 0.3 * 1.0

print(f"Max drag: {D.max():.1f}N")
print(f"Min drag: {D.min():.1f}N")
print(f"Speeds above 200 m/s: {v[v>200]}")
print(f"Number above 200: {len(v[v>200])}")
