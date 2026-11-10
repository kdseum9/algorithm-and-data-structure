import sys

sys.setrecursionlimit(300000)

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
x = int(data[p]); p += 1

child = [False]*(n+1)
for i in range(1, n+1):
    if L[i]: child[L[i]] = True
    if R[i]: child[R[i]] = True
root = 1
for i in range(1, n+1):
    if not child[i]:
        root = i
        break

height = [0]*(n+1)

def h(v):
    return height[v] if v else 0

order = []
st = [root]
while st:
    v = st.pop()
    order.append(v)
    if L[v]: st.append(L[v])
    if R[v]: st.append(R[v])
for v in reversed(order):
    hl = h(L[v]); hr = h(R[v])
    height[v] = 1 + (hl if hl > hr else hr)

def bal(v):
    return h(R[v]) - h(L[v])

def rotate_right(v):
    u = L[v]
    L[v] = R[u]
    R[u] = v
    height[v] = 1 + max(h(L[v]), h(R[v]))
    height[u] = 1 + max(h(L[u]), h(R[u]))
    return u

def rotate_left(v):
    u = R[v]
    R[v] = L[u]
    L[u] = v
    height[v] = 1 + max(h(L[v]), h(R[v]))
    height[u] = 1 + max(h(L[u]), h(R[u]))
    return u

def rebalance(v):
    height[v] = 1 + max(h(L[v]), h(R[v]))
    b = bal(v)
    if b == 2:
        if bal(R[v]) < 0:
            R[v] = rotate_right(R[v])
        return rotate_left(v)
    if b == -2:
        if bal(L[v]) > 0:
            L[v] = rotate_left(L[v])
        return rotate_right(v)
    return v

v = root
while v and key[v] != x:
    v = L[v] if x < key[v] else R[v]
target = v

def find_parent(v):
    if v == root:
        return 0
    cur = root
    while True:
        if L[cur] == v or R[cur] == v:
            return cur
        cur = L[cur] if key[v] < key[cur] else R[cur]

if n == 1:
    print(0)
    sys.exit()

if not L[target] and not R[target]:
    R_del = target
    start_parent = find_parent(target)
elif not L[target]:
    par = find_parent(target)
    if par == 0:
        root = R[target]
    elif L[par] == target:
        L[par] = R[target]
    else:
        R[par] = R[target]
    start_parent = par
    R_del = 0
else:
    rr = L[target]
    while R[rr]:
        rr = R[rr]
    key[target] = key[rr]
    R_del = rr
    start_parent = find_parent(rr)

if R_del:
    par = start_parent
    if par == 0:
        root = L[R_del] if L[R_del] else R[R_del]
    elif L[par] == R_del:
        L[par] = L[R_del] if L[R_del] else R[R_del]
    else:
        R[par] = L[R_del] if L[R_del] else R[R_del]

cur = start_parent
while cur:
    par = find_parent(cur)
    new_root = rebalance(cur)
    if par == 0:
        root = new_root
    elif L[par] == cur:
        L[par] = new_root
    else:
        R[par] = new_root
    cur = par

alive = []
st = [root]
while st:
    v = st.pop()
    if not v: continue
    alive.append(v)
    if L[v]: st.append(L[v])
    if R[v]: st.append(R[v])

newnum = {}
for i, v in enumerate(alive, 1):
    newnum[v] = i

out = [str(len(alive))]
for v in alive:
    nl = newnum[L[v]] if L[v] else 0
    nr = newnum[R[v]] if R[v] else 0
    out.append(f"{key[v]} {nl} {nr}")

open("output.txt", "w").write("\n".join(out))