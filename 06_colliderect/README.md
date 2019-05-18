# Pygame でゲームを作ろう

## 衝突判定を作ってみよう

この章では下記の内容を学習します。

- Rect同士の衝突判定の方法
- 衝突した方向の判別方法


### Rect同士の衝突判定

Rect同士の衝突を判定するには`Rect.collidrect()`を使います。
<br>
使い方は`あるrect.colliderect(別のrect)`です。
<br>
あるrectと別のrectが衝突している場合は`True`が返ってきます。
<br>
衝突していない場合は`False`が返ってきます。

実際のコードを見てみましょう。

このコードは移動している図形が、画面中央のブロックにぶつかると跳ね返るプログラムです。

##### 37-58行目

```python
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
```

少し長いですが見ていきましょう。

これまでは`move_ip()`で、rect自身の位置情報を更新していました。
<br>
しかし今回は`move()`で新たに移動後rectを作成しています。
<br>
これはあるrectがどの方向からぶつかったのかを判定するために使います。

```
if new_rect.colliderect(block_rect):
```

このコードで、移動後の図形がブロック図形と衝突しているかを判定します。
<br>
衝突している場合は`if`の中に入ります。

```
if circle_rect.right <= block_rect.left:
```

<br>
これは移動前の図形の右端が、ブロックの左端より左側にある場合という意味になります
<br>
これは図形が左側からブロックにぶつかったことを意味します。

また、移動前はブロックに左側にいたのに、移動後は右側がブロックの内側に埋まっています。
<br>
これでは良くないので `new_rect.right = block_rect.left`で、
図形の右側をブロックの左側の位置に移動させています

あとはx軸方向を逆に向ける必要があるので `dx = -dx`で方向転換しています。

```
elif circle_rect.left >= block_rect.right:
```

<br>
これは、移動前の図形の左側が、ブロックの右側より右にいる場合です。
<br>
図形が右側からブロックにぶつかったことを意味します。

こちらも先程同様、埋まっている場合の処理とx軸方向の方向転換を行います。

```
elif circle_rect.bottom <= block_rect.top:
elif circle_rect.top >= block_rect.bottom:
```

同様にこのコードはそれぞれ、上からブロックにぶつかった場合、下からブロックにぶつかった場合です。
これらの場合は `dy = -dy` とし、y軸方向の向きを変更しています。
これまで同様、埋まっている場合の処理も行います。

これで移動後のrect情報の更新が完了したので
<br>
画面の更新に利用している`circle_rect`を移動後のrect情報である`new_rect`に更新します。

これで図形はブロックに衝突したときに跳ね返る動きをします。


### まとめ

- rect同士の衝突判定にはrect.colliderect(rect)を使います。
- 衝突している場合はTrueを返します。
- 衝突していない場合はFalseを返します。
- 衝突方向を判別にするには`move()`を使って、移動後の`rect`を新たに作成します。
- 移動後のrectがブロックにぶつかった場合に、移動前のrectの位置を見てどの方向からぶつかったかを判断します。
