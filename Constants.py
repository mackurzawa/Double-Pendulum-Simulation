import math

screen_width = 1200
screen_height = 800

bg_color = (255, 255, 255)  # background color
pendulum_color = (0, 0, 0)
trace_color = (155, 155, 0)
trace_length = 70  # How many points will be remembered


g = 0.001  # Strength of gravity


alpha1 = math.pi/2  # Angle of the first pendulum at the start
alpha2 = math.pi/2  # Angle of the second pendulum at the start


m1 = 35  # Mass of the first pendulum
m2 = 20  # Mass of the second pendulum


r1 = 200  # Radius of the first pendulum
r2 = 300  # Radius of the second pendulum
