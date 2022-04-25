# JavaScript

## JS intro

## 브라우저

### 브라우저에서 할 수 있는 일

* DOM(문서) 조작
* BOM(브라우저) 조작
* JavaScript Core





## 변수와 식별자

* 식별자는 변수를 구분할 수 있는 변수명을 말함
* 반드시 문자, 달러($), 밑줄(_) 로 시작



### 변수

* 파이썬처럼 그냥 쓰면 `var` 선언

* `let <name>`

  * 재할당 가능

* `const <name>`

  * 재할당 불가능

* `var`

  * 사용 지양

  * var의 hoisting

    * ```javascript
      console.log(username)
      var username = '김'
      >>> 김
      ```



## 데이터타입

### 원시 타입

* 원시타입 데이터는 데이터의 값을 저장함

#### 숫자

* 정수, 실수 구분 없는 하나의 숫자 타입
* 부동소수점 형식을 따름
* 계산 불가능한 경우 NaN 반환

#### 문자열

* 텍스트 데이터를 나타내는 타입
* 템플릿 리터럴 : 따옴표 대신 backtick(``)사용
  * const fullName = \`${firstName} ${lastName}`

#### undefined

* 변수의 값이 없음
* 선언 이후 직접 값을 할당하지 않으면 자동으로 undefined가 할당됨

#### null

* 빈 값
* typeof(null) 은 object 임

#### boolean

### 참조타입

* 함수, 배열, 객체 등



## 조건문

```javascript
if (true) {
  const language = 'Python'
  console.log(language)
}
```

```javascript
switch(operator) {
    case '+': {
        console.log(1 + 2)
        break
    }
    case '-': {
        console.log(1 - 2)
        break
    }
    default: {
        console.log('hi')
    }
}
```



## 반복문

### while

* 전과 동일

### for

* 근본 for

* ```javascript
  for (let i = 0; i < 5; i++) {
      console.log(i)
  }
  ```

### for (key in object)

* 객체의 속성(key)들을 순회
* 배열도 순회 가능하지만 권장하지 않음

### for (variable of iterables)

* 반복 가능한 객체를 순회하며 값을 꺼낼 때 사용
* 반복 불가능한 객체의 경우 오류



