from copy import deepcopy

with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

monkeys = {}
m_solution = {}

for line in lines:
    m, op = [x.strip() for x in line.split(":")]

    if op.isnumeric():
        m_solution[m] = int(op)
        monkeys[m] = int(op)
    else:
        first, operation, second = op.split()
        monkeys[m] = (first, operation, second)

m_solution_orig = deepcopy(m_solution)

def recursion(m, m_solution):
    if m in m_solution:
        return m_solution[m]

    first, operation, second = monkeys[m]
    f = recursion(first, m_solution)
    s = recursion(second, m_solution)

    # check operation
    if operation == '+':
        m_solution[m] = f + s
    if operation == '-':
        m_solution[m] = f - s
    if operation == '*':
        m_solution[m] = f * s
    if operation == '/':
        m_solution[m] = int(f / s)
    return m_solution[m]


print(recursion("root", m_solution))

# Part 2
m_solution = m_solution_orig

def find_key(key):
    for k, v in monkeys.items():
        if isinstance(v, tuple):
            if key in v:
                return k
    
    raise Exception(f"Could not find key for {key}")

def recursion_up(m, m_solution, prev):
    if m == "humn":
        next_key = find_key(m)
        return recursion_up(next_key, m_solution, m)

    first, operation, second = monkeys[m]
    first_flag = False
    if first == prev:
        other = recursion(second, m_solution)
        first_flag = True
    if second == prev:
        other = recursion(first, m_solution)

    if m == "root":
        return other
    else:
        next_key = find_key(m)
        res = recursion_up(next_key, m_solution, m)
        if operation == '+':
            return res - other
        if operation == '*':
            return int(res / other)
        if operation == '-':
            if first_flag:
                return res + other
            else:
                return other - res
        if operation =='/':
            if first_flag:
                return res * other
            else:
                return int(other / res)
    
    raise Exception("Should not get here")

print(recursion_up("humn", m_solution, "humn"))