# 데이터 불러오기

> 20220121

## import json

* .json 확장자를 갖는 파일을 불러올 수 있음

* ```python
  import json
  xxx_json = open('xxx.json', encoding = 'UTF8')
  xxx_dict = json.load(xxx_json)
  ```

* 딕셔너리/ 리스트 같은 것들이 들어있음



## 리스트/ 딕셔너리 활용

```python
def movie_info(movie):
    new_movie_dict = {}
    info_list = ['title', 'genre', 'revenue']
    for info in info_list:
        new_movie_dict[info] = movie[info]
    
    return new_movie_dict
```

* 이런 식으로 딕셔너리를 정제할 수 있음

```python
for key, value in movie.items():
```

* key, value 뽑아오기

```python
    for movie in movies: # 딕셔너리 1개씩 호출
        file_name = '{0}.json'.format(movie['title'])
        details_json = open(file_name, encoding = 'UTF8')
        details_dict = json.load(details_json)

        revenue_list.append(details_dict['revenue']) 
        # max함수를 쓰기 위해 리스트에 수입을 저장함
        
        if max(revenue_list) == details_dict['revenue']: # 최대 수입 작품의 id 갱신
            max_id = details_dict['id']
        if max_id == details_dict['id']: # 갱신된 id에 따라 영화 이름 갱신
            movie_name = details_dict['title']
```

* 특정 값을 갖는 딕셔너리에서 다른 값을 가져오기
