"""
Info functions
Created by \
18 / 03 / 18
"""
from parameters import *
import hoard
import weapons


def intro_screen():
    introstr = "PIOU PIOU WARS"
    introtxt = FONT2.render(introstr, True, WHITE, BLACK)
    introrect = introtxt.get_rect()
    introrect.center = (250, 350)

    pressstr = "Press space to play..."
    presstxt = FONT1.render(pressstr, True, WHITE, BLACK)
    pressrect = presstxt.get_rect()
    pressrect.center = (250, 370)

    DISPLAY.blit(BKG_IMG, (0, 0))
    DISPLAY.blit(SHIP_IMG, (240, 500))
    DISPLAY.blit(BUD_IMG, (50, 100))
    DISPLAY.blit(BUD_IMG, (200, 160))
    DISPLAY.blit(BUD_IMG, (100, 190))
    DISPLAY.blit(introtxt, introrect)
    DISPLAY.blit(presstxt, pressrect)


def draw_wave_num():
    wavestr = "Wave : " + str(hoard.Hoard.WAVE_NUM)
    wavetxt = FONT1.render(wavestr, True, WHITE, BLACK)
    DISPLAY.blit(wavetxt, (30, 40))


def pause_screen():
    pausestr = "Pause"
    pausetxt = FONT2.render(pausestr, True, WHITE, BLACK)
    pauserect = pausetxt.get_rect()
    pauserect.center = (250, 350)

    resumestr = "Press P to resume"
    resumetxt = FONT1.render(resumestr, True, WHITE, BLACK)
    resumerect = resumetxt.get_rect()
    resumerect.center = (250, 370)

    restartstr = "Press R to restart"
    restarttxt = FONT1.render(restartstr, True, WHITE, BLACK)
    restartrect = restarttxt.get_rect()
    restartrect.center = (250, 390)

    mutestr =   "Press M to turn SFX : OFF"
    unmutestr = "Press M to turn SFX :  ON"
    if weapons.Weapon.SFX_BOOL:
        mutebtnstr = mutestr
    else:
        mutebtnstr = unmutestr
    mutetxt = FONT1.render(mutebtnstr, True, WHITE, BLACK)
    muterect = mutetxt.get_rect()
    muterect.center = (250, 410)

    DISPLAY.blit(pausetxt, pauserect)
    DISPLAY.blit(resumetxt, resumerect)
    DISPLAY.blit(restarttxt, restartrect)
    DISPLAY.blit(mutetxt, muterect)


def lost_screen():
    loststr = "GAME OVER... "
    losttxt = FONT2.render(loststr, True, WHITE, BLACK)
    lostrect = losttxt.get_rect()
    lostrect.center = (250, 350)

    restartstr = "Press R to restart"
    restarttxt = FONT1.render(restartstr, True, WHITE, BLACK)
    restartrect = restarttxt.get_rect()
    restartrect.center = (250, 370)

    DISPLAY.blit(losttxt, lostrect)
    DISPLAY.blit(restarttxt, restartrect)


def won_screen():
    wonstr = "You Won !!!"
    wontxt = FONT2.render(wonstr, True, WHITE, BLACK)
    wonrect = wontxt.get_rect()
    wonrect.center = (250, 350)

    restartstr = "Press R to restart"
    restarttxt = FONT1.render(restartstr, True, WHITE, BLACK)
    restartrect = restarttxt.get_rect()
    restartrect.center = (250, 370)

    DISPLAY.blit(wontxt, wonrect)
    DISPLAY.blit(restarttxt, restartrect)
