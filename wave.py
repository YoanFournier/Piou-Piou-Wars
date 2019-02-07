"""
Waves Level Creator
Created by \
18 / 03 / 18
"""
from parameters import *
import random

options = [B, C, S]

WAVE1 = [[0, B, 0, B, 0],
         [B, 0, B, 0, B],
         [0, B, 0, B, 0],
         [B, 0, B, 0, B],
         [0, S, 0, S, 0],
         [B, 0, B, 0, B],
         [0, B, 0, B, 0],
         [B, 0, B, 0, B],
         [0, B, 0, B, 0],
         [B, 0, B, 0, B]]


def create_random_wave():
    wave = []
    for y in range(WAVE_HEIGHT):
        wave.append([])
        r = random.randint(0, 100)
        for i in range(WAVE_WIDTH):
            if y % 2 == 0:
                if 0 <= r < 60:
                    wave[y].append(B)
                elif 60 <= r < 90:
                    wave[y].append(S)
                elif 90 <= r <= 100:
                    if i % 2 == 0:
                        wave[y].append(C)
                    else:
                        wave[y].append(0)
    return wave


WAVES = []
for i in range(1):
    WAVES.append(create_random_wave())
WAVES.append([[REGIS]])
for j in range(1):
    WAVES.append(create_random_wave())
WAVES.append([[ROGER]])
