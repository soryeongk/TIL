# Typescript Record

> 알고 있는 것과 직접 사용해보는 것의 차이를 많이 느끼는!! 왜 활용할 생각을 하지 않았는가!!

generic이나 union을 사용해 타입을 만들고 싶을 때에는 몇 가지 제약이 있습니다.

key 값은 다른 타입과 연관되어있고, 최종으로 만들고 싶은 모양은 다음과 같다고 가정하겠습니다.

```typescript
type MyObject = {
  A: boolean;
  B: boolean;
  C: boolean;
}
```

* union을 사용할 때

  ```typescript
  type MyKeys = "A" | "B" | "C";
  
  type MyObject = { [key: MyKeys]: boolean };
  ```

* keyof만 사용할 때

  ```typescript
  type OtherType = {
    A: string;
    B: string;
    C: string;
  };
  
  type MyKeys = keyof OtherType;
  
  type MyObject = { [key: MyKeys]: boolean };
  ```

두 경우 모두 다음과 같은 오류가 발생합니다.

```
An index signature parameter type cannot be a literal type or generic type. Consider using a mapped object type instead.
```

## Record를 사용해보자

```typescript
type OtherType = {
  A: string;
  B: string;
  C: string;
};

type MyObject = Record<keyof OtherType, boolean>;
```

이렇게 되면, otherType이 변경됨에 따라 MyObject의 key 값도 연결되어 원하는대로 사용이 가능합니다.
