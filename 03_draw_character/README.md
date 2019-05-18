# Pygame でゲームを作ろう

## 文字を描画しよう

この章では下記の内容を学習します。

- 文字の描画の方法

### 文字の描画の方法

文字を描画するには下記のコードを使って、文字を描いたsurfaceを作成します。

##### 23-24行目

```python
    font = pygame.font.Font(None, 32)
    character = font.render('Hello Pygame!', True, (255, 255, 255))
```

出来上がったsurfaceは図形のときと同じように利用します。

```python
    character_rect = character.get_rect()
    character_rect.center = screen.get_rect().center
```

rect情報を取り出し、表示位置を画面中央に設定します。

その後メインループの中で`blit()`することで画面に表示されます。

### まとめ

- `pygame.font.Font()`でフォントオブジェクトの作成
- `font.render()`で文字を描いたsurfaceの作成
- `screen.blit()`を使ってsurfaceを描画