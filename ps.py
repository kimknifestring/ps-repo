N, C = map(int,input().split())
li=[int(input()) for _ in range(N)]
li.sort()

s, e = 1, li[-1] - li[0] 
result = 0 

while s <= e:
    mid = (s + e) // 2  
    count = 1 
    last_pos = li[0]

    for i in range(1, N):
        if li[i] >= last_pos + mid:
            count += 1 
            last_pos = li[i] 
    if count >= C:
        result = mid 
        s = mid + 1
    else:
        e = mid - 1

print(result)