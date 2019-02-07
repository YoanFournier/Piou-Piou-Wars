"""
Loot class
Created by \
13 / 03 / 18
"""
from parameters import *
import item
import time


class Loot(item.Item):
    LOOT = []

    def __init__(self, x, y):
        item.Item.__init__(self, x, y)
        self.vy = 0.3
        Loot.LOOT.append(self)

    def destroy(self):
        if self in Loot.LOOT:
            del Loot.LOOT[Loot.LOOT.index(self)]
        del self


class Shield(Loot):
    SHIELD_WIDTH = 20
    SHIELD_HEIGHT = 20

    def __init__(self, x, y):
        Loot.__init__(self, x, y)
        self.img = SHIELD_ICON_IMG
        self.w = Shield.SHIELD_WIDTH
        self.h = Shield.SHIELD_HEIGHT

    def check_collision_player(self, player):
        if self.check_collision_with(player):
            self.destroy()
            player.SHIELD_BOOL = True
            player.shield = 3


class Firerate(Loot):
    pass


class Instantkill(Loot):
    INSTANT_KILL_WIDTH = 20
    INSTANT_KILL_HEIGHT = 20

    def __init__(self, x, y):
        Loot.__init__(self, x, y)
        self.img = INSTANT_KILL_ICON_IMG
        self.w = Instantkill.INSTANT_KILL_WIDTH
        self.h = Instantkill.INSTANT_KILL_HEIGHT

    def check_collision_player(self, player):
        if self.check_collision_with(player):
            self.destroy()
            player.INSTANT_KILL_BOOL = True
            player.instant_kill_time = time.time()


class HealthPack(Loot):
    HEALTHPACK_WIDTH = 20
    HEALTHPACK_HEIGHT = 19

    def __init__(self, x, y):
        Loot.__init__(self, x, y)
        self.img = SHIP_ICON_IMG
        self.w = HealthPack.HEALTHPACK_WIDTH
        self.h = HealthPack.HEALTHPACK_HEIGHT

    def check_collision_player(self, player):
        if self.check_collision_with(player):
            self.destroy()
            player.lifes += 1
