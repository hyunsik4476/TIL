# 평가 대비



## HTML

* hyper text markup language
* HTML 문서의 기본 구조
  * html: 문서의 최상위 요소
  * head: 문서의 메타데이터 요소(일반적으로 브라우저 상에 안보임)
    * `<title>` 페이지 제목
    * `<link>` 외부 리로스 연결
    * `<script>` 스크립트 요소

  * body: 문서 본문 요소
    * 크게 블럭과 인라인으로 나눠볼 수 있음
    * 블럭: `<p>` `<hr>` `<ul>` `<ol>` `<div>`
    * 인라인: `<a>` `<b>` `<br>` `<img>` `<span>`
* 시맨틱 태그
  * 보기 편하게끔 태그마다 이름을 붙여줌
    * `header`
    * `nav`
    * `aside` 
    * `section`: 컨텐츠의 그룹 
    * `ariticle`: 문서 내 독립적으로 구분되는 영역 
    * `footer`
    * `main`
    * 자체로 뭐가 있진 않지만 사람이 보고 구분하기에 좋음
* 주요 태그와 속성



* 기타
  * 모든 태그가 별도의 닫는 태그를 요하지는 않음 ex) \<br\> \<hr>
  * 리스트의 경우 \<ul> \<ol> 로 순서가 없는/ 있는 리스트를 만들 수 있다
* 



## CSS

* 어떻게 사용하는가?
  * `<head>` 안에 설정
  * 태그 안에 선언(인라인~)
  * 별도의 css 파일 사용
* 단위(크기, 속성)
  * rem: 브라우저 root 설정을 기준으로 배수(기본 16px)
  * em: 부모 요소의 크기를 기준으로 배수

* 선택자
  * p:nth-child(num): 부모 안의 모든 요소 중 num번째 요소가 p 일때 변함
  * p:nth-of-type(num): 부모 안의 p 요소 중 num 번째 요소가 변함

* 선택자 및 우선순위 ***
  * `!important`
  * Inline style `style=""`
  * id 선택자 `#id`
  * class 선택자 `.class`
  * 요소 선택자 `태그이름`
  * 같은 우선순위를 갖는 경우, css내에서 뒤에 선언한 속성이 우선


* 박스모델 (마진 순서 같은 것들)
* 인라인/ 블록 요소의 특징
* position
  * static
  * relative(normal flow)
  * absolute(out of flow) 스태틱이 아닌 부모 요소 기준
  * fixed(out of flow)
  * sticky
* Flex ***
  * align-content X
  * `flex-direction:` `row-(reverse)`/` column-(reverse)`
  * `flex-flow:` `row-revere wrap-reverse` (flex-direction + wrap)
  * `justify-content:` `flex-start` `flex-end` `center` `space-around` `space-between` `space-evenly`
  * `align-items:` `flex-start/end`, `center`, `baseline`, `stretch`



* 기타
  * html과 css는 각자 문법을 갖는 별개의 언어이다
  * 자식 요소는 부모의 속성 중, 텍스트 크기, 색상 등 일부만을 상속받는다
  * vh, vw 등 디바이스 화면 크기에 따른 크기를 정할 수 있다
