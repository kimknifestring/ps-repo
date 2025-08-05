from collections import deque

M,N=map(int,input().split())
arr=[]
visited = [[[False for _ in range(5)] for _ in range(N)] for _ in range(M)]
for _ in range(M):
    line=list(map(int,input().split()))
    arr.append(line)

sy, sx, sd = map(int, input().split())
sy-=1
sx-=1
ey, ex, ed = map(int, input().split())
ey-=1
ex-=1
#동서남북순
dy=[0,0,1,-1]
dx=[1,-1,0,0]

q=deque([(sy,sx,sd,0)])
visited[sy][sx][sd]=True

dirdic={1:(3,4),2:(4,3),3:(2,1),4:(1,2)}
while q:
    y,x,d,cnt=q.popleft()    
    if (y, x, d) == (ey, ex, ed):
        print(cnt)
        break
    for k in range(1,4):
        ny = y + dy[d - 1] * k
        nx = x + dx[d - 1] * k
    
        if 0 <= ny < M and 0 <= nx < N and arr[ny][nx] == 0:
            if not visited[ny][nx][d]:
                visited[ny][nx][d] = True
                q.append((ny, nx, d, cnt + 1))
        else:
            break
    
    for nd in dirdic[d]:
        if not visited[y][x][nd]:
            visited[y][x][nd]=True
            q.append((y,x,nd,cnt+1))

    
