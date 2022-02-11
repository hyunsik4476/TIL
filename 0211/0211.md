# 0211

> 20220211

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
    *  `nav`
    *  `aside` 
    * `section`: 컨텐츠의 그룹 
    *  `ariticle`: 문서 내 독립적으로 구분되는 영역 
    * `footer`
    * 자체로 뭐가 있진 않지만 사람이 보고 구분하기에 좋음

* 주요 태그와 속성
  * ~~table, form, input X~~



## CSS

* 어떻게 사용하는가?
  * `<head>` 안에 설정
  * 태그 안에 선언(인라인~)
  * 별도의 css 파일 사용
* 단위(크기, 속성)
* 선택자 및 우선순위 ***

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



## 반응형 웹

* 부트스트랩
  * 그리드 시스템 w/ 브레이크포인트



## 마크업

* 각 태그별 속성
  * 인라인, 블록
  * ex) `a` 태그는 `href` 속성이 반드시 필요\



## 스타일링

* Flex 는 신이다