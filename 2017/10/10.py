from copy import deepcopy

with open("input3", "r") as fp:
    line = fp.readline()

standard_list_size = 5

def round(elements, input_lengths, curr_position, skip_size):
    for i, x in enumerate(input_lengths):

        double_elements = elements + elements

        # modify elements list
        element_end_pos = x + curr_position
        print(element_end_pos)
        rev_section = double_elements[curr_position:element_end_pos]
        rev_section = rev_section[::-1]

        for j in rev_section:
            

        exit(0)
        rev_section = elements[:element_end_pos]
        rev_section = rev_section[::-1]
        elements = rev_section + elements[element_end_pos:]

        # rotate elements to start at new current position
        # keep track of current position for silver result
        curr_position = (curr_position - (x + skip_size)) % standard_list_size
        new_pos = (x + skip_size) % standard_list_size
        elements = elements[:new_pos] + elements[new_pos:]

        skip_size += 1

    elements = elements[new_pos + 1:] + elements[:new_pos + 1]
    return (elements, curr_position, skip_size)

# silver
input_lengths = [int(x) for x in line.split(",")]
elements = list(range(standard_list_size))

curr_position = 0
skip_size = 0
elements, curr_position, skip_size = round(elements, input_lengths, curr_position, skip_size)
print(elements[0] * elements[1])

# # gold
with open("input2", "r") as fp:
    line = fp.readline()

input_lengths = [ord(x) for x in line.strip()]
input_lengths += [17, 31, 73, 47, 23]
elements = list(range(standard_list_size))

curr_position = 0
skip_size = 0
for i in range(64):
    elements, curr_position, skip_size = round(elements, input_lengths, curr_position, skip_size)

print(elements)
hash = ""
curr_byte = 0
for i, x in enumerate(elements):
    curr_byte ^= x
    if (i % 16) == 15:
        hash += hex(curr_byte)[2:]
        curr_byte = 0

print(hash)