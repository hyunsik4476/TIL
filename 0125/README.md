# 데이터 구조 실습

> 20220125

```python
blood_types = [
    'A', 'B', 'A', 'O', 'AB', 'AB',
    'O', 'A', 'B', 'O', 'B', 'AB',
]

result = {}
for blood_type in blood_types:
    if blood_type in result:
        result[blood_type] += 1
    else:
        result[blood_type] = 1

# for blood_type in blood_types:
#     result[blood_type] = blood_types.get(blood_type, 0) + 1
# get 을 사용해 if 없이 key 가 존재하지 않을 때 0을 가져오고 +1 할 수 있음
```

