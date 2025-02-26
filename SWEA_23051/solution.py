import sys
sys.stdin = open('input.txt')

"""
유니온 파인드를 해결하면 빠르게 할 수 있을 거 같음.

"""


def find(parent, x):
    # 부모가 자기 자신이 아니라면
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    # 부모 리턴
    return parent[x]


def union(parent, rank, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)

    if rootA != rootB:
        if rank[rootA] > rank[rootB]:
            parent[rootB] = rootA
        elif rank[rootA] < rank[rootB]:
            parent[rootA] = rootB
        else:
            parent[rootB] = rootA
            rank[rootA] += 1


def count_groups(n, app):
    parent = [i for i in range(n + 1)]  # 1부터 n까지 초기화
    rank = [0] * (n + 1)

    # 유니온 연산 수행
    for i in range(0, M*2, 2):
        union(parent, rank, app[i], app[i + 1])

    # 모든 노드의 대표를 찾고 조 개수 세기
    groups = set(find(parent, i) for i in range(1, n + 1))
    return len(groups)


T = int(input())
for tc in range(1, T + 1):
    # N: 인원, M: 신청서
    N, M = map(int, input().split())
    # 신청서 내용
    applications = list(map(int, input().split()))

    result = count_groups(N, applications)
    print(f"#{tc} {result}")
