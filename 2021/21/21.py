with open("input", "r") as fp:
    lines = [line.strip() for line in fp]

p1bak = int(lines.pop(0).split(" ")[4])-1
p2bak = int(lines.pop(0).split(" ")[4])-1
board = list(range(1,11))

# Silver
p1 = p1bak
p2 = p2bak
dice = list(range(1,11))

score1 = 0
score2 = 0
d = 0
while score1 < 1000:
    # player 1
    rolls = dice[d%len(dice)] + dice[(d+1)%len(dice)] + dice[(d+2)%len(dice)]
    d += 3
    p1 += rolls
    place = board[p1 % len(board)]
    score1 += place

    if score1 >= 1000:
        break
		
    # player 2
    rolls = dice[d%len(dice)] + dice[(d+1)%len(dice)] + dice[(d+2)%len(dice)]
    d += 3
    p2 += rolls
    place = board[p2 % len(board)]
    score2 += place

    if score2 >= 1000:
        break
		
print(min(score1, score2) * d)

# Gold
p1 = p1bak
p2 = p2bak
dice = [1,2,3]
foundResults = {}

def rolling(p1, p2, s1, s2, turn):
    global foundResults
    global dice
    global board
	
    if s1 >= 21:
        return [1,0]
    if s2 >= 21:
        return [0,1]

    key = str(p1) + str(p2) + str(s1).zfill(2) + str(s2).zfill(2) + str(turn)
    if key in foundResults:
        return foundResults[key]
		
    result = [0,0]
	
    if turn == 0:
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    np1 = (p1 + dice[i] + dice[j] + dice[k]) % len(board)
                    ns1 = s1 + board[np1]
                    a, b = rolling(np1, p2, ns1, s2, (turn+1)%2)
                    result[0] += a
                    result[1] += b
					
    else:
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    np2 = (p2 + dice[i] + dice[j] + dice[k]) % len(board)
                    ns2 = s2 + board[np2]
                    a, b = rolling(p1, np2, s1, ns2, (turn+1)%2)
                    result[0] += a
                    result[1] += b
					
    foundResults[key] = result
    return result
	
res = rolling(p1, p2, 0, 0, 0)
print(max(res))
