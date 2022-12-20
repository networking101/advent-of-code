class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

with open("input", "r") as fp:
    lines = [int(line.strip()) for line in fp]

def print_list():
    head = order[0]
    print(head.data, end=" ")
    curr = head.next
    while curr != head:
        print(curr.data, end=" ")
        curr = curr.next
    print()

order = []

# create nodes
for i, v in enumerate(lines):
    order.append(Node(v))

# set up linked list
for i, v in enumerate(order):
    if i == 0:
        v.prev = order[-1]
    else:
        v.prev = order[i-1]
    if i == len(order) - 1:
        v.next = order[0]
    else:
        v.next = order[i+1]

# starting with the first value, rearrange positions
for i, v in enumerate(order):
    n_value = v.data
    n_prev = v.prev
    n_next = v.next

    if n_value > 0:
        # remove node from linked list
        n_prev.next = n_next
        n_next.prev = n_prev

        pos = n_prev
        for steps in range(n_value):
            pos = pos.next
        pos_plus = pos.next
        pos.next = v
        pos_plus.prev = v
        v.next = pos_plus
        v.prev = pos

    if n_value < 0:
        # remove node from linked list
        n_prev.next = n_next
        n_next.prev = n_prev

        pos = n_next
        for steps in range(abs(n_value)):
            pos = pos.prev
        pos_minus = pos.prev
        pos.prev = v
        pos_minus.next = v
        v.next = pos
        v.prev = pos_minus

# find 0
zero = order[0]
while zero.data != 0:
    zero = zero.next

curr = zero
tot = 0
for i in range(3000):
    curr = curr.next
    if i % 1000 == 999:
        tot += curr.data

print(tot)

# Part 2
order = []

# create nodes
for i, v in enumerate(lines):
    order.append(Node(v * 811589153))

# set up linked list
for i, v in enumerate(order):
    if i == 0:
        v.prev = order[-1]
    else:
        v.prev = order[i-1]
    if i == len(order) - 1:
        v.next = order[0]
    else:
        v.next = order[i+1]

# print_list()
# tmp = 0

# starting with the first value, rearrange positions
for x in range(10):
    for i, v in enumerate(order):
        print(i)
        n_value = v.data
        n_prev = v.prev
        n_next = v.next

        if n_value > 0:
            # remove node from linked list
            n_prev.next = n_next
            n_next.prev = n_prev

            pos = n_prev
            for steps in range(n_value):
                pos = pos.next
            pos_plus = pos.next
            pos.next = v
            pos_plus.prev = v
            v.next = pos_plus
            v.prev = pos

        if n_value < 0:
            # remove node from linked list
            n_prev.next = n_next
            n_next.prev = n_prev

            pos = n_next
            for steps in range(abs(n_value)):
                pos = pos.prev
            pos_minus = pos.prev
            pos.prev = v
            pos_minus.next = v
            v.next = pos
            v.prev = pos_minus

    # print_list()
    # tmp = 0

# find 0
zero = order[0]
while zero.data != 0:
    zero = zero.next

curr = zero
tot = 0
for i in range(3000):
    curr = curr.next
    if i % 1000 == 999:
        tot += curr.data

print(tot)
