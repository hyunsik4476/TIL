# PJT 09

## Social Login

### django allauth

[문서](https://django-allauth.readthedocs.io/en/latest/overview.html)

## paginator

[문서](https://docs.djangoproject.com/en/4.0/topics/pagination/)

[bootstrap5](https://django-bootstrap-v5.readthedocs.io/en/latest/templatetags.html#bootstrap-pagination)

```python
from django.core.paginator import Paginator

@require_safe
def index(request):
    movies = Movie.objects.all()
    paginator = Paginator(movies, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'movies': page_obj,
    }
    return render(request, 'movies/index.html', context)
```

```html
  <h1>Movies</h1>
  <div id="movieList">
    {% for movie in movies %}
    <div class="movie">
      <h2>{{ movie.title }}</h2>
      <p>{{ movie.overview }}</p>
      <a href="{% url 'movies:detail' movie.pk %}">[detail]</a>
      <hr>
      {% endfor %}
    </div>
    {% comment %} JSON 내용 추가 {% endcomment %}

  </div>
  <div class="d-flex justify-content-center">
    {% bootstrap_pagination movies %}
  </div>
```



## Infinite Scroll

```javascript
<script>  
  let page = 2
  const movieList = document.querySelector('#movieList')

  document.addEventListener('scroll', function (event) {
    const {scrollTop, clientHeight, scrollHeight} = document.documentElement
    // 완전 바닥에 도달
    if (scrollHeight - scrollTop === clientHeight) {
      console.log('bott')
    }
    if (scrollTop + clientHeight >= scrollHeight - 10) {
      axios({
        method: 'get',
        url: `/movies/ajax/?page=${page}`
      })
        .then(res => {
          const movies = res.data
          movies.forEach(movie => {
            console.log(movie.title, movie.overview)
            const movieDiv = document.createElement('div')
            const h2 = document.createElement('h2')
            const p = document.createElement('p')
            const a = document.createElement('a')
            const hr = document.createElement('hr')
            
            h2.innerText = movie.title
            p.innerText = movie.overview
            a.innerText = '[detail]'
            a.href = `/movies/${movie.id}/`

            movieDiv.append(h2, p, a, hr)
            movieList.appendChild(movieDiv)
          })
          page++
        })
        .catch(err => console.log(err))
    }
  })
</script>
```

