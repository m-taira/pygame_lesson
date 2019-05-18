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
    pygame.display.set_caption('Draw Object')

    # ゲームキャラなどを初期化
    # (0, 0) から (50, 80) まで線幅5pxで#009500の直線を描く
    line_surface = pygame.Surface((50, 80))
    pygame.draw.line(line_surface, (0, 95, 0), (0, 0), (50, 80), 5)

    # 幅80px、高さ50pxの長方形を線幅5pxの#800000の色で描く
    rect_surface = pygame.Surface((80, 50))
    pygame.draw.rect(rect_surface, (80, 0, 0), Rect(0, 0, 80, 50), 5)

    # 幅150px、高さ50の矩形に内接する線幅5の#000090の円を描く
    ellipse_surface = pygame.Surface((200, 100))
    pygame.draw.ellipse(ellipse_surface, (0, 0, 90), (0, 0, 200, 100), 5)

    # (30, 30)に半径30pxの円を描く
    circle_surface = pygame.Surface((60, 60))
    pygame.draw.circle(circle_surface, (0, 50, 50), (30, 30), 30 )

    while True:
        # 画面を #000000 で埋める
        screen.fill((0, 0, 0))

        # 画面に描画
        screen.blit(line_surface, (0, 0))
        screen.blit(rect_surface, (100, 100))
        screen.blit(ellipse_surface, (200, 200))
        screen.blit(circle_surface, (200, 50))

        # 画面を更新
        pygame.display.update() 

        # イベント処理
        for event in pygame.event.get():
            # 閉じるボタンが押されたら終了
            if event.type == QUIT:
                # pygameの終了
                pygame.quit()
                sys.exit()
        clock.tick(63)

if __name__ == "__main__":
    main()