with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

cards = {}

found = []
count1 = 0
for line in lines:
    int_count = 0
    card, rest = line.split(':')
    _, card = card.split()
    winning_numbers, your_numbers = [z.split() for z in rest.split('|')]
    found.append([int(card), winning_numbers, your_numbers])
    cards[int(card)] = 1
    
    for n in your_numbers:
        if n in winning_numbers:
            int_count += 1

    if int_count > 0:
        count1 += 2**(int_count-1)

print(count1)

for card, winning_numbers, your_numbers in found:
    matches = 1
    for n in your_numbers:
        if n in winning_numbers:
            cards[card+matches] += cards[card]
            matches += 1

count2 = 0
for k, v in cards.items():
    count2 += v

print(count2)
