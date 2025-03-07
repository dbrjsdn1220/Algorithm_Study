T = int(input())
for tc in range(1, T+1):
    N = int(input())

    count = 1
    while True:
        temp = count ** 3

        if temp > N:
            print(f"#{tc} {-1}")
            break
        elif temp == N:
            print(f"#{tc} {count}")
            break

        count += 1
