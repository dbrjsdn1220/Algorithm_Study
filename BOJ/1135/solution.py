"""
뉴스 전하기 - 골드2(https://www.acmicpc.net/problem/1135)
모든 사람은 직속 부하에게만 전화할 수 있다. 여기서 어떤 직속부하에 먼저 전화할 것인지가 중요해 보임.
DP로 각 노드 걸리는 시간 저장.
"""
import sys
sys.stdin = open('input.txt')


# 직속 + 간접 부하가 몇 명인지 세서 돌려줌.
def count_calling(n):
    if rank_junior[n]:
        calling = 0
        maximum = 0
        temp = []   # 최소시간 내림차순 정렬해서 넣을 거임.

        for i in rank_junior[n]:  # 직속 부하 넣기
            count_calling(i)

        for i in rank_junior[n]:   # 최대값 찾기
            temp.append(calling_min[i])
        temp.sort(reverse=True)
        maximum = temp[0]
        calling = maximum

        for t in temp:   # 필요로 하는 최소 전화 시간 계산
            if t > maximum:
                calling += t-maximum
            maximum -= 1

        calling_min[n] = calling + 1

    else:
        calling_min[n] = 0


N = int(input())   # 직원의 수
rank_senior = list(map(int, input().split()))   # 직속 상사 정보

rank_junior = [[] for _ in range(N)]  # 직속 부하 정보
for i in range(1, N):
    rank_junior[rank_senior[i]].append(i)

calling_min = [0] * N   # 전화를 건 최소의 수
boss_junior = []
for i in rank_junior[0]:
    boss_junior.append(count_calling(0))

print(max(calling_min))
