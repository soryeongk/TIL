![의미있는 변수명을 고민하는 우리 모습](./photo/0819-meaningful-variable-names.png)

# 2장 의미있는 이름

- 의도를 분명히 밝히기

- 그릇된 정보 피하기

- 의미 있게 구분하기

- 발음하기 쉬운 이름을 사용하기

- 검색하기 쉬운 이름을 사용하기

- 자신의 기억력 자랑하지 말기

  > 작성자의 기억은 독자가 모른다.
  > ⇒ i, j, k 외의 자신만 아는 변수를 쓰는 것은 옳지 않다.

- 기발한 이름은 피하기

- 한 개념에 한 단어를 사용하기

  > 예를 들어, fetch/retrieve/get을 혼용하면 좋지 않다.
  > controller/manager/driver도 섞어쓰면 혼란스럽다.

- 말장난 금지

- 해법 영역에서 가져온 이름을 사용하기

  > 프로그래머에게 익숙한 기술 개념의 용어는 사용해도 된다.
  >
  > ⇒ 전산용어/알고리즘/패턴/수학 용어는 사용 가능

- 의미있는 맥락 추가하기

  > 그냥 name, street, city가 아니라 addr이라는 접두어를 추가해 addrName, addrStreet, addrCity로 쓰면 좋다.

- 불필요한 맥락 없애기

# 3장 함수

- 작게 만들기
- 한 가지 일만 하기
- 함수 당 추상화 수준은 하나로 하기
- 서술적인 이름 사용하기
- 함수 인수
- 부수 효과를 일으키지 말기
- 명령과 조회를 분리하기
- 오류 코드보다 예외를 사용하기
- 반복하지말기

## Tire-Squad에 적용해보기!

### useVehicleSpec.ts

코드가 길어질 땐 줄여보자

- 기존 코드

  ```typescript
  const search = async (input: { ownerName: string; plateNumber: string }) => {
    setState((state) => ({ ...state, loading: true }));
  
    try {
      const response = await tireInstance.post("/...", ...);
      const data = response.data.data;
  
      if (!data.vehicleSpec) {
        setState({
          loading: false,
          errorMessage: "해당 소유주명과 차량번호의 차량을 찾을 수 없습니다.",
          vehicleSpec: null,
        });
        return;
      }
  
      // 이 부분이 불필요하게 긴 것은 아닐까?
      const tireSizes: VehicleSpec["tireSizes"] = [];
      for (const subgrade of data.vehicleSpec.subgrades) {
        // 거의 20줄에 가까운 코드
        ...
      }
  
      const vehicleSpec = {
        ...input,
        brandName: data.vehicleSpec.brand.name,
        modelName: data.vehicleSpec.submodel.name,
        imageUrl: data.vehicleSpec.submodel.imageUrl,
        tireSizes,
      };
  
      setState(() => ({ loading: false, errorMessage: null, vehicleSpec }));
  
      ...
    } catch (error) {
      setState({
        loading: false,
        errorMessage: "차량 정보를 조회하는데 실패했습니다.",
        vehicleSpec: null,
      });
    }
  };
  ```

- 변경된 코드

  graphql의 타입과 연관되어 있어서 아래와 같이 가져오는 게 낫다고 생각하나, 실패했다 😧 → 해결법 고민 중

  ```
  VehicleSpecQuery["vehicleSpec"]["subgrades"]
  ```

  그래서 타입을 따로 만들었다.

  ```typescript
  type Subgrade = {
    id: string;
    name: string;
    tireSizes: { front: TireSize, rear: TireSize };
  }
  
  const getTireSizesBySubgrades = (
      subgrades: Subgrade[]
    ) => {
      const tireSizes = [];
      for (const subgrade of subgrades) {
        ...
      }
      return tireSizes;
    };
  ```

  ```typescript
  const search = async (input: { ownerName: string; plateNumber: string }) => {
    setState((state) => ({ ...state, loading: true }));
  
    try {
      const response = await tireInstance.post("/...", ...);
      const data = response.data.data;
  
      if (!data.vehicleSpec) {
        setState({
          loading: false,
          errorMessage: "해당 소유주명과 차량번호의 차량을 찾을 수 없습니다.",
          vehicleSpec: null,
        });
        return;
      }
  
      // 함수 분리!
      const tireSizes: VehicleSpec["tireSizes"] = getTireSizesBySubgrades(
        data.vehicleSpec.subgrades
      );
  
      const vehicleSpec = {
        ...input,
        brandName: data.vehicleSpec.brand.name,
        modelName: data.vehicleSpec.submodel.name,
        imageUrl: data.vehicleSpec.submodel.imageUrl,
        tireSizes,
      };
  
      setState(() => ({ loading: false, errorMessage: null, vehicleSpec }));
  
      ...
    } catch (error) {
      setState({
        loading: false,
        errorMessage: "차량 정보를 조회하는데 실패했습니다.",
        vehicleSpec: null,
      });
    }
  };
  ```

### 객체의 값을 하나씩 관리하자.

- 중복을 줄인다고 능사가 아니다.

- Object로 관리하면 유지보수가 힘들다. 각 값의 변동 원인은 달라질 수 있는데, 이렇게 합쳐두면 가독성도 떨어지고 분기처리도 힘들어지기 때문이다.

  - 유지보수 힘든 코드 예시 → 과거에 자주 싸던 똥 💩

    ```typescript
    const setVehicle = (
      key: string,
      vehicleSpec: { id: string; name: string } | string | null
    ) => {
      onChange?.((current) => {
        const obj = { ...current };
        obj[key] = vehicleSpec;
        return obj;
      });
    };
    ```

- 잘 적용된 코드

  ```typescript
  const setBrand = React.useCallback(
    (brand: { id: string; name: string } | null) => {
      onChange?.({ ...value, brand, model: null });
    },
    [onChange, value]
  );
  
  const setModel = React.useCallback(
    (model: { id: string; name: string } | null) => {
      onChange?.({ ...value, model });
    },
    [onChange, value]
  );
  
  const setPlateNumber = React.useCallback(
    (plateNumber: string | null) => {
      onChange?.({ ...value, plateNumber });
    },
    [onChange, value]
  );
  ```

### Button.tsx

button 자체의 type이 있기 때문에 혼용될 수 있다. 기존의 type을 `colorType` 이라고 변환.

```tsx
type ButtonProps = {
  className?: string;
  children?: React.ReactNode;
  // 🌻: button의 type과 헷갈리지 않을까? colorType은 어떨지?
  type?: "primary" | "default";
  // 🌻: textColor로 변경
  color?: "primary" | "error";
```
