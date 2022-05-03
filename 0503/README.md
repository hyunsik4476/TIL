# JS & django

## 무엇을?

### AJAX

* 비동기식으로 전에 만든 django 코드의 일부분을 변경하려고 함
* 좋아요 버튼 클릭 시 새로고침 없이 버튼, 좋아요 수 변경
* 팔로우 버튼 클릭 시 새로고침 없이 버튼, 팔로우 수 변경

## 코드

### 시작하기

```javascript
{% block script %}
  <script>
    // CODE HERE
    formTags = document.querySelectorAll('.like-form')
    formTags.forEach(formTag => {
      formTag.addEventListener('submit', event => {
        event.preventDefault()
        ...
```

* 하던 대로, 단 django 코드 상 for 문으로 여러 개의 article 정보를 받아오므로 forEach를 사용해 각 form에 이벤트리스너를 추가해야함
* 다음 할 일
  * 버튼을 눌렀을 때 like URL로 요청을 보내야함
* 필요한 것
  * 글의 정보 (article_pk)

### 정보 받아오기

```django
<form class="like-form" data-article-id="{{ article.pk }}">
  {% csrf_token %}
  {% if user in article.like_users.all %}
    <button id="like-{{ article.pk }}">좋아요 취소</button>
  {% else %}
    <button id="like-{{ article.pk }}">좋아요</button>
  {% endif %}
</form>
```

* `data-article-id="{{ article.pk }}"`
  * 자동으로 articleId 라는 요소를 갖는 dataset을 만들어줌
  * 어디에? event.target에

```javascript
const articleId = event.target.dataset.articleId
        const button = document.querySelector(`#like-${articleId}`)
        const likeCount = document.querySelector(`#like-count-${articleId}`)
        URL = `/articles/${articleId}/likes/`
```

### 요청 보내기(CSRFToken)

```javascript
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
axios.post(URL, {}, {
  headers : {'X-CSRFToken': csrftoken}
})
  .then(res => {
	console.log(res)
  })
```

* post 요청일 때 axios 에서 csrf 토큰 문제 해결하기
* 문제점
  * 원래 views 의 like 함수의 return 은 redirect 였음
  * `.then()`에서 활용하기 위해 JSON 으로 바꿔야 함
  * 이 JSON에 내가 사용할 정보들, 즉 좋아요 여부 & 각 글의 좋아요 수를 담아 넘김

### JSON

```python
@require_POST
def likes(request, article_pk):
    # CODE HERE
    from django.http import JsonResponse, HttpResponse
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk = article_pk)
        if article.like_users.filter(pk = request.user.pk).exists():
            is_liked = False
            article.like_users.remove(request.user)
        else:
            is_liked = True
            article.like_users.add(request.user)
        context = {
            'is_liked': is_liked,
            'num_liked': article.like_users.count(),
        }
        return JsonResponse(context)
    else:
        return redirect('accounts:login')
```

* 원래 코드와 다른 건 context를 만들고 필요한 정보들을 JsonResponse를 통해 JSON으로 응답함

### JS 변경

```javascript
.then(res => {
  if (res.data.is_liked) {
    button.innerText = '좋아요 취소'
  } else {
    button.innerText = '좋아요'
  }
  likeCount.innerText = res.data.num_liked
})
```

* 변경된 응답을 활용
* 문제점
  * 로그인 되어있지 않을 때의 동작
  * 현재 views의 함수에서 return redirect를 변경해야함
  * HTTPstatus를 응답하게 변경할 예정

### views

```python
from django.http import JsonResponse, HttpResponse
    ...
    context = {
        'is_liked': is_liked,
        'num_liked': article.like_users.count(),
    }
    return JsonResponse(context)
else:
    return HttpResponse(status=401)
```

* 로그인되어있지 않을 시 401 status 반환

### error handling

```javascript
.then(res => {...})
.catch(err => {
  if (err.response.status === 401) {
    window.location.href ='/accounts/login/'
  } else {
    console.log(err)
  }
})
```

* 401(권한 없음) 코드 응답 시 로그인 화면으로 전환
* 그 외 에러 발생 시 에러 코드만 출력하도록 하고 마무리