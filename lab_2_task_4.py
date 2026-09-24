import sys

sys.stdin = open('input.txt', 'r')
values = []
sizes = []
left = []
right = []


def new_node(x):
    values.append(x)
    sizes.append(1)
    left.append(-1)
    right.append(-1)
    return len(values) - 1


def get_size(ind):
    if ind == -1:
        return 0
    return sizes[ind]


def update_size(ind):
    if ind != -1:
        sizes[ind] = 1 + get_size(left[ind]) + get_size(right[ind])


def insert(ind, x):
    if ind == -1:
        return new_node(x)

    if x < values[ind]:
        left[ind] = insert(left[ind], x)
    elif x > values[ind]:
        right[ind] = insert(right[ind], x)

    update_size(ind)
    return ind


def find_k(ind, k):
    left_size = get_size(left[ind])
    right_size = get_size(right[ind])

    if k == left_size + 1:
        return values[ind]
    elif k <= left_size:
        return find_k(left[ind], k)
    else:
        return find_k(right[ind], k - left_size - 1)


def main():
    root = -1

    lines = sys.stdin.read().splitlines()
    for line in lines:
        if not line.strip():
            continue

        parts = line.split()
        operation = parts[0]
        x = int(parts[1])

        if operation == '+':
            root = insert(root, x)
        elif operation == '?':
            answer = find_k(root, x)
            print(answer)


if __name__ == '__main__':
    main()