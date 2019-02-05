#! /usr/bin/env python3

import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
import game_functions as gf


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Testo game")
    game_icon = pygame.image.load('images/testo_small.png')
    pygame.display.set_icon(game_icon)
    play_button = Button(screen, 310, "New game")
    highscores_button = Button(screen, 380, "High scores")

    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, highscores_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, play_button, highscores_button, ship, aliens, bullets)


run_game()
