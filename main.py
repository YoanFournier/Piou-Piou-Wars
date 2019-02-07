#!/usr/bin/env python3

"""
Main program
Created by \
13 / 03 / 18
"""
import sys
import ship, hoard, info, loot, weapons, alien
from wave import *
from parameters import *
from pygame.locals import *


def main():
    # ------------------- Reset Weapon list and Wave number and speed -------------------
    loot.Loot.LOOT = []
    ship.Ship.PlayerWeapon.WEAPONS = []
    alien.Bud.BudWeapon.WEAPONS = []
    alien.Carlo.CarloWeapon.WEAPONS = []
    alien.Roger.RogerWeapon.WEAPONS = []
    hoard.Hoard.WAVE_NUM = 0
    hoard.Hoard.SPEED = 0.3
    hoard.Hoard.DMG_FACTOR = 1

    # ------------------- Screen caption and object creation -------------------
    pygame.display.set_caption("Piou Piou Wars")
    player = ship.Ship(PLAYER_START_POS[0], PLAYER_START_POS[1])
    wave_num = 0
    wave = hoard.Hoard(WAVES[wave_num], player)
    for enemy in wave.alien_list:
        enemy.hoard = wave
        enemy.vy = wave.speed

    # ------------------- Loop conditions -------------------
    pause = False
    lost = False
    won = False
    intro = True

    # ------------------- Main loop -------------------
    while True:

        # ------------------- Intro screen -------------------
        if intro:
            info.intro_screen()
            for event in pygame.event.get():
                if event.type == KEYUP:
                    if event.key == K_SPACE:
                        intro = False
                    if event.key == K_r:
                        main()
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

        # ------------------- Pause screen -------------------
        if pause:
            info.pause_screen()
            for event in pygame.event.get():
                if event.type == KEYUP:
                    if event.key == K_p:
                        pause = False
                    if event.key == K_r:
                        main()
                    if event.key == K_m:
                        weapons.Weapon.SFX_BOOL = not weapons.Weapon.SFX_BOOL
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

        # ------------------- Loosing screen -------------------
        if lost:
            info.lost_screen()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYUP:
                    if event.key == K_r:
                        main()

        # ------------------- Winning screen -------------------
        if won:
            info.won_screen()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYUP:
                    if event.key == K_r:
                        main()

        pygame.display.update()
        FPS_CLOCK.tick(FPS)

        # ------------------- Game loop -------------------
        while not pause and not lost and not won and not intro:

            # ------------------- Next wave -------------------
            if not wave.alien_list:
                wave_num += 1
                if wave_num >= len(WAVES):
                    won = True
                else:
                    wave = hoard.Hoard(WAVES[wave_num], player)
                for enemy in wave.alien_list:
                    enemy.hoard = wave
                    if not enemy.type == REGIS or not enemy.type == ROGER:
                        enemy.vy = wave.speed

            # ------------------- Collision Control & Drawing Images -------------------
            DISPLAY.fill(BLACK)
            player.check_ship_pos()
            for unit in loot.Loot.LOOT:
                unit.check_collision_player(player)
                if unit.y > SCREEN_HEIGHT:
                    unit.destroy()
            for enemy in wave.alien_list:
                player.check_collision_enemy(enemy)
                if enemy.y > SCREEN_HEIGHT:
                    enemy.destroy(False)
                for unit in player.PlayerWeapon.WEAPONS:
                    enemy.check_collision(unit)
                    if unit.y < 0:
                        unit.destroy()
            for unit in alien.Bud.BudWeapon.WEAPONS:
                player.check_collision_weapon(unit)
                if unit.y > SCREEN_HEIGHT:
                    unit.destroy()
            for unit in alien.Carlo.CarloWeapon.WEAPONS:
                player.check_collision_weapon(unit)
                if unit.y > SCREEN_HEIGHT:
                    unit.destroy()
            for unit in alien.Roger.RogerWeapon.WEAPONS:
                player.check_collision_weapon(unit)
                if unit.y > SCREEN_HEIGHT:
                    unit.destroy()
            for unit in loot.Loot.LOOT:
                unit.new_pos()
                DISPLAY.blit(unit.img, unit.get_pos())
            for enemy in wave.alien_list:
                enemy.new_pos()
                DISPLAY.blit(enemy.img, enemy.get_pos())
            for unit in alien.Bud.BudWeapon.WEAPONS:
                unit.new_pos()
                DISPLAY.blit(unit.img, unit.get_pos())
            for unit in alien.Carlo.CarloWeapon.WEAPONS:
                unit.new_pos()
                DISPLAY.blit(unit.img, unit.get_pos())
            for unit in alien.Roger.RogerWeapon.WEAPONS:
                unit.new_pos()
                DISPLAY.blit(unit.img, unit.get_pos())
            for unit in player.PlayerWeapon.WEAPONS:
                unit.new_pos()
                DISPLAY.blit(unit.img, unit.get_pos())
            if player.check_lifes():
                lost = True
            player.new_pos()
            player.update()
            player.check_player_input()
            info.draw_wave_num()

            # ------------------- Input and Event Control -------------------
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == KEYDOWN:
                    if event.key == K_w:
                        player.TOP_BOOL = True
                    if event.key == K_s:
                        player.BOT_BOOL = True
                    if event.key == K_a:
                        player.LEFT_BOOL = True
                    if event.key == K_d:
                        player.RIGHT_BOOL = True
                    if event.key == K_SPACE:
                        player.SHOOT_BOOL = True

                if event.type == KEYUP:
                    if event.key == K_p:
                        pause = True
                    if event.key == K_n:
                        won = True
                    if event.key == K_w:
                        player.TOP_BOOL = False
                    if event.key == K_s:
                        player.BOT_BOOL = False
                    if event.key == K_a:
                        player.LEFT_BOOL = False
                    if event.key == K_d:
                        player.RIGHT_BOOL = False
                    if event.key == K_SPACE:
                        player.SHOOT_BOOL = False
                    if event.key == K_x:
                        player.SHOOT_BOOL = not player.SHOOT_BOOL

            # ------------------- Refresh Screen -------------------
            pygame.display.update()
            FPS_CLOCK.tick(FPS)


if __name__ == "__main__":
    main()
