# JavaScript

## 함수

### 특징

* 참조 타입 중 하나로써 function 타입에 속함
* JavaScript에서 함수를 정의하는 방법은 2가지로 구분
  * 선언식
  * 표현식
* JavaScript의 함수는 일급 객체에 해당
  * 변수에 할당 가능
  * 함수의 매개변수로 전달 가능
  * 함수의 반환 값으로 사용 가능
* 매개변수와 인자의 개수 불일치 허용
  * 부족한 인자는 undefined, 초과한 인자는 사용하지 않음

### 함수 선언식

```javascript
function name(args) {
    // to do
}
```

* 함수 선언식으로 선언한 함수는 var로 정의한 변수처럼 hoisting 발생

### 함수 표현식

```javascript
const name = function(args) {
    // to do
}
```

* 함수의 이름을 생략하고 익명 함수로 정의 가능

### Rest Parameter

```javascript
const name = function (arg1, arg2, restArgs) {
    return [arg1, arg2, restArgs]
}
name(1,2,3,4,5)
>>> restArgs = [3,4,5]
```

* 파이썬의 `*args` 와 유사한 용도

### Spread operator

```javascript
const arr = [1,2,3]
functionName(...name)
// = functionName(1,2,3)
```

* 배열 인자를 전개하여 전달 가능

## Arrow Function

### 화살표 함수란

```javascript
const f1 = function (name) {
    return 'hi'
}
const f1 = (name) => {return 'hi'}
const f1 = name => {return 'h1'}	// 매개변수가 하나라면 괄호 생략 가능
const f1 = name => 'hi'	// 중괄호 내 표현식이 return 을 포함한 하나라면 생략 가능
```

* 함수를 비교적 간결하게 정의할 수 있는 문법
* function 키워드 생략 가능



## 문자열

### includes

* 특정 문자열의 존재 여부 T/F 반환

### split

* 문자열을 토큰 기준으로 나눈 배열 반환
* 인자가 없으면 기존 문자열을 배열에 담아 반환

### replace / replaceAll

* `str.replace(' ', '-')` : 한 개만 치환
* `str.replaceAll(' ', '-')` : 모두 치환

### trim

* `str.trim()` 문자열 양 끝의 공백문자 제거
* `str.trimStart()` `str.trimEnd()` 



## 배열

### 배열이란

* 키와 속성을 갖는 참조 타입의 **객체**
* 순서를 보장함
* 음수 인덱스 접근이 불가능
* 배열의 길이는 `array.length`로 접근

### join

* 파이썬과 다르게 배열의 메서드
* `result = arr.join()`

### push / pop

* 배열의 가장 뒤에 요소 추가 / 제거

### unshift / shift

* 배열의 가장 앞에 요소를 추가 / 제거

### indexOf

* 특정 값이 존재하면 인덱스 / **없으면 -1** 반환

### spread operator (...)

```javascript
const array = [1,2,3]
const narray = [0, ...array, 4]
>>> [0,1,2,3,4]
```



## 콜백

### 콜백함수

* 3가지 매개변수 element, index, array 구성

### forEach

```javascript
const fruits = ['a', 'b', 'c']
// 1
fruits.forEach(function(fruit, index) {
               console.log(fruit, index)
               })
// 2
fruits.forEach(function(fruit, index) => {console.log(fruit, index)})
```

* 배열의 각 요소에 대해 콜백 함수를 한번씩 실행
* 반환값 없음

### map

```javascript
const numbers = [1, 2, 3, 4, 5]
const doubleNums = numbers.map((num) => {return num*2})
const doubleNums = numbers.map(num => num*2)
>>> doubleNums = [2,4,6,8,10]
```

```javascript
const rectangles = [
    {'width': 30, 'height': 20}, 
    {'width': 10, 'height': 20}
]
const area = rectangles.map(wh => wh.width*wh.height)
```

* 그 맵

### filter

```javascript
const numbers = [1, 2, 3, 4, 5]
const oddNums = numbers.filter((num, index) => num%2)
const oddNums = numbers.filter(function(num) {
    return (num%2)
})
```

* 콜백함수의 반환 값이 참인 요소들만 모아서 새로운 배열을 반환

### reduce

```javascript
const students = [
    {python: 100, js: 95},
    {python: 80, js: 100}
]
const result = students.reduce((acc, score) => acc + score.python, 0)
console.log(result)
```

### find

* 조건을 만족하는 첫 번째 요소 반환

* 없으면 undefined 반환

### some

* 요소 중 하나라도 판별함수를 통과하면 참을 반환
* 빈 배열은 항상 거짓 반환

### every

* 모든 요소가 판별 함수를 통과하면 참을 반환
* 빈 배열은 항상 참 반환



## 객체

### 객체란

* 객체는 속성의 집합이며, 중괄호 내부에 key, value 의 쌍으로 표현
* key 는 문자열 타입만 가능
  * key 이름에 띄어쓰기 등이 있으면 따옴표로 묶어 표현
* value 는 함수를 포함한 모든 타입이 가능
* 객체 요소 접근은 점 또는 대괄호로 가능
  * 단, key 이름에 띄어쓰기가 있으면 대괄호 접근만 가능

### 객체와 메서드

* 메서드 내부에서 `this` 가 객체를 의미함

### JSON

* `JSON.parse() `
  * JSON => 자바스크립트 객체
* `JSON.stringify()`
  * 자바스크립트 객체 => JSON



## this 정리

### this

* JS의 this 는 실행 문맥에 따라 다른 대상을 가리킨다



## lodash

```html
<script src="https://cdn.jsdelivr.net/npm/lodash@4.17.21/lodash.min.js"></script>
const lotto = _.sampleSize(_.range(1, 46), 6)
console.log(...lotto)
```

