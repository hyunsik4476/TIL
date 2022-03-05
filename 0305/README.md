# Django

> 20220305

## Form

### form element

* 사용자 정보를 입력하는 여러 방식을 제공
  * text, button, checkbox, file, hidden, image, password, radio, rest, submit
* 중요한 속성으로 action 과 method가 있음
  * action : 입력 데이터가 전송될 url을 지정
  * method : 입력 데이터의 전달 방식을 지정(GET/ POST)



### input element

* 데이터를 입력받기 위해 사용
* type에 따라 동작 방식이 다름
* 핵심 속성
  * name : 입력된 내용을 저장하는 변수같은 역할
  * URL상에서 &message=hi 같이 확인 가능
  * request.GET.get('message') 처럼 활용도 가능

```html
<form action="/catch/" method="GET">
  <label for="message">Throw</label>
  <input type="text" id="message" name="message">
  <input type="submit">
</form>
```

```python
def catch(request):
    message = request.GET.get('message')
    context = {
        'message': message,
    }
    return render(request, 'catch.html', context)
```



