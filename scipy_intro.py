from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt 

def falling_ball(t,y):
    altitude = y[0]
    velocity = y[1]
    g = 9.81
    return [velocity, -g]
y0 = [1000, 0]
t_span = (0, 20)
t_eval = np.linspace(0,15,300)

sol = solve_ivp(falling_ball, t_span, y0, t_eval=t_eval)

plt.figure(figsize=(9,4))
plt.subplot(1,2,1)
plt.plot(sol.t, sol.y[0], 'b-', linewidth=2)
plt.xlabel('Time (s)')
plt.ylabel('Altitude (m)')
plt.title('Falling Ball - Altitude')
plt.grid(True)

plt.tight_layout()
plt.savefig('falling_ball_scipy.png', dpi=150)
plt.show()
