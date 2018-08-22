```
"따로 시간을 내서 자기계발할 자신이 없다면, 하루 중 가장 많은 시간을 보내는 업무 중에 성장하자!"
																			   by. 애란쌤
```

혼자 공부할 때 어떻게 예외처리를 잘 찾아낼 수 있을까? 애란쌤은 대단해

* 도서추천 : 소프트웨어 테스팅 법칙 293가지
* QA(Quality Assurance )  품질 보증
* SW Testing

>   QA(Quality Assurance)는 품질보증을 뜻합니다. 어떤 실체(품목, Entity)가 품질 요구 사항을 충족하는 것에 대한 적절한 신뢰감을 주기 위하여 품질시스템에서 실시되고 필요에 따라 실증되는 모든 계획적이고 체계적인 활동을 말합니다. 
>
>   QC(Quality Control)는  품질관리를 뜻합니다. 품질관리란 기업 경영상 제일 유리하다고 생각되는 품질을 보장하고 이것을 가장 경제적 제품으로서 생산하는 방법을 말합니다. 또한 품질에 대한 요구 사항을 만족시키기 위해 사용되는 운영상의 기법 및 활동을 말합니다. 
>
>   즉, 품질보증은 고객의 관점에 많은 비중을 두는 활동이며, 해당 제품에 대한 좀 더 포괄적인 책임을 지는 역할입니다.
>
>   품질관리(QC)는 제품에 많은 비중을 둔다고 볼 수 있는데, 제품의 목적에 준한 기능을 검증하는 역할을 수행합니다.
>
>   품질보증은 고품질(High-Quality)을 위해 품질관리보다 넓은 활동을 수행한다고 볼 수 있습니다.   

# Tidy Data

> 깔끔한 형태의 데이터, 즉 다루기가 편해서 분석에 적합한 데이터

도서관 데이터를 조금 더 다듬자. 어떤 부분을 다듬을 수 있는가?

* 지역 관련 정보를 통일

* 지역 칼럼을 별도로 분리

* 휴관일 양식을 통일 -> 어떻게?

* 위도랑 경도 분리 혹은 위경도 삭제

  -> 필요없는 데이터를 굳이? (그럼 필요있/없을 어떻게 알아?)

* 전화번호 양식을 통일(옛날 번호 처리)

## 데이터 다듬기

* 하나의 칼럼에는 하나의 내용만 (위경도, 휴관일)
* 하나의 행에는 하나의 observation이 담긴다.
* 일별 데이터가 나오다가 일주일 평균이 나오는 등 성격이 다른 데이터가 함께 묶여있으면 안됨



# Naver Clova AI

* 네이버와 라인이 함께 만든 AI 프로그램
* search도 AI의 일종이기 떄문에 Clova와 통합
* 영상, 음성, 추천, 언어 4가지 부류
  * 눈으로 들어오는 것
  * 청각적인 인식이 있고 다시 표현
  * 고객맞춤형 서비스 제공
  * 그리고 귀로 듣고 눈으로 봤던 것들을 무엇인지 이해하는 것
* 