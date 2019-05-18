#!/usr/bin/env python
# coding: utf-8

import pygame
from pygame.locals import *
import sys

WIDTH, HEIGHT = 400, 300

def main():

    # ゲームの初期化
    pygame.init()
    clock = pygame.time.Clock()

    # 画面の作成
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('First Game')

    # キャラクターなどのオブジェクトの準備

    # 文字フォント
    font = pygame.font.Font(None, 32)
    character = font.render('Hello Pygame!', True, (255, 255, 255))
    character_rect = character.get_rect()
    character_rect.center = screen.get_rect().center

    while True:
        # 画面を #000000 で埋める
        screen.fill((0, 0, 0))

        screen.blit(character, character_rect)

        # 画面を更新
        pygame.display.update() 

        # イベント処理
        for event in pygame.event.get():
            # 閉じるボタンが押されたら終了
            if event.type == QUIT:
                # pygameの終了
                pygame.quit()
                sys.exit()

        clock.tick(30)

if __name__ == "__main__":
    main()