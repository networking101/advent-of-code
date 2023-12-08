from copy import deepcopy

with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

five = []
four = []
full = []
three = []
two = []
one = []
high = []

five2 = []
four2 = []
full2 = []
three2 = []
two2 = []
one2 = []
high2 = []

hands = [high, one, two, three, full, four, five]
hands2 = [high2, one2, two2, three2, full2, four2, five2]

cards = {"A":0, "K":0, "Q":0, "J":0, "T":0, "9":0, "8":0, "7":0, "6":0, "5":0, "4":0, "3":0, "2":0}
cards2 = {"A":0, "K":0, "Q":0, "T":0, "9":0, "8":0, "7":0, "6":0, "5":0, "4":0, "3":0, "2":0, "J":0}

for line in lines:
    added = False
    hand, bid = line.split()
    curr_cards = deepcopy(cards)
    curr_cards2 = deepcopy(cards2)
    for c in hand:
        curr_cards[c] += 1
        curr_cards2[c] += 1
    
    if 5 in curr_cards.values():
        five.append([hand, int(bid)])
        five2.append([hand, int(bid)])
    elif 4 in curr_cards.values():
        four.append([hand, int(bid)])
        if curr_cards2["J"] > 0:
            five2.append([hand, int(bid)])
        else:
            four2.append([hand, int(bid)])
    elif 3 in curr_cards.values():
        if 2 in curr_cards.values():
            full.append([hand, int(bid)])
        else:
            three.append([hand, int(bid)])

        if curr_cards2["J"] == 3:
            if 2 in curr_cards2.values():
                five2.append([hand, int(bid)])
            else:
                four2.append([hand, int(bid)])
        elif curr_cards2["J"] == 2:
            five2.append([hand, int(bid)])
        elif curr_cards2["J"] == 1:
            four2.append([hand, int(bid)])
        else:
            if 2 in curr_cards2.values():
                full2.append([hand, int(bid)])
            else:
                three2.append([hand, int(bid)])
    elif 2 in curr_cards.values():
        if len([k for k, v in curr_cards.items() if v == 2]) == 2:
            two.append([hand, int(bid)])
        else:
            one.append([hand, int(bid)])

        if curr_cards2["J"] == 2:
            if len([k for k, v in curr_cards2.items() if v == 2]) == 2:
                four2.append([hand, int(bid)])
            else:
                three2.append([hand, int(bid)])
        elif curr_cards2["J"] == 1:
            if len([k for k, v in curr_cards2.items() if v == 2]) == 2:
                full2.append([hand, int(bid)])
            else:
                three2.append([hand, int(bid)])
        else:
            if len([k for k, v in curr_cards2.items() if v == 2]) == 2:
                two2.append([hand, int(bid)])
            else:
                one2.append([hand, int(bid)])
    else:
        high.append([hand, int(bid)])

        if curr_cards2["J"] == 1:
            one2.append([hand, int(bid)])
        else:
            high2.append([hand, int(bid)])

ordered = []
card_order = list(cards)[::-1]

def get_hand_val(hnd):
    value = ''
    for c in hnd:
        value += hex(card_order.index(c))[-1]
    return int(value, 16)

for hand_list in hands:
    while hand_list:
        h_min = hand_list[0]
        for h in hand_list[1:]:
            if get_hand_val(h[0]) < get_hand_val(h_min[0]):
                h_min = h
        hand_list.remove(h_min)
        ordered.append(h_min)

count1 = 0
for i, o in enumerate(ordered):
    count1 += o[1] * (i+1)

print(count1)


ordered2 = []
card_order2 = list(cards2)[::-1]

def get_hand_val2(hnd):
    value = ''
    for c in hnd:
        value += hex(card_order2.index(c))[-1]
    return int(value, 16)

for hand_list in hands2:
    while hand_list:
        h_min = hand_list[0]
        for h in hand_list[1:]:
            if get_hand_val2(h[0]) < get_hand_val2(h_min[0]):
                h_min = h
        hand_list.remove(h_min)
        ordered2.append(h_min)

count2 = 0
for i, o in enumerate(ordered2):
    count2 += o[1] * (i+1)
print(count2)