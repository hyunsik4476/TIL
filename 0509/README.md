# Vue

## SFC

> Single File Component

### Component

* 기본 html 엘리먼트를 확장하여 재사용 가능한 코드를 캡슐화 하는데 도움을 줌

### SFC

* Vue의 컴포넌트 기반 개발의 핵심 특징
* 화면의 특정 영역에 대한 HTML, CSS, JS 코드를 하나의 파일 (.vue)에서 관리
  * Vue 컴포넌트 = Vue 인스턴스 = .vue 파일
* 각 기능 별로 파일을 나눠서 개발하게 됨



## Vue CLI

### Node.js

* 자바스크립트를 브라우저가 아닌 환경에서도 구동할 수 있도록 하는 자바스크립트 런타임 환경



## Babel & webpack

### Babel

* 자바스크립트 컴파일러
* ECMAScript 2015 코드를 이전 버전으로 번역 변환해 주는 도구

### Webpack

* 모듈간의 종속성 문제를 해결하기 위함
* 여러 모듈 시스템이 등장
  * ESM(ECMA Script Module)
* 모듈 의존성 문제를 해결해주는 작업을 Bundling이라 함
* 웹팩은 다양한 Bundler 중 하나



## Pass Props & Emit Events

### 컴포넌트 작성

* Vue app은 컴포넌트 트리로 구성됨
* 컴포넌트간 부모 - 자식 관계가 구성되며 이들 사이에 의사 소통이 필요
  * 부모는 자식에게 데이터 전달(Pass props) / 자식은 부모에게 알림(Emit event)
* 하나의 .vue 파일은 template, script, style로 구성
  * html, JS, CSS

### 컴포넌트 등록 3단계

* 불러오기, 등록하기, 보여주기

* ```vue
  <template>
    <div id="app">
      <img alt="Vue logo" src="./assets/logo.png">
      <!-- 3. 보여주기 -->
      <!-- 카멜 케이스 -->
      <TheAbout my-message="CamelCase" />
      <!-- 케밥 케이스 -->
      <the-about my-message="kebab-case"></the-about>
    </div>
  </template>
  
  <script>
  // 1. 불러오기
  import TheAbout from './components/TheAbout.vue'
  export default {
    name: 'App',
    // 2. 등록하기
    components: {
      TheAbout,
    },
  }
  </script>
  ```

### Props

* ```vue
  <template>
    <h1>{{ myMessage }}</h1>
  </template>
  
  <script>
  export default {
    name: 'TheAbout',
    props: {
      myMessage: String,
    },
  }
  </script>
  ```

* 주의 : template 안에는 반드시 하나의 Element만 있어야 한다

* ```vue
  <template>
  
  <div>
    <h1>{{ myMessage }}</h1>
  </div>
  
  </template>
  
  <script>
  export default {
    name: 'TheAbout',
    props: {
      myMessage: String,
    },
  }
  </script>
  ```

* 일단 div로 묶고 시작하자

### data

* ```vue
  <template>
    <div id="app">
      <img alt="Vue logo" src="./assets/logo.png">
      <!-- 3. 보여주기 -->
      <!-- 카멜 케이스 -->
      <TheAbout :my-message="parentData" />
      <!-- 케밥 케이스 -->
      <the-about my-message="kebab-case"></the-about>
    </div>
  </template>
  
  <script>
  // 1. 불러오기
  import TheAbout from './components/TheAbout.vue'
  export default {
    name: 'App',
    // 2. 등록하기
    components: {
      TheAbout,
    },
    data: function() {
      return {
        parentData: 'This is parent data to child comp.',
      }
    }
  }
  </script>
  ```

* data는 함수형으로 쓰여야함

  * 같은 객체를 참조하는 것을 막기 위함

* v-bind를 사용해 접근할 수 있다

### Emit event

* ```vue
  <script>
  export default {
    name: 'TheAbout',
    props: {
      myMessage: String,
    },
    data: function() {
      return {
        childInputData: ''
      }
    },
    methods: {
      childInputChange: function() {
        console.log('enter', this.childInputData)
        // 부모 컴포넌트에게 ''라는 이름의 이벤트를 발생시킴
        this.$emit('child-input-change', this.childInputData)
      }
    }
  }
  </script>
  ```

* ```vue
  <template>
    <div id="app">
      <img alt="Vue logo" src="./assets/logo.png">
      <the-about
        my-message="parent"
        @child-input-change="parentGetChange"
      ></the-about>
    </div>
  </template>
  ```

* 여러 인자를 넘길 수도 있지만 객체로 묶어서 넘기는게 좋다



## Vue Router

* vue.js 공식 라우터
* 라우트에 컴포넌트를 매핑한 후, 어떤 주소에서 렌더할지 알려줌