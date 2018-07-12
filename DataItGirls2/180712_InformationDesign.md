# 데이터 시각화
## 큰 그림 이해하기
### 1. 여러 전통들:
* 통계그래픽스(Statistical graphics) - William Playfair, John Tukey
  * 막대그래프, 박스플랏 등 데이터를 설명하기 위한 (주로 기술 통계량) 통계량들을 어떻게 시각적으로 잘 보여줄 것인지의 측면에서 접근
* 전통적 지각심리(Gestalt psychology) - Max Wertheimer
  * 뇌는 어떤 이미지를 봤을 때 패턴을 찾아내는 것이라고 생각하면 편할 것
  * 무의식적으로라도 어떤 패턴이나 그림을 그려내는 것
* 생태-계산-신경-인지심리(Ecological-computational-neuro-cognitive psychology) - J. J. Gibson, David Marr, Colin Ware
  * 인간의 눈이 하는 일은 단순히 시각적 정보를 가져오는 것이 아니라 내가 어떤 일을 할 수 있는지에 대해서 파악할 수 있게 되는 것
  * "버튼은 버튼처럼 생겨야 이걸 누를 수 있게 된다."
* 소프트웨어 시스템 - Leland Wilkinson
  * 다양한 그래픽적 요소들을 어떻게 구현하는가에 대해서 체계적으로 정리한 것
  * Semiology of Graphics : 그래픽과 차트의 특성, 차이를 나타내는 방법 등에 대해서 말하는 책
* 중간 어딘가? Jacques Bertin, Edward Tufte, Stephen Few, Alberto Cairo
  * 번역본 : The functional arts

### 2. 데이터 시각화 왜 하나?
* 크게 보면, 컴퓨터와 사람이 협력하는 방식 중 하나.
* 컴퓨터가 잘하는 일은 컴퓨터가, 사람이 잘 하는 일은 사람이 하는 것.
* 서로 간의 대화를 하는 것(컴퓨터가 처리, 사람이 판단, 다시 지시... 반복)

* 컴퓨터가 잘 하는 일 :  많은 데이터를 빠르고 정확하게 처리하기
* 사람이 잘 하는 일: 패턴과 의미를 찾아내기
* 정확한 정의가 아직 모호
  * 불필요한 정보는 보지 않게 하기 위해서 하는 것이 아닐까
  * Information Design
  * Data Visualization
  * Data, Information, Knowledge, Wisdom

### 3. 체화된 인지 관점에서 바라보기.
* 데이터 시각화: 정보를 수동적으로 받아들이는 인식(perception)에 대한 것?
* 인터랙션 디자인: 몸을 능동적으로 움직이는 행동(action)에 대한 것?
* 인식적 행동(epistemic action)
	* 테트리스
	* 포커 게임
* 전통적 기준보다는 각 요소가 수행하는 기능이 중요
* 분산된 기능적 분해(Distributed Functional Decomposition)
	* 맹인의 지팡이는 인식 장치, 특히 보는 장치이다
	* Passive walker의 골격은 계산 장치(morphological computation)이다

### 4. 위 관점에서 인간과 컴퓨터를 서로 협력하는 하나의 시스템으로 바라보면 유익한 점이 많다.
* 초기 아이폰의 Notes 앱
* 지메일의 파일 첨부
* WiiMote의 입체 음향

### 5. 데이터 시각화란?
* 시각화된 표현은 외부로 확장된 기억 장치(externalized memory by Colin Ware, artificial memory by Jacques Bertin)
* 눈동자를 움직여서 질의(visual query)를 보내고 패턴 인식을 통해 답을 얻어내는 인터랙션

