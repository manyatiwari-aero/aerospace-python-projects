altitudes = [0, 1000, 5000, 10000, 20000]
for h in altitudes:
    P = 101325 * (1 - 0.0000226 * h) ** 5.256
    print(f"Altitude {h}m → Pressure {P:.0f} Pa")