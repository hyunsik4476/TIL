# 그리드 시스템

> 20220207

## Float

### CSS 원칙

* Normal Flow
  * 위에서 아래로(Block), 좌에서 우로(Inline)
  * -> 어떤 요소를 감싸는 형태/ 좌우 배치는 어떻게?



### Float

* 텍스트 포함 주변 요소들이 주변을 감싸도록 함
* Normal Flow에서 벗어난 요소



### Float 속성

* None : 기본값
* left/ right : float 할 위치 지정 가능
* Inline 요소에 선언하면 display 가 block 으로 바뀜



### Float clearing

```css
    .clearfix::after {
      content: "";
      display: block;
      clear: both;
    }
```

* 위와같은 클래스를 float 요소의 부모에 부여
* 부모 요소 이하로 float가 작동 안하도록



## Flexbox

[참고](https://developer.mozilla.org/ko/docs/Web/CSS/CSS_Flexible_Box_Layout/Basic_Concepts_of_Flexbox)

### 레이아웃

* 축

* 구성 요소

  * Flex container(부모)

    ```css
    .flex-container {
        display: flex;
    }
    ```

  * Flex Item(자식)



### 속성

* `flex-dirextion : row/ column(-reverse)` 
  * 메인 축이 x인지 y인지/ 정렬 순서
  * 역방향의 경우 태그 선언 순서와 실제 보이는 순서가 다를 수 있음
* `flex-wrap` 
  * 아이템의 너비 등을 바꾸지 않고도 컨테이너를 벗어나지 않도록
* `justyfy-content`
  * 메인 축을 기준 공간 배분
* `align-content`
  * 크로스 축을 기준 공간 배분
* `align-items`
  * 모든 아이템을 크로스 축을 기준으로 정렬
  * `align-content` 보다 많이 사용됨
* `align-self`
  * 개별 아이템을 크로스 축 기준으로 정렬
  * 컨테이너가 아닌 아이템이 적용하는 속성임에 유의



# 부트스트랩

## CDN



## 유틸리티

### spacing

* `mt-<size 0~5>` (margin top)
* `mx-<size>` (margin left, right)
* `my-<size>` (margin top, bottom)
* `p~` (padding 시리즈도 존재)



## color

* `bg-<primary 등>`
* `text-<primary 등>`



## display

* `d-inline`
* `d-block`
* `d-flex`
* `d-none`
  * 화면 사이즈에 따라 보이고 안보이고 정할수 있음



## position

* `position-relative`
* `position-absolute`



## 12col

* \<container>
* \<row> \<col> 순서대로 배치
