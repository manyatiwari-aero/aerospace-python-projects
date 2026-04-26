print("Hello Manya!")
name = "Manya"
age = 19
gravity = 9.81 #m/s^2
print(name, "is", age, "years old. Gravity =", gravity)

thrust = 5000    #newton
mass = 250       #kg
acceleration = thrust / mass
print("accelration =", acceleration, "m/s^2")

velocity = float(input("Enter final velocity (m/s):"))
time = float(input("Enter time (s):"))
acceleration = velocity/time
print("Äcceleration = ", acceleration, "m/s^2")

print(name, " College is KIIT. Studying in Branch Aerospace")

rocket_name = input("Enter rocket name: ")
fuel = float(input("Enter fuel in liters: "))
thrust = fuel * 9.81
print(rocket_name, "launches with thrust =", thrust, "N 🚀")