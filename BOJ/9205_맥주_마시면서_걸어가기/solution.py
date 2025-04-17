'''
맥주 마시면서 걸어가기 - 골드 5(https://www.acmicpc.net/problem/9205)
출발점에서 이동할 수 있는 편의점을 찾으면 que에 저장.
popleft 하면서 이동가능한 위치를 계속 확인. (중복 제거를 위해 visited 사용)
그러다 한 편의점이라도 페스티벌 위치와 연결되면 happy
만약 que가 다 비워진다면 sad
---------------------------------------------------------
visited 말고 방문한 곳을 pop하는 방식을 써봤는데 실행시간은 같았음.
난 pop이 더 오래걸릴 줄 알아서 계산해봄.

1. pop을 하는 경우 항상 len(stores)만큼 연산해야 함.
100개 중 50개 확인 후 pop 했다면, 뒤에 50개를 한번씩 당겨야 하므로,,,
대신! len(stores) 개수가 계속 줄어들음.
-> N = 100 이라면 최악의 연산횟수는 5,050번

2. visited는 100개 중 50개를 확인했다면 1번만 연산하면 됨 -> visited[i] = True
하지만, 이 경우 len(stores)번만큼 visited와 비교하는 연산이 추가됨.
그런데 len(stores)은 pop 방식과 다르게 줄어들지 않음.
-> N = 100 이라면 최악의 연산횟수는 10,000번
'''
# import sys
# sys.stdin = open('input.txt')
from collections import deque


T = int(input())
for tc in range(1, T+1):
    N = int(input())   # 편의점 개수
    house = list(map(int, input().split()))   # 출발지 좌표(현재는 집)
    stores = [list(map(int, input().split())) for _ in range(N)]   # 편의점 좌표들
    festival = list(map(int, input().split()))   # 락 페스티벌 좌표

    que = deque()
    que.append(house)
    answer = 'sad'

    while que:
        start = que.popleft()
        size = len(stores)
        i = 0

        if abs(festival[0] - start[0]) + abs(festival[1] - start[1]) <= 1000:
            answer = 'happy'  # 페스티벌 도착
            break

        while i < size:
            # 현재 위치에서 이동할 수 있는 편의점이이라면
            if abs(start[0] - stores[i][0]) + abs(start[1] - stores[i][1]) <= 1000:
                que.append(stores.pop(i))  # 저장
                size -= 1
            # 아니라면 다음 편의점 좌표로
            else:
                i += 1

    ''' visited 방식
        visited = [False for _ in range(N)]   # 탐색한 위치인지 표시
        
        while que:
            start = que.popleft()
    
            if abs(festival[0] - start[0]) + abs(festival[1] - start[1]) <= 1000:
                answer = 'happy'   # 페스티벌 도착 sad -> happy
                break
    
            for i in range(N):
                # 현재 위치에서 이동할 수 있는 편의점이이라면
                if not visited[i] and abs(start[0] - stores[i][0]) + abs(start[1] - stores[i][1]) <= 1000:
                    visited[i] = True
                    que.append(stores[i])   # 저장
    '''
    print(answer)
