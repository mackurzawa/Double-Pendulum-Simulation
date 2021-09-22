from math import sin as sin
from math import cos as cos

import pygame
import sys
import Constants

screen = pygame.display.set_mode((Constants.screen_width, Constants.screen_height))
x0 = Constants.screen_width/2
y0 = Constants.screen_height/6
trace = [(x0, y0 + Constants.r1 + Constants.r2) for i in range(Constants.trace_length)]
# trace = []
frame = 0

alpha1 = Constants.alpha1
alpha2 = Constants.alpha2
alpha1_v = 0
alpha2_v = 0
alpha1_a = 0
alpha2_a = 0

m1 = Constants.m1
m2 = Constants.m2

r1 = Constants.r1
r2 = Constants.r2

g = Constants.g
while True:
    screen.fill(Constants.bg_color)
    x1 = sin(alpha1) * r1 + x0
    y1 = cos(alpha1) * r1 + y0
    pygame.draw.aaline(screen, Constants.pendulum_color, (x0, y0), (x1, y1))
    pygame.draw.circle(screen, Constants.pendulum_color, (int(x1), int(y1)), m1)

    x2 = sin(alpha2) * r2 + x1
    y2 = cos(alpha2) * r2 + y1
    pygame.draw.aaline(screen, Constants.pendulum_color, (x1, y1), (x2, y2))
    pygame.draw.circle(screen, Constants.pendulum_color, (int(x2), int(y2)), m2)

    if frame%20 == 0:
        del trace[0]
        trace.append((x2, y2))
        print(len(trace))

    for i in range(len(trace)-1):
        pygame.draw.aaline(screen, Constants.trace_color, trace[i], trace[i+1])

    a1_temp1 = -g * (2 * m1 + m2) * sin(alpha1)
    a1_temp2 = - m2 * g * sin(alpha1 - 2 * alpha2)
    a1_temp3 = - 2 * sin(alpha1 - alpha2) * m2
    a1_temp4 = (alpha2_v * alpha2_v * r2 + alpha1_v * alpha1_v * r1 * cos(alpha1 - alpha2))
    a1_temp5 = r1 * (2 * m1 + m2 - m2 * cos(2 * alpha1 - 2 * alpha2))

    a2_temp1 = 2 * sin(alpha1 - alpha2)
    a2_temp2 = alpha1_v * alpha1_v * r1 * (m1 + m2)
    a2_temp3 = g * (m1 + m2) * cos(alpha1)
    a2_temp4 = alpha2_v * alpha2_v * r2 * m2 * cos(alpha1 - alpha2)
    a2_temp5 = r2 * (2 * m1 + m2 - m2 * cos(2 * alpha1 - 2 * alpha2))

    alpha1_a = (a1_temp1 + a1_temp2 + a1_temp3 * a1_temp4) / a1_temp5
    alpha2_a = (a2_temp1 * (a2_temp2 + a2_temp3 + a2_temp4)) / a2_temp5

    alpha1_v += alpha1_a
    alpha2_v += alpha2_a
    alpha1 += alpha1_v
    alpha2 += alpha2_v

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
    frame += 1
    pygame.display.flip()
