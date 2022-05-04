# Vue

## Vue.js

* 사용자 인터페이스를 만들기 위한 자바스크립트 프레임워크
* SPA(single page aplication)을 지원

### SPA

* 단일 페이지 애플리케이션
* 현재 페이지를 동적으로 렌더링함으로써 사용자와 소통하는웹 애플리케이션
* 단일 페이지로 구성되며 서버로부터 최초에만 페이지를 다운로드하고 이후 동적으로 DOM 구성
  * 즉, 현재 페이지 중 필요한 부분만 동적으로 다시 작성
* 연속되는 페이지 간의 사용자 경험을 향상
  * 트래픽 감소, 속도, 사용성, 반응성 향상
* 동작 원리의 일부가 CSR(client side rendering)을 따름

### CSR

* 서버에서 화면을 구성하는 SSR과 달리 클라이언트에서 화면을 구성

* 처음엔 뼈대만 받고 브라우저에서 동적으로 DOM을 그림
* 장점
  * 서버 - 클라이언트 간 트래픽 감소
* 단점
  * SSR에 비해 전체 페이지 최종 렌더링 시점이 느림
  * SEO(검색 엔진 최적화)에 어려움이 있음 (최초 문서에 데이터 마크업이 없어서)

### SSR

* 서버에서 클라이언트에 보여줄 페이지를 모두 구성하여 전달
* ex) `{% for article in articles %} ...`
  * django template engine(서버)가 
* 장점
  * 초기 구동 속도가 빠름
  * SEO에 적합
* 단점
  * 모든 요청마다 새로운 페이지를 구성하여 전달
  * 상대적으로 트래픽이 많아 서버의 부담이 클 수 있음



### 동작

* DOM과 Data가 연결되어 있고 Data를 변경하면 이에 연결된 DOM이 알아서 변경
  * 오직 Data에 대한 관리만 신경쓰면 됨

### MVVM

* Model, View, ViewModel
* Model
  * JS 오브젝트
  * key - value
* View
  * HTML
* ViewModel
  * DOM 과 Data의 중계자



## 선언형 프로그래밍

### 선언적 렌더링

```html
<h2>선언적 렌더링</h2>
<div id="app1">
  {{ message }}
</div>
```

```javascript
new Vue({ // VM
  el: '#app1', //어떤 HTML과 묶일지
  data: { // Data
    message: '안녕하세요 Vue'
  }
})
```

## Basic syntax

### Vue instance

* 모든 뷰 앱은 Vue 함수로 새 인스턴스를 만듬

### el

* 뷰 인스턴스에 연결할 DOM요소를 지정

### data

* 뷰 인스턴스의 데이터 객체
* 인스턴스의 상태 데이터를 정의
* 뷰 템플릿에서 interpolation을 통해 접근 가능
* v-bind, v-on 같은 directive에서도 사용 가능
* 객체 내 다른 함수에서 this로 접근 가능

### methods

* 뷰 인스턴스에 추가할 메서드
* 화살표 함수를 메서드를 정의하는데 사용하면 안됨
  * this가 window를 가리키게 됨



## Template syntax

### Interpolation

* 문자열
  * {{ message }}
* 원시 HTML
  * `<span v-html="rawHtml"></span>`
  * XSS 취약점으로 이어질 수 있으므로 사용자가 제공한 콘텐츠에서는 절대 사용하지 말것

### Directive

#### text

* `<p v-text="message"></p>`
  * `<p>{{ message }}</p>` 와 같은 동작
  * 사용자는 `<p>안녕하세요</p>` 로 렌더링이 완료된 페이지를 보게 됨

#### show

* `v-show="isTrue"`
  * 평가된 값이 true 면 태그가 보여짐
  * false 라면 `style ="display:none"` 속성이 추가돼 숨겨짐

#### if

* `v-if`, `v-else-if`, `v-else`
  * `v-if="seen"`
  * `<p v-if="myType === 'A'">A</P>`
  * `<p v-else-if="myType === 'B'">B</P>`
  * `<p v-else>C</P>`
    * 조건을 만족하지 않는 태그는 문서에도 보이지않음
    * 최초 로드 비용이 감소하지만, 자주 변경되는 요소(토글)의 경우 다시 렌더링 하기때문에 비용이 증가할 수 있다

#### for

* `<div v-for="item in items">{{ item }}</div>`
  * string : char 하나씩
  * array : 기본적으로 요소 / enumerate와 비슷한 사용도 가능
    * `<div v-for="(item, idx) in arr">{{ item }}</div>`
      * idx가 뒤에 나옴 주의
  * object : 기본적으로 value만 나옴
    * `<div v-for="(value, key) in obj">{{ key }}:{{ value }}</div>`
      * value, key 순서 주의
  * 언제나 `key`를 추가해야함
    * 뭐든 상관 없지만 독립적이어야함 = idx를 사용하고싶음
    * `<div v-for="(item, idx) in items">{{ item }} :key="idx"> </div> `
  * 가능하면 v-if 와 v-for를 동시에 사용하지 말 것

#### bind

* `v-bind:src="imageSrc"`
  * view 의 데이터를 html 태그 속성으로 넣을 수 있음
  * `:src="imageSrc"` 로 축약이 가능하다

#### on

* `v-on:eventName="cbFunction"`
  * `@eventName="cbFunction"` 으로 축약 가능
  * `@eventName.prevent="cbFunction"`  로 preventDefault() 동작 가능
  * cbFunction은 Vue 인스턴스의 methods 안에 정의됨

#### model

* `v-model="dataName"`
  * HTML form 요소의 값과 data를 양방향 바인딩

### computed

* `computed: {fn1, ...}`
  * data에 의존하는 계산된 **값**
  * 의존하는 데이터가 변할 때 계산을 진행
    * computed 속성은 종속 대상을 따라 캐싱(저장)된다
  * return이 반드시 필요함

### filters

* `filters:{filterFunction(){}, ...}`



## Lifecycle Hooks

