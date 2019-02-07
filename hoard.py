"""
Hoard class
Created by \
14 / 03 / 18
"""
from parameters import *
import alien


class Hoard:
    WAVE_NUM = 0
    SPEED = 0.3
    MAX_SPEED = 0.9
    DMG_FACTOR = 1

    def __init__(self, wave, enemy):
        self.wave = wave
        self.enemy = enemy
        self.alien_list = self.create_aliens()
        self.total = self.calc_total()
        self.speed = Hoard.SPEED
        self.dmg_factor = Hoard.DMG_FACTOR
        if Hoard.SPEED < Hoard.MAX_SPEED:
            Hoard.SPEED += 0.1
        if Hoard.WAVE_NUM % 5 == 0:
           Hoard.DMG_FACTOR += 1
        Hoard.WAVE_NUM += 1

    def create_aliens(self):
        alien_list = []
        y = - (len(self.wave) * ALIEN_Y_GAP + 10)
        for row in self.wave:
            x = ALIEN_X_START
            for unit in row:
                if unit == 0:
                    x += ALIEN_X_GAP
                    continue
                if unit == S:
                    alien_list.append(alien.Shroomy(x, y, self.enemy))
                    x += ALIEN_X_GAP
                if unit == B:
                    alien_list.append(alien.Bud(x, y, self.enemy))
                    x += ALIEN_Y_GAP
                    x += alien.Bud.BUD_WIDTH / 2
                if unit == C:
                    alien_list.append(alien.Carlo(x, y, self.enemy))
                    x += ALIEN_X_GAP
                if unit == REGIS:
                    alien_list.append(alien.Regi(220, y, self.enemy))
                if unit == ROGER:
                    alien_list.append(alien.Roger(220, y - 100, self.enemy))
            y += ALIEN_Y_GAP
        return alien_list

    def calc_total(self):
        return len(self.alien_list)

