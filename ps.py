from collections import deque
import copy
arr=[]
visited=set()
for _ in range(3):
    line=list(map(int,input().split()))
    arr.append(line)

def arrToStr(arr):
    state=''
    for i in range(3):
        for j in range(3):
            state+=str(arr[i][j])
    return state

def strToArr(str):
    result=[]
    line=[]
    for i in range(9):
        line.append(int(str[i]))
        if len(line)==3:
            result.append(line)
            line=[]
    return result

def findZero(arr):
    for i in range(3):
        for j in range(3):
            if arr[i][j]==0:
                return (i,j)

dx=[1,-1,0,0]
dy=[0,0,1,-1]      
def isInArr(i,j):
    return 0<=i<3 and 0<=j<3

isSuccess=False
q=deque([(arrToStr(arr),0)])
visited.add(arrToStr(arr))
while q:
    state,count=q.popleft()
    if state=='123456780':
        isSuccess=True
        print(count)
        break
    arr=strToArr(state)
    i,j=findZero(arr)
    for k in range(4):
        if isInArr(i+dy[k],j+dx[k]):
            newArr=copy.deepcopy(arr)
            newArr[i][j],newArr[i+dy[k]][j+dx[k]]=newArr[i+dy[k]][j+dx[k]],newArr[i][j]
            newState=arrToStr(newArr)
            if newState not in visited:
                visited.add(newState)
                q.append((newState,count+1))

if not isSuccess:
    print(-1)


            
