# D = 0.5 × rho × v² × Cd × A #
rho = 1.225
Cd = 0.3
A = 1.0
v = [50, 100, 150, 200, 250]
print(f"{'velocity':>12}{'drag force':>12}")
print("-"*26)
for v in v:
    D = 0.5 * rho * v**2 * Cd * A
    print(f"{v:>9.0f}m/s {D:>9.1f}")
