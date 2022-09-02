# GraphQL query directive

@skip과 @include는 query 필드에서 사용되는 명령어입니다.
argument 값을 skip할지 include할지를 결정할 수 있게 합니다.

아래 예시 코드와 설명은 [여기(클릭)](https://dgraph.io/docs/graphql/queries/skip-include/)를 참고했습니다.

## @skip

아래 코드는 argument로 들어온 값 중에 if skipTitle의 값이 true가 되면 제목(title)을 가져오지 않고 넘어가도록 하는 코드입니다.

```gql
query ($skipTitle: Boolean!) {
  queryPost {
    id
    title @skip(if: $skipTitle)
    text
  }
}
```

```gql
{
    "skipTitle": true
}
```

## @include

아래 코드는 includeAuthor로 넘어온 값에 따라 저자(author)를 fetch할지를 결정합니다.

```gql
query ($includeAuthor: Boolean!) {
  queryPost {
    id
    title
    text
    author @include(if: $includeAuthor) {
      id
      name
    }
  }
}
```

```gql
{
    "includeAuthor": false
}
```

로그인 여부에 따라 가져올 정보를 구분할 때 유용하게 사용될 것 같습니다.

## @cascade

@cascade는 아래 query가 모두 포함될 때만 내용을 가져올 수 있도록 하는 명령어입니다. 아래 코드의 경우 reputation과 posts(text까지)을 모두 가진 경우에만 fetch하도록 합니다.

```gql
{
  queryAuthor @cascade {
    reputation
    posts {
      text
    }
  }
}
```
