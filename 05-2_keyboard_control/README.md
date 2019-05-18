# Pygame でゲームを作ろう

## キーボードで操作してみよう

この章では下記の内容を学習します。

- 押されたキーの判別方法


### 押されたキーの判別方法

マウスのボタンが押されたこと判定するには`pygame.key.get_pressed()`を使います。

`pygame.key.get_pressed()`はすべてのキーの状態を持った配列を返します。

ここで、その配列の中からどのキーが押されているか判別にするには
<br>
`K_LEFT`, `K_RIGHT`, `K_UP`, `K_DOWN`などの定数を利用します。

取得した配列の添字に`K_LEFT`などの定数を指定すると
<br>
`K_LEFT`ならば左矢印が押されている場合は`True`，押されていなければ`False`が格納されています。

コードで表現するとこのようになります。

```python
  if pressed_keys[K_LEFT]:
```

この場合、左矢印キーが押されていると`pressed_keys[K_LEFT]`が`True`となり
<br>
`if`文の中が実行されます。
 
 上記以外のキーの添字は下記のURLから確認できます。

 https://www.pygame.org/docs/ref/key.html


 これを使って、図形を矢印キーで操作してみましょう

 #####  31-40行目

 ```python
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_LEFT]:
            circle_rect.move_ip(-10, 0)
        if pressed_keys[K_RIGHT]:
            circle_rect.move_ip(10, 0)
        if pressed_keys[K_UP]:
            circle_rect.move_ip(0, -10)
        if pressed_keys[K_DOWN]:
            circle_rect.move_ip(0, 10)
```

`ed_keys = pygame.key.get_pressed()` でキーの状態の配列を取得します。

その中から、L_LEFT, K_RIGHT, K_UP, K_DOWNが押された場合野`if`文を記述しています。

それぞれ、rectを左に移動、右に移動、上に移動、下に移動という命令を記述しています。

これによってキーボードで図形を移動させることができます。

### まとめ

キーボードで図形を操作するには

- `pygame.key.pressed_keys()`でキーの状態を取得する。
- 取得した状態から、`K_LEFT`などの定数を利用して特定のキーの状態を判断する。