# Javascript EventLinstner

## eventlistner 를 이용해 태그 속성 바꾸기

```javascript
const bodyTag = document.querySelector('body')
const nB = document.querySelector('.switcher #navyButton')

nB.addEventListener('click', function () {
  bodyTag.setAttribute('style', 'background-color: navy; color: white')
  //bodyTag.style.backgroundColor= 'navy'
})
```



## 문자열 메서드

```javascript
// const badWords = ['바보', '멍청', '메롱',]
const badWords = [/바보/g, /멍청/g, /메롱/g,]
const userInput = document.querySelector('#userInput')
const output = document.querySelector('#output')

let filteredInput = ''
function filterMessage(event) {
  // badWords에 포함된 단어가 입력될 경우, '**'으로 변환하여 output에 출력
  console.log(event.target.value)
  filteredInput = event.target.value
  for (badWord of badWords) {
    filteredInput = filteredInput.replace(badWord, '**')
    console.log(filteredInput)
  }
  output.innerText = filteredInput
}
```

* 정규식으로 replace 사용시 전체 문자열에 대해 검사 가능
  * '바보'를 정규식 /바보/g 로 바로 바꾸는 방법?



## preventDefault()

```javascript
formTag.addEventListener('submit', function(e) {
  e.preventDefault()
  newCard = createCard(e.target[0].value, e.target[1].value)
  cardsSection.append(newCard)
  e.target.reset()
})
```

* form 태그는 데이터에 접근하려면 target 에 먼저



## loadash

```javascript
<script src="https://cdn.jsdelivr.net/npm/lodash@4.17.21/lodash.min.js"></script>
<script>
const body = document.querySelector('body')

const paths = ['./images/1.jpg', ... , './images/6.jpg']
const path = _.sample(paths)
console.log(path)
body.setAttribute('style', `background-image: url(${path})`)
...
</script>
```

* 자바 라이브러리
* src 속성을 가진 script 내부의 코드는 동작하지 않는다.
  * 즉, loadash를 불러온 후 script 를 닫고 다시 내부 코드를 입력할 script를 연다



## 구현

```javascript
const timeDiv = document.querySelector('#time')

let span = document.createElement('span')
timeDiv.appendChild(span)

const displayTime = function () {
  // 2. 아래 now를 활용하여 timeDiv의 innerText를 적절하게 re-format
  const now = new Date().toString()
  let time = now.split(' ')[4]
  let [hour, min, sec] = [time.split(':')[0], time.split(':')[1], time.split(':')[2]]
  if (Number(hour) > 12) {
    hour = hour - 12
    time = `오후 ${hour}:${min}:${sec}`
  } else if (Number(hour) === 12) {
    time = `오후 ${hour}:${min}:${sec}`
  } else {
    time = `오전 ${hour}:${min}:${sec}`
  }
  span.innerText = time
}

setInterval(displayTime, 1000)
```

* 함수를 인자로 넘길 때, 함수의 반환값이 필요한건지 함수의 동작이 필요한건지 잘 생각해서 넘겨야한다