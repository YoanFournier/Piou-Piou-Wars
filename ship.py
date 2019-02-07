"""
Ship class
Created by \
13 / 03 / 18
"""
import time
from parameters import *
import weapons
import item


class Ship(item.Item):
    SHIP_WIDTH = 54
    SHIP_HEIGHT = 50
    SHIP_SPEED = 5
    SHIP_LIFES = 3
    SHIP_SHIELD = 3
    SHOOT_INTERVAL = 0.1
    SHIP_HP = 90
    SHIP_HP_COL = [0, 255, 0]

    def __init__(self, x, y):
        item.Item.__init__(self, x, y)
        self.x = x
        self.y = y
        self.lifes = Ship.SHIP_LIFES
        self.shield = 0
        self.instant_kill_time = time.time()
        self.vx = 0
        self.vy = 0
        self.pts = 0
        self.hp = Ship.SHIP_HP
        self.hp_col = Ship.SHIP_HP_COL[:]
        self.MOVE_BOOL = True
        self.stop_time = None
        self.TOP_BOOL = False
        self.BOT_BOOL = False
        self.LEFT_BOOL = False
        self.RIGHT_BOOL = False
        self.SHOOT_BOOL = False
        self.SHIELD_BOOL = False
        self.INSTANT_KILL_BOOL = False
        self.img = SHIP_IMG
        self.w = Ship.SHIP_WIDTH
        self.h = Ship.SHIP_HEIGHT
        self.last_shot = 0

    def shield_active(self):
        self.shield -= 1
        if self.shield == 0:
            self.SHIELD_BOOL = False

    def instant_kill_active(self):
        newtime = time.time()
        if newtime - self.instant_kill_time >= 5:
            self.instant_kill_time = newtime
            self.INSTANT_KILL_BOOL = False
            Ship.PlayerWeapon.WEAPON_DMG = 1
        if self.INSTANT_KILL_BOOL:
            Ship.PlayerWeapon.WEAPON_DMG = 50
            DISPLAY.blit(INSTANT_KILL_IMG, (self.x + self.w, self.y + 10))

    def check_ship_pos(self):
        if self.y == 0:
            self.y += Ship.SHIP_SPEED
        if self.y + self.h == SCREEN_HEIGHT:
            self.y -= Ship.SHIP_SPEED
        if self.x <= 0:
            self.x += Ship.SHIP_SPEED
        if self.x + self.w >= SCREEN_WIDTH:
            self.x -= Ship.SHIP_SPEED

    def stop_moving(self):
        new_time = time.time()
        if not self.MOVE_BOOL:
            if new_time - self.stop_time >= 1:
                self.MOVE_BOOL = True

    def check_player_input(self):
        if self.MOVE_BOOL:

            if self.SHOOT_BOOL:
                self.shoot()
            if not self.TOP_BOOL and not self.BOT_BOOL:
                self.stop_y()

            if self.TOP_BOOL and self.BOT_BOOL:
                self.stop_y()

            elif self.BOT_BOOL:
                self.go_bot()

            elif self.TOP_BOOL:
                self.go_top()

            if not self.LEFT_BOOL and not self.RIGHT_BOOL:
                self.stop_x()

            if self.LEFT_BOOL and self.RIGHT_BOOL:
                self.stop_x()

            elif self.LEFT_BOOL:
                self.go_left()

            elif self.RIGHT_BOOL:
                self.go_right()

    def update(self):
        DISPLAY.blit(self.img, (self.x, self.y))
        if self.SHIELD_BOOL:
            DISPLAY.blit(SHIELD_IMG, (self.x, self.y))
        self.stop_moving()
        self.instant_kill_active()
        self.draw_player_info()

    def draw_player_info(self):
        lifestr = "Ships left :    " + "x " + str(self.lifes)
        lifetxt = FONT1.render(lifestr, True, WHITE, BLACK)
        DISPLAY.blit(lifetxt, (320, 800))
        DISPLAY.blit(SHIP_ICON_IMG, (420, 792))

        pointstr = "Points : " + str(self.pts)
        pointtxt = FONT1.render(pointstr, True, WHITE, BLACK)
        DISPLAY.blit(pointtxt, (320, 770))

        hpstr = "HP : " + str(self.hp)
        hptxt = FONT1.render(hpstr, True, WHITE, BLACK)
        DISPLAY.blit(hptxt, (30, 800))
        pygame.draw.rect(DISPLAY, self.hp_col, (100, 801, self.hp, 5))

    def shoot(self):
        t = time.time()
        if t - self.last_shot >= Ship.SHOOT_INTERVAL:
            Ship.PlayerWeapon(self.x + Ship.SHIP_WIDTH / 2 - Ship.PlayerWeapon.WEAPON_WIDTH / 2, self.y, -15, LASER_4)
            Ship.PlayerWeapon(self.x + Ship.PlayerWeapon.WEAPON_WIDTH / 2, self.y, -10, LASER_3)
            Ship.PlayerWeapon(self.x + Ship.SHIP_WIDTH - 3/2 * Ship.PlayerWeapon.WEAPON_WIDTH, self.y, -10, LASER_3)
            self.last_shot = t

    def go_top(self):
        self.vy = -Ship.SHIP_SPEED

    def go_bot(self):
        self.vy = Ship.SHIP_SPEED

    def go_right(self):
        self.vx = Ship.SHIP_SPEED

    def go_left(self):
        self.vx = -Ship.SHIP_SPEED

    def stop_x(self):
        self.vx = 0

    def stop_y(self):
        self.vy = 0

    def change_hp_bar(self, dmg):
        col_change = dmg * 3
        if self.hp_col[0] + col_change <= 255 and self.hp_col[1] - col_change >= 0:
            self.hp_col[0] += col_change
            self.hp_col[1] -= col_change

    def check_collision_enemy(self, enemy):
        if self.check_collision_with(enemy):
            enemy.hp -= 1
            enemy.check_hp()
            if self.SHIELD_BOOL:
                self.shield_active()
            else:
                if self.hp - enemy.dmg > 0:
                    self.hp -= enemy.dmg
                    self.change_hp_bar(enemy.dmg)
                else:
                    self.hp -= self.hp
                    self.change_hp_bar(enemy.dmg)
            self.check_hp()

    def check_collision_weapon(self, weapon):
        if self.check_collision_with(weapon):
            weapon.destroy()
            if self.SHIELD_BOOL:
                self.shield_active()
                return
            elif weapon.type == C:
                self.stop_time = time.time()
                self.MOVE_BOOL = False
                self.TOP_BOOL = False
                self.BOT_BOOL = False
                self.LEFT_BOOL = False
                self.RIGHT_BOOL = False
                self.vx = 0
                self.vy = 0
            if self.hp - weapon.dmg > 0:
                self.hp -= weapon.dmg
                self.change_hp_bar(weapon.dmg)
            else:
                self.hp -= self.hp
                self.change_hp_bar(weapon.dmg)
            self.check_hp()

    def check_hp(self):
        if self.hp == 0 and self.lifes > 0:
            self.lifes -= 1
            self.hp = Ship.SHIP_HP
            self.hp_col = Ship.SHIP_HP_COL[:]

    def check_lifes(self):
        return self.lifes == 0

    def destroy(self):
        del self

    class PlayerWeapon(weapons.Weapon):
        WEAPONS = []
        WEAPON_WIDTH = 10
        WEAPON_HEIGHT = 26
        WEAPON_DMG = 1

        def __init__(self, x, y, speed, img):
            weapons.Weapon.__init__(self, x, y)
            self.img = img
            self.w = Ship.PlayerWeapon.WEAPON_WIDTH
            self.h = Ship.PlayerWeapon.WEAPON_HEIGHT
            self.vy = speed
            self.dmg = Ship.PlayerWeapon.WEAPON_DMG
            Ship.PlayerWeapon.WEAPONS.append(self)

        def destroy(self):
            if self in Ship.PlayerWeapon.WEAPONS:
                del Ship.PlayerWeapon.WEAPONS[Ship.PlayerWeapon.WEAPONS.index(self)]
            del self
