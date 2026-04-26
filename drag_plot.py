import numpy as np
import matplotlib.pyplot as plt

rho = 1.225
A   = 1.0
Cd  = 0.3
Cl  = 1.2

v = np.linspace(0, 300, 200)

D = 0.5 * rho * v**2 * Cd * A
L = 0.5 * rho * v**2 * Cl * A

plt.figure(figsize=(8, 5))
plt.plot(v, D, 'r-',  linewidth=2, label='Drag force')
plt.plot(v, L, 'b--', linewidth=2, label='Lift force')
plt.xlabel('Velocity (m/s)', fontsize=12)
plt.ylabel('Force (N)',      fontsize=12)
plt.title('Aerodynamic forces vs velocity')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('drag_lift_plot.png', dpi=150, bbox_inches='tight')
plt.show()