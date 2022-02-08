# 내용 정리

> 20220208

## Flex

* `display: flex;` 로 플렉스 컨테이너 선언 가능

### flex-direction

* `flex-direction: row;`  기본값
* `column` 정렬 축을 y축으로
* `flex-direction: row/column-reverse` 정한 축에 대하여 역방향으로



### flex-wrap

* `flex-wrap: nowrap;` 기본값, 모든 요소를 한 줄에 정렬
* `wrap` 요소를 여러 줄에 걸쳐 정렬
* `wrap-reverse` 요소를 여러 줄에 걸쳐 반대로 정렬(wrap 에 중심축 대칭)



### flex-flow

* `flex-direction` + `flex-wrap`
* `flex-flow: column wrap;`



### justify-content

* `justify-content: center;` 요소들을 컨테이너의 가운데로 정렬
* `flex-start` 요소들을 컨테이너의 왼쪽으로 정렬
* `flex-end` 요소들을 컨테이너의 오른쪽으로 정렬
* `space-between` 요소들 사이에 동일한 간격을 둠
* `space-around` 요소들 주위에 동일한 간격을 둠



### align-items

* `align-items: center;` 요소들을 컨테이너의 y축 가운데로 정렬
* `flex-start` 요소들을 컨테이너의 y축 가장 위로 정렬
* `flex-start` 요소들을 컨테이너의 y축 가장 아래로 정렬
* `baseline` 요소들을 컨테이너의 시작위치에 정렬
* `stretch` 요소들을 컨테이너에 맞도록 늘림



### align-self

* `align-items` 가 사용하는 인자들을 값으로 받음
* 개별 요소에 적용할 수 있는 속성



### order

* 요소에 넣을 수 있는 속성
* 기본값은 0이며 음수/ 양수로 바꿀 수 있음



### align-content

* align-items 와 가장 큰 차이: 한 줄만 있을 때 align-content 는 효과가 없음
* = 줄 사이의 간격을 지정하는 명령
* `justify-content: center;` 여러 줄을 컨테이너의 가운데로 정렬
* `flex-start` 여러 줄을 컨테이너의 왼쪽으로 정렬
* `flex-end` 여러 줄을 컨테이너의 오른쪽으로 정렬
* `space-between` 여러 줄 사이에 동일한 간격을 둠
* `space-around` 여러 줄 주위에 동일한 간격을 둠
* `stretch` 여러 줄들을 컨테이너에 맞도록 늘림



## Bootstrap

## 그리드

```html
  <div class="container">
    <div class="row">
      <div class="col">
        <h1>Bootstrap Grid System 3</h1>
      </div>
    </div>
  </div>
```

* `container` `row` `col` 순
* `col-md-6` 식으로 뷰포트 크기에 맞게 변화시킬 수 있음



## 그 외

### 기본 선택자

* 전체 선택자 `*` 모든 태그 선택
* 요소 선택자 `<태그명>` 태그마다 지정해서 속성 변경 가능
* 클래스 선택자: `.<클래스명>` 으로 선택 가능
  * 일반적인 스타일링시 사용되는 것
* 자식 선택
* 아이디 선택자 : `#<아이디명>` 으로 선택 가능
* 인라인
* `!important`
  * 아래로 내려갈 수록 우선순위가 높음
  * 같은 우선순위에선 나중에 선언된 스타일이 우선
