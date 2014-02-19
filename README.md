HalfImageSize
=============

## HalfImageSizeについて

Sublime Text2用のプラグインです。  
img要素のwidth, heightの値を半分にします。  
スマホサイトを作る場合に便利な痒いところに手が届くプラグインとなっています。

## 使い方

以下の様なimg要素に対して
```html
		<img src="hoge.jpg" width="100" height="100" />
```

img要素を選択した後、<kbd>ctrl</kbd>+<kbd>alt</kbd>+<kbd>h</kbd>を押すことで	
```html
		<img src="hoge.jpg" width="50" height="50" />
```
とwidth, heightの値が半分になります。

因みに要素を選択しなくても<kbd>ctrl</kbd>+<kbd>shift</kbd>+<kbd>h</kbd>を押すことで  
現在の**行**に対してwidth, heightの値を半分にすることができます。

また、<kbd>ctrl</kbd>+<kbd>alt</kbd>+<kbd>shift</kbd>+<kbd>h</kbd>を押すことで
現在の**ファイル**に対してwidth, heightの値を半分にします。
