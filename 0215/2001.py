from pprint import pprint

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split()) # N*N 판, M*M 파리채
    lst = [list(map(int, input().split())) for _ in range(N)]
    for y in range(N-2):
        for x in range(N-2):