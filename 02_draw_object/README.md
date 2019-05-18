# Pygame でゲームを作ろう

## 図形を描画しよう

この章では下記の内容を学習します。

- 図形の作成
- Surfaceとは
- 座標について
- 図形の描画

それではコードを見ていきましょう。

`02_draw_object.py` を開いてください。

### 図形の作成

前回学習した通り、Pygameの基本構成と同じような作りになっています。

違いをいくつか見ていきましょう

#### 線を描く

前回のコードでは、何もキャラクターは登場しなかったため、この部分のコードはありませんでした。

今回はいくつか図形を画面に表示します。

##### 19-20行目

```python
    line_surface = pygame.Surface((50, 80))
    pygame.draw.line(line_surface, (0, 95, 0), (0, 0), (80, 80), 5)
```

図形を作成するには、その図形を描くためのSurfaceを準備します。
<br>
Surfaceとは図形や画像などを表示するための紙のようなものです。

`pygame.Surface((50, 80))`では横50px、縦80pxのSurfaceを作って`line_surface`という変数に格納しています。

次に準備したSurface上に線を描くには`pygame.draw.line()`関数を使います。
<br>
引数は`pygame.draw.line(描くSurface, 色, 始点, 終点, 線の幅)`となります。
<br>
`pygame.draw.line(line_surface, (0, 95, 0), (0, 0), (50, 80), 5)`は
<br>
先程作った`line_surface`に`(0, 95, 0)`の色で、Surface上の`(0, 0)`の座標を始点、`(50, 80)`を終点とした直線を幅`5`pxので描くという意味になります。


#### 四角形を描く

##### 23-24行目

```python
    rect_surface = pygame.Surface((80, 50))
    pygame.draw.rect(rect_surface, (80, 0, 0), Rect(0, 0, 80, 50), 5)
```

四角形を描くには`pygame.draw.rect()`関数を使います。
<br>
引数は`pygame.draw.rect(描くsurface, 色, 四角形の大きさ, 線の幅)`です。
<br>
`pygame.draw.rect(rect_surface, (80, 0, 0), Rect(0, 0, 80, 50), 5)`は
<br>
先程作った`rect_surface`に`(80, 0, 0)`の色で`Rect(0, 0, 80, 50)`の大きさの線幅`5`pxの四角形を描くという意味になります。

ここで`Rect(0, 0, 80, 50)`が出てきましたがこれはRect（レクト）と良い、四角形の描写情報を表現したものです。
<br>
`(0, 0, 80, 50)`はそれぞれ`(0, 0)`から横80px、縦50pxの四角形という意味になります。

Rectはこの先さまざまな場面で利用します。頑張って覚えましょう。

#### 楕円を描く

##### 27-28行目

```python
    ellipse_surface = pygame.Surface((200, 100))
    pygame.draw.ellipse(ellipse_surface, (0, 0, 90), (0, 0, 200, 100), 5)
```

次は楕円を書く方法です。

楕円を描くには`pygame.draw.ellipse()`を使います。
引数は四角形を描くときと同じになります。

`ellipse()`を使うと、その四角形に内接した円を描くことができます。


#### 円を描く

##### 31-32行目

```python
    circle_surface = pygame.Surface((60, 60))
    pygame.draw.circle(circle_surface, (0, 50, 50), (30, 30), 30, 3)
```

円を描くには`pygame.draw.circle()`をつかいます。
引数は`pygame.draw.cirlce(描くsurface, 色, 円の中心、円の半径, 先の太さ)`になります。

`pygame.draw.circle(circle_surface, (0, 50, 50), (30, 30), 30, 3)`は
<br>
事前に作った`circle_surface`というsurfaceに`(0, 50, 50)`という色で、`(30, 30)`の位置に、半径`30`pxの円を線幅`3px`の円を描くという意味になります。

### 座標について

Scratchを使ったことのある人は座標という言葉を聞いたことがあると思います。
<br>
Scratchの座標は画面の中心を`(0, 0)`として、右に行くとX座標が増え、左に行くと減ります。
上に行くとY座標が増え、下に行くと減ります。

しかし、Pygameでは少し違います。
<br>
Pygameでは画面の左上の座標を`(0, 0)`とします。
<br>
X座標については、右に行くと増え、左に行くと減るということに関しては同じですが
<br>
Y座標は下に行くと増え、上に行くと減ります。

Scratchとは逆になるので気をつけましょう。


### 図形の描写

さて、ここまでで図形をsurfaceに描画することができました。
<br>
しかし、まだ画面には描画されていません。
<br>
図形を画面に描画するには`blit()`メソッドを使います。

#### 38-42行目
```python
        # 画面に描画
        screen.blit(line_surface, (0, 0))
        screen.blit(rect_surface, (100, 100))
        screen.blit(ellipse_surface, (200, 200))
        screen.blit(circle_surface, (200, 50))
```

`blit()`のレシーバは`screen`です。
<br>
`screen.blit()`とすることで呼び出すことができます。
<br>
引数は`blit(screenに描画するsurface, 位置)`です

`screen.blit(line_surface, (0, 0))`は`line_surface`を`(0, 0)`の位置に描画するという意味になります。
<br>
その他の図形も同様に`blit()`で`screen`に描画します。
<br>

ここまでで内部的には画面に図形が描画されている状態になりますが、
<br>
実際に目に見えるようにするには`pygame.display.update()`を実行する必要があります。

### まとめ

図形を描画するには

1. `Surface`を作成する
2. 作成した`Surface`に`draw()`を使って図形を描画する
3. `blit()`を使ってスクリーンに描画する
4. `pygame.display.update()`を使ってディスプレイを更新して画面に写す