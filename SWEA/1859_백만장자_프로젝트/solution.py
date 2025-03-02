"""
단순하게 최고 가격을 저장해두고,
최고 가격에 도달하면 판매해서 결과를 저장 / 최고가 갱신
"""

# import sys
# sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    # N: 예측 가능 일 수
    N = int(input())
    # price: 미래 가격
    price = list(map(int, input().split()))
    price.reverse()

    max_price = max(price)   # 최고가
    count = 0   # 구매한 물품 개수
    paid = 0   # 지금까지 지불한 금액
    answer = 0   # 정답

    for _ in range(N):
        today_price = price.pop()

        # 최고 가격보다 낮으면 구매
        if today_price < max_price:
            count += 1
            paid += today_price

        # 최고 가격에 오면
        elif today_price == max_price:
            # 산 게 있으면 판매
            if count > 0:
                answer += max_price * count - paid
                count = 0
                paid = 0

            # 최고 가격이 지났으니 최고가 갱신
            if price:
                max_price = max(price)

    print(f"#{tc} {answer}")