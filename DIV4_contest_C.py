def convert(tm):
    hr, mit = map(int, tm.split(':'))

    p = 'AM' if hr < 12 else 'PM'
    hr = hr % 12
    if hr == 0:
        hr = 12

    return f"{hr:02d}:{mit:02d} {p}"


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        tm = input().strip()
        print(convert(tm))
