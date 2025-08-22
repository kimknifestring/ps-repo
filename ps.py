from collections import deque
N,M=map(int,input().split())
dic={}
for _ in range(M):
    A,B=map(int,input().split())
    dic.setdefault(A,[]).append(B)
    dic.setdefault(B,[]).append(A)

kevinList=[0 for _ in range(N+1)]

def bfs(idx):
    q=deque([(idx,0)])
    visited=[False for _ in range(N+1)]
    visited[idx]=True
    retrunKevin=0
    while q:
        current,kevinBacon=q.popleft()
        retrunKevin+=kevinBacon
        if current in dic:
            for i in dic[current]:
                if not visited[i]:
                    visited[i]=True
                    q.append((i,kevinBacon+1))
    kevinList[idx]=retrunKevin

for i in range(1,N+1):
    bfs(i)

targetBaconNum=min(kevinList[1:])
for i in range(1,N+1):
    if kevinList[i]==targetBaconNum:
        print(i)
        break
