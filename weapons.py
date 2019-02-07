"""
Weapon class
Created by \
18 / 03 / 18
"""
import item
from parameters import *


class Weapon(item.Item):
    WEAPONS = []
    SFX_BOOL = True

    def __init__(self, x, y):
        item.Item.__init__(self, x, y)
        if Weapon.SFX_BOOL:
            SHOOT_SOUND.play()
        self.x = x
        self.y = y
        self.vy = None
        self.dmg = 0
        Weapon.WEAPONS.append(self)

    def destroy(self):
        if self in Weapon.WEAPONS:
            del Weapon.WEAPONS[Weapon.WEAPONS.index(self)]
        del self
