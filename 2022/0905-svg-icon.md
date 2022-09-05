# html에서 svg 넣는 방법

개인적으로 사이트에서 사용되는 이미지의 파일 포멧을 png, svg 중 선택하는 기준은 다음과 같습니다.

- .png 파일: static하다. 비교적 크기가 크다.

- .svg 파일: interaction이 있을 수 있다. 비교적 크기가 작다. 깨질 위험이 있다.

  > svg는 연산에 가깝기 때문에 너무 큰 이미지에 대해서는 로딩 속도를 저하시킬 수 있어 장단점을 잘 비교해서 의사결정해야 합니다.

이러한 이유로 리액트에서 svg 파일을 사용할 때는 static asset보다는 React Component로 바라보고 사용하곤 합니다.

그런데 html에서 svg 이미지를 img 태그로 넣을 때를 생각해보면 alt 작성에서 항상 멈칫합니다.

아래와 같은 페이지를 만들 때 "이 아이콘의 alt는 뭘까..?"하는 고민이 들기 때문입니다.

![사진 첨부](./photo/0905-svg-example.png)

무지성으로 코드를 짜던 지금까지는 아래와 같이 입력했던 것 같습니다.

```html
<img src="exclamation-mark-with-circle.svg" alt="유의사항 아이콘" />
<img src="arrow-right-with-circle.svg" alt="한정수량 구매하기 버튼 아이콘" />
```

간혹, svg를 그대로 붙여넣기도 해봤지만, 유지보수의 측면에서 매우 좋지 않은 방법이라는 생각이 들었습니다 🧐

코드가 너무 길어져서 읽기 힘들어지고, 나중에 아이콘을 교체할 때는 파일을 교체하는 편이 훨씬 편하니까요!

웹 접근성에서의 alt가 원하는 내용이 이게 맞을까?에 대한 고민을 하면서 찾아보니, 역시 다른 방법이 있었습니다.

## embed 태그 사용하기

`<embed />` 를 사용해 다음과 같이 작성할 수 있습니다. 설명이 필요하다면 `aria-label`에 작성합니다.

```html
<embed
  src="exclamation-mark-with-circle.svg"
  type="image/svg+xml"
  aria-label="~~~"
/>
<embed
  src="arrow-right-with-circle.svg"
  type="image/svg+xml"
  aria-label="~~~"
/>
```

## object 태그 사용하기

`<object />` 를 사용해 다음과 같이 작성할 수 있습니다. 마찬가지로 설명이 필요하다면 `aria-label`에 작성합니다.

```html
<object
  data="exclamation-mark-with-circle.svg"
  type="image/svg+xml"
  aria-label="~~~"
>
  <object
    data="arrow-right-with-circle.svg"
    type="image/svg+xml"
    aria-label="~~~"
  ></object>
</object>
```

## iframe 태그 사용하기

`<iframe>`를 사용해 다음과 같이 작성할 수 있습니다. 마찬가지로 설명이 필요하다면 `aria-label`에 작성합니다.

```html
<iframe src="exclamation-mark-with-circle.svg" aria-label="~~~">
  <iframe src="arrow-right-with-circle.svg" aria-label="~~~"></iframe
></iframe>
```

css에서 iframe에 대해 `border: none;`을 추가해야 어색하지 않게 표현이 가능합니다.

## 무엇을 사용할까?

이상의 사진에서와 같은 표현을 위해서 제가 선택한 것은 object 입니다.

1. embed 태그는 html 문서 내에서 사용할 수 없는 데이터, 플러그인을 넣기 위한 것입니다. svg 아이콘을 넣기위한 용도로 사용되는 태그는 아닌 것 같습니다.
2. iframe태그는 현재 브라우저 문서 안에 또다른 html을 삽입하는데 주로 사용됩니다. inline frame 용 태그라는 점을 생각하면 svg 아이콘을 위한 것은 아닌 것 같습니다.
3. 간단한 도형 아이콘이라면 직접 svg를 작성하는 것이 더 나을 수도 있겠다는 생각을 했습니다. [svg 기본 도형 그리기(클릭)](https://a11y.gitbook.io/graphics-aria/svg-graphics/svg-basic-shapes)

## 아이콘 설명에 대하여

svg 아이콘의 alt에 대한 고민에서 시작된 이번 호기심덕분에 svg 아이콘 접근성에 대해 공부할 수 있었습니다.

관련 문서: [Graphics ARIA Guidebook: svg-icon-a11y(클릭)](https://a11y.gitbook.io/graphics-aria/svg-graphics/svg-icon-a11y)

아이콘이라도 의미를 가지는 것이 있고, 단지 UI 표현만을 위한 아이콘이 있습니다.

각각에 대해서는 `aria-`로 잘 조정해주어야합니다. 어떤 것이 스크린리더기에 읽히고 어떤 것이 무시될지 말이죠.

### 표현 아이콘

아이콘 자체는 의미를 가지지 않고 UI 표현만을 위한 아이콘으로, 스크린리더기에서 무시되어야합니다.

이 경우에는 `aira-hidden="true"`를 추가합니다.

### 의미 아이콘

별도의 라벨없이 아이콘이 의미를 가지는 경우에는 스크린리더기에 꼭 읽혀야합니다.

이 때는 `aria-label`에 아이콘의 의미를 작성합니다.
