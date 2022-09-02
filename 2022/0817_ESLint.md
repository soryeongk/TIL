# ESLint 설정

클린코드 5장: 형식맞추기에도 나오는 내용이지만, 개발 협업에서 컨벤션은 정말 중요합니다.

지금까지의 프로젝트에서 ESLint를 설정해왔는데, 새로운 설정을 알게 되었습니다.

나의 팀원의 개발환경에서 ESLint가 제대로 작동하지 않을 때의 가이드라인입니다.

## ESLint를 설치합니다.

vscode extension에 ESLint가 설치되어 있어야 합니다.

정말 초보적이라서 놓칠 수 있는 실수입니다.

.vscode > settings.json에 코드를 추가하면 프로젝트별로 원하는 extension을 설치하는 것도 가능하다고 합니다.

## vscode 열 때, 해당 프로젝트 폴더에서만 열어야 합니다.

검색에서도 알기 어려운 부분이었는데, 레포가 포함된 상위 폴더를 여는 것도 안되고, 딱 그 레포에서 vscode를 열어야합니다.

## 이제 기본 설정

1. command/ctrl + shift + p를 눌러서 나오는 input에 format document with … 을 클릭해서 prettier가 default가 되도록 설정합니다.

  > 지금까지의 플젝에서는 prettier가 기본으로 형식을 맞추고 나머지 부분을 eslint가 잡아주는 정도였기 때문에 기본을 prettier로 했었습니다.

2. 좌측 explorer의 빈 곳에서 우클릭 > open folder setting을 클릭합니다. 혹은 그냥 command/ctrl + , 입력 후 좌측 상단에서 workspace를 선택합니다.
3. 그리고 format on save를 검색해 Editor: Format On Save를 true로 설정해줍니다. 이는 저장할 때마다 기본 포매팅 문서 형식에 맞춰 형식을 잡아주겠다는 말입니다!

이 부분은 아래 코드를 .vscode > settings.json에 넣어 공유하는 것과 동일합니다.

```json
{
  "editor.formatOnSave": true,
}
```

## prettier가 아닌 우리만의 ESLint만을 검사해서 형식을 맞추고 싶다면?

아래 코드를 .vscode > settings.json에 넣어 공유합니다.

```json
{
  "editor.formatOnSave": false,
  // 파일 저장 시 ESLint 실행
  "editor.codeActionsOnSave": {
      "source.fixAll": true,
  },
  "eslint.alwaysShowStatus": true,
  "eslint.validate": ["javascript", "javascriptreact", "typescript", "typescriptreact", "html", "markdown"]
}
```

저장마다 ESLint를 실행해 --fix하겠다는 의미이며, 본 린트가 적용될 파일은 "eslint.validate"에 배열로 담으면 됩니다.

"eslint.alwaysShowStatus"는 크게 중요한 부분은 아닌데, 우측 하단에서 ESLint의 서버 동작 여부를 늘 확인할 수 있도록 하는 설정입니다.

이걸로도 적용되지 않으면 ESLint와 다시 맞짱떠야함..
