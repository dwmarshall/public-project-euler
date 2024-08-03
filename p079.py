from collections import Counter, defaultdict

incoming_edges = Counter()
adjacencies = defaultdict(list)

with open("data/0079_keylog.txt") as f:
    for s in f:
        a, b, c = list(s.strip())
        adjacencies[a].append(b)
        adjacencies[b].append(c)
        incoming_edges[a] += 0
        incoming_edges[b] += 1
        incoming_edges[c] += 1

S = [x for x in incoming_edges if incoming_edges[x] == 0]
L = []

while S:
    curr = S.pop()
    L.append(curr)
    for a in adjacencies[curr]:
        incoming_edges[a] -= 1
        if incoming_edges[a] == 0:
            S.append(a)

print("".join(L))
