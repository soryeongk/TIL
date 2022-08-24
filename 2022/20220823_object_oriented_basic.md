# 객체와 자료구조

타이어 예약/판매를 위한 사이트를 제작하면서 타이어 사이즈 입력(ex. 215/45R18)에 대해 다룰 일이 많았습니다.

타이어 사이즈는 `width`, `aspectRatio`, `wheelDiameter` 3개의 값으로 구성되어있습니다.

각 값을 객체로 가지고 있다가 원하는 시점에는 string(`000/00R00`)으로 변환해야합니다.

이 부분과 관련하여 지금까지 내가 싸던 똥💩을 생각해보면 다음과 같습니다.

```typescript
const handleTireSizeInput = (e: React.ChangeEvent<HTMLInputElement>) => {
	const value = e.target.value;

	// 입력값에 따라 타이어 사이즈 포맷에 맞게 변경
	blahblah
};

const convertToString = (tireSize: { width: number; aspectRatio: number; wheelDiameter: number; }) => {
	return `${width}/${aspectRatio}R${wheelDiameter}`;
};

const convertToObject = (tireSize: string) => {
	// 000/00R00을 다시 object로 바꾸는 코드
};

...
```

타이어 사이즈에 대한 다양한 메소들이 퍼져있습니다.

심지어 convertToString은 n개의 파일에서 중복으로 정의되어 사용됩니다.

고작 utils로 함수를 분리하는 것만으로는 명확한 해결책이 되지 못합니다.

객체의 측면에서 타이어 사이즈에 대한 메소드들을 한 곳에 모아 관리하는 편이 더욱 좋기 때문입니다.

## 객체로 바꾸자

그래서 승수님께서 변경해주신 코드는 다음과 같은 형태입니다.

```typescript
// tire-size.ts에서 class로 만들어 관리
class TireSize {
	width: number | null;
  aspectRatio: number | null;
  wheelDiameter: number | null;

	...

	toValidObject(): {
    width: number;
    aspectRatio: number;
    wheelDiameter: number;
  } {
    this.validate();

    return this.toObject() as {
      width: number;
      aspectRatio: number;
      wheelDiameter: number;
    };
  }

  private validateWidthForm(width: number) {
    return width >= 100;
  }

  private validateAspectRatioForm(width: number) {
    return width >= 30 && width <= 125;
  }

  toString(): string {
    let value = "";

    ...

    return value;
  }

	...
}
```

`TireSize` 클래스를 만들어 관리함으로써 유지보수가 더욱 쉬워졌습니다.

### 객체 지향으로 코드를 짜는게 무엇일까

클린코드의 예시를 보면 한 번에 와닿는다.

```javascript
// 절차적으로 짠 경우
class Square {
  topLeft: number;
  side: number;
}

class Rectangle {
  topLeft: number;
  height: number;
  width: number;
}

class Geometry {
  ...
  getArea(shape) {
    if (shape instanceof Square) {
      return shape.side * shpe.side;
    } else if (shape instanceof Rectangle) {
      return shape.width * shape.height;
    }
    ...
  }
  ...
}
```

위 코드는 각 클래스들의 공간을 침범하지 않고 둘레를 구하는 함수(getPerimeter)를 추가할 수 있다는 장점이 있다.

각 클래스들에 의존하고 있는 다른 함수들도 영향을 받지 않는다.

하지만 만약 원(Circle)을 추가하게 된다면 어떻게 될까?

Class Circle을 정의하고 getArea와 getPreimeter에 원을 위한 함수를 추가해야 한다.

---

객체 지향이라면 다음과 같은 코드가 될 수 있다.

```typescript
// 객체 지향으로 짠 경우 - 다형적
class Square {
  topLeft: number;
  side: number;
  
  ...
  
  get area() {
    return this.side * this.side;
  }

	get perimeter() {
    return this.side * 4;
  }
}

class Rectangle {
  topLeft: number;
  width: number;
  height: number;
  
  ...
  
  get area() {
    return this.width * this.height;
  }

	get perimeter() {
    return (this.width + this.height) * 2;
  }
}
```

여기에 Circle을 추가하더라도 나머지 클래스들과 함수의 영역은 침범하지 않고 새로운 클래스를 만들 수 있게 된다.

## 타이어 사이즈를 클래스로 관리하는 이유

1. 타이어 사이즈를 string으로 변환하는 방식이 215/45R17에서 215 45 17로 변경되었다고 가정했을 때, 해당 부분에 대한 수정을 한 곳에서 할 수 있다. (물론 이 부분은 단순히 util 함수로 분리하는 것만으로도 충분히 가능하다.)
2. 타이어 사이즈는 width, aspectRatio, wheelDiameter 각 값을 모두 가진 객체의 형태와 이를 변환한 string의 형태를 모두 갖고 있어야한다.
3. 객체와 문자열 모두 정확한 타입의 값이 들어오는지 확인하는 메소드가 필수적이며, 해당하지 않을 때에는 그에 맞는 예외를 던질 수 있어야한다.
