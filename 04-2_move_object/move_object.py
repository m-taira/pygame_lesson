#!/usr/bin/env python
# coding: utf-8

import pygame
from pygame.locals import *
import sys

def main():
    # ゲームの初期化
    pygame.init()
    clock = pygame.time.Clock()

    # 画面の作成
    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption('First Game')

    # キャラクターなどのオブジェクトの準備
    circle = pygame.Surface((20, 20))
    pygame.draw.circle(circle, (255, 255, 255), (10, 10), 10)    
    circle_rect = circle.get_rect()

    dx, dy = 5, 5

    while True:
        # 画面を #000000 で埋める
        screen.fill((0, 0, 0))

        screen.blit(circle, circle_rect)
        circle_rect.move_ip(dx, dy)
        circle_rect.clamp_ip(screen.get_rect())

        if circle_rect.bottom >= screen.get_rect().bottom or circle_rect.top <= screen.get_rect().top:
            dy = -dy
        
        if circle_rect.left <= screen.get_rect().left or circle_rect.right >= screen.get_rect().right:
            dx = -dx

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