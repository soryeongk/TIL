
야구친구 홈페이지는 매일 업데이트된 순위표와 함께 세 줄 요약을 적어두는데, 그 맨션을 가져오고 싶다!


```python
from urllib import request
from bs4 import BeautifulSoup

url = "http://www.yachin.co.kr/rankTable/"
with request.urlopen(url) as f:
  html = f.read().decode('utf-8')

bs = BeautifulSoup(html, 'html5lib')

```


```python
yachin_contents = bs.select('div.content div div')

yachin = [t.text.strip().replace('\n', '') for t in content_elements]  # 제목을 텍스트만 리스트에 담음
```

야구친구 홈페이지의 경우,  순위 후 바로 오늘 경기 리뷰를 3줄 남기므로 titles리스트에 담긴 내용 중 9~11인덱스가 그 내용에 해당


```python
for s in yachin[9:12]:
    print(s)
```

    - 연패의 끝, 그 선봉은 신재영!
    - SK, 롯데 잡고 2위 탈환!
    - 이틀 연속 엄청난 경기 펼친 잠실..
    

애란쌤의 조언으로 다시 해보자!

```HTML이 엉망이라 깔끔하게 가져올 방법이 없겠어요. 저라면 `select_one('.board_t_slide')` 하신 후 얻어진 엘리먼트의 다음 형제(next sibling)을 얻어오고 그 children 중 text가 있는 애들만 뽑는 식으로 할 것 같아요.```


```python
brief_elements = bs.select_one('.board_t_slide').nextSibling.nextSibling.select('div')
briefs = [b.text for b in brief_elements if b.text.strip() != '']
print(briefs)
```

    ['- 연패의 끝, 그 선봉은 신재영!', '- SK, 롯데 잡고 2위 탈환!', '- 이틀 연속 엄청난 경기 펼친 잠실..']
    

```
<div>
    <div class='x'>A</div>
    <div class='y'>B</div>
</div>```

x의 다음 형제는 y가 아니라 빈 텍스트. 따라서 y를 가리키기 위해서는 다음 다음 형제를 가져와야 함

```
<div class='x'>A</div><div class='y'>B</div>
```

이렇게 열고 닫는 명령 사이에 공백이 없을 때는 다음 형제를 가져오면 y를 가리킴
