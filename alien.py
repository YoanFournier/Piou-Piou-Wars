"""
Alien class
Created by \
13 / 03 / 18
"""
from parameters import *
import item
import random
import weapons
import time
from math import sin, pi, sqrt
import loot


class Alien(item.Item):
    ALIENS = []

    def __init__(self, x, y, enemy):
        item.Item.__init__(self, x, y)
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.time = pi / 2
        self.hp = None
        self.w = None
        self.h = None
        self.hoard = None
        self.pts = None
        self.enemy = enemy

    def new_pos(self):
        self.x += self.speed_fct()[0]
        self.y += self.vy

    def speed_fct(self):
        return [self.vx, self.vy]

    def check_collision(self, bullet):
        if self.y + self.h > bullet.y > self.y and self.x < bullet.x + bullet.w and bullet.x < self.x + self.w:
            bullet.destroy()
            self.hp -= bullet.dmg
            self.check_hp()

    def check_hp(self):
        if self.hp <= 0:
            self.destroy(True)

    def give_pts(self):
        return self.pts

    def give_loot(self):
        if random.randint(0, 350) == random.randint(0, 350):
            loot.HealthPack(self.x, self.y)
        elif random.randint(0, 150) == random.randint(0, 150):
            loot.Shield(self.x, self.y)
        elif random.randint(0, 150) == random.randint(0, 150):
            loot.Instantkill(self.x, self.y)

    def destroy(self, points):
        if points:
            self.enemy.pts += self.give_pts()
        if self in self.hoard.alien_list:
            del self.hoard.alien_list[self.hoard.alien_list.index(self)]
        self.give_loot()
        del self


class Shroomy(Alien):
    SHROOMY_WIDTH = 25
    SHROOMY_HEIGHT = 24
    SHROOMY_HP = 3
    SHROOMY_VY = 0.5
    SHROOMY_PTS = 30
    SHROOMY_DMG = 10
    SHROOMY_DETECTION = 600

    def __init__(self, x, y, enemy):
        Alien.__init__(self, x, y, enemy)
        self.img = SHROOMY_IMG
        self.w = Shroomy.SHROOMY_WIDTH
        self.h = Shroomy.SHROOMY_HEIGHT
        self.hp = Shroomy.SHROOMY_HP
        self.type = S
        self.vy = Shroomy.SHROOMY_VY
        self.pts = Shroomy.SHROOMY_PTS
        self.dmg = Shroomy.SHROOMY_DMG

    def speed_fct(self):
        x = (self.enemy.x + self.enemy.w / 2) - (self.x + self.w / 2)
        y = (self.enemy.y + self.enemy.h / 2) - (self.y + self.h / 2)
        norm = sqrt(x ** 2 + y ** 2)
        if -Shroomy.SHROOMY_DETECTION <= y < 0:
            self.vy = -Shroomy.SHROOMY_VY * 10
            self.vx = x / norm * 3
        elif y < -Shroomy.SHROOMY_DETECTION:
            self.vy = -self.vy
            self.vx = 0
        elif Shroomy.SHROOMY_DETECTION > y > 0:
            self.vy = Shroomy.SHROOMY_VY * 10
            self.vx = x / norm * 3
        elif y > Shroomy.SHROOMY_DETECTION:
            self.vy = self.vy
            self.vx = 0
        elif y == 0:
            self.vy = 0
            self.vx = x / norm * 3
        return [self.vx, self.vy]


class Bud(Alien):
    BUD_WIDTH = 30
    BUD_HEIGHT = 22
    BUD_HP = 7
    BUD_VX = 0
    BUD_VY = 0.5
    BUD_PTS = 50
    BUD_DMG = 5

    def __init__(self, x, y, enemy):
        Alien.__init__(self, x, y, enemy)
        self.img = BUD_IMG
        self.w = Bud.BUD_WIDTH
        self.h = Bud.BUD_HEIGHT
        self.hp = Bud.BUD_HP
        self.vx = Bud.BUD_VX
        self.type = B
        self.pts = Bud.BUD_PTS
        self.dmg = Bud.BUD_DMG

    def new_pos(self):
        self.x += self.speed_fct()[0]
        self.y += self.vy
        self.shoot()

    def speed_fct(self):
        if self.y >= 0:
            self.time += 0.01
            self.vx = sin(self.time) * 0.7
        return [self.vx, self.vy]

    def shoot(self):
        t = random.randint(0, 500)
        if t == random.randint(0, 500):
            if (self.enemy.y - self.y) < 750:
                Bud.BudWeapon(self.x + self.w / 2 - 4, self.y, 3, LASER_1, self.enemy, self.hoard)

    class BudWeapon(weapons.Weapon):
        WEAPONS = []
        WEAPON_WIDTH = 8
        WEAPON_HEIGHT = 21
        WEAPON_DMG = 10

        def __init__(self, x, y, speed, img, enemy, hoard):
            weapons.Weapon.__init__(self, x, y)
            self.img = img
            self.enemy = enemy
            self.hoard = hoard
            self.type = B
            self.w = Bud.BudWeapon.WEAPON_WIDTH
            self.h = Bud.BudWeapon.WEAPON_HEIGHT
            self.vy = speed
            self.dmg = Bud.BudWeapon.WEAPON_DMG * self.hoard.dmg_factor
            Bud.BudWeapon.WEAPONS.append(self)

        def destroy(self):
            weapons.Weapon.destroy(self)
            if self in Bud.BudWeapon.WEAPONS:
                del Bud.BudWeapon.WEAPONS[Bud.BudWeapon.WEAPONS.index(self)]
            del self


class Carlo(Alien):
    CARLO_WIDTH = 35
    CARLO_HEIGHT = 25
    CARLO_HP = 15
    CARLO_VX = 1.5
    CARLO_PTS = 70
    CARLO_DMG = 5

    def __init__(self, x, y, enemy):
        Alien.__init__(self, x, y, enemy)
        self.img = CARLO_IMG
        self.w = Carlo.CARLO_WIDTH
        self.h = Carlo.CARLO_HEIGHT
        self.hp = Carlo.CARLO_HP
        self.vx = Carlo.CARLO_VX
        self.type = C
        self.pts = Carlo.CARLO_PTS
        self.dmg = Carlo.CARLO_DMG

    def new_pos(self):
        self.x += self.speed_fct()[0]
        self.y += self.vy
        self.shoot()

    def speed_fct(self):
        if self.x <= 10:
            self.vx = Carlo.CARLO_VX
        if self.x + self.w >= SCREEN_WIDTH - 10:
            self.vx = -Carlo.CARLO_VX
        return [self.vx, self.vy]

    def shoot(self):
        t = random.randint(0, 1000)
        if t == random.randint(0, 1000):
            if (self.enemy.y - self.y) < 750:
                Carlo.CarloWeapon(self.x + self.w / 2 - 4, self.y, 1, LASER_2, self.enemy, self.hoard)

    class CarloWeapon(weapons.Weapon):
        WEAPONS = []
        WEAPON_WIDTH = 20
        WEAPON_HEIGHT = 20
        WEAPON_DMG = 10

        def __init__(self, x, y, speed, img, enemy, hoard):
            weapons.Weapon.__init__(self, x, y)
            self.img = img
            self.enemy = enemy
            self.hoard = hoard
            self.type = C
            self.w = Carlo.CarloWeapon.WEAPON_WIDTH
            self.h = Carlo.CarloWeapon.WEAPON_HEIGHT
            self.vy = speed
            self.dmg = Carlo.CarloWeapon.WEAPON_DMG * self.hoard.dmg_factor
            Carlo.CarloWeapon.WEAPONS.append(self)

        def destroy(self):
            weapons.Weapon.destroy(self)
            if self in Carlo.CarloWeapon.WEAPONS:
                del Carlo.CarloWeapon.WEAPONS[Carlo.CarloWeapon.WEAPONS.index(self)]
            del self


# ------------------- Bosses -------------------
class Regi(Alien):
    REGI_WIDTH = 77
    REGI_HEIGHT = 96
    REGI_HP = 250
    REGI_VX = 0.8
    TIME = time.time()

    def __init__(self, x, y, enemy):
        Alien.__init__(self, x, y, enemy)
        self.img = REGI_IMG
        self.w = Regi.REGI_WIDTH
        self.h = Regi.REGI_HEIGHT
        self.hp = Regi.REGI_HP
        self.type = REGIS
        self.pts = 5000
        self.dmg = 90
        self.vx = Regi.REGI_VX

    def speed_fct(self):
        if self.x <= 10:
            self.vx = Regi.REGI_VX
            self.vy = 0.2
        elif self.x + self.w >= SCREEN_WIDTH - 10:
            self.vx = -Regi.REGI_VX
            self.vy = 0.2
        newtime = time.time()
        if newtime - Regi.TIME >= 3:
            Regi.TIME = newtime
            i = 25
            j = 10
            for x in range(3):
                i += 20
                unit = RegiPawn(self.x - i, self.y, self.enemy)
                self.hoard.alien_list.append(unit)
                unit.hoard = self.hoard
            for x in range(3):
                j += 20
                unit = RegiPawn(self.x + self.w + j, self.y, self.enemy)
                self.hoard.alien_list.append(unit)
                unit.hoard = self.hoard
        return [self.vx, self.vy]


class RegiPawn(Shroomy):
    REGI_PAWN_WIDTH = 15
    REGI_PAWN_HEIGHT = 28

    def __init__(self, x, y, enemy):
        Shroomy.__init__(self, x, y, enemy)
        self.img = REGI_PAWN_IMG
        self.w = RegiPawn.REGI_PAWN_WIDTH
        self.h = RegiPawn.REGI_PAWN_HEIGHT

    def destroy(self, points):
        if points:
            self.enemy.pts += self.give_pts()
        if self in self.hoard.alien_list:
            del self.hoard.alien_list[self.hoard.alien_list.index(self)]
        del self


class Roger(Alien):
    ROGER_WIDTH = 100
    ROGER_HEIGHT = 190
    ROGER_HP = 350
    ROGER_VX = 2
    ROGER_VY = 0.2
    SHOOT_INTERVAL = 0.5
    TIME = time.time()

    def __init__(self, x, y, enemy):
        Alien.__init__(self, x, y, enemy)
        self.img = ROGER_IMG
        self.w = Roger.ROGER_WIDTH
        self.h = Roger.ROGER_HEIGHT
        self.hp = Roger.ROGER_HP
        self.type = ROGER
        self.last_shot = 0
        self.pts = 10000
        self.dmg = 90
        self.vx = Roger.ROGER_VX
        self.vy = Roger.ROGER_VY

    def new_pos(self):
        self.x += self.speed_fct()[0]
        self.y += self.vy
        self.shoot()

    def speed_fct(self):
        if self.x <= 10:
            self.vx = Roger.ROGER_VX
        if self.x + self.w >= SCREEN_WIDTH - 10:
            self.vx = -Roger.ROGER_VX
        return [self.vx, self.vy]

    def shoot(self):
        t = time.time()
        if t - self.last_shot >= Roger.SHOOT_INTERVAL:
            Roger.RogerWeapon(self.x + self.w / 2 - 4, self.y + self.h, 5, SMILE, self.enemy, self.hoard)
            self.last_shot = t

    class RogerWeapon(weapons.Weapon):
        WEAPONS = []
        WEAPON_WIDTH = 50
        WEAPON_HEIGHT = 42
        WEAPON_DMG = 100

        def __init__(self, x, y, speed, img, enemy, hoard):
            weapons.Weapon.__init__(self, x, y)
            self.img = img
            self.enemy = enemy
            self.hoard = hoard
            self.type = ROGER
            self.w = Roger.RogerWeapon.WEAPON_WIDTH
            self.h = Roger.RogerWeapon.WEAPON_HEIGHT
            self.vy = speed
            self.dmg = Roger.RogerWeapon.WEAPON_DMG
            Roger.RogerWeapon.WEAPONS.append(self)

        def destroy(self):
            weapons.Weapon.destroy(self)
            if self in Roger.RogerWeapon.WEAPONS:
                del Roger.RogerWeapon.WEAPONS[Roger.RogerWeapon.WEAPONS.index(self)]
            del self
