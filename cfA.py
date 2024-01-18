
def can_make_abc(cards):
    if cards == "abc":
        return "YES"
    if cards[0] != "a" and cards[1] != "b" and cards[2] != "c":
        return "NO"

    return "YES"


t = int(input())

for _ in range(t):

    cards = input()
    result = can_make_abc(cards)
    print(result)