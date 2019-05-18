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
    circle_rect = circle.get_rect()
    pygame.draw.circle(circle, (255, 255, 255), (10, 10), 10)

    block = pygame.Surface((100, 100))
    block_rect = block.get_rect()
    block_rect.center = screen.get_rect().center
    pygame.draw.rect(block, (255, 255, 255), (0, 0, 100, 100))

    dx, dy = 5, 5

    while True:
        # 画面を #000000 で埋める
        screen.fill((0, 0, 0))

        screen.blit(circle, circle_rect)
        screen.blit(block, block_rect)

        new_rect = circle_rect.move(dx, dy)
        new_rect.clamp_ip(screen.get_rect())

        if new_rect.colliderect(block_rect):
            # 左からブロックにぶつかった
            if circle_rect.right <= block_rect.left:
                new_rect.right = block_rect.left
                dx = -dx
            # 右からブロックにぶつかった
            elif circle_rect.left >= block_rect.right:
                new_rect.left = block_rect.right
                dx = -dx
            # 上からブロックにぶつかった
            elif circle_rect.bottom <= block_rect.top:
                new_rect.bottom = block_rect.top
                dy = -dy
            # 下からブロックにぶつかった
            elif circle_rect.top >= block_rect.bottom:
                new_rect.top = block_rect.bottom
                dy = -dy

        circle_rect = new_rect
        
        # 上 についたら跳ね返る
        if circle_rect.top <= 0 or circle_rect.bottom >= 300:
            dy = -dy

        # 右 もしくは 左についたら跳ね返る
        if circle_rect.left <= 0 or circle_rect.right >= 400:
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