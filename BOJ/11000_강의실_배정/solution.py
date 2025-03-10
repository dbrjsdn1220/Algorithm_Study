"""
단순하게 수업을 끝나는 시간으로 정렬해서, 선택된 수업 pop 하기
-> 수업을 계속 순회해서 시간 초과.
수업을 하나씩 확인하면서 현재 사용했던 강의실의 끝나는 시간과 비교 및 추가
-> 강의실을 계속 순회해서 시간 초과.

시작하는 시간을 기준으로 정렬해서 heapq를 이용하여 끝나는 시간 저장.
가장 빨리 끝나는 시간과, 가장 빨리 시작하는 시간을 비교하며 계산.\
"""
import heapq
# import sys
# sys.stdin = open('input.txt')


# N: 수업 개수
N = int(input())
lessons = [list(map(int, input().split())) for _ in range(N)]
lessons.sort()


rooms = []
heapq.heappush(rooms, lessons[0][1])

for i in range(1, N):
    if rooms[0] <= lessons[i][0]:
        heapq.heappop(rooms)

    heapq.heappush(rooms, lessons[i][1])

print(len(rooms))
