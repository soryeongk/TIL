# controlled vs uncontrolled component

리액트는 controlled component와 un-controlled component를 위한 훅을 각각 제공하고 있습니다.

그리고 각 영역을 침범해서는 안된다고 말하며, 각 컴포넌트가 어떻게 관리될지는 하나로 결정되어야 합니다.

각각의 예시는 다음과 같습니다.

```tsx
// controlled component
const ControlledInputComponent = (props: ControlledInputComponentProps) => {
  const [inputValue, setInputValue] = useState<string>(defaultValue);
  
  ...
  
  return <form onSubmit={onSubmitForm}>
  	<label>name</label>
    <input
      type="text"
      name="name"
      id="name-input"
      value={inputValue}
      onChange={(e) => setInputValue(e.target.value)}
    />
    <button type="submit" onClick={onClickSubmitButton}>submit</button>
  </form>
};

export default ControlledInputComponent;
```

```tsx
// uncontrolled component
const UncontrolledInputComponent = (props: UncontrolledInputComponentProps) => {
  const inputRef = useRef(defaultValue);
  
  const onSubmitForm = () => {
    ...inputRef.current.value...
  };
  
  ...
  
  return <form onSubmit={onSubmitForm}>
  	<label>soryeongk</label>
    <input
      type="text"
      name="name"
      id="name-input"
      ref={inputRef}
    />
    <button type="submit" onClick={onClickSubmitButton}>submit</button>
  </form>
};

export default UncontrolledInputComponent;
```

## 둘을 혼용하는 경우가 있나?

useRef와 useState를 함께 쓰는 것도 아닌데, 혼용하는 경우가 있을 수 있는가?를 살펴본다면, 다음과 같은 경우가 있습니다.

```tsx
type SpecialInputComponentProps = {
  // useState로 관리되는 state
  value?: string;
  // value를 변경하는 setState 함수
  onChangeValue?: (e: React.ChangeEvent<HTMLInputElement>) => void;
};

const SpecialInputComponent = ({ value, onChangeValue }: SpecialInputComponentProps) => {
  const [inputValue, setInputValue] = useState<string | null>(value || null);
  
  const onChangeSpecialInput = (e: React.ChangeEvent<HTMLInputElement>) => {
    ...setInputValue(e.target.value)...
  };
    
  useEffect(() => {
    onChangeValue?.(inputValue)
  }, [inputValue, onChangeValue])

  ...
  return (
  	<form>
    	<label>...</label>
      <input value={inputValue} onChange={onChangeSpecialInput} ... />
    </form>
  )
};
```

이 코드를 실행하면 작동하는 것만 본다면 딱히 문제가 없습니다.

하지만, 첫 렌더링 직후 혹은 input에 무언가 처음 입력되자마자 react는 콘솔에서 워닝을 뱉습니다.

```
Warning: A component is changing an uncontrolled input to be controlled.
This is likely caused by the value changing from undefined to a defined value, which should not happen.
Decide between using a controlled or uncontrolled input element for the lifetime of the component.
More info: https://reactjs.org/link/controlled-components
```

이 워닝을 해석해보면 다음과 같습니다.

> Uncontrolled input을 Controlled input으로 변경하고 있습니다.
>
> 이는 undefined(정의되지 않음)로 있던 값을 정의된 값으로 변경할 때 종종 나타나는데, 그래서는 안됩니다.
>
> 컴포넌트의 생명주기 동안에 해당 Input을 무엇으로 관리할지 결정하세요.

분명 상위 컴포넌트에서 value를 받아와 변경하고 있고, 컴포넌트 내부에 있는 input 또한 state로 관리되고 있으니 Controlled component가 아닌가? 생각하게 됩니다.

맞습니다. 대부분의 경우, 이 코드는 Controlled component로 보이고 문제가 없는 경우가 많습니다.

그런데, 이 컴포넌트의 입장에서 생각해보면 조금 다릅니다.

이 컴포넌트가 처음 탄생한 시점에 value값은 undefined가 될 가능성이 있습니다. props의 타입이 optional이기 때문입니다.

> props가 왜 optional인가?에 대해서는 본 컴포넌트가 어디서든 잘 사용될 수 있게 하기 위함입니다.
>
> 다른 곳에서 사용될 때, value나 onChangeValue 중 하나가 정의되지 않더라도 이 컴포넌트는 잘 작동할 수 있어야합니다.

초기값이 undefined인 채로 태어난 이 컴포넌트는 자신이 uncontrolled component라고 판단하게 됩니다.

더 이상 값이 들어올 의지가 보이지 않으니까요!

그런데 input에 다른 값이 들어오는 시점부터 갑자기 undefined인 줄 알았던 공간에 defined value가 들어오게 되면서 component의 정체성에 혼란이 오게 되는 것입니다..

그래서 애초에 Input의 value에는 undefined와 null이 들어가면 안됩니다.

때문에, input의 value에 값을 그대로 넘기지 말고 {value || ""}로 작성해주어야하며, input의 value를 관리하는 state의 type도 string으로 지정해 state가 담길 "안전한 바구니"를 만드는 것이 좋다고 생각합니다.

## 이게 그렇게 중요한가?

제법 중요한 이야기라고 생각합니다.

"controlled/uncontrolled component를 언제 사용해야하는가?"는 전적으로 개발자의 결정입니다.

각각이 가지는 장단점이 분명하고 상황은 너무 다양하기 때문입니다.

때문에, 두 컴포넌트의 동작과 사용법, 차이점 등을 잘 알고 적절한 상황에서 적절하게 사용하는 것은 매우 중요합니다.

1. controlled component는 관리가 용이합니다. immutable한 state로 관리되기 때문에, state를 수정하는 곳 또한 setState만이 가능하고 언제든 값의 제어와 제한이 가능합니다.

2. 반면에, uncontrolled component는 생명주기 동안에 외부 변화로부터 보호받지 못하고, 언제든 변경되거나 영향을 받을 가능성이 있습니다.

   > ref로 관리되는 것만이 uncontrolled component가 아닙니다. <input name="name" id="name" />로 정의된 input은 uncontrolled이고, window.name.value와 같은 접근으로 언제든 변경될 수 있습니다.

3. controlled component는 변화하는 값마다의 validation을 실시간으로 체크하고 화면에 반영할 수 있습니다. validation 체크를 실시간으로 할 필요가 없다면 uncontrolled component는 리렌더링을 줄이는 면에서 효과적입니다.

이런 면에서 상기 예시는 controlled component의 무결성(immutable)을 깨버리고 있습니다.

undefined로 정의된 곳에 갑자기 string을 넣기도 하고, 그 변화 역시 본 컴포넌트가 아닌 외부에 의해 제어되고 있기 때문입니다.
