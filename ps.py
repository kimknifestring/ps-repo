from collections import deque

arr=[]
for _ in range(12):
    line=list(input())
    arr.append(line)

answer=0

dy=[1,-1,0,0]
dx=[0,0,1,-1]

def debug():
    for i in arr:
        print(i)
isBoom=False
def BFS(X,Y,C,visited):
    global isBoom
    puyoN=1
    coordinate=[]
    q=deque([(X,Y,C)])
    visited[Y][X]=True
    coordinate.append((X,Y))
    while q:
        x,y,color=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<6 and 0<=ny<12 and not visited[ny][nx]:
                if arr[ny][nx]==color:
                    # print('연결된 같은 뿌요를 찾았다',ny,nx,arr[ny][nx])
                    puyoN+=1
                    # print(puyoN)
                    visited[ny][nx]=True
                    q.append((nx,ny,color))
                    coordinate.append((nx,ny))
    if puyoN>=4:
        # print('터진다')
        for x,y in coordinate:
            arr[y][x]='.'
        isBoom=True
def down(X,Y):
    dest_y=Y
    while dest_y+1<12 and arr[dest_y+1][X]=='.':
        dest_y+=1
    if dest_y!=Y:
        arr[dest_y][X] = arr[Y][X]
        arr[Y][X] = '.'

isPlus=True
while isPlus:
    # 터지는 거 하나라도 있는지 체크
    visited=[[False for _ in range(6)] for _ in range(12)]
    isBoom=False
    for i in range(12):
        for j in range(6):
            if arr[i][j]!='.' and not visited[i][j]:
                # print('뿌요를 찾았다',arr[i][j],visited)
                BFS(j,i,arr[i][j],visited)
    # 터졌으면 +1 연쇄
    if isBoom:
        # debug()
        answer+=1
    else:
        isPlus=False
        break

    for i in range(11,-1,-1):
        for j in range(6):
            if arr[i][j]!='.':
                down(j,i)
print(answer)
