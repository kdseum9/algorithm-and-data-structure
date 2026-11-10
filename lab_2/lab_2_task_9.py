

data = open("input.txt", "rb").read().split()

p = 0
n = int(data[p]); p += 1

key = [0]*(n+1)
L = [0]*(n+1)
R = [0]*(n+1)
for i in range(1, n+1):
    key[i] = int(data[p]); p += 1
    L[i] = int(data[p]); p += 1
    R[i] = int(data[p]); p += 1

size = [0]*(n+1)
child = [False]*(n+1)
for i in range(1, n+1):
    if L[i]: child[L[i]] = True
    if R[i]: child[R[i]] = True
root = 1
for i in range(1, n+1):
    if not child[i]:
        root = i
        break

order = []
st = [root]
while st:
    v = st.pop()
    order.append(v)
    if L[v]: st.append(L[v])
    if R[v]: st.append(R[v])
for v in reversed(order):
    size[v] = 1 + (size[L[v]] if L[v] else 0) + (size[R[v]] if R[v] else 0)

alive = [True]*(n+1)
remaining = n

m = int(data[p]); p += 1
out = []
for _ in range(m):
    target = int(data[p]); p += 1

    v = root
    while v and alive[v] and key[v] != target:
        v = L[v] if target < key[v] else R[v]

    if v and alive[v]:
        cnt = 0
        st = [v]
        while st:
            u = st.pop()
            if not alive[u]:
                continue
            alive[u] = False
            cnt += 1
            if L[u]: st.append(L[u])
            if R[u]: st.append(R[u])
        remaining -= cnt

    out.append(str(remaining))
open("output.txt", "w").write("\n".join(out))