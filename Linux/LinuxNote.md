# vi로 Binary 접근
* :%!xxd : hex 편집모드 
* :%!xxd -r : 원복

## Ubuntu 부팅 후 자동 실행 아래 파일에 추가
```
/etc/rc.local
```

# ImageMagicK 
moved :  http://dlwiki.finfra.com/for_staff:draft_doc:imagemagick
---
# Example
- source : http://www.albumbang.com/board/board_view.jsp?board_name=free&no=57
## 파일포맷변경
```
convert image_org.gif  image_out.jpg
```
[설명] image_org.gif  이미지를 image_out.jpg로 바꾼다.

```
convert image_org.png  image_out.jpg
```
[설명] image_org.png  이미지를 image_out.jpg로 바꾼다.





## 확대,축소,리사이즈

```
convert image_org.jpg -resize 25%x25% -quality 100 image_out.jpg
```
[설명] image_org.jpg  이미지를 1/4 축소한 image_out.jpg로 바꾼다.

```
convert image_org.jpg -resize 800x600 -quality 100 image_out.jpg
```
[설명] image_org.jpg  이미지를 800x600픽셀로 리사이즈 하지만 비율을 유지하며 큰사이즈 비율 기준으로 image_out.jpg를 생성한다.

```
convert image_org.jpg -resize 800x600\! -quality 100 image_out.jpg
```
[설명] image_org.jpg  이미지를 800x600픽셀로 강제적으로 바꾸어 image_out.jpg를 생성한다.

[설명] "-quality 100"이란 옵션을 주면 품질을 최대한 좋게한다.





## 회전

```
convert image_org.png -matte -background none -rotate 90
image_out.png
```
[설명] 이미지를 90도 회전하고 나머지 영역은 투명하게한다.

```
convert image_org.png -matte -background none -rotate -15
 image_out.png
 ```
[설명] 이미지를 -15도 회전하고 나머지 영역은 투명하게한다.





좌우반전,상하반전

```
convert -flop image_org.jpg  image_out.jpg
```
[설명] image_org.jpg  이미지를 좌우반전시켜 image_out.jpg 이미지를 생성한다.

```
convert -flip image_org.jpg  image_out.jpg
```
[설명] image_org.jpg  이미지를 상하반전시켜 image_out.jpg 이미지를 생성한다.





## 흑백,갈색 효과

```
convert image_org.jpg -colorspace gray image_out.jpg
```
[설명] image_org.jpg  이미지를 흑백효과를 적용하고 image_out.jpg 이미지를 생성한다.

```
convert image_org.jpg -sepia-tone 80% image_out.jpg
```
[설명] image_org.jpg  이미지를 갈색효과를 적용하고 image_out.jpg 이미지를 생성한다.





## 밝게,어둡게

```
convert image_org.jpg -sigmoidal-contrast 3,0% image_out.jpg
```
[설명] image_org.jpg  이미지를 밝게하여 image_out.jpg 이미지를 생성한다.

```
convert image_org.jpg -sigmoidal-contrast 3,100% image_out.jpg
```
[설명] image_org.jpg  이미지를 어둡게하여 image_out.jpg 이미지를 생성한다.





## 자르기(crop)

```
convert image_org.jpg -crop 800x600+10+20  image_out.jpg
```
[설명] image_org.jpg를 Left 10픽셀 Top 20픽셀 부터 800x600픽셀까지  자르고 그 결과로 image_out.jpg 이미지를 생성한다.

```
convert image_org.jpg -crop 800x600+10-30  image_out.jpg
```
[설명] image_org.jpg를 Left 10픽셀 Top -30픽셀 부터 800x600픽셀까지  자르고 그 결과로 image_out.jpg 이미지를 생성한다.





## 캔버스생성

```
convert -size 800x600 xc:white image_out.jpg
```
[설명] 800x600픽셀인 흰색 image_out.jpg 이미지를 생성한다.

```
convert -size 800x600 xc:skyblue image_out.gif
```
[설명] 800x600픽셀인 하늘색 image_out.jpg 이미지를 생성한다.

```
convert -size 800x600 xc:none image_out.png
```
[설명] 800x600픽셀인 투명 image_out.png 이미지를 생성한다.


## 글자이미지생성
```
convert -background white -fill black -font batang.ttf -pointsize 36 label:"Test\n한글" image_out.png
```
[설명] "Test\n한글"이란 글자로 image_out.png 이미지를 생성한다. (이미지배경은 흰색, 글자색은 검정색, 폰트는 바탕, 폰트사이즈는 36pt)


