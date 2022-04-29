# 

## 구조분해할당

```javascript
const user = {
    name: 'me',
    age: 16
}
const name = user.name
const { name } = user
```

* 변수명과 객체의 키 이름이 같을 때 중복을 제거하기

```javascript
const user = {
    name: 'me',
    age: 16
}
function printUser(user) {
    console.log(user.name, user.age)
}
function printUser({ name, age }) {
    console.log(name, age)
}
printUser(user)
```



## this

```javascript
const me = {
    name: 'neo',
    printName: function() {
        console.log(this.name)
    }
}
me.printName()
>>> neo
```

* class 내부의 생성자 함수
  * this는 생성되는 객체를 가리킴
* 메서드
  * this는 해당 메서드가 소속된 객체를 가리킴
  * 주의 : 메서드 내부에 함수가 있다면 그 함수의 this는 window를 가리킬수 있음
  * `.bind(this)` 가 필요한 이유

