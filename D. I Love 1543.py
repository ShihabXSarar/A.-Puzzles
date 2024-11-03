def count_occurrences(layer, target):
    extended_layer = layer + layer[:len(target) - 1]
    count = 0
    for i in range(len(extended_layer) - len(target) + 1):
        if extended_layer[i:i+len(target)] == target:
            count += 1
    return count

def extract_layers(n, m, carpet):
    layers = []
    sr, er, sc, ec = 0, n - 1, 0, m - 1

    while sr <= er and sc <= ec:
        layer = ""
        for j in range(sc, ec + 1):
            layer += carpet[sr][j]
        for i in range(sr + 1, er):
            layer += carpet[i][ec]
        if sr < er:
            for j in range(ec, sc - 1, -1):
                layer += carpet[er][j]
        if sc < ec:
            for i in range(er - 1, sr, -1):
                layer += carpet[i][sc]
        layers.append(layer)
        sr, er, sc, ec = sr + 1, er - 1, sc + 1, ec - 1
    return layers

def count_1543(t, cases):
    target = "1543"
    results = []
    for n, m, carpet in cases:
        layers = extract_layers(n, m, carpet)
        total = 0
        for layer in layers:
            total += count_occurrences(layer, target)
        results.append(total)
    return results

if __name__ == "__main__":
    t = int(input())
    cases = []
    for _ in range(t):
        n, m = map(int, input().split())
        carpet = [input() for _ in range(n)]
        cases.append((n, m, carpet))

    results = count_1543(t, cases)
    for result in results:
        print(result)