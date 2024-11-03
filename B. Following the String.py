def st(n, trace):
    s = []
    cnt = [0] * 26
    for i in range(n):
        for j in range(26):
            if cnt[j] == trace[i]:
                s.append(chr(ord('a') + j))
                break
        for j in range(26):
            if s[i] == chr(ord('a') + j):
                cnt[j] += 1
    return ''.join(s)

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        trace = list(map(int, input().split()))
        print(st(n, trace))

if __name__ == "__main__":
    main()
