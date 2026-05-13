import numpy as np
import matplotlib.pyplot as plt
v = np.linspace(0, 300, 200)
D = 0.5 * 1.225 * v**2 * 0.3 * 1.0 
L = 0.5* 1.225 * v**2 * 1.2 * 1.0
plt.figure(figsize=(8,5))
plt.plot(v,D, 'r-', linewidth=2, label='Drag')
plt.plot(v,L, 'b--', linewidth=2, label='Lift')
plt.xlabel('Velocity(m/s)')
plt.ylabel('Force(N)')
plt.title('Aerodynamic forces vs Velocity')
plt.legend() 
plt.grid(True)
plt.tight_layout()
plt.savefig('aero_forces.png', dpi=150)
plt.show()
