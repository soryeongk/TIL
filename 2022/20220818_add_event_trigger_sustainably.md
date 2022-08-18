# 데이터 수집을 위한 이벤트 추적 심기 - 유지보수를 고려하면서 설계해보자!

서비스는 만들고 배포했다고 끝이 아닙니다.

유저가 잘 사용하고 있는지, 어떤 부분에서 망설이는지, 어떤 것에 가장 관심을 가지는지 등의 데이터를 수집하고 데이터를 보면서 의사결정을 하고 계속 서비스를 개선해나가는 과정이 필요합니다.

그런 면에서 프론트엔드 개발자는 정확한 데이터가 잘 수집될 수 있도록 이벤트를 심는 것이 매우매우매우 중요합니다.

너무 당연한 이야기지만, 한 번 클릭한 것에 대해서 렌더링 문제로 2번 클릭으로 수집되어도 안되고, 결제 페이지 진입 이벤트와 결제 시도 이벤트와 결제 완료 이벤트는 모두 다르게 수집되어야합니다.

아 이정도는 좀 어긋나도 괜찮겠지~라는 마인드로 다른 데이터가 수집되는 것을 방관해서는 안됩니다!!!

데이터는 매우 민감하고 예민한 친구이기 때문에 그 입맛에 맞게 잘 수집되어야합니다.

그래야 우리가 데이터로 의사결정하는 의미가 있을테니까요.

## 소위 말하는 노가다..

좋은 데이터를 수집하는 세팅은 생각보다도 더 귀찮습니다.

비슷한 일을 몇 번이고 반복하고, 제대로 수집되는지를 확인하는 등의 작업이 반복반복반복...

우리가 심은 gtm 데이터는 현재 다음과 같은 구조를 가지고 있습니다.

```ts
type ViewCartPageEvent = {
  event: 'view-cart-page-event';
  // Event로 전달될 데이터들 - 예) 장바구니 아이템 정보
  cartItems: {
    id: string;
    name: string;
    quantity: number;
    timestamp: string; // yy-mm-dd-hh-mm
  }[];
};

type ViewCartPageEventData = {
  // Event 데이터를 받기 위해 가져와야하는 데이터
  // 실제 UI에서 사용되는 데이터와 Event로 넘겨야하는 데이터는 다를 수 있기 때문에 따로 정의
  cartItems: {
    item: {
      id: string;
      name: string;
    };
    quantity: number;
	  timestamp: Date;
	}[];
};

const callViewCartPageEvent = (data: ViewCartPageEventData) => {
  const event: ViewCartPageEvent = {
    event: 'view-cart-page-event';
    
    cartItems: data.cartItems.map(cartItem => {
    	return {
    		id: cartItem.item.id,
    		name: cartItem.item.name,
    		quantity: cartItem.quantity,
    		timestamp: cartItem.timestamp.parseString(blah..)
  		}
  	})
  }

  pushToDataLayer(event)
};

export default callViewCartPageEvent;
```

실제 UI에서 사용하고 있는 데이터의 형태와 이벤트로 넘겨주는 데이터의 형태는 다를 수밖에 없습니다.

설계한 사람이 다르기 때문이죠!

그리고 각자의 이유로 언제든 다르게 더 변경될 수 있으니 더욱 분리된 후, Event 전송 전에 알아서 처리하게끔 하는 것이 맞습니다.

이렇게 만들어진 `callViewCartPageEvent`는 필요할 때마다 import하여 사용하면 됩니다.

## 유지보수가 너무 어려울 것 같다!

주1회 개발팀 전체가 참여하는 프론트엔드 개발 회고에서 이벤트를 이렇게 심는 것에 대해 유지보수의 어려움 이야기가 나왔습니다.

현재의 방식으로 이벤트를 심었을 때 발생하는 문제는 크게 2가지가 있습니다.

### 1. 이벤트를 보내는 페이지의 UI를 그릴 때는 사용되지 않던 데이터를 이벤트에 싣게 되는 경우

> P.S. 닥터차 개발팀은 현재 graphQL을 사용해 overfetch를 경계하고 필요한 데이터만을 query하고 있습니다.

예를 들어, 장바구니 페이지에 진입했을 때, 현재 장바구니에 담겨있는 모든 item의 array를 이벤트로 보낸다고 가정해보겠습니다.

이 때 필요한 데이터는 상기 예시처럼 `id`, `name`, `quantity`, `timestamp`가 있습니다.

그런데 정작 장바구니 페이지를 그리는 시점에는 timestamp는 사실 필요가 없다면, 이 페이지에 진입했을 때 어떻게 이벤트를 넘겨야할까요?

디자이너가 작업한대로 UI를 잘 만들었고, overfetch를 막기 위해 이 페이지에서는 사용되지 않는 timestamp는 query하지 않은 상황이라면?

상기 예시대로 작성되어있다면, timestamp를 query에 추가해 받아온 다음 넘겨주는 방법밖에 없습니다.

지금의 예시에서는 고작 하나의 데이터였지만, 만약 이런 데이터가 너무 많아진다면?

SSR 페이지에서 서버 데이터를 가공하는 과정을 한 번 거치고 있다면?

서비스가 성장하면서 이벤트 설계가 자주 많이 변경된다면? 그리고 UI는 UI대로 또 새롭게 변경된다면?

기획과 디자인은 언제든 변경될 수 있고, 그걸 빠르게 대응하고 반영하는 것은 개발자의 몫입니다.

우리는 변경이 발생할 때마다 데이터 하나하나를 확인하면서 이 query가 지금 UI에 쓰이는지, 이벤트에 쓰이는지 확인하고 추적하고 가공해야합니다.

사실 UI와 이벤트는 서로 데이터를 공유하고 있을 이유가 없습니다. 유지보수 시간이 너무 많이 듭니다.

그래서 나온 해결책은 상기 코드를 다음과 같이 수정하는 방향으로 합의했습니다.

```typescript
type ViewCartPageEvent = {
  event: 'view-cart-page-event';
  // Event로 전달될 데이터들 - 예) 장바구니 아이템 정보
  cartItems: {
    id: string;
    name: string;
    quantity: number;
    timestamp: string; // yy-mm-dd-hh-mm
  }[];
};

const CART_PAGE_QUERY = gql`
  query cartItems($userId: ID!) {
    item: {
      id
      name
    }
    quantity
    timestamp
  }
`;

const getViewCartPageEventData = async (userId: string) => {
  const response = await baseInstance.post('/graphql', {
    query: print(CART_PAGE_QUERY),
    variables: { id: userId },
  });

  return response.data;
};

const callViewCartPageEvent = (userId: string) => {
  const viewCartPageEventData = getViewCartPageEventData(userId);

  const event: ViewCartPageEvent = {
    event: 'view-cart-page-event';
    
    cartItems: viewCartPageEventData.cartItems.map(cartItem => {
    	return {
    		id: cartItem.item.id,
    		name: cartItem.item.name,
    		quantity: cartItem.quantity,
    		timestamp: cartItem.timestamp.parseString(blah..)
  		}
  	})
  }

  pushToDataLayer(event)
};

export default callViewCartPageEvent;
```

이벤트마다 필요한 데이터를 그 때 그 때 다시 서버 요청을 보내서 가져오는 것입니다!

"엥 서버 요청을 불필요하게 2번 하는 것은 너무 비효율적이지 않나요?"라는 의문에 대한 답은 아래와 같습니다.

1. 이벤트를 제대로 설계하기 위한 것이므로 불필요하지 않습니다.
2. 이벤트를 제대로 설계하고 유지보수를 쉽게 하기 위해 서버 요청을 한 번 더 보내는 것은 꽤나 가성비가 좋습니다. 큰 부하가 되지 않는다고 판단됩니다.

## 2. 비즈니스 로직에 의존하는 이벤트들이 너무 흩어져있습니다.

필요할 때마다 해당 이벤트 함수를 호출하는 것은 중복된 코드를 양산합니다.

가령, 장바구니에 아이템을 추가할 때마다 event를 보낸다고 가정하겠습니다.

장바구니에 아이템을 추가하는 곳은 제품 상세 페이지에서 "장바구니에 담기"라는 식의 버튼을 누르는 경우는 물론,

장바구니 페이지에서 "+"등의 버튼을 눌러서 수량을 증가하는 경우에도 아이템 추가 이벤트에 해당됩니다.

이 외에도 수많은 곳에서 장바구니에 아이템을 추가하는 로직이 사용될 것입니다.

로직이 추가될 때마다 그 페이지를 찾아가서 그 함수를 찾아서 이벤트를 등록한다면 `callAddCartItemEvent`라는 이벤트 함수를 계속 입력해둘 것입니다.

별 일 아닌 것 같지만, 사람은 언제든 실수할 수 있고, 비즈니스 로직에 의존하는 이벤트를 UI에 의존하여 심어두는 격이 됩니다.

이것에 대한 해결책은 다음과 같습니다.

1. 장바구니에 아이템을 추가하는 로직을 먼저 분리한다. - 예) cart class를 만들어 관리하는 등
2. 분리된 로직의 addItems라는 식의 함수 내에 이벤트를 심어둔다.

이렇게 되면 어떤 뷰가 추가되건, `addItems`라는 동작이 실행되면 자동으로 `callAddCartItemEvent`를 실행하므로 매번 중복된 코드를 추가할 필요가 없어집니다.
