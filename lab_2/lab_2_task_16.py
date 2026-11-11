import sys
import random

sys.setrecursionlimit(300000)

def main():
    data = open("input.txt", "rb").read().split()
    n = int(data[0])
    pos = 1

    random.seed(42)

    key = []
    prio = []
    left = []
    right = []
    size = []

    def new_node(k):
        key.append(k)
        prio.append(random.getrandbits(30))
        left.append(-1)
        right.append(-1)
        size.append(1)
        return len(key) - 1

    def sz(v):
        return size[v] if v != -1 else 0

    def upd(v):
        size[v] = 1 + sz(left[v]) + sz(right[v])

    def split(v, k):
        if v == -1:
            return -1, -1
        if key[v] < k:
            a, b = split(right[v], k)
            right[v] = a
            upd(v)
            return v, b
        else:
            a, b = split(left[v], k)
            left[v] = b
            upd(v)
            return a, v

    def merge(a, b):
        if a == -1: return b
        if b == -1: return a
        if prio[a] > prio[b]:
            right[a] = merge(right[a], b)
            upd(a)
            return a
        else:
            left[b] = merge(a, left[b])
            upd(b)
            return b

    def insert(root, k):
        a, b = split(root, k)
        node = new_node(k)
        return merge(a, merge(node, b))

    def erase(root, k):
        a, b = split(root, k)
        c, d = split(b, k + 1)
        return merge(a, d)

    def kth_max(root, k):
        v = root
        while True:
            r = sz(right[v])
            if k == r + 1:
                return key[v]
            elif k <= r:
                v = right[v]
            else:
                k -= r + 1
                v = left[v]

    root = -1
    out = []

    for _ in range(n):
        c = int(data[pos]); pos += 1
        k = int(data[pos]); pos += 1
        if c == 1:
            root = insert(root, k)
        elif c == -1:
            root = erase(root, k)
        else:
            out.append(str(kth_max(root, k)))

    open("output.txt", "w").write("\n".join(out))

main()