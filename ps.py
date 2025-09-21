import sys
input=sys.stdin.readline
N, startATK = map(int,input().split())
room = []
for _ in range(N):
    t, a, h = map(int,input().split())
    room.append((t, a, h))

def battle(a,h):
    global currentHP
    global currentATK
    global canThis
    monsterATK = a
    monsterHP = h

    attack_count = (monsterHP - 1) // currentATK
    damage = monsterATK * attack_count
    currentHP -= damage
    if currentHP > 0:
        return True
    else:
        canThis = False
        return False

def potion(a,h):
    global currentHP
    global currentATK

    currentATK += a
    currentHP += h
    if currentHP > midHP:
        currentHP = midHP

startHP = 1
endHP = 10**18
while startHP<=endHP:
    canThis = True
    midHP = (startHP+endHP)//2
    currentHP = midHP
    currentATK = startATK
    
    for t, a, h in room:
        if t == 1:
            if not battle(a,h):
                break
        else:
            potion(a,h)

    if not canThis:
        startHP = midHP+1
    else:
        endHP = midHP-1

print(startHP)