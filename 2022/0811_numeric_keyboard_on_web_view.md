# 모바일 웹 뷰에서 숫자 키패드 띄우기

서비스 개발을 하다보면, 숫자만 입력하더라도 자동 포멧팅에 의해 value가 string이 되어야하는 경우가 있습니다.

휴대전화번호가 가장 대표적인 예시입니다. 사용자에게는 숫자 `01012345678`만 입력하게 하고,

input에서는 자동으로 `010-1234-5678`으로 포멧팅을 한다고 가정해봅시다.

입력을 위해 input의 type은 `text`가 되어야하지만, 사용자의 편의를 위해 키패드는 숫자만 뜨는 것이 좋을 것 같습니다.

이 때, 웹 뷰에서 숫자 키패드를 띄우는 방법은 브라우저 별로가 아닌 OS별로 상이합니다.

하지만 대개, iOS와 안드로이드 모든 기기에서 동작하게 하는 것을 목표로 하기 때문에 아래 두 조건을 모두 포함하는 것을 추천합니다.

## iOS

```html
<input type="text" pattern="\d*" ... />
```

입력받는 값의 패턴을 지정하여 숫자 키패드만 올라오게 하는 것입니다.

## 안드로이드

```html
<input type="text" inputmode="numeric" ... />
```

inputMode를 따로 설정주어야합니다.
