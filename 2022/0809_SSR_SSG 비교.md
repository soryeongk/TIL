# Next.js pre-rendering SSR vs SSG

Next.js에서 가장 많이 언급되는 pre-rendering 두 대장 SSR과 SSG에 대해서 비교를 해보았다.

현재 참여 중인 [타이어 커머스](https://tire.doctor-cha.com/)의 타이어 상세 페이지 작업 부분이다.

> 닥터차의 타이어 커머스?
> 주소: https://tire.doctor-cha.com/
> 타이어 사이즈만 입력하면 합리적인 가격에 타이어 확인과 장착점 예약까지 연결해주는 서비스입니다.

커머스의 특성상 상세 페이지는 한 번 등록된 후에 변경될 가능성이 매우 적습니다.

그래서 각 타이어별로 상세 페이지의 내용을 미리 빌드해둔다면 더 빠르게 접속하는 것도 가능할 것이라고 생각해

기존의 SSR 방식의 페이지를 SSG로 변경해보았습니다.

## getServerSideProps

```tsx
export const getServerSideProps: GetServerSideProps<
  TireFamilyPageProps
> = async ({ query }) => {
  const tireFamilyId = query[...];

  if (!tireFamilyId) {
    return {
      redirect: {
        permanent: false,
        destination: "/redirect-destination-url",
      },
    };
  }

  const response = await tireInstance.post("/...", {
    query: print(TIRE_FAMILY_PAGE_QUERY),
    variables: { tireFamilyId... },
  });

  ...

}
```

## getStaticPaths & getStaticProps

```tsx
type Params = {
  id: string;
} & ParsedUrlQuery;

export const getStaticPaths: GetStaticPaths<Params> = async () => {
  const response = await tireInstance.post("/...", {
    query: print(TIRE_FAMILY_IDS_QUERY),
    variables: { ... },
  });
  const data = response.data.data;

  const paths = data.tireFamilies.map((tireFamily) => ({
    params: {
      id: tireFamily.id,
    },
  }));

  return {
    paths,
    fallback: false,
  };
};

export const getStaticProps: GetStaticProps<
  TireFamilyPageProps,
  Params
> = async ({ params }) => {
  const tireFamilyId = params?.id;

  if (!tireFamilyId) {
    return {
      redirect: {
        permanent: false,
        destination: "/redirect-destination-url",
      },
    };
  }

  const response = await tireInstance.post("/...", {
    query: print(TIRE_FAMILY_PAGE_QUERY),
    variables: { tireFamilyId... },
  });

  ...
}
```

## 결과: 속도 차이

|     | requests | transferred | resources |  Finish   | DOMContentLoaded |   Load    |
| :-: | :------: | :---------: | :-------: | :-------: | :--------------: | :-------: |
| 😞 SSR |    49    |    6.7kB    |   1.9MB   | **5.37s** |    **196ms**     | **235ms** |
| :sparkles: SSG |    48    |    6.2kB    |   1.9MB   | **5.26s** |     **85ms**     | **130ms** |
